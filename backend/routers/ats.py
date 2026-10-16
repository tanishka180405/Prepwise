"""Transparent ATS-style resume analysis for DS and AI students."""
from collections import OrderedDict
import re

from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/ats", tags=["ATS Checker"])

# Canonical skills and aliases. A skill is counted once, so repetition cannot
# inflate the score.
SKILL_GROUPS = OrderedDict([
    ("Programming", {"python": ["python"], "sql": ["sql", "postgresql", "mysql"]}),
    ("Data", {"pandas": ["pandas"], "numpy": ["numpy"], "visualization": ["tableau", "power bi", "matplotlib", "seaborn", "data visualization"]}),
    ("Machine learning", {"machine learning": ["machine learning"], "scikit-learn": ["scikit-learn", "sklearn"], "feature engineering": ["feature engineering"], "model evaluation": ["cross validation", "cross-validation", "model evaluation"]}),
    ("Deep learning / AI", {"deep learning": ["deep learning"], "pytorch": ["pytorch"], "tensorflow": ["tensorflow", "keras"], "nlp": ["natural language processing", "nlp", "transformers"], "computer vision": ["computer vision", "opencv", "object detection"]}),
    ("Engineering", {"git": ["git", "github"], "deployment": ["model deployment", "fastapi", "flask", "streamlit", "api"], "docker": ["docker", "containerization", "containerisation"]}),
])
SECTION_PATTERNS = {
    "education": r"\beducation\b|\bacademic\b",
    "experience": r"\bexperience\b|\bemployment\b|\bwork history\b|\binternship\b",
    "projects": r"\bprojects?\b|\bpersonal projects?\b|\bacademic projects?\b",
    "skills": r"\btechnical skills?\b|\bskills?\b|\bcompetencies\b",
}
ACTION_VERBS = r"\b(built|developed|designed|implemented|created|automated|improved|reduced|increased|analyzed|analysed|deployed|led|optimized|optimised|trained|evaluated)\b"
EMAIL_PATTERN = r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b"
PHONE_PATTERN = r"(?:\+?\d[\d\s().-]{7,}\d)"


def _contains(text: str, phrase: str) -> bool:
    return bool(re.search(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", text, re.I))


def extract_text_from_pdf(pdf_bytes: bytes) -> tuple[str, int]:
    try:
        import fitz
        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
            if not document.page_count:
                raise HTTPException(status_code=422, detail="The PDF has no pages.")
            return "\n".join(page.get_text("text") for page in document), document.page_count
    except HTTPException:
        raise
    except ImportError:
        raise HTTPException(status_code=500, detail="Resume analysis is unavailable because PyMuPDF is not installed.")
    except Exception:
        raise HTTPException(status_code=422, detail="We could not read this PDF. Upload a text-based, unlocked PDF.")


def _skill_analysis(text: str):
    found, missing, details = [], [], []
    possible = sum(len(group) for group in SKILL_GROUPS.values())
    for group_name, skills in SKILL_GROUPS.items():
        group_found, group_missing = [], []
        for canonical, aliases in skills.items():
            if any(_contains(text, alias) for alias in aliases):
                found.append(canonical)
                group_found.append(canonical)
            else:
                group_missing.append(canonical)
        details.append({"name": group_name, "found": group_found, "total": len(skills)})
        missing.extend(group_missing[:2])
    return found, missing[:10], round(100 * len(found) / possible, 1), details


def score_resume(extracted_text: str, page_count: int) -> dict:
    text = re.sub(r"\s+", " ", extracted_text).strip()
    lower = text.lower()
    word_count = len(re.findall(r"\b[\w+#.-]+\b", text))
    found, missing, skills_score, skill_groups = _skill_analysis(lower)

    sections = [name for name, pattern in SECTION_PATTERNS.items() if re.search(pattern, lower, re.I)]
    has_email = bool(re.search(EMAIL_PATTERN, text, re.I))
    has_phone = bool(re.search(PHONE_PATTERN, text))
    has_linkedin, has_github = "linkedin.com" in lower, "github.com" in lower
    formatting_score = round(min(100, (len(sections) + has_email + has_phone + has_linkedin + has_github) / 9 * 100), 1)

    metrics = re.findall(r"\b\d+(?:\.\d+)?\s*(?:%|x|ms|seconds?|minutes?|hours?|users?|customers?|records?|rows?|projects?)\b", lower)
    action_count = len(re.findall(ACTION_VERBS, lower, re.I))
    impact_score = round(min(100, action_count * 8 + len(metrics) * 12), 1)

    unreadable_markers = len(re.findall(r"[■□�]", extracted_text))
    length_score = 100 if 180 <= word_count <= 1200 else (70 if 120 <= word_count <= 1500 else 40)
    readability_score = round(max(0, length_score - min(30, unreadable_markers * 5)), 1)
    overall = round(skills_score * .35 + formatting_score * .25 + impact_score * .25 + readability_score * .15, 1)

    suggestions = []
    if not has_email or not has_phone:
        suggestions.append("Add a professional email address and phone number in the resume header.")
    absent_sections = {"education", "skills", "projects"} - set(sections)
    if absent_sections:
        suggestions.append("Add clear section headings for: " + ", ".join(sorted(absent_sections)) + ".")
    if action_count < 3:
        suggestions.append("Start project and experience bullets with action verbs such as Built, Developed, Analysed or Deployed.")
    if len(metrics) < 2:
        suggestions.append("Quantify truthful results: dataset size, latency, accuracy, time saved or users served.")
    if word_count < 180:
        suggestions.append("Add detail for each project: problem, your contribution, tools used and outcome.")
    if word_count > 1200 or page_count > 2:
        suggestions.append("Keep an early-career resume concise—usually one page, or two only when experience justifies it.")
    if missing:
        suggestions.append("Add missing skills only when they truthfully describe your experience; tailor them to the job description.")
    if not suggestions:
        suggestions.append("Strong foundation. Tailor the summary and skills to each job description before applying.")

    return {
        "overall_score": overall, "skills_score": skills_score,
        "formatting_score": formatting_score, "keyword_score": impact_score,
        "readability_score": readability_score, "word_count": word_count,
        "page_count": page_count, "found_keywords": found,
        "missing_keywords": missing, "skill_groups": skill_groups,
        "sections_found": sections, "suggestions": suggestions[:6],
        "score_note": "This is a transparent DS/AI resume-match score, not a hiring prediction. Never add a keyword unless it truthfully reflects your experience.",
    }


@router.post("/check")
async def check_resume(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported. Please upload a .pdf file.")
    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="The uploaded file is empty.")
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large. Maximum supported size is 5 MB.")
    if not contents.startswith(b"%PDF-"):
        raise HTTPException(status_code=400, detail="The file does not appear to be a valid PDF.")
    text, page_count = extract_text_from_pdf(contents)
    if len(text.strip()) < 80:
        raise HTTPException(status_code=422, detail="Very little readable text was found. Upload a text-based PDF instead of a scanned image.")
    return JSONResponse(content={"filename": file.filename, **score_resume(text, page_count)})


@router.get("/history")
async def ats_history():
    return {"results": []}
