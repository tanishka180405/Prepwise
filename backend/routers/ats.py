from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import re

router = APIRouter(prefix="/ats", tags=["ATS Checker"])

# ── Complete DS & AI keyword list ─────────────────────
DSAI_KEYWORDS = [
    # Core ML
    "machine learning", "deep learning", "neural network", "model training",
    "supervised learning", "unsupervised learning", "reinforcement learning",
    "classification", "regression", "clustering", "feature engineering",
    "hyperparameter tuning", "cross-validation", "overfitting", "regularization",
    "ensemble learning", "bagging", "boosting", "random forest", "decision tree",
    "gradient boosting", "xgboost", "lightgbm", "adaboost", "svm",
    "support vector machine", "k-nearest neighbors", "naive bayes", "k-means",
    # Libraries
    "python", "tensorflow", "pytorch", "keras", "scikit-learn", "sklearn",
    "pandas", "numpy", "matplotlib", "seaborn", "opencv", "huggingface",
    "transformers", "xgboost", "lightgbm", "fastapi", "flask", "django",
    "streamlit", "gradio", "nltk", "spacy", "gensim", "scipy", "plotly",
    # Data
    "sql", "postgresql", "mysql", "mongodb", "redis", "data cleaning",
    "data wrangling", "etl", "data pipeline", "spark", "hadoop",
    "data visualization", "tableau", "power bi", "exploratory data analysis",
    # NLP
    "nlp", "natural language processing", "bert", "gpt", "tokenization",
    "word embeddings", "text classification", "sentiment analysis", "ner",
    "word2vec", "glove", "transformer", "attention mechanism", "fine-tuning",
    "language model", "prompt engineering", "rag", "zero-shot", "few-shot",
    # CV
    "computer vision", "cnn", "convolutional neural network", "image classification",
    "object detection", "yolo", "resnet", "transfer learning", "image segmentation",
    # MLOps
    "mlops", "docker", "kubernetes", "ci/cd", "git", "github", "mlflow",
    "model deployment", "rest api", "aws", "gcp", "azure", "jupyter",
    "google colab", "version control", "linux", "bash",
    # Stats
    "statistics", "probability", "hypothesis testing", "a/b testing",
    "linear algebra", "gradient descent", "backpropagation", "bayesian",
    "confidence interval", "p-value", "correlation", "standard deviation",
    # DL specific
    "lstm", "gru", "rnn", "dropout", "batch normalization", "relu",
    "activation function", "loss function", "optimizer", "adam", "sgd",
    "vanishing gradient", "residual connection", "autoencoder", "gan",
    # Soft/Academic
    "research", "internship", "project", "publication", "hackathon",
    "data science", "artificial intelligence", "b.tech", "machine learning engineer",
    "data analyst", "data engineer", "model accuracy", "feature selection",
]


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract text from PDF using PyMuPDF."""
    try:
        import fitz
        text = ""
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text.lower()
    except ImportError:
        raise HTTPException(status_code=500, detail="PyMuPDF not installed. Run: pip install pymupdf")
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Could not read PDF: {str(e)}")


def score_resume(text: str) -> dict:
    """Score resume against DSAI keywords."""
    found = []
    missing = []

    for kw in DSAI_KEYWORDS:
        if kw.lower() in text:
            found.append(kw)
        else:
            missing.append(kw)

    # Skills score
    skills_score = round((len(found) / len(DSAI_KEYWORDS)) * 100, 1)

    # Formatting score
    formatting_score = 60.0
    if re.search(r'\b(education|experience|projects|skills|certifications)\b', text):
        formatting_score += 15
    if re.search(r'\d{4}', text):
        formatting_score += 5
    if re.search(r'@\w+\.\w+', text):
        formatting_score += 5
    if re.search(r'github\.com', text):
        formatting_score += 8
    if re.search(r'linkedin\.com', text):
        formatting_score += 7
    formatting_score = min(formatting_score, 100.0)

    # Keyword density score
    word_count = max(len(text.split()), 1)
    keyword_hits = sum(text.count(kw) for kw in found)
    keyword_score = min(round((keyword_hits / word_count) * 1000, 1), 100.0)

    # Overall
    overall = round((skills_score * 0.5 + formatting_score * 0.3 + keyword_score * 0.2), 1)

    # Suggestions
    suggestions = []
    if skills_score < 60:
        suggestions.append("Add a dedicated 'Technical Skills' section near the top of your resume.")
    if "docker" not in text:
        suggestions.append("Mention Docker or containerisation experience if applicable.")
    if "mlops" not in text and "model deployment" not in text:
        suggestions.append("Include MLOps or model deployment experience from projects.")
    if not re.search(r'\d+\s*%', text):
        suggestions.append("Quantify your impact — e.g. 'improved model accuracy by 12%'.")
    if "github" not in text:
        suggestions.append("Add your GitHub profile link — recruiters always check this.")
    if len(found) < 10:
        suggestions.append("Add more DS & AI keywords relevant to your experience.")
    if not suggestions:
        suggestions.append("Great resume! Keep it updated with your latest projects and skills.")

    # Top missing keywords (most important ones)
    priority_missing = [kw for kw in missing if kw in [
        "pytorch", "docker", "mlops", "sql", "a/b testing",
        "feature engineering", "model deployment", "ci/cd",
        "mlflow", "fastapi", "huggingface", "deep learning",
        "natural language processing", "computer vision", "git",
        "tensorflow", "scikit-learn", "pandas", "numpy", "keras"
    ]][:12]

    return {
        "overall_score": overall,
        "skills_score": skills_score,
        "formatting_score": formatting_score,
        "keyword_score": keyword_score,
        "found_keywords": found[:25],
        "missing_keywords": priority_missing,
        "suggestions": suggestions,
    }


@router.post("/check")
async def check_resume(file: UploadFile = File(...)):
    """
    Upload a PDF resume and get a real ATS score.
    No login required.
    """
    try:
        # Validate file type
        if not file.filename.lower().endswith(".pdf"):
            return JSONResponse(
                status_code=400,
                content={"detail": "Only PDF files are supported. Please upload a .pdf file."}
            )

        # Read file
        contents = await file.read()

        # Validate size (5MB max)
        if len(contents) > 5 * 1024 * 1024:
            return JSONResponse(
                status_code=400,
                content={"detail": "File too large. Maximum size is 5MB."}
            )

        # Extract text
        text = extract_text_from_pdf(contents)

        # Check if PDF has readable text
        if len(text.strip()) < 30:
            return JSONResponse(
                status_code=422,
                content={"detail": "Resume appears empty or is a scanned image. Please use a text-based PDF."}
            )

        # Score it
        result = score_resume(text)

        return JSONResponse(content={
            "filename": file.filename,
            **result,
        })

    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"detail": e.detail})
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detail": f"Analysis failed: {str(e)}"}
        )


@router.get("/history")
async def ats_history():
    """Return empty history — auth not required in this version."""
    return {"results": []}
