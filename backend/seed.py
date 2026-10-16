"""
Run to populate the questions table:
    python seed.py
"""
from database import SessionLocal, engine
from models.question import Question
import models

from database import Base
Base.metadata.create_all(bind=engine)

QUESTIONS = [

    # ─────────────────────────────────────────
    # MACHINE LEARNING — 18 questions
    # ─────────────────────────────────────────
    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What is the difference between supervised and unsupervised learning?",
         answer="Supervised learning trains on labelled data to predict outputs (classification, regression). Unsupervised learning finds hidden patterns in unlabelled data (clustering, dimensionality reduction). Example: spam detection is supervised; customer segmentation is unsupervised."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Wipro", topic="Fundamentals",
         text="What is overfitting and how do you prevent it?",
         answer="Overfitting is when a model memorises training data and performs poorly on new data. Prevention: regularisation (L1/L2), dropout, cross-validation, early stopping, more training data, or simplifying the model."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Infosys", topic="Evaluation",
         text="What is a confusion matrix and what does it tell you?",
         answer="A confusion matrix shows TP, TN, FP, FN for a classifier. From it you derive precision (TP/TP+FP), recall (TP/TP+FN), F1-score, and accuracy. It tells you not just overall accuracy but where the model fails — which classes get confused."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between classification and regression?",
         answer="Classification predicts a discrete label (spam/not spam, cat/dog). Regression predicts a continuous value (house price, temperature). Both are supervised learning. Logistic Regression despite its name is used for classification."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Algorithms",
         text="How does K-Nearest Neighbours (KNN) work?",
         answer="KNN classifies a new point by finding the K nearest training points (using Euclidean distance) and taking a majority vote. No training phase — it is a lazy learner. Drawbacks: slow at inference for large datasets, sensitive to irrelevant features and scale."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Fundamentals",
         text="What is the bias-variance tradeoff in machine learning?",
         answer="Bias is error from wrong assumptions (underfitting). Variance is sensitivity to training data fluctuations (overfitting). High bias = model too simple. High variance = model too complex. Optimal models balance both via regularisation and cross-validation."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Regularisation",
         text="What is the difference between L1 and L2 regularisation?",
         answer="L1 (Lasso) adds absolute weight penalty — drives some weights to exactly zero, good for feature selection. L2 (Ridge) adds squared weight penalty — shrinks all weights but rarely to zero. Use L1 when few features matter; L2 when most features contribute."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Infosys", topic="Ensembles",
         text="What is the difference between bagging and boosting?",
         answer="Bagging trains models in parallel on random subsets to reduce variance (Random Forest). Boosting trains sequentially where each model corrects previous errors, reducing bias (XGBoost, AdaBoost). Bagging is less prone to overfitting; boosting usually achieves higher accuracy."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Optimisation",
         text="Explain gradient descent and its main variants.",
         answer="Gradient Descent minimises loss by adjusting parameters in the direction of the negative gradient. Batch GD uses all data per step (stable, slow). SGD uses one sample (fast, noisy). Mini-batch GD uses small batches (best trade-off). Adam adapts learning rates per parameter."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Fractal Analytics", topic="Evaluation",
         text="What is the ROC-AUC curve and when would you use it over accuracy?",
         answer="ROC plots True Positive Rate vs False Positive Rate at varying thresholds. AUC measures area under it — 1.0 is perfect, 0.5 is random. Use AUC over accuracy when classes are imbalanced, since accuracy is misleading when one class dominates."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="MuSigma", topic="Algorithms",
         text="What is the difference between a Decision Tree and Random Forest?",
         answer="A Decision Tree is a single model prone to overfitting. Random Forest builds many trees on random data and feature subsets then averages predictions, drastically reducing variance. Random Forest handles missing values, outliers, and high dimensions better."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Algorithms",
         text="How does the XGBoost algorithm work?",
         answer="XGBoost is gradient boosting that builds trees sequentially, each correcting residual errors of the previous. It uses second-order gradients, regularisation (L1/L2 on leaf weights), and parallel tree construction. It dominates structured/tabular data competitions due to speed and accuracy."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Amazon", topic="Algorithms",
         text="Explain how SVM works and what the kernel trick does.",
         answer="SVM finds the hyperplane that maximises the margin between classes using support vectors. The kernel trick implicitly maps data to a higher-dimensional space making non-linear data linearly separable. Common kernels: RBF, polynomial, sigmoid. Effective in high-dimensional spaces."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Google", topic="Algorithms",
         text="What is Principal Component Analysis (PCA) and when do you use it?",
         answer="PCA reduces dimensionality by projecting data onto principal components — directions of maximum variance. Use it when features are correlated, to speed up training, or to visualise high-dimensional data. Limitation: components are less interpretable than original features."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Fractal Analytics", topic="Evaluation",
         text="What is cross-validation and what are its different types?",
         answer="Cross-validation estimates model generalisation. k-fold: split into k folds, train on k-1, test on 1, rotate. Stratified k-fold: preserves class ratios. Leave-One-Out (LOOCV): each sample is the test set once. 5-fold or 10-fold are standard choices for most problems."),

    dict(subject="ML", difficulty="Hard", type="Coding", company="Microsoft", topic="Algorithms",
         text="How would you implement a simple linear regression from scratch without using sklearn?",
         answer="Using gradient descent: initialise weights w=0, b=0. For each epoch, compute predictions y_hat = w*X + b. Compute loss (MSE). Compute gradients: dw = (2/n)*X.T*(y_hat-y), db = (2/n)*sum(y_hat-y). Update: w -= lr*dw, b -= lr*db. Repeat until convergence."),

    dict(subject="ML", difficulty="Medium", type="Situational", company="Any", topic="Applied ML",
         text="You built a fraud detection model with 99% accuracy but your manager is unhappy. Why might this be, and what would you do?",
         answer="99% accuracy sounds great but fraud datasets are heavily imbalanced — if only 1% of transactions are fraud, predicting 'not fraud' always gives 99% accuracy. The model likely has zero recall on fraud cases. Fix: use AUC-ROC, precision-recall curve, F1-score. Apply SMOTE, class weights, or threshold tuning to handle imbalance."),

    dict(subject="ML", difficulty="Hard", type="Situational", company="Amazon", topic="Applied ML",
         text="Your ML model performs well in testing but fails in production. What do you check first?",
         answer="This is a data drift problem. Check: (1) Training-serving skew — are features computed the same way in prod as in training? (2) Data drift — has the distribution of input features shifted? (3) Concept drift — has the relationship between features and target changed? Use monitoring tools, retrain periodically, and log predictions for analysis."),

    # ─────────────────────────────────────────
    # DEEP LEARNING — 17 questions
    # ─────────────────────────────────────────
    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is a neural network and how does it learn?",
         answer="A neural network is layers of interconnected nodes (neurons). It learns by forward propagation (compute predictions), calculating loss, then backpropagation (compute gradients) and updating weights via gradient descent. Repeated over many epochs until loss converges."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="TCS", topic="Activation",
         text="What are activation functions and why are they needed?",
         answer="Activation functions introduce non-linearity into neural networks. Without them, stacking linear layers is still linear. Common ones: ReLU (max(0,x)) — fast, avoids vanishing gradient. Sigmoid — squashes to 0-1, used in output for binary classification. Softmax — multi-class output. Tanh — zero-centred, used in RNNs."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Wipro", topic="Fundamentals",
         text="What is the difference between a shallow and a deep neural network?",
         answer="A shallow network has one hidden layer. A deep network has multiple hidden layers. Depth allows learning hierarchical features — edges → shapes → objects in image recognition. Deep networks can represent complex functions with fewer neurons than shallow ones."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Infosys", topic="Regularisation",
         text="What is dropout in neural networks and why is it used?",
         answer="Dropout randomly sets a fraction of neurons to zero during training, preventing co-adaptation. This forces the network to learn redundant representations. At inference, all neurons are active but outputs are scaled. Acts as an ensemble of many different networks."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Training",
         text="What is the vanishing gradient problem and how is it solved?",
         answer="During backpropagation, gradients shrink exponentially through layers — deep layers stop learning. Solutions: ReLU activation (gradients don't shrink for positive inputs), Batch Normalisation, residual connections (ResNet skip connections), gradient clipping, He/Xavier initialisation."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Architectures",
         text="What is the difference between CNN and RNN?",
         answer="CNN processes grid-like data (images) using convolutional filters for spatial feature detection. RNN processes sequential data with a hidden state carrying context across time. LSTMs and GRUs are improved RNNs that solve the vanishing gradient in long sequences."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Fractal Analytics", topic="Training",
         text="What is batch normalisation and why does it help training?",
         answer="Batch Norm normalises layer inputs to zero mean and unit variance per mini-batch, then scales and shifts with learnable parameters. Benefits: reduces internal covariate shift, allows higher learning rates, reduces sensitivity to weight initialisation, slight regularisation effect."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Transformers",
         text="Explain the attention mechanism in transformers.",
         answer="Attention computes a weighted sum of value vectors where weights (attention scores) come from query-key similarity via dot product and softmax. Self-attention lets each token attend to all others in the sequence. Multi-head attention runs several attention heads in parallel, capturing different relationships."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Architectures",
         text="What is the difference between LSTM and GRU?",
         answer="LSTM has three gates (input, forget, output) and a separate cell state — more expressive but heavier. GRU has two gates (reset, update) and no separate cell state — simpler and faster with similar performance on most tasks. Use LSTM for complex long-term dependencies; GRU when speed matters."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Transfer Learning",
         text="What is transfer learning and when should you use it?",
         answer="Transfer learning reuses a pretrained model (e.g. ResNet on ImageNet) as a starting point and fine-tunes on your task. Use when: small dataset, limited compute, or similar source and target domains. Freeze lower layers (general features), retrain upper layers (domain-specific). Drastically reduces data and compute requirements."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Architectures",
         text="How does a Generative Adversarial Network (GAN) work?",
         answer="A GAN has two networks: a Generator that creates fake samples and a Discriminator that distinguishes real from fake. They compete — Generator improves to fool Discriminator, Discriminator improves to detect fakes. At convergence, Generator produces realistic data. Used for image synthesis, data augmentation."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Google", topic="Transformers",
         text="What is the difference between BERT and GPT in terms of architecture and use case?",
         answer="BERT is encoder-only, trained with masked language modelling — predicts masked tokens using bidirectional context. Best for understanding tasks: classification, NER, QA. GPT is decoder-only, trained autoregressively — predicts next token. Best for generation tasks: text completion, summarisation, chatbots."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Any", topic="Training",
         text="How would you handle class imbalance when training a deep learning classifier?",
         answer="Options: (1) Class weights — penalise misclassification of minority class more. (2) Oversampling minority class (SMOTE). (3) Undersampling majority class. (4) Use focal loss instead of cross-entropy — down-weights easy examples. (5) Generate synthetic samples with GANs. (6) Threshold tuning at inference."),

    dict(subject="DL", difficulty="Hard", type="Coding", company="Amazon", topic="Training",
         text="What is the difference between model.train() and model.eval() in PyTorch?",
         answer="model.train() enables dropout and batch normalisation in training mode. model.eval() disables dropout (all neurons active) and switches batch norm to use running statistics instead of batch statistics. Always call model.eval() before inference and model.train() before training loops."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="Explain residual connections in ResNet and what problem they solve.",
         answer="ResNet adds skip connections that bypass one or more layers: output = F(x) + x. This solves the degradation problem — deeper networks were performing worse than shallower ones. Skip connections let gradients flow directly, making very deep networks (100+ layers) trainable. Also allows identity mapping as a baseline."),

    dict(subject="DL", difficulty="Medium", type="Situational", company="Any", topic="Applied DL",
         text="You are training a deep learning model and the training loss keeps decreasing but validation loss starts increasing after epoch 10. What is happening and what do you do?",
         answer="This is classic overfitting. The model is memorising training data. Fix: (1) Add dropout layers. (2) Add L2 regularisation on weights. (3) Use early stopping — stop training when validation loss stops improving. (4) Reduce model size. (5) Get more training data or use data augmentation."),

    dict(subject="DL", difficulty="Hard", type="Situational", company="Google", topic="Applied DL",
         text="Your image classification model works great on the test set but performs poorly on real-world images from a phone camera. What could be wrong?",
         answer="This is a domain shift problem. Training images may differ from phone camera images in brightness, angle, resolution, or compression. Fix: (1) Collect real-world images for fine-tuning. (2) Add data augmentation: brightness, rotation, noise, blur. (3) Use a more robust pretrained backbone. (4) Check if preprocessing (normalisation) is applied consistently in production."),

    # ─────────────────────────────────────────
    # DSA — 18 questions
    # ─────────────────────────────────────────
    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Arrays",
         text="What is the difference between an array and a linked list?",
         answer="Array: contiguous memory, O(1) random access, O(n) insert/delete. Linked list: non-contiguous nodes with pointers, O(n) access, O(1) insert/delete at head. Use arrays when random access is needed; linked lists when frequent insert/delete at arbitrary positions."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Wipro", topic="Data Structures",
         text="What is the difference between a stack and a queue?",
         answer="Stack is LIFO (Last In First Out) — push and pop from the same end. Use for: function call stack, undo operations, DFS. Queue is FIFO (First In First Out) — enqueue at rear, dequeue at front. Use for: BFS, task scheduling, print queues."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Infosys", topic="Searching",
         text="What is binary search and what is its time complexity?",
         answer="Binary search finds an element in a sorted array by repeatedly halving the search space. Compare target with middle element — if equal return it, if less search left half, if greater search right half. Time complexity: O(log n). Requires sorted input."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Graphs",
         text="Explain BFS vs DFS — when do you use each?",
         answer="BFS explores level by level using a queue — finds shortest path in unweighted graphs. DFS explores depth-first using a stack or recursion — use for cycle detection, topological sort, connected components. BFS uses more memory; DFS is simpler to implement recursively."),

    dict(subject="DSA", difficulty="Easy", type="Coding", company="Any", topic="Arrays",
         text="How do you find the maximum element in an array?",
         answer="Iterate through the array, keep track of the current maximum. Initialize max = arr[0], then for each element if arr[i] > max, update max = arr[i]. Return max. Time: O(n), Space: O(1). In Python: max(arr) does this in one line."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Amazon", topic="Sorting",
         text="What is the time and space complexity of quicksort in average and worst case?",
         answer="Average: O(n log n) time, O(log n) space. Worst case: O(n²) time when pivot always picks smallest/largest element (sorted array). Mitigate with random pivot or median-of-three. In-place (O(log n) stack space) and cache-friendly, preferred for general-purpose sorting."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Data Structures",
         text="How does a hash table work and how does it handle collisions?",
         answer="A hash table maps keys to indices via a hash function. Collision handling: (1) Chaining — each bucket holds a linked list of entries. (2) Open addressing — probe for the next empty slot (linear probing, quadratic probing). Average O(1) for get/set. Worst case O(n) if many collisions."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Amazon", topic="Linked Lists",
         text="How do you detect a cycle in a linked list?",
         answer="Use Floyd's cycle detection (tortoise and hare). Two pointers: slow moves one step, fast moves two steps. If they meet, there is a cycle. If fast reaches null, no cycle. Time: O(n), Space: O(1). Alternative: use a hash set to track visited nodes — O(n) space."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Google", topic="Arrays",
         text="How do you find all pairs in an array that sum to a target value?",
         answer="Use a hash set. For each element x, check if (target - x) exists in the set. If yes, found a pair. Add x to the set. Time: O(n), Space: O(n). Better than the brute force O(n²) approach of nested loops."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Any", topic="Trees",
         text="What is a binary search tree (BST) and what are its time complexities?",
         answer="BST is a binary tree where left child < node < right child. Search, insert, delete: O(h) where h is height. Balanced BST (AVL, Red-Black): O(log n). Worst case unbalanced (like a linked list): O(n). In-order traversal of BST gives sorted output."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Microsoft", topic="DP",
         text="What is dynamic programming? What makes a problem suitable for DP?",
         answer="DP solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation. A problem is suitable for DP if it has: (1) Optimal substructure — optimal solution built from optimal sub-solutions. (2) Overlapping subproblems — same subproblems solved repeatedly. Examples: Fibonacci, 0/1 Knapsack, LCS."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Microsoft", topic="Data Structures",
         text="How would you find the median of a real-time data stream?",
         answer="Use two heaps: max-heap for the lower half and min-heap for the upper half. For each new number: push to max-heap, then transfer max-heap top to min-heap. If min-heap is larger, transfer back. Median = max-heap top (odd count) or average of both tops (even). O(log n) per insertion, O(1) for median."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Google", topic="DP",
         text="Explain the longest common subsequence (LCS) problem and its DP solution.",
         answer="LCS finds the longest sequence present in both strings in the same order (not necessarily contiguous). DP table: dp[i][j] = LCS of first i chars of s1 and first j chars of s2. If s1[i]==s2[j]: dp[i][j] = dp[i-1][j-1]+1. Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1]). Time: O(mn), Space: O(mn)."),

    dict(subject="DSA", difficulty="Hard", type="Conceptual", company="Amazon", topic="Graphs",
         text="Explain Dijkstra's algorithm and its time complexity.",
         answer="Dijkstra finds shortest paths from a source to all nodes in a weighted graph with non-negative edges. Uses a min-heap priority queue. For each node, relax all neighbours — update distance if a shorter path is found. Time: O((V+E) log V) with a binary heap. Does not work with negative edge weights — use Bellman-Ford instead."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Google", topic="Trees",
         text="How do you check if a binary tree is balanced and what is the time complexity?",
         answer="A balanced binary tree has height difference between left and right subtrees at most 1, for every node. Recursive approach: compute height of left and right subtrees. If either returns -1 (unbalanced) or height difference > 1, return -1. Otherwise return max(left, right)+1. Time: O(n), Space: O(h) recursion stack."),

    dict(subject="DSA", difficulty="Medium", type="Situational", company="Amazon", topic="Applied DSA",
         text="You are designing a system that needs to find the most frequently searched keywords in real time from millions of queries per second. Which data structure would you use?",
         answer="Use a combination: (1) HashMap to count keyword frequencies in O(1). (2) Min-heap of size k to maintain top-k keywords — when a keyword's count exceeds the heap minimum, replace it. For real-time streaming, use a Count-Min Sketch for approximate frequency counting with O(1) updates and low memory. For exact top-k: HashMap + heap gives O(n log k)."),

    dict(subject="DSA", difficulty="Hard", type="Situational", company="Google", topic="Applied DSA",
         text="You are building a navigation app. Users ask for the shortest route between two cities. The road network has 1 million nodes. Which algorithm do you use and why?",
         answer="Use A* algorithm — an informed search that uses a heuristic (straight-line distance) to guide the search toward the destination, making it much faster than Dijkstra for point-to-point queries. For pre-processing, Contraction Hierarchies are used in production GPS systems (Google Maps, Waze) as they reduce query time to milliseconds on large graphs."),

    dict(subject="DSA", difficulty="Easy", type="Situational", company="TCS", topic="Applied DSA",
         text="You need to implement the undo functionality in a text editor. Which data structure would you use and why?",
         answer="Use a Stack. Every user action (type, delete, format) is pushed onto the stack. When the user presses Ctrl+Z, pop the top action and reverse it. For redo, use a second stack. This gives O(1) push and pop. Real editors like VS Code use a more complex command pattern but the core data structure is a stack."),

    # ─────────────────────────────────────────
    # PYTHON — 16 questions
    # ─────────────────────────────────────────
    dict(subject="Python", difficulty="Easy", type="Conceptual", company="TCS", topic="Data Types",
         text="What is the difference between a list and a tuple in Python?",
         answer="Lists are mutable (can change), use [], have more methods. Tuples are immutable (cannot change), use (), are faster and use less memory. Use tuples for fixed data (coordinates, DB records) and as dict keys. Lists for dynamic collections. Tuples are hashable; lists are not."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Infosys", topic="Data Types",
         text="What is the difference between a dictionary and a set in Python?",
         answer="Dictionary: key-value pairs, ordered (Python 3.7+), O(1) access by key. Set: unordered collection of unique elements, O(1) membership test. Both use hash tables. Use dict when you need to associate values with keys; set when you only need to track unique elements or perform union/intersection operations."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Wipro", topic="Syntax",
         text="What are list comprehensions and when should you use them?",
         answer="List comprehensions provide concise syntax: [x*2 for x in range(10) if x%2==0]. They are faster than equivalent for loops. Use them for simple transformations and filters. Avoid when: logic is complex (hurts readability), list is large (use generator expressions for memory efficiency), or nesting exceeds 2 levels."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="Syntax",
         text="What does the 'with' statement do in Python?",
         answer="The 'with' statement is a context manager that ensures proper resource cleanup. with open('file.txt') as f: automatically closes the file even if an exception occurs. Equivalent to try/finally. Works with any object implementing __enter__ and __exit__ methods. Common uses: file I/O, database connections, threading locks."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="TCS", topic="OOP",
         text="What is the difference between == and 'is' in Python?",
         answer="== checks value equality — do the two objects have the same value? 'is' checks identity — are they the exact same object in memory? Example: a=[1,2]; b=[1,2]; a==b is True but a is b is False. For None checks, always use 'is None' not '== None'."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Google", topic="Concurrency",
         text="What is Python's GIL and how does it affect ML code?",
         answer="The Global Interpreter Lock allows only one thread to execute Python bytecode at a time, even on multi-core machines. For CPU-bound ML tasks it limits true parallelism. Use multiprocessing (separate processes, each with its own GIL) to bypass it. NumPy, TensorFlow, and PyTorch release the GIL during C-level operations."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="OOP",
         text="What is the difference between a class method, static method, and instance method?",
         answer="Instance method: takes self, accesses instance and class data. Class method: decorated with @classmethod, takes cls, accesses class but not instance — used for alternative constructors. Static method: decorated with @staticmethod, takes neither self nor cls — just a utility function logically grouped in the class."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Amazon", topic="Syntax",
         text="What are Python decorators and give a practical example.",
         answer="Decorators wrap a function to add behaviour without modifying it. They use the @syntax. Example: @timer decorator measures execution time. @login_required in Flask checks authentication before a route runs. Built-ins: @staticmethod, @classmethod, @property. Internally they are higher-order functions that take and return a function."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Memory",
         text="What is the difference between shallow copy and deep copy in Python?",
         answer="Shallow copy (copy.copy) creates a new object but references the same nested objects. Deep copy (copy.deepcopy) creates a completely independent copy including all nested objects. Example: shallow copying a list of lists — modifying the inner list affects both copies. Deep copy prevents this."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Syntax",
         text="What are Python generators and why are they memory efficient?",
         answer="Generators produce values one at a time using the yield keyword, without storing all values in memory. Perfect for large datasets. Example: (x*2 for x in range(1000000)) uses almost no memory vs a list which stores all values. Use next() to get the next value or iterate in a for loop."),

    dict(subject="Python", difficulty="Medium", type="Coding", company="Google", topic="Data Structures",
         text="How would you count the frequency of each word in a large text file efficiently in Python?",
         answer="Use collections.Counter: from collections import Counter; counter = Counter(open('file.txt').read().split()). Counter is a dict subclass optimised for counting. most_common(10) gives top 10. For very large files, read line by line to avoid loading the whole file into memory: for line in f: counter.update(line.split())."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Google", topic="Concurrency",
         text="What is the difference between multiprocessing and multithreading in Python?",
         answer="Multithreading: multiple threads share the same memory space. Good for I/O-bound tasks (file read, network calls). Limited by GIL for CPU-bound work. Multiprocessing: multiple processes with separate memory. Bypasses GIL, good for CPU-bound tasks (ML training, data processing). Higher memory overhead. For ML: use multiprocessing for data loading (num_workers in DataLoader)."),

    dict(subject="Python", difficulty="Hard", type="Coding", company="Amazon", topic="OOP",
         text="Implement a singleton pattern in Python.",
         answer="Using a class variable: class Singleton: _instance=None; def __new__(cls): if cls._instance is None: cls._instance=super().__new__(cls); return cls._instance. Or using a decorator that wraps the class and returns the same instance on subsequent calls. Thread-safe version uses a lock to prevent race conditions in concurrent environments."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Any", topic="Memory",
         text="How does Python's garbage collection work?",
         answer="Python uses reference counting as the primary mechanism — when an object's reference count drops to zero it is freed. For circular references (A references B, B references A), a cyclic garbage collector runs periodically to detect and free them. The gc module lets you control this. Use del to explicitly decrement references."),

    dict(subject="Python", difficulty="Medium", type="Situational", company="Any", topic="Applied Python",
         text="You have a Python script that processes 10 million records and it is very slow. How would you optimise it?",
         answer="Step 1: Profile first using cProfile or line_profiler to find the bottleneck — do not optimise blindly. Step 2: Use vectorised operations with NumPy/Pandas instead of Python loops. Step 3: Use multiprocessing for CPU-bound work. Step 4: Use generators instead of lists for large datasets. Step 5: Consider chunking the data. Step 6: If I/O bound, use async or multithreading."),

    dict(subject="Python", difficulty="Hard", type="Situational", company="Google", topic="Applied Python",
         text="Your Python web scraper worked fine locally but crashes after 1000 requests in production. What do you check?",
         answer="Check: (1) Memory leak — are you storing all responses in memory? Use generators or flush data periodically. (2) Rate limiting — the server is blocking you. Add random delays between requests. (3) Session handling — reuse a requests.Session() instead of creating new connections. (4) Exception handling — wrap requests in try/except with retries using the tenacity library. (5) Rotating proxies and user-agents if being blocked."),

    # ─────────────────────────────────────────
    # STATISTICS — 16 questions
    # ─────────────────────────────────────────
    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Descriptive",
         text="What is the difference between mean, median, and mode?",
         answer="Mean: average of all values — sensitive to outliers. Median: middle value when sorted — robust to outliers. Mode: most frequent value — used for categorical data. Example: salary data with a few very high earners — median is more representative than mean. Always check the distribution before choosing a measure."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="TCS", topic="Probability",
         text="What is the difference between probability and statistics?",
         answer="Probability moves from model to data — given a fair coin, what is the chance of 3 heads? Statistics moves from data to model — given 3 heads in 3 flips, is the coin fair? Probability is deductive; statistics is inductive. ML uses both: probability for modelling uncertainty, statistics for learning from data."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Infosys", topic="Descriptive",
         text="What is standard deviation and what does it tell you?",
         answer="Standard deviation measures how spread out values are around the mean. Low SD = values clustered near mean. High SD = values spread widely. Formula: sqrt of average squared deviations from mean. Used in normalisation (z-score = (x - mean) / SD). SD is in the same units as the data, making it interpretable."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Probability",
         text="What is a normal distribution and why is it so important?",
         answer="A normal distribution is symmetric, bell-shaped, defined by mean and standard deviation. Important because: Central Limit Theorem says sample means approach normal regardless of original distribution. Many natural phenomena follow it. Most statistical tests assume it. 68% of data within 1 SD, 95% within 2 SD, 99.7% within 3 SD (empirical rule)."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Fractal Analytics", topic="Probability",
         text="What is the Central Limit Theorem and why does it matter in ML?",
         answer="CLT: the sampling distribution of the mean approaches normal as sample size grows, regardless of the original distribution. Matters in ML because it justifies using z-tests and t-tests on large samples, underlies confidence intervals, and explains why Gaussian assumptions work in practice even when data is not perfectly normal."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="MuSigma", topic="Hypothesis Testing",
         text="Explain Type I and Type II errors in hypothesis testing.",
         answer="Type I (false positive): rejecting a true null hypothesis. Controlled by significance level α (usually 5%). Type II (false negative): failing to reject a false null. Controlled by power (1-β). In ML: Type I = flagging innocent users as fraud. Type II = missing actual fraud. The tradeoff depends on which error costs more in your use case."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Amazon", topic="Hypothesis Testing",
         text="What does a p-value of 0.03 mean?",
         answer="A p-value of 0.03 means there is a 3% probability of observing results this extreme if the null hypothesis were true. Since 0.03 < 0.05, we reject H0 at 5% significance level. Common misconception: it does NOT mean H0 has 3% chance of being true. Also does not measure effect size — a significant result can be practically meaningless."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Correlation",
         text="What is the difference between correlation and causation?",
         answer="Correlation measures the linear relationship between two variables (Pearson r). Causation means one variable directly causes changes in another. Example: ice cream sales and drowning rates are correlated (both increase in summer) but ice cream does not cause drowning — a confounder (hot weather) drives both. Always think about confounders and use experiments to establish causation."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="MuSigma", topic="Testing",
         text="What is A/B testing and what are common pitfalls?",
         answer="A/B testing compares two variants (A=control, B=treatment) by randomly assigning users and measuring a metric. Common pitfalls: (1) Stopping early when results look significant (peeking problem). (2) Not ensuring random assignment (selection bias). (3) Multiple comparisons — testing many metrics inflates false positive rate. (4) Novelty effect — new feature looks better just because it is new. Use proper sample size calculation upfront."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Regression",
         text="What is multicollinearity and how does it affect regression models?",
         answer="Multicollinearity occurs when two or more predictors are highly correlated. It does not affect model predictions but makes coefficient estimates unstable and hard to interpret — small data changes cause large coefficient changes. Detection: VIF (Variance Inflation Factor) > 10 is problematic. Fix: remove one of the correlated features, use PCA, or use Ridge regression."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Fractal Analytics", topic="Regression",
         text="What does R-squared mean in linear regression and what are its limitations?",
         answer="R-squared measures the proportion of variance in the target explained by the model (0 to 1). R²=0.85 means the model explains 85% of variance. Limitations: always increases when you add more features even if useless — use Adjusted R² instead. Does not tell you if the model is appropriate (could be non-linear), does not indicate bias, and can be high even with a bad model if features are just noisy copies of the target."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Any", topic="Probability",
         text="What is Bayesian inference and how is it different from frequentist statistics?",
         answer="Frequentist: probability is the long-run frequency of events. Parameters are fixed, data is random. Uses p-values and confidence intervals. Bayesian: probability represents degree of belief. Starts with a prior belief about parameters, updates with data using Bayes theorem to get a posterior. Parameters are distributions, not fixed values. More flexible but computationally expensive."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="MuSigma", topic="Testing",
         text="What is the difference between a confidence interval and a prediction interval?",
         answer="Confidence interval: range where the true population parameter (e.g. mean) lies with given probability. Narrower, reflects uncertainty about the parameter. Prediction interval: range where a single new observation will fall with given probability. Wider, because it includes both parameter uncertainty AND natural data variability. Always use prediction intervals when making individual predictions."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Any", topic="Testing",
         text="What is the multiple comparisons problem and how do you correct for it?",
         answer="When you run many statistical tests simultaneously, the chance of at least one false positive increases. With 20 tests at α=0.05, you expect 1 false positive by chance. Corrections: Bonferroni — divide α by number of tests (conservative). Benjamini-Hochberg FDR — controls false discovery rate (less conservative, preferred in ML/genomics). Always specify hypotheses before seeing data."),

    dict(subject="Stats", difficulty="Medium", type="Situational", company="Fractal Analytics", topic="Applied Stats",
         text="Your A/B test shows a statistically significant improvement in click-through rate but your manager says not to ship. What might be their concern?",
         answer="Statistical significance does not mean practical significance. The improvement might be tiny — a 0.001% increase in CTR may not justify engineering cost and risk. Manager might also worry about: (1) Was the test run long enough? (2) Was the sample size pre-calculated? (3) Are there secondary metrics that degraded (revenue, bounce rate)? Always report effect size and confidence interval, not just p-value."),

    dict(subject="Stats", difficulty="Hard", type="Situational", company="MuSigma", topic="Applied Stats",
         text="You are analysing customer churn and find that customers who contact support more often churn less. Your colleague says to increase support contacts to reduce churn. What is wrong with this reasoning?",
         answer="This is confusing correlation with causation and reverse causation. Customers who contact support more might be more engaged with the product overall — engagement reduces churn, not support contacts. Artificially increasing support contacts for disengaged customers will not replicate this. To establish causation, run a randomised experiment. Also consider: maybe customers who would have churned never contacted support in the first place (survivorship bias)."),

    # ─────────────────────────────────────────
    # NLP — 17 questions
    # ─────────────────────────────────────────
    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="TCS", topic="Preprocessing",
         text="What is tokenisation in NLP and why does it matter?",
         answer="Tokenisation splits text into units (tokens) — words, subwords, or characters. It is the first step in any NLP pipeline. WordPiece and BPE (Byte Pair Encoding) are subword tokenisers used in BERT and GPT — they handle unknown words and reduce vocabulary size. Poor tokenisation loses meaning and affects all downstream tasks."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Infosys", topic="Preprocessing",
         text="What is the difference between stemming and lemmatisation?",
         answer="Stemming cuts word endings using rules (running → run, studies → studi) — fast but crude, can produce non-words. Lemmatisation uses vocabulary and morphology to return the base form (running → run, studies → study) — slower but linguistically correct. Use stemming for search engines where speed matters; lemmatisation for tasks needing linguistic accuracy."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Wipro", topic="Representations",
         text="What is TF-IDF and how is it used in NLP?",
         answer="TF-IDF scores word importance. TF (Term Frequency) = word count / total words in doc. IDF = log(total docs / docs with word). TF-IDF = TF × IDF. High score means the word is frequent in this document but rare across the corpus — discriminative. Used for document retrieval, text classification, and keyword extraction."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Representations",
         text="What is a bag of words model and what are its limitations?",
         answer="Bag of Words represents text as a vector of word counts, ignoring order and grammar. Simple and fast, works for many classification tasks. Limitations: (1) Loses word order and context. (2) High dimensionality with large vocabulary. (3) Cannot capture semantic similarity (king and monarch are unrelated). (4) Does not handle negation well (not good vs good)."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Embeddings",
         text="What are word embeddings and how does Word2Vec work?",
         answer="Word embeddings represent words as dense vectors in a continuous space where semantically similar words are close together. Word2Vec trains a shallow neural network on two tasks: CBOW (predict word from context) or Skip-gram (predict context from word). The hidden layer weights become the embeddings. king - man + woman ≈ queen is a famous example."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Embeddings",
         text="Explain the difference between Word2Vec, GloVe, and BERT embeddings.",
         answer="Word2Vec: local context windows, produces static embeddings — same word always has same vector. GloVe: global co-occurrence statistics, also static. BERT: transformer-based, produces contextual embeddings — same word gets different representations based on context. BERT embeddings are far superior for tasks requiring context understanding like NER, QA, and sentiment analysis."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Amazon", topic="Models",
         text="What is named entity recognition (NER) and how does a modern NER system work?",
         answer="NER identifies and classifies named entities in text: persons, organisations, locations, dates. Modern approach: pretrained transformer (BERT) fine-tuned on labelled NER data. The model outputs an IOB tag for each token (B-PER = beginning of person entity, I-PER = inside, O = outside). spaCy and HuggingFace Transformers provide pre-trained NER models."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Models",
         text="What is a language model and what does perplexity measure?",
         answer="A language model assigns probabilities to sequences of words or predicts the next word given context. Perplexity measures how well the model predicts a test set — lower is better. Perplexity = 2^(cross-entropy loss). A perplexity of 50 means the model is as confused as if choosing uniformly among 50 options. Used to compare language models on the same test set."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Models",
         text="How do GPT-style models differ from BERT-style models?",
         answer="BERT is encoder-only, bidirectional — sees left and right context simultaneously. Trained with masked language modelling. Best for understanding tasks: classification, NER, extractive QA. GPT is decoder-only, unidirectional (left to right). Trained autoregressively (predict next token). Best for generation: text completion, summarisation, chatbots, code generation."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Models",
         text="What is beam search in text generation and why is it used?",
         answer="Beam search keeps the top-k most probable partial sequences (beams) at each step instead of just the best one (greedy). At each step, it expands all beams and keeps only the top-k. Greedy search is fast but may miss the globally optimal sequence. Beam search with k=5 significantly improves quality. Trade-off: larger k = better quality but slower. Used in machine translation and summarisation."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Modern NLP",
         text="What is the difference between zero-shot, one-shot, and few-shot learning in LLMs?",
         answer="Zero-shot: model answers without any examples — relies purely on pretrained knowledge. One-shot: one example provided in the prompt. Few-shot: a few examples (typically 3-10) in the prompt. GPT-3 demonstrated strong few-shot performance, showing that large models generalise from just a few prompt examples without weight updates (in-context learning)."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Google", topic="Models",
         text="How does BERT use masked language modelling to pretrain?",
         answer="BERT masks 15% of input tokens randomly. For masked tokens: 80% replaced with [MASK], 10% replaced with a random word, 10% kept unchanged. The model must predict the original token. This forces bidirectional context learning. Also trained with Next Sentence Prediction (NSP) — predict if sentence B follows sentence A. Result: deep bidirectional representations."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Amazon", topic="Preprocessing",
         text="How would you handle out-of-vocabulary (OOV) words in NLP?",
         answer="Solutions: (1) Subword tokenisation (BPE, WordPiece) — rare words split into known subwords (playing → play + ##ing). Used by BERT, GPT. (2) Character-level models — no OOV at all. (3) FastText embeddings — generates embeddings from character n-grams so any word has a representation. (4) Map OOV to a special [UNK] token — simple but loses information."),

    dict(subject="NLP", difficulty="Hard", type="Coding", company="Any", topic="Applied NLP",
         text="How would you build a text sentiment classifier from scratch using Python?",
         answer="Steps: (1) Collect and label data (positive/negative/neutral). (2) Preprocess: lowercase, remove punctuation, tokenise. (3) Vectorise: TF-IDF or word embeddings. (4) Train classifier: Logistic Regression for baseline, then fine-tune BERT for best results. (5) Evaluate: accuracy, F1, confusion matrix. (6) For production: use HuggingFace pipeline('sentiment-analysis') for quick deployment."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Google", topic="Modern NLP",
         text="What is RAG (Retrieval Augmented Generation) and why is it used?",
         answer="RAG combines a retrieval system with a language model. Instead of relying on parametric knowledge baked into LLM weights, RAG retrieves relevant documents from an external database (using vector similarity search) and feeds them as context to the LLM. Benefits: reduces hallucinations, allows knowledge updates without retraining, provides citations. Used in enterprise chatbots and question-answering systems."),

    dict(subject="NLP", difficulty="Medium", type="Situational", company="Any", topic="Applied NLP",
         text="You are building a customer support chatbot. Users sometimes write in Hinglish (Hindi + English mixed). How would you handle this?",
         answer="Challenges: code-switching, transliteration (Hindi words in Roman script), informal grammar. Approach: (1) Use a multilingual model like mBERT or XLM-RoBERTa trained on 100+ languages. (2) Collect Hinglish-specific training data for fine-tuning. (3) Use language detection as a preprocessing step. (4) Consider transliteration tools to normalise Hindi words. (5) IndicBERT is specifically trained on Indian languages including code-switching."),

    dict(subject="NLP", difficulty="Hard", type="Situational", company="Google", topic="Applied NLP",
         text="Your text summarisation model produces summaries that are factually incorrect — it makes up information not in the source document. How do you fix this?",
         answer="This is called hallucination. Fixes: (1) Use extractive summarisation instead of abstractive — only use sentences from the source. (2) Add a faithfulness metric during training (FactCC, BERTScore against source). (3) Use RAG approach — constrain generation to retrieved source content. (4) Post-process: verify each claim in the summary appears in the source using NLI (natural language inference). (5) Use smaller, more factual models fine-tuned on verified summaries."),

    # ─────────────────────────────────────────
    # COMPUTER VISION — 16 questions
    # ─────────────────────────────────────────
    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is computer vision and give three real-world applications?",
         answer="Computer vision enables machines to interpret and understand visual information from images and video. Applications: (1) Medical imaging — tumour detection in MRI scans. (2) Autonomous vehicles — object detection and lane recognition. (3) Face recognition — phone unlock, security systems. (4) Quality control in manufacturing — defect detection. (5) Retail — cashierless stores like Amazon Go."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="TCS", topic="CNN",
         text="What are convolutional neural networks (CNNs) and why are they good for images?",
         answer="CNNs use convolutional filters that slide over the image detecting local patterns. Early layers detect edges, middle layers detect shapes, deep layers detect complex objects. Key properties: local connectivity (each neuron sees a small patch), weight sharing (same filter applied everywhere reduces parameters), translation invariance. Much more efficient than fully connected networks for images."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="CNN",
         text="What is the role of pooling layers in CNNs?",
         answer="Pooling reduces spatial dimensions (width, height) while retaining important features. Max pooling takes the maximum value in each window — preserves strong activations. Average pooling averages values — smoother. Benefits: reduces computation, provides translation invariance, reduces overfitting by summarising features, and reduces the number of parameters in deeper layers."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Infosys", topic="Preprocessing",
         text="What is image normalisation and why is it done before feeding images to a CNN?",
         answer="Normalisation scales pixel values (0-255) to a standard range like 0-1 or -1 to 1. Done by dividing by 255, or subtracting mean and dividing by std. Reasons: (1) Speeds up gradient descent — all inputs on same scale. (2) Prevents any one colour channel from dominating. (3) Matches pretrained model expectations (ImageNet models expect specific mean/std). Always normalise consistently at training and inference."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Transfer Learning",
         text="What is transfer learning and when should you use it in computer vision?",
         answer="Transfer learning reuses a model pretrained on a large dataset (ResNet on ImageNet) as a starting point. Fine-tune on your dataset. Use when: small dataset, limited GPU, or similar domains. Freeze early layers (general features like edges), retrain later layers (domain-specific). Even fine-tuning just the last layer (feature extraction) works well for similar tasks."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Architectures",
         text="What is the difference between ResNet, VGG, and EfficientNet?",
         answer="VGG: simple deep network with 3x3 convolutions, 138M parameters — large and slow but easy to understand. ResNet: introduces skip connections solving vanishing gradient, allows 100+ layer networks, 25M parameters. EfficientNet: scales width, depth, and resolution jointly using a compound coefficient — achieves better accuracy with fewer parameters. For production, EfficientNet or MobileNet are preferred for efficiency."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Object Detection",
         text="What is the difference between image classification and object detection?",
         answer="Classification: assigns one label to the entire image (cat or dog). Detection: finds and classifies multiple objects in an image with bounding boxes (3 cats at locations x1y1, x2y2, x3y3). Detection is harder — must solve both localisation and classification. Algorithms: YOLO (real-time), Faster R-CNN (more accurate). Segmentation goes further — pixel-level masks."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Object Detection",
         text="How does the YOLO algorithm work for object detection?",
         answer="YOLO (You Only Look Once) divides the image into an SxS grid. Each cell predicts B bounding boxes with confidence scores and C class probabilities simultaneously in a single forward pass. This makes it extremely fast (real-time). Unlike two-stage detectors (R-CNN) that first propose regions then classify, YOLO does it in one shot. Latest versions (YOLOv8) are both fast and accurate."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Augmentation",
         text="What is data augmentation in computer vision and why is it important?",
         answer="Data augmentation creates new training samples by applying random transformations to existing images: rotation, flipping, cropping, brightness change, zoom, adding noise. Prevents overfitting, improves generalisation, and effectively multiplies dataset size without collecting new data. Critical when training data is limited. Libraries: torchvision.transforms, albumentations (more powerful)."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Fractal Analytics", topic="Metrics",
         text="What is Intersection over Union (IoU) and how is it used in object detection?",
         answer="IoU measures overlap between predicted and ground truth bounding boxes: IoU = Area of Intersection / Area of Union. Range: 0 (no overlap) to 1 (perfect overlap). Used in: (1) Evaluation — mAP (mean Average Precision) uses IoU threshold (typically 0.5) to determine if a detection is correct. (2) Non-maximum suppression — removes duplicate detections by suppressing boxes with high IoU overlap."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="How do Vision Transformers (ViT) work and how do they differ from CNNs?",
         answer="ViT splits an image into fixed-size patches (e.g. 16x16 pixels), linearly embeds each patch, and processes them as tokens using a standard transformer encoder (like BERT). No convolutions — uses self-attention to relate all patches globally. CNNs use local receptive fields and inductive bias for translation invariance. ViT needs more data to train but scales better. Hybrid models combine both approaches."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Any", topic="Architectures",
         text="What is image segmentation and what are the different types?",
         answer="Segmentation assigns a label to every pixel. Types: (1) Semantic segmentation — all pixels of the same class get the same label (all cars are red). (2) Instance segmentation — each individual object gets a unique label (car1, car2 separately). (3) Panoptic segmentation — combines both. Algorithms: U-Net (medical imaging), Mask R-CNN (instance), DeepLab (semantic). Harder than detection as it requires pixel-level precision."),

    dict(subject="CV", difficulty="Hard", type="Coding", company="Amazon", topic="Applied CV",
         text="How would you build a pipeline to detect whether a person is wearing a face mask in a video stream?",
         answer="Steps: (1) Face detection — use MTCNN or OpenCV's Haar cascade to find face regions in each frame. (2) Crop and resize face region to 224x224. (3) Classify each face: fine-tune MobileNetV2 on a mask/no-mask dataset (fast and lightweight for real-time). (4) Draw bounding box with label and confidence. (5) For video: process every 3rd frame for efficiency. OpenCV handles video stream capture and display. Deploy with ONNX for production."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Any", topic="GANs",
         text="What are Generative Adversarial Networks (GANs) used for in computer vision?",
         answer="GANs generate realistic synthetic images. Applications: (1) Image synthesis — generate photorealistic faces (StyleGAN). (2) Image-to-image translation — horse to zebra (CycleGAN), sketch to photo (pix2pix). (3) Super-resolution — upscale low-res images (SRGAN). (4) Data augmentation — generate training samples for rare classes. (5) Inpainting — fill in missing parts of images. Training challenge: mode collapse and instability."),

    dict(subject="CV", difficulty="Medium", type="Situational", company="Any", topic="Applied CV",
         text="You are building a plant disease detection app for farmers. You have only 500 images per class. How would you train a good model?",
         answer="500 images per class is small. Strategy: (1) Use transfer learning — start with ResNet50 or EfficientNetB0 pretrained on ImageNet. Freeze early layers, fine-tune last 2-3 layers. (2) Heavy data augmentation: rotation, flip, zoom, brightness, hue shifts (plants vary in lighting). (3) Use test-time augmentation for better predictions. (4) Try few-shot learning methods if classes have < 100 images. (5) Collect more data from agricultural image databases. Expected accuracy: 85-90%+ with this approach."),

    dict(subject="CV", difficulty="Hard", type="Situational", company="Google", topic="Applied CV",
         text="Your medical image classification model achieves 95% accuracy but doctors refuse to use it. What might be their concern and how do you address it?",
         answer="Doctors need explainability and safety guarantees, not just accuracy. Concerns: (1) Black box — why did it predict cancer? Use Grad-CAM to visualise which regions influenced the prediction. (2) False negatives are catastrophic in medicine — report sensitivity/specificity, not just accuracy. (3) Was it tested on their patient population? Dataset shift between training hospital and their patients. (4) Regulatory approval needed (FDA/CE marking). Address by: adding explainability (Grad-CAM, LIME), reporting detailed metrics, clinical validation study, and involving doctors in development from the start."),

]

# Additional interview-ready questions. Each answer is written as a concise model
# response that a student can adapt and say naturally in an interview.
QUESTIONS.extend([
    # MACHINE LEARNING
    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Feature Engineering", text="What is feature scaling, and when is it important?", answer="Feature scaling puts numeric features on comparable ranges, commonly with standardisation to mean zero and unit variance. It is important for distance- or gradient-based models such as k-NN, k-means, SVM, logistic regression and neural networks. Tree-based models usually do not need it because they split by thresholds."),
    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Imbalanced Data", text="How would you handle a highly imbalanced classification dataset?", answer="First I would use precision, recall, F1, PR-AUC and the confusion matrix instead of accuracy. Then I would try class weights, over-sampling the minority class or under-sampling the majority class, while applying resampling only inside training folds. I would tune the decision threshold according to the business cost of false positives and false negatives."),
    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Validation", text="What is data leakage? Give an example and prevention strategy.", answer="Data leakage happens when training uses information unavailable at prediction time, producing overly optimistic validation scores. For example, fitting a scaler on the full dataset before a train-test split lets test statistics influence training. I prevent it by splitting early and putting preprocessing, feature selection and resampling inside a pipeline fitted only on each training fold."),
    dict(subject="ML", difficulty="Medium", type="Situational", company="Any", topic="Model Selection", text="How would you choose between a simple and a complex model?", answer="I would start with a simple, interpretable baseline and a meaningful validation scheme. I would choose the more complex model only if it gives a reliable improvement on held-out data that justifies its latency, maintenance and explainability cost. The final choice depends on the business metric, not training accuracy."),
    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Any", topic="Evaluation", text="When is ROC-AUC misleading, and what would you use instead?", answer="ROC-AUC can look high on a severely imbalanced dataset because true-negative rate dominates. If I care about finding rare positives, I would inspect precision-recall curves, PR-AUC, recall at a chosen precision and the confusion matrix at the operating threshold."),
    dict(subject="ML", difficulty="Hard", type="Situational", company="Any", topic="Monitoring", text="A model performed well at launch but degrades after three months. How would you investigate?", answer="I would first confirm that labels and the evaluation pipeline are correct. Then I would compare recent feature distributions, prediction distributions and performance by segment with the training period to detect data drift, concept drift or a pipeline change. I would set monitoring alerts, retrain only after validating new data, and keep a rollback model."),

    # DEEP LEARNING
    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Training", text="What is the difference between an epoch, batch and iteration?", answer="An epoch is one complete pass through the training dataset. A batch is the subset processed at once. An iteration is one parameter update, so an epoch contains roughly dataset size divided by batch size iterations."),
    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Optimisation", text="Why is Adam popular, and what is one limitation?", answer="Adam combines momentum-like first-moment estimates with adaptive per-parameter learning rates from second moments, so it usually trains quickly with little tuning. A limitation is that it can generalise worse than SGD with momentum in some vision tasks, so I still compare optimisers on validation performance."),
    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Regularisation", text="Explain early stopping and how you would use it.", answer="Early stopping stops training when validation performance no longer improves for a chosen patience period. I would save the checkpoint with the best validation metric, allow a few noisy epochs through patience, and use a validation set that represents deployment data. It reduces overfitting and wasted compute."),
    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Attention", text="What problem does attention solve in sequence models?", answer="Attention lets a model weigh the most relevant input tokens for each output token instead of compressing an entire sequence into one fixed vector. This improves long-range dependencies and enables transformers to process tokens in parallel during training."),
    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Any", topic="Training", text="What causes exploding gradients and how can you mitigate them?", answer="Exploding gradients occur when repeated multiplications through deep networks or long sequences make derivatives very large. I would use gradient clipping, sensible initialization, residual connections, normalization, a lower learning rate and architectures such as LSTMs or transformers where appropriate."),
    dict(subject="DL", difficulty="Hard", type="Situational", company="Any", topic="Deployment", text="How would you reduce the inference cost of a deep learning model?", answer="I would measure the latency and memory bottleneck first. Options include a smaller architecture, distillation into a student model, quantization, pruning, batching where latency allows, hardware-aware compilation and caching. I would verify accuracy and fairness after every optimisation rather than assuming the smaller model is acceptable."),

    # DATA STRUCTURES AND ALGORITHMS
    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Any", topic="Complexity", text="What is the difference between time complexity and space complexity?", answer="Time complexity describes how runtime grows with input size; space complexity describes how additional memory grows. I state both for an algorithm, including auxiliary memory. For example, merge sort runs in O(n log n) time and needs O(n) auxiliary space."),
    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Any", topic="Hashing", text="Why are hash-table operations O(1) on average but not always?", answer="A hash table maps keys to buckets, giving expected O(1) lookup, insertion and deletion when keys are distributed well and the load factor is controlled. Collisions can create long chains or probe sequences, giving O(n) worst case, so implementations resize and use robust hash functions."),
    dict(subject="DSA", difficulty="Medium", type="Coding", company="Any", topic="Arrays", text="How would you find the longest substring without repeating characters?", answer="I would use a sliding window and a map from character to its latest index. Move the right pointer through the string; if a character is already inside the window, move the left pointer just after its previous index. This visits each character at most twice, so the time is O(n) and space is O(min(n, alphabet size))."),
    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Any", topic="Graphs", text="When would you use BFS instead of DFS?", answer="I use BFS when I need the shortest path by number of edges in an unweighted graph, level-order traversal or the nearest state, because it explores layer by layer. DFS is useful for connectivity, cycle detection, topological sorting and exhaustive backtracking, often with lower queue memory on wide graphs."),
    dict(subject="DSA", difficulty="Hard", type="Conceptual", company="Any", topic="DP", text="How do you recognise a dynamic-programming problem?", answer="I look for optimal substructure and overlapping subproblems: the answer can be built from answers to smaller repeated states. I define the state, recurrence, base cases and iteration order, then decide whether memoization or tabulation is clearer. I also check whether the DP table can be compressed to save memory."),
    dict(subject="DSA", difficulty="Hard", type="Situational", company="Any", topic="System Design", text="How would you find the top K most frequent items in a very large stream?", answer="For exact results that fit in memory, I would count with a hash map then use a min-heap of size K, giving O(n log K). For an unbounded stream, I would use approximate heavy-hitter methods such as Count-Min Sketch plus a heap, and explain the accuracy-memory trade-off."),

    # PYTHON
    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="Functions", text="What are *args and **kwargs in Python?", answer="*args collects extra positional arguments into a tuple, while **kwargs collects extra keyword arguments into a dictionary. They make wrappers and flexible APIs possible. I use explicit named parameters for required inputs so the function remains readable."),
    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Data Types", text="What is the difference between a shallow copy and a deep copy?", answer="A shallow copy creates a new outer container but keeps references to nested objects, so changes to a nested mutable object appear in both. A deep copy recursively copies nested objects. I use copy.copy and copy.deepcopy deliberately, because deep copies can be expensive and sometimes unnecessary."),
    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Errors", text="How should exceptions be handled in production Python code?", answer="I catch specific exceptions close to the operation that can fail, add useful context through logging, and either recover or re-raise a meaningful error. I avoid bare except because it hides programming errors. I use finally or context managers for cleanup, and I do not expose sensitive internals to users."),
    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Iteration", text="What is a generator, and why would you use one?", answer="A generator yields values lazily instead of materialising the whole sequence. It is useful for large files, streams and pipelines because it saves memory and can start producing results immediately. The trade-off is that it is usually consumed once and may be less convenient for random access."),
    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Any", topic="Concurrency", text="When would you use threading, multiprocessing and asyncio?", answer="For I/O-bound work I use threading or asyncio; asyncio is especially effective when libraries are async and many tasks wait on network I/O. For CPU-bound Python code, multiprocessing bypasses the GIL using separate processes. I choose based on the workload, shared-state needs and operational overhead."),
    dict(subject="Python", difficulty="Hard", type="Situational", company="Any", topic="Testing", text="How would you make a Python data-processing function reliable?", answer="I would keep it small and deterministic, validate inputs, use type hints and write unit tests for normal, boundary and invalid cases. I would separate I/O from transformation logic, log useful metadata, and add integration tests around files or databases. For production pipelines I would make retries and writes idempotent."),

    # STATISTICS
    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Descriptive", text="When is median more useful than mean?", answer="The median is more robust to outliers and skewed distributions. For example, income and house prices often have a few very large values that pull the mean upward, so I would report the median with percentiles to describe a typical observation."),
    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Probability", text="What is conditional probability, and why is it useful?", answer="Conditional probability is the probability of event A given that event B occurred: P(A|B) = P(A and B) / P(B). It lets us update reasoning when new information is known, and it is the foundation of Bayes' theorem, diagnostic testing and many classification models."),
    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Experimentation", text="What is statistical power in an A/B test?", answer="Power is the probability of detecting a real effect of a chosen minimum size when it exists, equal to one minus the false-negative rate. It increases with sample size, effect size and a higher significance threshold. I calculate sample size before the test so an inconclusive result is not mistaken for no effect."),
    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Regression", text="What assumptions does linear regression make?", answer="Key assumptions are linearity in parameters, independent errors, roughly constant error variance, no severe multicollinearity and approximately normal residuals when doing small-sample inference. I check residual plots and diagnostics; prediction can still be useful if some inference assumptions are imperfect, but I state the limitation."),
    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Any", topic="Experimentation", text="Why is peeking at an A/B test repeatedly a problem?", answer="If we test significance after every small data update and stop when p is below 0.05, the false-positive rate becomes much higher than 5 percent. I would pre-register the sample size and stopping rule, or use a sequential-testing method designed for repeated looks."),
    dict(subject="Stats", difficulty="Hard", type="Situational", company="Any", topic="Causality", text="A correlation appears between a product feature and retention. Can you claim the feature caused retention?", answer="No. Users who choose the feature may already be more engaged, so selection bias or confounding can create the correlation. I would run a randomized experiment if ethical and feasible, or use a careful quasi-experimental design, then report uncertainty and remaining assumptions."),

    # NATURAL LANGUAGE PROCESSING
    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Tokenization", text="What is tokenization, and why does the choice matter?", answer="Tokenization splits text into units a model can process, such as words, subwords or characters. The choice affects vocabulary size, handling of rare words, sequence length and multilingual coverage. Modern transformer models often use subword tokenizers because they balance coverage and efficiency."),
    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Evaluation", text="Why is accuracy often insufficient for a text classifier?", answer="Accuracy hides which classes are failing, especially with imbalance. For spam, toxicity or medical text I would examine precision, recall, F1, per-class metrics and a confusion matrix. The right metric follows the error cost: missing harmful content and wrongly blocking safe content have different consequences."),
    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Embeddings", text="What are sentence embeddings used for?", answer="Sentence embeddings map whole texts to vectors where semantically similar texts are close together. I use them for semantic search, clustering, retrieval, duplicate detection and retrieval-augmented generation. I evaluate them on representative queries because similarity quality depends on the domain and model."),
    dict(subject="NLP", difficulty="Medium", type="Situational", company="Any", topic="LLM Safety", text="How would you reduce hallucinations in an LLM support chatbot?", answer="I would ground responses with retrieval from approved, current documents, require citations, instruct the model to say it does not know when evidence is missing, and add answer validation or confidence rules. I would also log failures, test adversarial prompts and keep humans in the loop for high-risk cases."),
    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Any", topic="Evaluation", text="How would you evaluate a retrieval-augmented generation system?", answer="I would evaluate retrieval and generation separately and end to end. Retrieval metrics include recall@K and MRR against relevant documents; answer metrics include correctness, faithfulness to retrieved context, citation quality, latency and user success. I would use a labelled test set plus human review for nuanced or safety-critical answers."),
    dict(subject="NLP", difficulty="Hard", type="Situational", company="Any", topic="Fine-tuning", text="When would you fine-tune an LLM rather than use prompting and RAG?", answer="I use prompting and RAG first for changing knowledge or document-grounded answers. I fine-tune when I need a stable style, task behaviour, format or domain pattern that prompting cannot achieve reliably, and I have high-quality examples. I still evaluate for regressions, privacy and cost before deploying."),

    # COMPUTER VISION
    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Preprocessing", text="Why are images normalized before training a vision model?", answer="Normalization makes pixel distributions consistent, which stabilizes gradients and speeds optimization. For pretrained models I use the normalization expected by the original training setup. I apply the same deterministic preprocessing at inference so training and production inputs match."),
    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Metrics", text="What is intersection over union, or IoU?", answer="IoU is the area of overlap between a predicted box or mask and the ground truth divided by their union. It measures localization quality. Object-detection metrics such as mAP count a detection as correct only when its class is right and its IoU exceeds a chosen threshold."),
    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Augmentation", text="How do you choose image augmentations?", answer="I choose transformations that represent realistic deployment variation while preserving the label: for example, lighting changes and small crops for everyday photos. I avoid transforms that change meaning, such as vertical flips for digit recognition or medical images when orientation matters. I validate each augmentation policy on held-out data."),
    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Detection", text="What is non-maximum suppression in object detection?", answer="A detector may predict several overlapping boxes for one object. Non-maximum suppression keeps the highest-confidence box and removes other boxes with IoU above a threshold. This produces one final detection per object, though the threshold must be tuned for crowded scenes."),
    dict(subject="CV", difficulty="Hard", type="Situational", company="Any", topic="Dataset Shift", text="A vision model works in daylight but fails at night. What would you do?", answer="I would first collect and label representative night examples and measure performance by lighting condition. I would inspect preprocessing and camera differences, then use targeted augmentation, domain adaptation or retraining with balanced day-and-night data. I would monitor this segment after launch rather than reporting only an overall score."),
    dict(subject="CV", difficulty="Hard", type="Situational", company="Any", topic="Deployment", text="How would you deploy an object detector on a mobile device?", answer="I would choose a mobile-friendly architecture, export to the platform runtime, and profile latency, memory, battery and accuracy on target devices. I would use quantization or distillation if needed, keep preprocessing consistent, and test across camera models and real lighting. A lightweight fallback or server option can handle difficult cases."),
])

# Scenario questions mirror the open-ended follow-ups commonly used in interviews.
QUESTIONS.extend([
    dict(subject="ML", difficulty="Medium", type="Situational", company="Any", topic="Business Metrics", text="A churn model has good offline accuracy, but the retention team says its recommendations are not useful. How would you respond?", answer="I would clarify the action the team can take and the value of saving a customer. Then I would inspect precision and recall among the highest-risk customers, calibration, lift over the current process and performance by segment. I would work with the team to choose a threshold based on intervention capacity and run a controlled test measuring retained customers, not only offline accuracy."),
    dict(subject="ML", difficulty="Hard", type="Situational", company="Any", topic="Fairness", text="You discover that a loan-approval model performs worse for one demographic group. What are your next steps?", answer="I would pause expansion of the affected use case, verify the labels and group definitions, and measure error rates, calibration and outcomes by group. I would investigate data quality, proxy variables and historical bias, involve legal and domain stakeholders, and test mitigations such as better data, constraints or a different decision process. I would document the trade-offs and monitor fairness after release."),
    dict(subject="DL", difficulty="Medium", type="Situational", company="Any", topic="Overfitting", text="Your training loss keeps falling but validation loss rises after a few epochs. What would you try?", answer="That pattern indicates overfitting. I would first check that the split and preprocessing are correct, then use early stopping, data augmentation, weight decay or dropout, and potentially a smaller model. I would compare changes on a fixed validation set and avoid tuning repeatedly on the final test set."),
    dict(subject="DL", difficulty="Hard", type="Situational", company="Any", topic="Data Quality", text="A deep model's performance drops after new labelled data is added. How would you diagnose it?", answer="I would compare the old and new datasets for label errors, duplicates, class balance, distribution shift and leakage. I would evaluate the old and new model on separate old and new validation slices and inspect high-loss examples. If labels are noisy, I would correct or down-weight them rather than simply training longer, then re-run the experiment with versioned data."),
    dict(subject="DSA", difficulty="Medium", type="Situational", company="Any", topic="Algorithm Choice", text="During an interview, your O(n squared) solution times out. How would you improve it?", answer="I would state the bottleneck clearly, examine repeated work and ask about input constraints. Depending on the pattern, I would consider sorting with two pointers, a hash map, a sliding window, binary search or dynamic programming. I would explain the new complexity, walk through an example and check edge cases before coding."),
    dict(subject="DSA", difficulty="Hard", type="Situational", company="Any", topic="Production Systems", text="A service needs to answer shortest-path queries on a graph that changes frequently. What trade-offs would you discuss?", answer="I would ask about graph size, update rate, weights, query latency and whether approximate answers are acceptable. Running Dijkstra per query is simple but expensive at scale; precomputation is fast for reads but costly to update. I would consider caching popular routes, incremental algorithms or partitioning, then measure the read-write workload before selecting a design."),
    dict(subject="Python", difficulty="Medium", type="Situational", company="Any", topic="Debugging", text="A Python API becomes slow only under heavy traffic. How would you investigate?", answer="I would reproduce the load safely and collect request latency, error rate, CPU, memory, database timing and dependency traces. I would profile hot paths and look for blocking I/O, connection-pool exhaustion, N+1 queries or lock contention. I would fix the measured bottleneck, add a regression load test and verify the change does not hide errors through excessive timeouts."),
    dict(subject="Python", difficulty="Hard", type="Situational", company="Any", topic="Data Integrity", text="A scheduled Python job sometimes writes duplicate records after retries. How would you fix it?", answer="I would make the operation idempotent by using a stable event or request identifier and a database unique constraint or upsert. I would distinguish transient failures from permanent ones, record retry state, and ensure that acknowledgement happens only after the durable write. Tests should simulate a failure between the write and acknowledgement."),
    dict(subject="Stats", difficulty="Medium", type="Situational", company="Any", topic="A/B Testing", text="An A/B test shows a small statistically significant improvement, but the team is unsure whether to launch. What would you say?", answer="Statistical significance alone is not a launch decision. I would report the confidence interval, practical effect size, guardrail metrics, duration, segment results and any multiple-testing issues. I would compare the expected business value with engineering and risk costs, then either launch gradually, run longer for precision or decide the gain is too small to justify rollout."),
    dict(subject="Stats", difficulty="Hard", type="Situational", company="Any", topic="Data Quality", text="You find many missing values in a key variable. How would you decide what to do?", answer="I would first understand why values are missing and whether missingness is random, related to observed data or related to the unseen value itself. I would quantify missingness by segment and time, consider an explicit missing indicator, and choose appropriate imputation or a model that handles missing values. I would validate the choice and avoid using future information in the imputation process."),
    dict(subject="NLP", difficulty="Medium", type="Situational", company="Any", topic="Data Quality", text="A sentiment model works on product reviews but fails on social-media posts. How would you improve it?", answer="I would examine examples to identify domain shift such as slang, abbreviations, sarcasm and different class balance. I would collect representative labelled social-media data, adapt preprocessing and fine-tune or retrain with a held-out target-domain evaluation set. I would also report uncertainty and route low-confidence posts for review if the use case is important."),
    dict(subject="NLP", difficulty="Hard", type="Situational", company="Any", topic="Privacy", text="A customer asks for an internal chatbot trained on confidential documents. What safeguards would you propose?", answer="I would use access-controlled retrieval so each user sees only documents they are authorized to view, encrypt data in transit and at rest, minimise retention and audit access. I would ensure the provider's data-use terms meet requirements, prevent document text from entering logs unnecessarily, test prompt-injection defenses and establish human escalation for sensitive requests."),
    dict(subject="CV", difficulty="Medium", type="Situational", company="Any", topic="Metrics", text="An object detector has high mAP but misses small objects that customers care about. What would you change?", answer="I would break metrics down by object size, class and confidence instead of relying on one overall mAP. I would inspect labels and examples, then consider higher input resolution, multi-scale features, anchor or architecture changes, and more representative small-object data. The acceptance metric should include recall for the small objects at the required precision."),
    dict(subject="CV", difficulty="Hard", type="Situational", company="Any", topic="Safety", text="A facial-recognition prototype is proposed for workplace access. What concerns would you raise?", answer="I would raise consent, privacy, legal compliance, bias across demographic groups, false-match harm, spoofing and whether less intrusive alternatives work. Before deployment I would require a clear purpose, independent evaluation by group, liveness detection, secure retention limits, human appeal paths and stakeholder approval. In many workplaces, a badge-based approach may be safer and more proportionate."),
])

# Large-scale, product-focused scenarios for interview practice.  These train
# students to explain assumptions, trade-offs, metrics and a safe rollout.
SCENARIO_QUESTIONS = [
    ('ML','Live-stream recommendations are slow during a cricket final. How would you improve them?','Use a two-stage system: precompute candidate content, then rank a small set online. Cache popular results, use low-latency features only, set latency SLOs, and fall back to a simple popular-now model when dependencies fail.'),
    ('ML','A fraud model blocks too many genuine payments during a sale. What would you do?','Inspect precision and false positives by merchant and customer segment, then tune the threshold using fraud versus customer-loss cost. Add a review or step-up-authentication path and validate the policy with a controlled rollout.'),
    ('ML','Your demand model is wrong on festival days. How would you fix it?','Add holiday, promotion and event features, evaluate separately on event periods, and retrain with representative history. I would keep a seasonal baseline and monitor forecast error so unusual events are detected early.'),
    ('ML','A model is trained on one city and launched in another. What risks do you check?','I check population, behavior, data-collection and label differences. I evaluate by city before launch, collect local labels, use a cautious rollout, and monitor drift and business metrics after release.'),
    ('ML','Sales asks for a model score with no explanation. What do you provide?','I provide the score plus calibrated confidence, top understandable drivers where appropriate, the intended use, limits and a recommended action. I avoid presenting correlation as causation and give users a path to challenge bad data.'),
    ('ML','Labels arrive 30 days after prediction. How can you monitor the model now?','Monitor input drift, prediction distribution, missingness and pipeline health immediately. When labels arrive, join them to prediction snapshots for delayed performance metrics; use leading business indicators but do not mistake them for ground truth.'),
    ('ML','A stakeholder wants one global threshold for every customer. How do you respond?','I explain that a single threshold may be unfair or inefficient if costs and base rates differ. I compare segment performance, agree policy constraints with stakeholders, and choose thresholds only when legally and operationally justified.'),
    ('ML','Training data contains customer names. How do you protect privacy?','Remove direct identifiers, minimise features, restrict access, encrypt data and log access. I would assess re-identification risk, use approved retention rules, and ensure the model cannot expose training examples.'),
    ('ML','An executive wants accuracy improved by tomorrow. What is your plan?','I would set realistic expectations and first diagnose errors, data quality and the metric. I can test safe quick wins such as threshold tuning or a baseline ensemble, but production changes require validation, rollback and monitoring.'),
    ('ML','The model performs well overall but poorly for new users. What do you do?','Slice results by user tenure, identify unavailable history features, and create cold-start features or a separate new-user strategy. A rules or popularity fallback can be better until enough behavior is available.'),
    ('ML','How would you launch a new model safely?','Version data, code and model; validate offline; run shadow traffic; then use a small canary with guardrails. Monitor quality, latency, fairness and business impact, keep the previous model ready, and expand only after success criteria are met.'),
    ('DL','A video model must detect unsafe content within seconds. What architecture concerns matter?','I would balance accuracy with end-to-end latency: sample frames intelligently, use an efficient model, batch only within the latency budget, and use a fast high-recall first stage followed by a stronger verifier. Human review should handle uncertain high-risk cases.'),
    ('DL','GPU costs double after traffic grows. How do you reduce them?','Profile utilization and latency, then try batching, mixed precision, quantization, distillation and a smaller model. Autoscale workers and cache repeated inference, but validate accuracy and tail latency on real traffic.'),
    ('DL','A model trained on professional images fails on phone cameras. What is your response?','This is domain shift. Collect representative phone images, inspect compression and lighting differences, use realistic augmentation, and fine-tune with a target-domain validation set. Track performance by device after rollout.'),
    ('DL','Your classifier is confident on nonsense images. How would you handle it?','Add out-of-distribution testing, calibrate confidence, and use an abstain or review path for uncertain inputs. I would train with diverse negatives where useful and log novel inputs for later analysis.'),
    ('DL','Training suddenly becomes unstable after a code change. What do you check?','Reproduce with fixed seeds, compare data, preprocessing, loss, optimizer and learning rate to the last good run. Inspect gradients and activations for NaNs, then change one variable at a time with experiment tracking.'),
    ('DL','You have only 200 labelled images for a new class. What would you do?','Start with transfer learning, careful augmentation and a small validation split. Consider active learning to label the most informative examples and report uncertainty; I would not claim reliable performance without representative test data.'),
    ('DL','A team asks to retrain the neural model every hour. Is that sensible?','Only if labels, drift and business value justify it. Frequent retraining can amplify bad data and create operational risk. I would separate feature refresh from model retraining, validate candidates, and use a promotion gate.'),
    ('DL','Mobile inference is too slow on older devices. What is your plan?','Profile on target hardware, use a mobile architecture, quantize or distill, reduce input size where acceptable and use hardware delegates. I would set device-specific fallbacks and test quality across the supported device range.'),
    ('DL','A model misses rare but dangerous cases. Which metric do you optimise?','I focus on recall or sensitivity at an acceptable precision, not average accuracy. I would inspect the rare-case data, use class weighting or targeted collection, and add a human escalation path for low-confidence cases.'),
    ('DL','How do you explain a vision model decision to a nontechnical reviewer?','Show the input, predicted class, confidence, and an explanation such as a saliency map with clear limitations. I explain that it is supporting evidence, not proof, and pair it with error rates and human review guidance.'),
    ('DL','A supplier changes image resolution without notice. How do you prevent outages?','Validate input schema and dimensions at the boundary, resize through a versioned preprocessing pipeline, alert on distribution changes, and keep contract tests with suppliers. Invalid inputs should degrade gracefully rather than crash inference.'),
    ('DSA','How would you design a queue for millions of live chat messages?','Partition messages by room, append to a durable log, and let consumers process each partition in order. Use backpressure, bounded retries and dead-letter handling; the key trade-off is ordering versus throughput.'),
    ('DSA','Hotstar has millions joining one live event. Which data structures help serve viewers?','Use a CDN with cache-friendly segment keys for video, consistent hashing to distribute sessions, queues for asynchronous work and counters or sketches for approximate real-time analytics. Avoid a central mutable structure on the request path.'),
    ('DSA','How do you find duplicate events in a high-volume stream?','For an exact short window, store event IDs in a hash set with TTL. For very large streams, use a probabilistic Bloom filter and accept false positives, or a durable keyed store when exactness is required.'),
    ('DSA','A leaderboard updates constantly. How can you return top 100 quickly?','Maintain scores in a balanced ordered structure or a heap plus index, depending on update patterns. For distributed scale, shard by user and merge shard top lists; define how much eventual consistency is acceptable.'),
    ('DSA','A service repeatedly recomputes the same expensive result. What do you use?','Use memoization or a cache keyed by input and version. Choose TTL and eviction policy, protect against stampedes with request coalescing, and invalidate safely when source data changes.'),
    ('DSA','You need shortest routes but some roads update every minute. What would you explain?','Discuss graph size, weighted edges, update rate and latency. Per-query Dijkstra is simple; precomputed paths are fast but expensive to update. Caching and incremental updates can help when traffic is localized.'),
    ('DSA','How do you prevent one slow consumer from exhausting a message queue?','Use consumer groups, bounded in-flight work, backpressure and rate limits. Scale consumers where ordering permits, monitor lag, and move repeatedly failing messages to a dead-letter queue.'),
    ('DSA','A URL shortener needs fast lookup. What is the core lookup design?','Map a short code to the long URL in a hash-based key-value store, cache hot keys, and use replication for reads. I would discuss collision handling, expiry, analytics writes and consistency requirements.'),
    ('DSA','You must merge sorted logs from many servers. What algorithm do you choose?','Use a min-heap containing the current item from each stream. Pop the minimum and push the next from that stream, giving O(N log k) time and O(k) extra memory.'),
    ('DSA','How would you detect a cycle in a dependency graph?','Use DFS with visiting and visited states; reaching a visiting node means a cycle. For build ordering, topological sort also exposes a cycle when not all nodes can be processed.'),
    ('DSA','What do you do when an interviewer gives unclear constraints?','State the assumptions I need: input size, ordering, memory, latency and edge cases. I propose a simple solution first, then improve it once constraints are confirmed, explaining complexity at each step.'),
    ('Python','A background job crashes halfway through processing a file. How do you make it recoverable?','Process in idempotent chunks, checkpoint progress durably, and record each completed item with a unique key. On retry, skip completed work and send permanently bad records to a review queue.'),
    ('Python','A web API leaks memory over several days. How would you debug it?','Track memory over time, capture heap snapshots and inspect object growth. I would check caches, global references, unclosed files and tasks, then reproduce under load and add a regression test after fixing the retained object.'),
    ('Python','How would you handle 10,000 outbound HTTP calls reliably?','Use async I/O or a bounded worker pool, connection reuse, concurrency limits, timeouts and retries with exponential backoff and jitter. I would classify errors and use a circuit breaker for failing dependencies.'),
    ('Python','A data script is slow because it loops over a large table. What can improve it?','Profile first, then move filtering and aggregation to the database, batch I/O, use vectorized libraries where suitable and avoid per-row network calls. I would measure memory as well as runtime before and after.'),
    ('Python','A configuration change breaks production. How do you reduce this risk?','Validate configuration at startup, keep it versioned, use safe defaults and separate environments. Roll out changes gradually, support quick rollback and never put secrets in source code or logs.'),
    ('Python','Multiple workers update the same record. How do you avoid races?','Use database transactions with appropriate isolation, optimistic version checks or a scoped lock. Make writes idempotent and handle conflicts explicitly rather than assuming a read-modify-write sequence is safe.'),
    ('Python','An API dependency times out intermittently. What should your code do?','Set connect and read timeouts, retry only safe transient failures with backoff, and add a circuit breaker. Return a clear fallback or error, log correlation IDs, and do not retry non-idempotent writes blindly.'),
    ('Python','How would you secure a file-upload endpoint?','Enforce authentication, size and type limits, generate server-side names, scan files, store outside the web root and use least-privilege access. I would never trust the filename or MIME type supplied by the client.'),
    ('Python','Your tests pass locally but fail in CI. What do you investigate?','Compare Python and dependency versions, environment variables, time zones, filesystem behavior and hidden test order dependencies. I would pin dependencies, remove reliance on global state and make tests deterministic.'),
    ('Python','A batch task must run daily exactly once. What caveat would you mention?','Distributed exactly-once execution is difficult. I would use a scheduler plus a durable run key, idempotent writes and monitoring; duplicate execution should be safe, and missed runs should be detectable and replayable.'),
    ('Python','A junior developer uses bare except everywhere. How would you improve it?','Catch only expected exceptions, log context, preserve the traceback when re-raising and separate recovery from programming errors. Bare except can hide bugs such as KeyboardInterrupt and make operations unsafe.'),
    ('Stats','Hotstar sees a spike in watch time during a match. How do you tell whether a new feature caused it?','Compare against a randomized control exposed over the same event window, with pre-specified metrics and guardrails. Event traffic is a confounder, so before-after comparison alone cannot establish causality.'),
    ('Stats','An experiment result is significant but only by 0.1 percent. What do you recommend?','Report the confidence interval and practical value, not only the p-value. I would check guardrails and cost, then choose gradual launch, more data for precision or no launch if the effect is too small to matter.'),
    ('Stats','A dashboard average improves while user complaints rise. What do you inspect?','Break the metric into distributions and segments: median, percentiles, geography, device and new versus existing users. Averages can hide a harmed minority, so I would pair the dashboard metric with complaint and reliability guardrails.'),
    ('Stats','A survey has a very low response rate. Why is that risky?','Respondents may differ systematically from nonrespondents, creating selection bias. I would compare known demographics, adjust cautiously with weights, improve sampling and report that the result may not represent all users.'),
    ('Stats','Conversion rises after a homepage redesign. What alternative explanations exist?','Seasonality, campaigns, traffic mix, tracking changes and regression to the mean can explain it. I would verify instrumentation and use an A/B test or a credible counterfactual before attributing the change to the redesign.'),
    ('Stats','How would you set an alert threshold for stream startup failures?','Use historical baseline and variance by time and region, then choose a threshold balancing missed incidents and alert noise. I would require persistence across a few intervals and review the alert after real incidents.'),
    ('Stats','A stakeholder removes outliers to make a chart look better. What do you say?','I ask why they are outliers and whether they are data errors or meaningful customers. I show results with and without them, use robust summaries, document the rule and avoid deleting inconvenient valid observations.'),
    ('Stats','How do you estimate the sample size for a new experiment?','Specify the primary metric, baseline, minimum meaningful effect, desired power and significance level, then calculate sample size. I also account for clustering, multiple variants and expected drop-off before committing to duration.'),
    ('Stats','Why can a high correlation in a feature dashboard be dangerous?','It may be a proxy for a confounder, a data leak or chance among many comparisons. I would validate timing and definitions, test on new data and use experiments or causal methods before making a causal decision.'),
    ('Stats','An A/B test is run in many countries. How do you report results?','Report the overall result plus country estimates and uncertainty, checking whether effects truly differ rather than overreacting to noise. I would predefine key segments and adjust interpretation for multiple comparisons.'),
    ('Stats','A metric has a long tail. Which summaries do you show?','Show median, p75, p95, p99 and a distribution plot alongside the mean. For latency and spend, tail behavior often matters most, so I would define an SLO using a percentile.'),
    ('NLP','A live-chat moderation model must act in under 100 ms. How do you design it?','Use a lightweight high-recall classifier or rules on the request path, cache common patterns and send borderline content to an asynchronous stronger model or human review. Measure false positives because unnecessary blocking damages conversation.'),
    ('NLP','A support chatbot answers confidently from an outdated policy. How do you fix it?','Use retrieval from a versioned approved source, show citations, set document freshness rules and make the model abstain when evidence is absent. Test policy updates before release and monitor unanswered or disputed queries.'),
    ('NLP','Users try prompt injection against an internal assistant. What controls help?','Treat retrieved text as untrusted, separate instructions from data, restrict tool permissions, filter and test hostile inputs, and require authorization at the tool layer. Logging and red-team evaluation are essential because no prompt alone is sufficient.'),
    ('NLP','A multilingual classifier performs poorly for one language. What do you investigate?','Check data volume, label consistency, tokenizer coverage, dialects and translation artifacts. Collect native-speaker-reviewed examples, evaluate by language and subgroup, and avoid claiming global quality from an English-heavy test set.'),
    ('NLP','How would you build search for thousands of help articles?','Index keyword fields for exact matches and embeddings for semantic recall, retrieve a small candidate set and rerank it. Track click success, zero-result rate, latency and freshness, with access controls applied before retrieval.'),
    ('NLP','The chatbot sometimes exposes one user\'s data to another. What is the priority?','Treat it as a security incident: stop or restrict the affected capability, preserve evidence, notify the security process and fix authorization at retrieval and tool boundaries. I would not rely on prompt wording to enforce data isolation.'),
    ('NLP','How do you evaluate summaries of long incident reports?','Use representative reports and score factual faithfulness, coverage of key actions, harmful omissions, readability and time saved. Combine automated checks with expert review, because fluent text can still invent facts.'),
    ('NLP','A text classifier degrades after product terminology changes. What do you do?','Monitor vocabulary and error drift, collect recent labelled examples and update the model or retrieval resources. I would retain an evaluation set for old and new terms so improvement does not regress established categories.'),
    ('NLP','Should you fine-tune or use RAG for an employee handbook assistant?','Use RAG for changing handbook facts and citations. Fine-tuning may help stable tone or output format, but it is not a substitute for current source retrieval and access controls.'),
    ('NLP','How do you handle abusive language that is quoted in a news discussion?','Use context-sensitive labels and allow reviewer escalation rather than treating every keyword identically. Evaluate false positives on reclaimed, quoted and educational uses, then make the enforcement policy transparent.'),
    ('NLP','An LLM tool can send emails. What safeguards are required?','Require explicit user confirmation for consequential sends, restrict recipients and scopes, validate generated fields, log actions and use least-privilege credentials. The model should propose actions, not silently perform irreversible ones.'),
    ('CV','During a live sports stream, camera angles change and player tracking fails. What would you do?','Measure failures by camera and motion type, then train with multi-view and motion-blur examples or use a tracker that re-identifies after occlusion. Keep confidence-aware fallback behavior and verify latency on the live pipeline.'),
    ('CV','A retail shelf detector works in one store but not another. How do you respond?','Inspect lighting, camera placement, product assortment and annotation differences. Collect target-store data, calibrate cameras, augment realistically and report results by store rather than relying on one global metric.'),
    ('CV','A safety camera model has false alarms at night. What would you change?','Slice errors by lighting and weather, inspect infrared or exposure differences, then add representative data and augmentation. Tune the decision policy with the operations team so alarms can trigger verification rather than unnecessary emergency action.'),
    ('CV','How would you handle an object detector receiving a corrupted video frame?','Validate decoding and dimensions, drop or mark invalid frames, and avoid feeding undefined data to the model. Track corruption rate, alert when it rises and use the last safe state only when the product requirements permit it.'),
    ('CV','A model must run on an edge camera with poor connectivity. What is the design?','Run essential inference locally with a compact model, buffer encrypted events, and sync summaries when connectivity returns. Use remote processing only for selected clips, with clear retention and failure behavior.'),
    ('CV','The training set has very few examples of a rare safety helmet violation. What do you do?','Collect real representative examples first, then use targeted augmentation and class-aware sampling. Evaluate recall for the rare class and use human review for uncertain cases; synthetic data should supplement, not replace, validation.'),
    ('CV','A customer asks why a camera flagged their face. How do you respond technically?','Provide the policy-approved explanation, confidence and audit trail without exposing other people\'s data or overstating model certainty. Ensure there is a human appeal process and investigate systematic error by demographic group.'),
    ('CV','How do you deploy a vision-model update with minimal risk?','Run offline regression tests, shadow it on live frames, compare outputs and latency, then canary by device group. Monitor drift and failures, retain the previous model, and roll back automatically if guardrails are breached.'),
    ('CV','How would you measure annotation quality for bounding boxes?','Sample labels for expert review, compute inter-annotator agreement and inspect IoU disagreements by class. Define clear guidelines and feedback loops; poor labels can cap model quality even with a better architecture.'),
    ('CV','A CCTV analytics system stores more video than policy allows. What should change?','Enforce retention deletion automatically, minimise stored footage, separate metadata from video, restrict access and audit use. Privacy and legal requirements should shape the architecture, not be added after deployment.'),
    ('CV','Your model is fast on a GPU server but slow in production cameras. What do you check?','Profile end to end: capture, decode, preprocessing, transfer, inference and postprocessing. Optimise the measured bottleneck, test target hardware and monitor p95 latency rather than only model inference time.'),
]
QUESTIONS.extend(dict(subject=subject, difficulty='Hard', type='Situational', company='Any', topic='Real-world Scenarios', text=text, answer=answer) for subject, text, answer in SCENARIO_QUESTIONS)

# HR answers give students a clear structure without sounding memorised.
HR_QUESTIONS = [
    ('Easy','Introduction','Tell me about yourself.','I am a data science and AI student with a strong interest in turning data into useful products. Through my coursework and projects, I have built skills in Python, machine learning and problem solving. I am now looking for a role where I can learn from a strong team, contribute reliably and grow into an engineer who understands both users and technology.'),
    ('Easy','Motivation','Why do you want to work here?','I am interested in this role because the work connects technology with real user impact. I have researched your products and the skills this team uses, and they match the direction I want to grow in. I would bring curiosity, a willingness to learn quickly and a disciplined approach to delivering work.'),
    ('Easy','Strengths','What are your strengths?','One strength is structured problem solving: I break an unclear problem into assumptions, data and small testable steps. Another is ownership: when I commit to a task, I communicate progress and ask for help early if I am blocked. For example, this helped me complete team projects on time while keeping the work documented.'),
    ('Medium','Self-awareness','What is one weakness you are working on?','Earlier, I sometimes spent too long trying to make an early solution perfect. I now time-box exploration, share a working version sooner and ask for feedback before polishing. This has made me faster while still keeping quality high.'),
    ('Medium','Projects','Explain a project you are proud of.','I would explain the problem, my specific role, the approach, result and learning. For example: I built a model-based project, cleaned and validated the data, compared a baseline with an improved approach, and documented the evaluation. The key learning was that clear metrics and reliable data mattered as much as the model itself.'),
    ('Medium','Failure','Tell me about a failure and what you learned.','In one project, I assumed the first approach would work and did not validate it early enough. When the result failed, I informed the team, identified the incorrect assumption and rebuilt a smaller baseline. I learned to test risks early, communicate sooner and treat setbacks as information rather than hide them.'),
    ('Medium','Teamwork','Describe a time you worked with someone who disagreed with you.','I first listened to understand the other person\'s goal and evidence. Then I proposed agreeing on a shared metric or small experiment instead of debating opinions. In a team project, this helped us choose an approach based on results, while keeping the relationship respectful.'),
    ('Medium','Conflict','How do you handle conflict in a team?','I address it early and privately, focus on the work rather than the person, and clarify the shared goal. I ask for each view, use facts or a small test to resolve technical disagreements, and involve a lead only when the team cannot move forward fairly.'),
    ('Medium','Ownership','Tell me about a time you took initiative.','I noticed that a repeated task was causing delays, so I proposed a simple checklist or automation, validated it with the team and documented how to use it. I would emphasise the problem, my action, the measurable improvement and how I made sure the change helped others.'),
    ('Medium','Pressure','How do you work under pressure or tight deadlines?','I clarify the outcome and deadline, split work into the highest-value tasks, communicate risks early and avoid sacrificing critical quality checks. If the scope is unrealistic, I propose a smaller safe deliverable first, then continue iterating after the deadline.'),
    ('Medium','Feedback','How do you react to feedback?','I listen without becoming defensive, ask for a concrete example and turn it into an action. I then follow up after applying the feedback. I see useful feedback as a faster way to improve, even when it is difficult to hear.'),
    ('Medium','Learning','How do you learn a new technology quickly?','I begin with the problem it solves and a small hands-on example, then read official documentation and build a focused mini-project. I keep notes, ask targeted questions and teach back what I learned. This helps me move from theory to practical understanding quickly.'),
    ('Hard','Ethics','What would you do if you found a privacy or security issue in your work?','I would avoid exposing the issue further, preserve the relevant evidence and report it immediately through the company\'s security or manager process. I would not attempt an unapproved fix on production data. I would help assess impact, remediate safely and document prevention steps.'),
    ('Hard','Ethics','Your manager asks you to use data in a way that feels unethical. What do you do?','I would ask clarifying questions and explain the specific privacy, fairness or compliance concern respectfully. I would propose a safer alternative and follow the established escalation process if needed. Protecting users and acting with integrity is more important than silently doing something harmful.'),
    ('Medium','Career Goals','Where do you see yourself in five years?','In five years, I want to be a dependable professional who can own meaningful technical problems from understanding the user need through delivery and measurement. I also want to support newer teammates. I am focused on learning deeply now, rather than claiming a fixed title too early.'),
    ('Medium','Role Fit','Why should we hire you?','I bring a solid foundation in the role\'s core skills, genuine interest in learning and a reliable working style. I can communicate clearly, accept feedback and work through problems systematically. I may be early in my career, but I will prepare well, take ownership and contribute positively to the team.'),
    ('Medium','Priorities','How do you prioritise when multiple tasks are urgent?','I compare impact, deadline, dependency and risk, then confirm priorities with the relevant stakeholder rather than guessing. I communicate what I can deliver, break work into milestones and raise conflicts early. This keeps urgent work visible without losing important long-term commitments.'),
    ('Hard','Salary','What are your salary expectations?','I am mainly looking for a role with strong learning and meaningful responsibility. I am open to a fair, market-aligned package based on the role, location and total opportunity. I would be happy to understand the company\'s range and discuss it thoughtfully.'),
    ('Medium','Relocation','Are you willing to relocate or work in a hybrid setting?','I am open to the working arrangement required for the role and would plan responsibly for it. I would confirm practical details such as location, start date and expectations early, because being dependable includes being clear about availability.'),
    ('Easy','Questions for Interviewer','Do you have any questions for us?','Yes. I would ask: What does success look like in the first three to six months? How does the team give feedback and support learning? What technical or business problem is most important for this role to solve? These questions show that I care about contributing effectively.'),
]
QUESTIONS.extend(dict(subject='HR', difficulty=difficulty, type='HR', company='Any', topic=topic, text=text, answer=answer) for difficulty, topic, text, answer in HR_QUESTIONS)

def seed():
    db = SessionLocal()
    try:
        existing = db.query(Question).count()
        if existing > 0:
            print(f"⚠️  {existing} questions already in DB.")
            ans = input("Delete existing and reseed? (y/n): ").strip().lower()
            if ans != 'y':
                print("Skipping seed.")
                return
            db.query(Question).delete()
            db.commit()
            print("🗑️  Deleted existing questions.")

        for q in QUESTIONS:
            db.add(Question(**q))

        db.commit()
        print(f"✅ Seeded {len(QUESTIONS)} questions successfully.")

        # Print summary
        from sqlalchemy import func
        counts = db.query(Question.subject, func.count(Question.id)).group_by(Question.subject).all()
        print("\n📊 Questions per subject:")
        for subject, count in sorted(counts):
            print(f"   {subject}: {count} questions")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
