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

# ══════════════════════════════════════════════════════════════
# NEW QUESTIONS — BATCH 2  (expanding to 400+)
# ══════════════════════════════════════════════════════════════

QUESTIONS.extend([

    # ─────────────────────────────────────────
    # MACHINE LEARNING — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Algorithms",
         text="How does Naive Bayes work and what is the 'naive' assumption?",
         answer="Naive Bayes applies Bayes' theorem with the assumption that all features are conditionally independent given the class label. Despite this 'naive' assumption rarely holding in practice, it works surprisingly well for text classification, spam filtering and sentiment analysis. It is fast, simple and needs little training data."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Wipro", topic="Clustering",
         text="How does K-Means clustering work?",
         answer="K-Means partitions data into K clusters by iteratively assigning each point to the nearest centroid, then recomputing centroids as the mean of assigned points. It repeats until centroids stabilise. You must choose K in advance (using elbow method or silhouette score). It assumes spherical, equally-sized clusters."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Infosys", topic="Algorithms",
         text="What is logistic regression and how does it differ from linear regression?",
         answer="Logistic regression predicts the probability of a binary outcome using a sigmoid function that maps a linear combination of features to [0,1]. Unlike linear regression which predicts continuous values, logistic regression outputs probabilities and uses log-loss (cross-entropy) as its cost function."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between multi-class and multi-label classification?",
         answer="Multi-class means each sample belongs to exactly one of K classes (e.g., classifying an image as cat, dog, or bird). Multi-label means each sample can belong to multiple classes simultaneously (e.g., a movie tagged as both 'comedy' and 'romance'). Different loss functions and architectures are used for each."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Preprocessing",
         text="What are common strategies for handling missing data?",
         answer="Common strategies: deletion (drop rows/columns if missingness is random and small), imputation with mean/median/mode, model-based imputation (KNN imputer, iterative imputer), or using algorithms that handle missing values natively (XGBoost). The choice depends on the missingness pattern (MCAR, MAR, MNAR) and data size."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between parametric and non-parametric models?",
         answer="Parametric models assume a fixed functional form and have a fixed number of parameters regardless of data size (e.g., linear regression, logistic regression). Non-parametric models make fewer assumptions and their complexity grows with data (e.g., KNN, decision trees, kernel SVM). Parametric models are faster but may underfit complex patterns."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Wipro", topic="Evaluation",
         text="What is precision and recall, and when do you prioritise one over the other?",
         answer="Precision is TP/(TP+FP) — how many predicted positives are correct. Recall is TP/(TP+FN) — how many actual positives are found. Prioritise precision when false positives are costly (spam filter). Prioritise recall when false negatives are costly (cancer detection). F1-score balances both."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Clustering",
         text="What is the difference between DBSCAN and K-Means?",
         answer="K-Means requires specifying K and assumes spherical clusters. DBSCAN discovers clusters of arbitrary shape based on density, requires epsilon (neighbourhood radius) and min_points parameters, and automatically identifies noise points. DBSCAN handles outliers better but struggles with varying density clusters."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Infosys", topic="Feature Engineering",
         text="What is one-hot encoding and when would you use it?",
         answer="One-hot encoding converts categorical variables into binary columns, one per category. Use it for nominal (unordered) categories like colour or country. For high-cardinality features, consider target encoding or embedding instead to avoid dimensionality explosion. Ordinal categories can use label encoding."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What is the difference between a generative and discriminative model?",
         answer="Discriminative models learn the boundary between classes directly (P(y|x)), like logistic regression and SVM. Generative models learn the joint distribution P(x,y) and can generate new samples, like Naive Bayes and GANs. Discriminative models usually have better classification accuracy; generative models can handle missing data and generate synthetic data."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Clustering",
         text="How do you choose the optimal number of clusters in K-Means?",
         answer="Common methods: Elbow method (plot inertia vs K, look for the 'elbow'), Silhouette score (measures cluster cohesion vs separation, higher is better), Gap statistic (compares inertia to a null reference distribution), and domain knowledge. No single method is definitive — use multiple and validate with business context."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Interpretability",
         text="What are SHAP values and how do they help explain model predictions?",
         answer="SHAP (SHapley Additive exPlanations) assigns each feature an importance value for a specific prediction based on game theory. SHAP values sum to the difference between the model output and the average prediction. They provide consistent, locally faithful explanations and can show both global feature importance and individual prediction breakdowns."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Interpretability",
         text="What is LIME and how does it differ from SHAP?",
         answer="LIME (Local Interpretable Model-agnostic Explanations) explains individual predictions by fitting a simple interpretable model locally around the prediction. Unlike SHAP which has theoretical guarantees from Shapley values, LIME is faster but can produce inconsistent explanations. SHAP is more computationally expensive but provides theoretically grounded feature attributions."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Hyperparameters",
         text="Compare grid search, random search, and Bayesian optimisation for hyperparameter tuning.",
         answer="Grid search exhaustively evaluates all combinations — thorough but exponentially expensive. Random search samples randomly and often finds good results faster since not all hyperparameters are equally important. Bayesian optimisation (e.g., Optuna, Hyperopt) builds a probabilistic model of the objective and selects promising configurations, balancing exploration and exploitation. It is most efficient for expensive evaluations."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Ensembles",
         text="What is stacking in ensemble methods and how does it work?",
         answer="Stacking trains multiple diverse base models (e.g., Random Forest, SVM, Neural Net), then uses their predictions as input features for a meta-learner (often logistic regression or a simple model). The meta-learner learns the optimal way to combine base model predictions. It typically uses cross-validated predictions to avoid overfitting."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Flipkart", topic="Recommendation",
         text="What is the difference between collaborative filtering and content-based recommendation?",
         answer="Collaborative filtering recommends based on user-item interaction patterns (users who liked X also liked Y) without needing item features. Content-based filtering uses item attributes to recommend similar items. Collaborative filtering suffers from cold-start for new users/items; content-based is limited to known features. Hybrid approaches combine both."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Time Series",
         text="What makes time series data different from regular tabular data?",
         answer="Time series data has temporal ordering, autocorrelation (values depend on past values), and potential trends, seasonality and non-stationarity. You cannot randomly split train/test — you must use temporal splits. Feature engineering involves lags, rolling statistics and calendar features. Models must respect the temporal structure."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Dimensionality",
         text="How does t-SNE differ from PCA for dimensionality reduction?",
         answer="PCA is linear — it finds orthogonal directions of maximum variance. t-SNE is non-linear — it preserves local neighbourhood structure by minimising KL divergence between high and low-dimensional probability distributions. PCA is fast, deterministic and preserves global structure. t-SNE is slow, stochastic, great for visualisation but not suitable for preprocessing or new data projection."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Anomaly Detection",
         text="What are the main approaches to anomaly detection?",
         answer="Statistical methods (z-score, IQR), distance-based (KNN, LOF — Local Outlier Factor), model-based (Isolation Forest, One-Class SVM), density-based (DBSCAN), and deep learning (autoencoders where reconstruction error flags anomalies). Choice depends on data dimensionality, labelled anomalies availability, and whether anomalies are global or contextual."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Learning Types",
         text="What is semi-supervised learning and when is it useful?",
         answer="Semi-supervised learning uses a small amount of labelled data with a large amount of unlabelled data. Techniques include self-training (model labels unlabelled data, retrains), co-training (two models teach each other), and graph-based methods. Useful when labelling is expensive (medical imaging, NLP) but unlabelled data is abundant."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Learning Types",
         text="What is active learning and how does it reduce labelling cost?",
         answer="Active learning lets the model query the most informative unlabelled samples for human labelling, rather than labelling randomly. Strategies include uncertainty sampling (label samples the model is least confident about), query-by-committee, and expected model change. This dramatically reduces the number of labels needed to achieve good performance."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Calibration",
         text="What is probability calibration and why does it matter?",
         answer="A calibrated classifier's predicted probabilities match the true frequency of outcomes — if it predicts 70% probability, the event should occur 70% of the time. Many models (SVM, Random Forest) are poorly calibrated. Calibration matters for decision-making, risk assessment and when you threshold predictions. Methods include Platt scaling and isotonic regression."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="MLOps",
         text="What is model versioning and why is it important in MLOps?",
         answer="Model versioning tracks different iterations of models along with their code, data, hyperparameters and metrics. Tools like MLflow, DVC and Weights & Biases enable this. It is critical for reproducibility, rollback capability, A/B testing in production, audit trails, and collaboration. Without it, you cannot reliably reproduce or compare experiments."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Feature Engineering",
         text="What are some common feature engineering techniques for tabular data?",
         answer="Key techniques: binning continuous variables, polynomial features, interaction features, target encoding for categoricals, date/time decomposition (day of week, month), log/sqrt transforms for skewed distributions, aggregation features (group statistics), lag features for temporal data, and domain-specific features. Good feature engineering often matters more than model choice."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Any", topic="Feature Selection",
         text="What are the main approaches to feature selection?",
         answer="Filter methods use statistical tests (correlation, chi-squared, mutual information) independently of the model. Wrapper methods evaluate feature subsets with the model (forward selection, backward elimination, recursive feature elimination). Embedded methods learn feature importance during training (L1 regularisation, tree-based importance). Filters are fastest; wrappers are most accurate but expensive."),

    dict(subject="ML", difficulty="Medium", type="Coding", company="Google", topic="Algorithms",
         text="How would you implement K-Means clustering from scratch?",
         answer="1. Randomly initialise K centroids. 2. Assign each point to the nearest centroid using Euclidean distance. 3. Recompute centroids as the mean of assigned points. 4. Repeat steps 2-3 until centroids do not change (or max iterations reached). Use K-Means++ initialisation for better starting centroids. Track inertia (sum of squared distances) for convergence."),

    dict(subject="ML", difficulty="Medium", type="Coding", company="Amazon", topic="Evaluation",
         text="How would you implement stratified K-fold cross-validation from scratch?",
         answer="1. Compute class proportions in the full dataset. 2. Separate indices by class. 3. Shuffle indices within each class. 4. Distribute indices across K folds such that each fold has approximately the same class distribution as the full dataset. 5. For each fold, use it as validation and the rest as training. This ensures each fold is representative, critical for imbalanced data."),

    dict(subject="ML", difficulty="Medium", type="Coding", company="Microsoft", topic="Preprocessing",
         text="How would you write a custom feature transformer compatible with sklearn's Pipeline?",
         answer="Create a class inheriting from sklearn's BaseEstimator and TransformerMixin. Implement fit() to learn parameters from training data (e.g., means for imputation) and transform() to apply the transformation. TransformerMixin provides fit_transform() automatically. Store fitted parameters as attributes ending with _ (sklearn convention). This ensures proper train/test separation in pipelines."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Google", topic="AutoML",
         text="What is AutoML and what are its limitations?",
         answer="AutoML automates model selection, hyperparameter tuning, feature engineering and architecture search (e.g., Auto-sklearn, H2O, Google AutoML). Limitations: computationally expensive, may not outperform domain-expert feature engineering, can be a black box, may not handle data quality issues, and requires careful validation to avoid overfitting during the search process itself."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Amazon", topic="Recommendation",
         text="Explain matrix factorisation for recommendation systems.",
         answer="Matrix factorisation decomposes the sparse user-item rating matrix into two lower-rank matrices (user factors and item factors). The dot product of a user vector and item vector predicts the rating. ALS (Alternating Least Squares) and SGD are common optimisation methods. It handles sparsity well, captures latent factors, but struggles with cold-start. Modern approaches add side information and deep learning."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Google", topic="Dimensionality",
         text="Explain UMAP and how it compares to t-SNE for dimensionality reduction.",
         answer="UMAP (Uniform Manifold Approximation and Projection) is based on Riemannian geometry and topological data analysis. Compared to t-SNE, UMAP is significantly faster, scales better to large datasets, better preserves global structure, supports arbitrary embedding dimensions, and can transform new data points. Both are non-linear and useful for visualisation, but UMAP is generally preferred in practice."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Microsoft", topic="Fairness",
         text="What are the main metrics for measuring fairness in ML models?",
         answer="Key fairness metrics: demographic parity (equal positive prediction rates across groups), equalised odds (equal TPR and FPR across groups), predictive parity (equal precision), individual fairness (similar individuals get similar predictions), and counterfactual fairness. These metrics can conflict — satisfying all simultaneously is often mathematically impossible (impossibility theorem). The choice depends on context and legal requirements."),

    dict(subject="ML", difficulty="Hard", type="Situational", company="Google", topic="MLOps",
         text="You need to deploy an ML model that must handle 10,000 requests per second. What architecture would you design?",
         answer="Use a model serving framework (TensorFlow Serving, TorchServe, or Triton Inference Server) behind a load balancer. Batch inference requests for throughput. Cache frequent predictions. Optimise the model (quantisation, pruning, ONNX conversion). Use horizontal scaling with Kubernetes. Monitor latency percentiles (p50, p95, p99). Consider a feature store for real-time feature computation and an A/B testing framework for safe rollouts."),

    dict(subject="ML", difficulty="Hard", type="Situational", company="Amazon", topic="Data Quality",
         text="You discover that your training data has systematic label noise — about 15% of labels are incorrect. How do you handle this?",
         answer="Approaches: confident learning (identify likely mislabelled samples using model predictions and clean them), label smoothing to make the model less sensitive to noise, noise-robust loss functions (symmetric cross-entropy, generalised cross-entropy), training with noise-aware regularisation, crowdsourcing for re-labelling suspicious samples, and using ensemble agreement to flag noisy labels. The cleanlab library automates confident learning."),

    dict(subject="ML", difficulty="Hard", type="Situational", company="Meta", topic="Scale",
         text="Your training dataset has 100 million rows and does not fit in memory. How do you train a model?",
         answer="Options: out-of-core learning with algorithms that support partial_fit (SGDClassifier, MiniBatchKMeans), distributed frameworks (Spark MLlib, Dask-ML, Ray), gradient-boosted trees with data sampling (XGBoost external memory mode), online learning, or deep learning with data loaders and batching. Also consider feature selection to reduce dimensionality, and data sampling if the full dataset is not necessary for convergence."),

    dict(subject="ML", difficulty="Hard", type="Situational", company="Netflix", topic="Recommendation",
         text="You are building a movie recommendation system. Users complain that recommendations are repetitive and lack diversity. What do you do?",
         answer="Introduce diversity metrics alongside relevance (Intra-List Diversity, coverage, novelty). Use re-ranking strategies: Maximal Marginal Relevance (MMR) to balance relevance and diversity. Add exploration mechanisms (epsilon-greedy, Thompson sampling). Incorporate serendipity by occasionally recommending outside the user's typical preferences. Use multi-objective optimisation and A/B test the diversity-relevance tradeoff."),

    # ─────────────────────────────────────────
    # DEEP LEARNING — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What is a loss function and name three common ones?",
         answer="A loss function measures how far model predictions are from true labels, guiding optimisation. Common ones: MSE (mean squared error) for regression, cross-entropy (log loss) for classification, and binary cross-entropy for binary classification. The choice of loss function directly affects what the model optimises for."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Wipro", topic="Training",
         text="What is the difference between a hyperparameter and a learnable parameter?",
         answer="Learnable parameters (weights, biases) are updated by the optimiser during training. Hyperparameters (learning rate, batch size, number of layers) are set before training and control the learning process. Hyperparameters are tuned via validation performance; learnable parameters are tuned by gradient descent."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Initialisation",
         text="Why is weight initialisation important in neural networks?",
         answer="Bad initialisation causes vanishing or exploding gradients, making training fail. If weights are too small, signals shrink to zero through layers. If too large, they explode. Xavier initialisation works well with sigmoid/tanh; He initialisation works well with ReLU. Proper initialisation ensures gradients flow well and training converges faster."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Infosys", topic="Fundamentals",
         text="What is a softmax function and where is it used?",
         answer="Softmax converts a vector of raw scores (logits) into a probability distribution that sums to 1. Each output is exp(z_i) / sum(exp(z_j)). It is used as the final layer in multi-class classification networks, followed by cross-entropy loss. For binary classification, sigmoid is used instead."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="TCS", topic="Architectures",
         text="What is an autoencoder and what is it used for?",
         answer="An autoencoder is a neural network that learns to compress input into a lower-dimensional representation (encoder) and reconstruct it (decoder). It is used for dimensionality reduction, denoising, anomaly detection (high reconstruction error = anomaly), and learning useful representations. Variants include variational autoencoders (VAE) for generative modelling."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Training",
         text="What is the role of the learning rate in training neural networks?",
         answer="The learning rate controls how much weights are updated per gradient step. Too high: training oscillates or diverges. Too low: training is very slow and may get stuck in poor local minima. Common practice is to start with a moderate learning rate and use a schedule (cosine decay, step decay) or adaptive optimisers (Adam) that adjust it automatically."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Wipro", topic="Architectures",
         text="What is the difference between a dense (fully connected) layer and a convolutional layer?",
         answer="Dense layers connect every neuron to every neuron in the next layer — parameter count grows quadratically. Convolutional layers use small learnable filters that slide across the input, sharing parameters. Convolutions exploit spatial locality and translation invariance, making them much more parameter-efficient for grid-structured data like images."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is forward propagation and backpropagation?",
         answer="Forward propagation passes input through the network layer by layer to compute predictions. Backpropagation computes the gradient of the loss with respect to each weight by applying the chain rule backwards through the network. These gradients are then used by the optimiser to update weights. Together they form the core training loop."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Infosys", topic="Training",
         text="What is data augmentation in deep learning and why is it important?",
         answer="Data augmentation creates modified versions of training data (rotations, flips, crops, colour jitter for images; synonym replacement for text) to increase effective dataset size and diversity. It reduces overfitting, improves generalisation and is especially valuable when training data is limited. Augmentations should be semantically valid for the task."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between a Variational Autoencoder (VAE) and a regular autoencoder?",
         answer="A regular autoencoder maps inputs to fixed latent vectors. A VAE maps inputs to a distribution (mean and variance), samples from it, and reconstructs. The KL divergence term in VAE's loss encourages the latent space to be smooth and continuous, enabling meaningful interpolation and generation of new samples. VAEs are generative models; regular autoencoders are not."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Initialisation",
         text="What is the difference between Xavier and He weight initialisation?",
         answer="Xavier (Glorot) initialisation sets weights from N(0, 2/(n_in + n_out)), designed for sigmoid/tanh activations to keep variance stable across layers. He initialisation uses N(0, 2/n_in), designed for ReLU activations which kill half the signal. Using Xavier with ReLU leads to dying neurons; using He with sigmoid/tanh can cause saturation."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Amazon", topic="Training",
         text="What are learning rate schedules and name three common ones?",
         answer="Learning rate schedules adjust the learning rate during training. Step decay: reduce LR by a factor at fixed epochs. Cosine annealing: smoothly decreases LR following a cosine curve. Warmup + decay: start with a small LR, linearly increase to peak, then decay — essential for transformer training. One-cycle policy combines warmup with cosine decay for fast convergence."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Efficiency",
         text="What is knowledge distillation and why is it used?",
         answer="Knowledge distillation trains a smaller 'student' model to mimic a larger 'teacher' model's predictions (soft labels) rather than just learning from hard ground-truth labels. The soft labels contain richer information about inter-class relationships. This compresses model knowledge into a smaller, faster model suitable for deployment. Temperature scaling controls the softness of probability distributions."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Architectures",
         text="What are depthwise separable convolutions and why are they efficient?",
         answer="Depthwise separable convolutions split a standard convolution into two steps: depthwise convolution (applies a single filter per input channel) and pointwise convolution (1x1 convolution to combine channels). This reduces computation from O(K²·C_in·C_out) to O(K²·C_in + C_in·C_out), roughly 8-9x fewer operations. Used in MobileNet and EfficientNet for mobile deployment."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Training",
         text="What is mixed precision training and what are its benefits?",
         answer="Mixed precision training uses both FP16 (half precision) and FP32 (full precision) during training. Forward and backward passes use FP16 for speed; weight updates and loss scaling use FP32 for numerical stability. Benefits: 2-3x faster training, 50% less memory (enabling larger batches), with negligible accuracy loss. Supported via NVIDIA Tensor Cores and frameworks like PyTorch AMP."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Amazon", topic="Efficiency",
         text="What is gradient accumulation and when would you use it?",
         answer="Gradient accumulation simulates larger batch sizes by accumulating gradients over multiple forward-backward passes before performing a weight update. If your GPU can only fit batch size 8 but you want effective batch size 32, you accumulate gradients over 4 steps. Useful when memory-constrained but large batches are needed for training stability (especially with batch normalisation and transformer models)."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Meta", topic="Training",
         text="What is the difference between data parallelism and model parallelism?",
         answer="Data parallelism splits data across GPUs — each GPU has a copy of the full model and processes different mini-batches, then gradients are averaged. Model parallelism splits the model across GPUs — different layers or components on different GPUs. Data parallelism is simpler and more common. Model parallelism is needed when the model itself does not fit on one GPU (large transformers)."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Efficiency",
         text="What is model quantisation and what are its tradeoffs?",
         answer="Quantisation converts model weights and activations from FP32 to lower precision (INT8, INT4). Post-training quantisation is fast but may lose accuracy. Quantisation-aware training simulates quantised inference during training for better accuracy. Tradeoffs: 2-4x smaller model, 2-4x faster inference, but potential accuracy degradation especially for sensitive tasks. Critical for edge and mobile deployment."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Loss Functions",
         text="What is focal loss and when would you use it?",
         answer="Focal loss modifies cross-entropy by down-weighting easy examples and focusing on hard, misclassified ones using a focusing parameter gamma. FL = -alpha * (1-p)^gamma * log(p). When gamma=0, it reduces to standard cross-entropy. Introduced for object detection (RetinaNet) to handle extreme class imbalance between background and foreground. Also useful for any highly imbalanced classification task."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Loss Functions",
         text="What is contrastive loss and triplet loss?",
         answer="Contrastive loss takes pairs of samples and minimises distance for similar pairs while maximising it for dissimilar ones. Triplet loss takes an anchor, a positive (same class), and a negative (different class), pushing anchor-positive closer and anchor-negative farther by at least a margin. Both are used for learning embeddings in face recognition, similarity search, and metric learning."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Optimisers",
         text="Compare SGD with momentum, RMSProp, and AdamW.",
         answer="SGD+momentum accumulates past gradients for faster convergence and smoother updates. RMSProp adapts per-parameter learning rates using a running average of squared gradients — good for non-stationary objectives. AdamW combines momentum and adaptive rates with proper weight decay decoupling. SGD+momentum often generalises better; Adam converges faster. AdamW is standard for transformers."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Self-Supervised",
         text="What is self-supervised learning and give two examples?",
         answer="Self-supervised learning creates supervisory signals from the data itself, without human labels. Examples: masked language modelling (BERT predicts masked tokens), contrastive learning (SimCLR learns by comparing augmented views of the same image). The learned representations transfer well to downstream tasks. It bridges the gap between unsupervised and supervised learning."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Generative",
         text="How do diffusion models work at a high level?",
         answer="Diffusion models work in two phases: forward process gradually adds Gaussian noise to data until it becomes pure noise; reverse process learns to denoise step-by-step to reconstruct data. A neural network is trained to predict the noise at each step. At generation time, start from random noise and iteratively denoise. They produce high-quality, diverse samples and are behind DALL-E 2, Stable Diffusion, and Midjourney."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Meta", topic="Fine-Tuning",
         text="What is LoRA and why is it popular for fine-tuning large models?",
         answer="LoRA (Low-Rank Adaptation) freezes the pre-trained model weights and adds small trainable low-rank matrices to attention layers. Instead of fine-tuning all parameters, it trains only the low-rank additions (often less than 1% of parameters). This dramatically reduces memory, storage and compute while achieving comparable performance to full fine-tuning. Multiple LoRA adapters can be stored and swapped efficiently."),

    dict(subject="DL", difficulty="Medium", type="Coding", company="Google", topic="Training",
         text="How would you implement a custom training loop in PyTorch?",
         answer="Structure: 1) Define model, loss function, optimizer. 2) Loop over epochs. 3) For each batch: forward pass (predictions = model(inputs)), compute loss, call loss.backward() to compute gradients, call optimizer.step() to update weights, call optimizer.zero_grad() to clear gradients. 4) Evaluate on validation set each epoch. 5) Add learning rate scheduling, early stopping, and model checkpointing."),

    dict(subject="DL", difficulty="Medium", type="Coding", company="Amazon", topic="Architectures",
         text="How would you implement a simple multi-layer perceptron in PyTorch?",
         answer="Define a class inheriting nn.Module. In __init__, define layers: nn.Linear(input_dim, hidden_dim), nn.ReLU(), nn.Linear(hidden_dim, output_dim). In forward(), pass input through layers sequentially. For classification, add nn.Softmax or use nn.CrossEntropyLoss which includes softmax. Use nn.Sequential for simpler architectures. Add dropout between layers for regularisation."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="Explain the transformer architecture in detail — what are the key components?",
         answer="Transformers use self-attention to process sequences in parallel. Key components: multi-head self-attention (captures dependencies between all positions), positional encoding (injects sequence order since there is no recurrence), feed-forward networks (applied per position), layer normalisation, and residual connections. Encoder processes input; decoder generates output with masked attention. The attention formula is softmax(QK^T/sqrt(d_k))V."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Meta", topic="Self-Supervised",
         text="Explain contrastive learning frameworks like SimCLR and how they learn representations.",
         answer="SimCLR: 1) Create two augmented views of each image. 2) Pass both through an encoder and a projection head. 3) Use NT-Xent (normalised temperature-scaled cross-entropy) loss to pull augmented views of the same image together and push different images apart in embedding space. MoCo uses a momentum encoder and queue for negative samples. Key insight: good augmentations and large batch sizes (many negatives) are critical for performance."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Google", topic="Efficiency",
         text="What is Neural Architecture Search (NAS) and what are its challenges?",
         answer="NAS automates the design of neural network architectures by searching over a defined search space using optimisation (reinforcement learning, evolutionary algorithms, gradient-based methods like DARTS). Challenges: enormous computational cost (early NAS used 1000+ GPU-days), defining a good search space, transferability across tasks and datasets, and the risk of finding architectures that are hard to interpret or deploy."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Any", topic="Training",
         text="What is curriculum learning and how does it improve training?",
         answer="Curriculum learning trains models on examples ordered from easy to hard, mimicking human learning. The model first learns basic patterns on easy samples, then refines on harder ones. It can speed up convergence and improve final performance, especially with noisy data. Self-paced learning is a variant where the model itself decides what is easy. Anti-curriculum (hard-first) can also work for some tasks."),

    dict(subject="DL", difficulty="Hard", type="Situational", company="Google", topic="Deployment",
         text="You need to deploy a large language model (7B parameters) for real-time inference on a single GPU. How do you optimise it?",
         answer="Apply quantisation (GPTQ, AWQ) to reduce model to INT4/INT8. Use Flash Attention for memory-efficient attention. Apply KV-cache for faster autoregressive generation. Consider vLLM or TensorRT-LLM for optimised serving with continuous batching and PagedAttention. Use speculative decoding with a smaller draft model. Monitor memory with torch.cuda.memory_summary(). Target p95 latency requirements and set appropriate max sequence lengths."),

    dict(subject="DL", difficulty="Hard", type="Situational", company="Amazon", topic="Debugging",
         text="Your deep learning model's training loss is stuck and not decreasing. What systematic debugging steps would you follow?",
         answer="1) Verify data pipeline (check labels, normalisation, data loading). 2) Overfit on a single batch first — if it cannot, architecture or implementation is wrong. 3) Check learning rate (try 10x higher and lower). 4) Verify gradient flow (print gradient norms, check for NaN). 5) Simplify architecture. 6) Check loss function implementation. 7) Ensure correct weight initialisation. 8) Try a known-working baseline architecture and config."),

    dict(subject="DL", difficulty="Hard", type="Situational", company="Meta", topic="Scale",
         text="You are training a model that requires 80GB GPU memory but you only have 24GB GPUs. What strategies do you use?",
         answer="Gradient checkpointing (recompute activations during backward pass to save memory). Mixed precision training (FP16 halves activation memory). Gradient accumulation (smaller batch per step). Model parallelism (split model across GPUs). DeepSpeed ZeRO (shards optimiser states, gradients, and parameters across GPUs). LoRA or adapter-based fine-tuning if fine-tuning. Reduce sequence length or use efficient attention variants."),

    dict(subject="DL", difficulty="Hard", type="Situational", company="Microsoft", topic="Generative",
         text="You are fine-tuning a text-to-image diffusion model on a custom dataset of 500 product images. What approach and pitfalls do you consider?",
         answer="Use DreamBooth or textual inversion for few-shot fine-tuning rather than full fine-tuning. Apply LoRA to reduce memory and overfitting risk. Use proper regularisation images to prevent language drift. Watch for mode collapse (generating near-identical images). Evaluate with FID and CLIP score. Pitfalls: overfitting to 500 images, losing diversity, catastrophic forgetting of base model capabilities. Use a low learning rate and early stopping."),

    # ─────────────────────────────────────────
    # DATA STRUCTURES & ALGORITHMS — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Sorting",
         text="What is the difference between merge sort and quicksort?",
         answer="Merge sort always runs in O(n log n) but needs O(n) extra space. Quicksort is O(n log n) average but O(n²) worst case (mitigated by random pivot), and is in-place (O(log n) stack space). Merge sort is stable; quicksort is not. In practice, quicksort is faster due to better cache locality. Merge sort is preferred for linked lists and when stability matters."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Wipro", topic="Trees",
         text="What is a heap data structure and how is it used in priority queues?",
         answer="A heap is a complete binary tree where each parent is greater (max-heap) or smaller (min-heap) than its children. Insert and extract-min/max are O(log n). It is typically stored as an array (parent at i, children at 2i+1 and 2i+2). Priority queues use heaps to efficiently retrieve the highest/lowest priority element. Python has heapq module for min-heaps."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Infosys", topic="Strings",
         text="What is a Trie and where is it used?",
         answer="A Trie (prefix tree) is a tree where each node represents a character and paths from root to nodes represent prefixes. Used for autocomplete, spell checkers, IP routing, and dictionary word lookups. Insert and search are O(L) where L is word length. It trades memory for speed compared to hash tables for prefix-based queries."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Any", topic="Graphs",
         text="What are the two main ways to represent a graph and their tradeoffs?",
         answer="Adjacency matrix: 2D array where matrix[i][j]=1 if edge exists. O(1) edge lookup but O(V²) space. Adjacency list: each vertex stores a list of neighbours. O(V+E) space, efficient for sparse graphs. Matrix is better for dense graphs and quick edge checks. List is better for traversals and sparse graphs, which are more common in practice."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Techniques",
         text="What is the difference between recursion and iteration?",
         answer="Recursion solves a problem by calling itself with smaller subproblems and has a base case. Iteration uses loops. Every recursive solution can be converted to iterative (using an explicit stack). Recursion is more elegant for trees and divide-and-conquer but uses O(n) stack space and risks stack overflow. Iteration is more memory-efficient and often faster."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between a queue and a deque?",
         answer="A queue supports FIFO operations: enqueue at the rear, dequeue from the front. A deque (double-ended queue) supports insertion and removal from both ends in O(1). Deques can be used as both stacks and queues. Python's collections.deque is implemented as a doubly-linked list of blocks, supporting O(1) operations on both ends."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Wipro", topic="Techniques",
         text="What is the two-pointer technique? Give an example.",
         answer="Two pointers use two indices that move through a sorted array/string to solve problems in O(n) instead of O(n²). Example: finding if a pair in a sorted array sums to a target. Start one pointer at the beginning and one at the end. If sum is too large, move right pointer left. If too small, move left pointer right. Also used for removing duplicates and the container with most water problem."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Infosys", topic="Techniques",
         text="What is the sliding window technique?",
         answer="Sliding window maintains a window (subarray/substring) that slides over the data, adding elements at one end and removing from the other. It converts O(n·k) brute-force solutions to O(n). Fixed-size window: maximum sum subarray of size k. Variable-size window: longest substring with at most K distinct characters. Track window state using a hash map or variables."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Any", topic="Bit Manipulation",
         text="What are some common bit manipulation tricks used in interviews?",
         answer="Check if n is power of 2: n & (n-1) == 0. Count set bits: Brian Kernighan's algorithm (repeatedly do n = n & (n-1)). Toggle bit: n ^ (1 << i). Check if bit is set: n & (1 << i). XOR of array finds the single non-duplicate element. Bit manipulation is O(1) per operation and space-efficient for problems involving sets, toggling states, or finding missing/duplicate numbers."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Sorting",
         text="What is the difference between a stable and unstable sort?",
         answer="A stable sort preserves the relative order of equal elements. Merge sort, insertion sort and TimSort are stable. Quicksort and heapsort are unstable. Stability matters when sorting by multiple keys (e.g., sort by name then by age — a stable sort preserves name order within same age). Python's built-in sort (TimSort) is stable."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Google", topic="Graphs",
         text="What is topological sorting and where is it used?",
         answer="Topological sort orders vertices of a directed acyclic graph (DAG) such that for every edge u→v, u comes before v. Algorithms: Kahn's (BFS with in-degree tracking) or DFS-based (add to result in reverse post-order). Used for task scheduling, build systems, course prerequisite ordering, and dependency resolution. Only possible for DAGs — a cycle means no valid ordering."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Amazon", topic="Graphs",
         text="What is a minimum spanning tree and compare Kruskal's and Prim's algorithms?",
         answer="MST connects all vertices with minimum total edge weight without cycles. Kruskal's: sort edges by weight, add each if it does not create a cycle (use Union-Find), O(E log E). Prim's: grow tree from a vertex, always adding the cheapest edge to a new vertex (use min-heap), O(E log V). Kruskal's is better for sparse graphs; Prim's for dense graphs."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Google", topic="Union-Find",
         text="What is the Union-Find (Disjoint Set Union) data structure?",
         answer="Union-Find tracks elements partitioned into disjoint sets. Two operations: find(x) returns the set representative, union(x,y) merges two sets. With path compression and union by rank, both operations are nearly O(1) amortised (inverse Ackermann function). Used for Kruskal's MST, connected components, cycle detection in undirected graphs, and dynamic connectivity problems."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Amazon", topic="Techniques",
         text="What is backtracking and how does it differ from brute force?",
         answer="Backtracking builds solutions incrementally and abandons a path (backtracks) as soon as it determines the path cannot lead to a valid solution. Unlike brute force which checks all possibilities, backtracking prunes the search space. Examples: N-Queens, Sudoku solver, generating permutations/combinations. It is essentially DFS on the solution space tree with pruning."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Greedy",
         text="When should you use a greedy algorithm vs dynamic programming?",
         answer="Use greedy when a locally optimal choice leads to a globally optimal solution (greedy choice property) and the problem has optimal substructure. Examples: activity selection, Huffman coding. Use DP when the problem has overlapping subproblems and optimal substructure but greedy fails (because local optimal is not global). Example: 0/1 knapsack needs DP; fractional knapsack works with greedy."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Any", topic="Trees",
         text="What is the difference between AVL trees and Red-Black trees?",
         answer="Both are self-balancing BSTs. AVL trees are strictly balanced (height difference of subtrees <= 1), giving faster lookups O(log n) with a smaller constant. Red-Black trees are more loosely balanced (longest path <= 2x shortest), giving faster insertions and deletions due to fewer rotations. AVL is better for read-heavy workloads; Red-Black for write-heavy. Most language standard libraries use Red-Black trees."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Google", topic="Advanced",
         text="What is a monotonic stack and what problems does it solve?",
         answer="A monotonic stack maintains elements in increasing or decreasing order. When pushing a new element, pop all elements that violate the monotonic property. Solves 'next greater element', 'next smaller element', 'largest rectangle in histogram', and 'trapping rain water' in O(n). Each element is pushed and popped at most once, giving amortised O(1) per operation."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Google", topic="Design",
         text="How would you implement an LRU Cache?",
         answer="Use a hash map for O(1) key lookup combined with a doubly-linked list for O(1) insertion/deletion. On get: move the node to the head (most recently used). On put: add to head; if capacity exceeded, remove the tail (least recently used) and delete from hash map. Python: use OrderedDict or implement with a custom doubly-linked list. Total: O(1) for both get and put."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Amazon", topic="Strings",
         text="How would you implement KMP string matching?",
         answer="KMP builds a failure function (prefix table) that tells how far back to shift the pattern on a mismatch, avoiding re-scanning text characters. Build the prefix table in O(m) by comparing the pattern with itself. Search in O(n) by using the prefix table to skip redundant comparisons. Total: O(n+m) vs O(n·m) for brute force. The key insight is that the failure function captures the longest proper prefix that is also a suffix."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Microsoft", topic="Graphs",
         text="How would you detect a cycle in a directed graph?",
         answer="Use DFS with three states for each node: unvisited, in-progress (on current DFS path), completed. If DFS reaches an in-progress node, there is a cycle. Alternatively, use Kahn's algorithm for topological sort — if not all nodes are processed, a cycle exists. For undirected graphs, DFS cycle detection is simpler: if you revisit a node that is not the parent, there is a cycle."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Google", topic="Techniques",
         text="How would you solve the 'trapping rain water' problem?",
         answer="Two-pointer approach: maintain left and right pointers with running maxLeft and maxRight. At each step, move the pointer with the smaller max inward. Water at position i = min(maxLeft, maxRight) - height[i]. O(n) time, O(1) space. Alternatively, use a stack-based approach or precompute left_max and right_max arrays (O(n) space). The two-pointer solution is optimal."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Amazon", topic="Design",
         text="How would you implement a min-stack that supports push, pop, top, and getMin in O(1)?",
         answer="Use two stacks: one for actual values and one for tracking minimums. On push, push the value to the main stack and push min(value, current_min) to the min stack. On pop, pop from both. getMin returns the top of the min stack. Space-optimised variant: only push to min stack when the new value is <= current min. All operations are O(1) time."),

    dict(subject="DSA", difficulty="Medium", type="Coding", company="Microsoft", topic="Trees",
         text="How would you serialise and deserialise a binary tree?",
         answer="Use preorder traversal. Serialise: visit root, recursively serialise left then right. Use a special marker (like '#') for null nodes. Join with commas. Deserialise: split the string, use a queue/iterator. Pop the first value — if it is '#', return null, otherwise create a node and recursively build left and right subtrees. BFS (level-order) also works. Both are O(n) time and space."),

    dict(subject="DSA", difficulty="Hard", type="Conceptual", company="Google", topic="Advanced",
         text="What is a segment tree and when would you use it?",
         answer="A segment tree is a binary tree that stores information about array intervals. Each node represents a range and stores an aggregate (sum, min, max). Build in O(n), query any range in O(log n), update a point in O(log n). Used for range sum queries, range minimum queries, and problems requiring both updates and queries. Lazy propagation allows range updates in O(log n). Alternative: Fenwick tree (BIT) for simpler range sum problems."),

    dict(subject="DSA", difficulty="Hard", type="Conceptual", company="Amazon", topic="Graphs",
         text="What is the difference between Dijkstra's and Bellman-Ford algorithms?",
         answer="Dijkstra's finds shortest paths from a source with non-negative edge weights in O((V+E) log V) using a min-heap. Bellman-Ford handles negative weights in O(V·E) and can detect negative cycles. Dijkstra's is faster but fails with negative edges. For graphs with negative edges but no negative cycles, use Bellman-Ford. For all-pairs shortest paths, use Floyd-Warshall O(V³)."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Google", topic="DP",
         text="How would you solve the coin change problem (minimum coins)?",
         answer="DP approach: dp[i] = minimum coins to make amount i. Initialise dp[0]=0, all others = infinity. For each coin, for each amount from coin to target: dp[amount] = min(dp[amount], dp[amount-coin] + 1). Return dp[target] or -1 if infinity. Time: O(amount × num_coins), Space: O(amount). This is a classic unbounded knapsack variant. BFS also works by treating amounts as graph nodes."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Amazon", topic="DP",
         text="How would you find the length of the longest increasing subsequence (LIS)?",
         answer="O(n²) DP: dp[i] = length of LIS ending at index i. For each i, check all j < i: if arr[j] < arr[i], dp[i] = max(dp[i], dp[j]+1). O(n log n) optimised: maintain a list of smallest tail elements for subsequences of each length. Use binary search (bisect_left) to find the position to update. The length of this list is the LIS length."),

    dict(subject="DSA", difficulty="Hard", type="Coding", company="Google", topic="Backtracking",
         text="How would you solve the N-Queens problem?",
         answer="Use backtracking: place queens row by row. For each row, try each column. Check safety by tracking which columns, left diagonals (row-col) and right diagonals (row+col) are occupied using sets. If safe, place the queen and recurse to the next row. If no column works, backtrack. Time complexity: O(N!) in the worst case but pruning makes it much faster in practice. Return all valid board configurations."),

    dict(subject="DSA", difficulty="Hard", type="Situational", company="Google", topic="Design",
         text="You need to design a real-time autocomplete system that handles millions of queries per second. What data structure and architecture would you use?",
         answer="Use a Trie for prefix-based lookup. Augment each node with top-K suggestions (precomputed). For scale, shard the Trie by first characters across servers. Cache popular prefixes in Redis. Use a two-level approach: client-side caching for recent queries, server-side Trie for completions. Update suggestions asynchronously from query logs. Consider using a ternary search tree for memory efficiency."),

    dict(subject="DSA", difficulty="Hard", type="Situational", company="Amazon", topic="Design",
         text="You need to implement a rate limiter that allows at most N requests per minute per user. Which algorithm and data structure would you choose?",
         answer="Sliding window counter or token bucket algorithm. Sliding window: store timestamps in a deque per user, remove timestamps older than 1 minute, reject if size >= N. Token bucket: each user gets N tokens per minute, each request consumes one token, tokens refill at a fixed rate. For distributed systems, use Redis with atomic operations. Consider fixed window for simplicity but it has boundary issues. Token bucket allows bursts while maintaining average rate."),

    # ─────────────────────────────────────────
    # PYTHON — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="TCS", topic="Data Model",
         text="What are dunder (magic) methods in Python? Give three examples.",
         answer="Dunder methods (double underscore, e.g., __init__, __str__, __len__) are special methods that Python calls implicitly for operations like object creation, string representation, and operator overloading. __init__ initialises objects, __str__ returns a readable string (used by print), __len__ enables len(). They let your custom classes work with built-in Python syntax and functions."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Wipro", topic="Functions",
         text="What is a lambda function in Python and when would you use it?",
         answer="A lambda is an anonymous, single-expression function: lambda x: x*2. Used for short operations in map(), filter(), sorted() key functions, and as callback arguments. They cannot contain statements or multiple expressions. For complex logic, use regular def functions. Overusing lambdas hurts readability — PEP 8 discourages assigning lambdas to variables."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Infosys", topic="Collections",
         text="What are Counter, defaultdict and deque from Python's collections module?",
         answer="Counter counts element frequencies: Counter('hello') gives {'l':2, ...}. defaultdict provides default values for missing keys, avoiding KeyError: defaultdict(list) auto-creates empty lists. deque (double-ended queue) supports O(1) append/pop from both ends — useful for queues, sliding windows, and BFS. All three are heavily used in interviews and data processing."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="Strings",
         text="What are f-strings and how do they compare to other string formatting methods?",
         answer="F-strings (f'Hello {name}') were introduced in Python 3.6. They are the fastest and most readable formatting method. Compared to %-formatting ('Hello %s' % name) and .format('Hello {}'.format(name)), f-strings allow arbitrary expressions inside braces, support format specs (f'{pi:.2f}'), and are evaluated at runtime. They are the recommended approach in modern Python."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="TCS", topic="OOP",
         text="What is the property decorator in Python?",
         answer="@property makes a method accessible like an attribute, enabling getter/setter/deleter patterns. It provides a clean API while allowing validation, computation, or access control behind the scenes. Example: @property def age(self): return self._age, with @age.setter for validation. This follows encapsulation principles without forcing users to call getter/setter methods explicitly."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="OOP",
         text="What are dataclasses in Python and when would you use them?",
         answer="Dataclasses (@dataclass decorator, Python 3.7+) auto-generate __init__, __repr__, __eq__ and optionally __hash__ and comparison methods from class attributes with type annotations. Use them for data-holding classes (DTOs, configs, records). They reduce boilerplate. For immutable data, use frozen=True. NamedTuples are an alternative for simpler cases."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Wipro", topic="Types",
         text="What are type hints in Python and why should you use them?",
         answer="Type hints annotate expected types: def greet(name: str) -> str. They do not enforce types at runtime but enable static analysis tools (mypy, pyright) to catch type errors before execution. Benefits: better IDE autocompletion, clearer documentation, easier refactoring. Use typing module for complex types: List[int], Optional[str], Dict[str, Any], Union, Callable."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Infosys", topic="Fundamentals",
         text="What is the walrus operator (:=) and when is it useful?",
         answer="The walrus operator (:=) assigns a value to a variable as part of an expression (Python 3.8+). Example: if (n := len(data)) > 10: print(n). It avoids computing the same expression twice. Useful in while loops (while chunk := file.read(8192)), list comprehensions with filtering, and conditional assignments. Use sparingly — readability should come first."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="OOP",
         text="What are __slots__ in Python classes and why would you use them?",
         answer="__slots__ declares a fixed set of attributes for a class, preventing __dict__ creation. Benefits: 20-30% less memory per instance and slightly faster attribute access. Use when creating millions of instances (e.g., data processing). Limitation: cannot add arbitrary attributes at runtime, and subclasses need their own __slots__ declaration. Not necessary for most classes."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Google", topic="Functions",
         text="What is a closure in Python and give a practical example?",
         answer="A closure is a function that remembers the variables from its enclosing scope even after that scope has finished executing. Example: def make_multiplier(n): return lambda x: x * n. multiply_by_3 = make_multiplier(3) — the inner lambda 'closes over' n=3. Used in decorators, callbacks, partial application, and factory functions. The 'nonlocal' keyword allows modifying enclosed variables."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Amazon", topic="Modules",
         text="What is functools.lru_cache and when would you use it?",
         answer="@lru_cache (Least Recently Used cache) memoises function results based on arguments. It caches the return value for each unique set of arguments. Perfect for recursive functions (fibonacci) and expensive computations that are called repeatedly with the same inputs. lru_cache(maxsize=None) gives unlimited cache. Use cache_info() to check hit/miss rates. Arguments must be hashable."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Advanced",
         text="What are metaclasses in Python and when would you use them?",
         answer="A metaclass is the class of a class — it controls class creation. When Python encounters a class definition, it calls the metaclass's __new__ and __init__. Use cases: registering classes automatically (plugin systems), enforcing coding standards, auto-adding methods or validations, and implementing ORMs (SQLAlchemy's declarative base). Most developers rarely need metaclasses — 'if you're wondering whether you need them, you don't.'"),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="OOP",
         text="What are Abstract Base Classes (ABCs) in Python?",
         answer="ABCs (from abc module) define interfaces that subclasses must implement. Decorate methods with @abstractmethod to prevent instantiation of the ABC and enforce implementation in subclasses. Used to define contracts: class Shape(ABC): @abstractmethod def area(self): pass. Collections ABCs (Iterable, Mapping) let you check if objects implement protocols. They bring some of the benefits of static typing to Python."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Google", topic="Advanced",
         text="What is the difference between iterators and iterables in Python?",
         answer="An iterable has an __iter__ method that returns an iterator (lists, strings, dicts). An iterator has __iter__ (returns self) and __next__ (returns next value or raises StopIteration). Iterators are lazy — they produce values on demand. A for loop calls iter() on the iterable to get an iterator, then calls next() until StopIteration. Generators are a convenient way to create iterators."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Amazon", topic="Advanced",
         text="What is the mutable default argument trap in Python?",
         answer="Default mutable arguments (lists, dicts) are created once at function definition, not per call. def append_to(element, lst=[]): lst.append(element); return lst — repeated calls share the same list! Fix: use None as default and create the mutable inside the function. This is because default values are stored as function attributes and persist across calls."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Modules",
         text="What is the itertools module and name five useful functions?",
         answer="itertools provides memory-efficient iterator-building blocks. Key functions: chain (concatenate iterables), product (Cartesian product), combinations/permutations (combinatorics), groupby (group consecutive elements), islice (slice iterators), accumulate (running totals), zip_longest (zip with fill). They are lazy (generate values on demand) and composable. Essential for elegant solutions to iteration problems."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Testing",
         text="What is the difference between pytest and unittest, and which do you prefer?",
         answer="unittest is built-in, class-based, uses self.assertEqual-style assertions. pytest uses plain assert statements, auto-discovers tests, has powerful fixtures (@pytest.fixture), parametrize for test cases, and rich plugins. pytest is simpler, more Pythonic and has a better ecosystem. It can also run unittest-style tests. pytest is the industry standard for Python testing."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Any", topic="Performance",
         text="How do you profile Python code to find performance bottlenecks?",
         answer="cProfile: built-in profiler showing function call counts and time. line_profiler (@profile decorator) shows time per line. memory_profiler shows memory usage per line. py-spy: sampling profiler that attaches to running processes without modification. timeit: for micro-benchmarks. Workflow: profile first (do not guess), optimise the hotspot, and re-profile. 'Premature optimisation is the root of all evil.'"),

    dict(subject="Python", difficulty="Medium", type="Coding", company="Google", topic="Advanced",
         text="How would you implement a custom context manager in Python?",
         answer="Two approaches: 1) Class-based: implement __enter__ (return resource) and __exit__ (cleanup, handle exceptions). 2) Generator-based: use @contextlib.contextmanager decorator with a function that yields. Code before yield is setup, after yield is cleanup. Example: @contextmanager def timer(): start=time.time(); yield; print(f'Took {time.time()-start}s'). Generator-based is more concise for simple cases."),

    dict(subject="Python", difficulty="Medium", type="Coding", company="Amazon", topic="Data",
         text="How would you efficiently read and process a 10GB CSV file in Python?",
         answer="Use chunked reading: pd.read_csv('file.csv', chunksize=100000) returns an iterator of DataFrames. Process each chunk and aggregate results. For even more efficiency: use polars (Rust-based, faster than pandas), dask for parallel processing, or Python's csv module with generators for memory-efficient row-by-row reading. Specify dtypes upfront to reduce memory. Consider pyarrow for columnar reading."),

    dict(subject="Python", difficulty="Medium", type="Coding", company="Microsoft", topic="Patterns",
         text="How would you implement the observer pattern in Python?",
         answer="Create a Subject class with a list of observers, methods to add/remove observers, and a notify method that calls update() on each observer. Observers implement an update method. Alternatively, use Python's built-in mechanisms: callbacks (list of callables), signals (using blinker library), or property setters that trigger notifications. For simple cases, just pass callback functions."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Google", topic="Advanced",
         text="Explain Python's descriptor protocol and how property works under the hood.",
         answer="Descriptors implement __get__, __set__, and/or __delete__. When accessed as class attributes, Python calls these methods instead of returning the descriptor object. Data descriptors (with __set__) take priority over instance __dict__. Non-data descriptors (only __get__) do not. @property is implemented as a data descriptor. This protocol powers property, classmethod, staticmethod, and ORM field types like SQLAlchemy columns."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Amazon", topic="Concurrency",
         text="Explain Python's asyncio event loop and how async/await works internally.",
         answer="asyncio uses a single-threaded event loop that manages coroutines. async def creates a coroutine; await suspends it and returns control to the event loop, which can run other coroutines. Under the hood, coroutines are generators using yield from. The event loop uses selectors (epoll/kqueue) for I/O multiplexing. asyncio.gather() runs coroutines concurrently. It excels for I/O-bound tasks (network, file I/O) but does not help with CPU-bound work."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Google", topic="Memory",
         text="How does Python's memory management work internally?",
         answer="Python uses a private heap for all objects. The memory allocator (pymalloc) manages small objects (< 512 bytes) using arenas, pools and blocks, avoiding frequent OS system calls. Reference counting is the primary GC mechanism — objects are freed when refcount hits zero. A generational garbage collector handles reference cycles, scanning younger objects more frequently. The GIL ensures thread safety for refcount operations."),

    dict(subject="Python", difficulty="Hard", type="Situational", company="Google", topic="Performance",
         text="A Python data pipeline processes 50 million records daily and is too slow. How would you optimise it?",
         answer="Profile first to find bottlenecks. Potential optimisations: use vectorised pandas/numpy operations instead of loops, switch to polars for faster DataFrame operations, use multiprocessing for CPU-bound steps, async I/O for network calls, batch database writes, use generators/iterators to reduce memory, consider Cython or numba for hot loops, and cache intermediate results. If still insufficient, consider Spark or distributed computing."),

    dict(subject="Python", difficulty="Hard", type="Situational", company="Amazon", topic="Debugging",
         text="A Python service has a memory leak that causes it to crash every few days. How would you diagnose it?",
         answer="Use tracemalloc to track memory allocations and find the top allocation sites. Use objgraph to visualise object reference graphs and find unexpected references preventing garbage collection. Check for: circular references, global caches without size limits, event handler accumulation, unclosed file handles or database connections, and C extension memory leaks. Monitor with memory_profiler and set up alerts on memory usage trends."),

    dict(subject="Python", difficulty="Hard", type="Situational", company="Microsoft", topic="Architecture",
         text="You need to build a Python microservice that handles 5000 concurrent WebSocket connections. What framework and architecture would you use?",
         answer="Use an async framework: FastAPI with uvicorn (ASGI), or raw asyncio with websockets library. The async event loop handles thousands of connections on a single thread efficiently. Use Redis pub/sub for message broadcasting across multiple server instances. Deploy multiple workers behind a load balancer (with sticky sessions or shared state). Monitor connection counts, memory per connection, and implement heartbeat/keepalive."),

    # ─────────────────────────────────────────
    # STATISTICS — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="TCS", topic="Distributions",
         text="What is a Bernoulli distribution and how does it relate to the Binomial distribution?",
         answer="Bernoulli distribution models a single trial with two outcomes (success with probability p, failure with 1-p). The Binomial distribution is the sum of n independent Bernoulli trials — it models the number of successes in n trials. Mean of Binomial: np, Variance: np(1-p). Binomial is used for: defect rates, click-through rates, pass/fail counts."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Wipro", topic="Distributions",
         text="What is a Poisson distribution and when do you use it?",
         answer="Poisson distribution models the number of events in a fixed interval when events occur independently at a constant average rate lambda. P(k) = (lambda^k * e^-lambda) / k!. Mean = Variance = lambda. Used for: number of customer arrivals per hour, number of errors per page, number of calls to a call centre. It approximates Binomial when n is large and p is small."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Infosys", topic="Fundamentals",
         text="What are percentiles and quartiles?",
         answer="Percentiles divide data into 100 equal parts. The 50th percentile is the median. The 25th and 75th percentiles are Q1 and Q3. Quartiles divide data into four parts: Q1 (25%), Q2 (50%/median), Q3 (75%). The Interquartile Range (IQR = Q3-Q1) measures spread and is used for outlier detection: values below Q1-1.5*IQR or above Q3+1.5*IQR are outliers."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is expected value and why is it important?",
         answer="Expected value E(X) is the probability-weighted average of all possible outcomes: sum of x*P(x). It represents the long-run average if the experiment is repeated infinitely. Important in decision-making, risk assessment, and ML loss functions. Example: if a game pays $10 with probability 0.3 and $0 otherwise, E(X) = $3. It does not have to be an observable outcome."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What is the Law of Large Numbers?",
         answer="The Law of Large Numbers states that as sample size increases, the sample mean converges to the population mean. The weak version says convergence is in probability; the strong version says almost sure convergence. Practical implication: larger samples give more reliable estimates. It is why casinos always profit long-term despite individual wins and why polling becomes more accurate with more respondents."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Wipro", topic="Descriptive",
         text="What are skewness and kurtosis?",
         answer="Skewness measures asymmetry of a distribution. Positive skew: tail extends right (median < mean). Negative skew: tail extends left (mean < median). Zero skew: symmetric. Kurtosis measures tail heaviness. High kurtosis (leptokurtic): heavy tails, more outliers. Low kurtosis (platykurtic): light tails. Normal distribution has kurtosis = 3 (excess kurtosis = 0). Both affect which statistical tests are appropriate."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Inference",
         text="What is the difference between a population and a sample?",
         answer="A population is the entire group you want to study. A sample is a subset drawn from the population. We use samples because studying entire populations is usually impractical. Sample statistics (mean, std) estimate population parameters. The quality of estimation depends on sample size and sampling method. Key: a representative, random sample is more important than a large biased sample."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Infosys", topic="Inference",
         text="What is a sampling distribution?",
         answer="A sampling distribution is the distribution of a statistic (like the sample mean) computed from many random samples of the same size from a population. The Central Limit Theorem says the sampling distribution of the mean is approximately normal for large samples, regardless of the population distribution. Its standard deviation (standard error) decreases with sqrt(n), showing larger samples give more precise estimates."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Probability",
         text="What is Bayes' theorem and give a practical example?",
         answer="Bayes' theorem: P(A|B) = P(B|A) * P(A) / P(B). It updates the probability of a hypothesis given new evidence. Example: a disease test is 99% accurate, disease prevalence is 1%. If you test positive, P(disease|positive) = (0.99 * 0.01) / (0.99*0.01 + 0.01*0.99) = 50%, not 99%. This shows why prior probability matters and explains why rare disease screening has high false positive rates."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Google", topic="Testing",
         text="What is the Chi-squared test and when do you use it?",
         answer="Chi-squared test compares observed vs expected frequencies. Test of independence: are two categorical variables related? (e.g., is gender related to product preference). Goodness-of-fit: does data fit a distribution? Test statistic: sum of (observed-expected)² / expected. High chi-squared = significant difference. Degrees of freedom: (rows-1)*(cols-1). Assumes expected counts >= 5 in each cell."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Amazon", topic="Testing",
         text="What is ANOVA and when would you use it instead of t-tests?",
         answer="ANOVA (Analysis of Variance) tests if means of 3+ groups are significantly different. One-way ANOVA compares groups on one factor; two-way on two factors. It compares between-group variance to within-group variance (F-statistic). Using multiple t-tests inflates Type I error rate; ANOVA controls this. Assumptions: normality, homogeneity of variance, independence. Post-hoc tests (Tukey) identify which groups differ."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Google", topic="Methods",
         text="What is the bootstrap method and why is it useful?",
         answer="Bootstrap creates many samples by drawing with replacement from the original sample, computing the statistic on each. This builds an empirical sampling distribution without assumptions about the population. Useful for: confidence intervals, standard errors, hypothesis testing when parametric assumptions are violated. It works for complex statistics (median, correlation, model performance). Requires a reasonably representative original sample."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Estimation",
         text="What is Maximum Likelihood Estimation (MLE)?",
         answer="MLE finds the parameter values that maximise the likelihood (probability) of observing the given data. For a normal distribution, MLE gives the sample mean and variance. Process: write the likelihood function, take its log (log-likelihood), find the maximum by setting the derivative to zero or using numerical optimisation. MLE estimates are consistent, asymptotically efficient, and asymptotically normal. Most ML training is a form of MLE."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Testing",
         text="What is the Mann-Whitney U test and when would you use it?",
         answer="Mann-Whitney U is a non-parametric test comparing two independent groups when data is not normally distributed. It tests whether one group tends to have larger values than the other (compares medians/distributions). It uses ranks instead of raw values. Use it when: sample is small, data is ordinal, or normality assumption is violated. It is the non-parametric equivalent of the independent t-test."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Google", topic="Effect Size",
         text="What is effect size and why is it important beyond p-values?",
         answer="Effect size measures the magnitude of a difference or relationship, independent of sample size. Cohen's d: (mean1-mean2)/pooled_std (small=0.2, medium=0.5, large=0.8). With large samples, even trivially small differences can be statistically significant. Effect size tells you if the difference is practically meaningful. Always report effect size alongside p-values for proper interpretation."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Regression",
         text="What is heteroscedasticity and why does it matter in regression?",
         answer="Heteroscedasticity means the variance of residuals is not constant across values of independent variables (e.g., prediction errors increase with income). It violates OLS assumptions, leading to biased standard errors, unreliable confidence intervals and p-values (coefficients are still unbiased but inefficient). Detect with Breusch-Pagan test. Fix with: weighted least squares, robust standard errors, or log-transforming the dependent variable."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Amazon", topic="Paradoxes",
         text="What is Simpson's Paradox and give an example?",
         answer="Simpson's Paradox occurs when a trend in several subgroups reverses when the groups are combined. Classic example: Treatment A appears better overall, but Treatment B is better in every subgroup — because Treatment B was given more often to the harder cases. It arises from confounding variables. The lesson: always check if aggregated data hides important group-level differences. It is why stratified analysis matters."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Google", topic="Design",
         text="How do you calculate the required sample size for an A/B test?",
         answer="Sample size depends on: significance level alpha (typically 0.05), desired power (typically 0.8), minimum detectable effect (MDE), and baseline metric variance. Formula for proportions: n = (Z_alpha/2 + Z_beta)² * 2 * p(1-p) / MDE². Smaller effects need larger samples. Higher power needs larger samples. Use online calculators or scipy.stats. Always determine sample size before running the test, not after."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Distributions",
         text="What is the difference between PDF, PMF, and CDF?",
         answer="PMF (Probability Mass Function) gives the probability of each discrete value: P(X=k). PDF (Probability Density Function) gives the density for continuous variables — probability is the area under the curve, not the point value. CDF (Cumulative Distribution Function) gives P(X <= x) for both types. CDF is always non-decreasing from 0 to 1. PDF is the derivative of CDF; PMF values sum to 1."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Probability",
         text="What are joint, marginal, and conditional distributions?",
         answer="Joint distribution P(X,Y) describes the probability of X and Y occurring together. Marginal distribution P(X) is obtained by summing/integrating over Y: P(X) = sum P(X,Y) over all Y. Conditional distribution P(X|Y) is the distribution of X given Y: P(X|Y) = P(X,Y)/P(Y). Independence means P(X,Y) = P(X)*P(Y). Understanding these is fundamental to Bayesian inference and probabilistic modelling."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Any", topic="Sampling",
         text="What are the main sampling methods and when would you use each?",
         answer="Simple random: every element has equal chance — gold standard but may miss subgroups. Stratified: divide population into strata, sample from each — ensures representation of subgroups. Cluster: randomly select groups, sample all within — efficient for geographically dispersed populations. Systematic: every kth element — simple but risks periodicity bias. Convenience sampling is biased and should be avoided in research."),

    dict(subject="Stats", difficulty="Medium", type="Coding", company="Google", topic="Methods",
         text="How would you implement a bootstrap confidence interval in Python?",
         answer="Draw B bootstrap samples (e.g., B=10000) by sampling with replacement from the original data (using np.random.choice with replace=True). Compute the statistic (mean, median, etc.) on each bootstrap sample. Sort the B statistics and take the 2.5th and 97.5th percentiles for a 95% CI (percentile method). For bias-corrected intervals, use the BCa method from scipy or arch library."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Google", topic="Stochastic",
         text="What is a Markov chain and where is it used in data science?",
         answer="A Markov chain is a stochastic process where the next state depends only on the current state (memoryless property). Defined by states and transition probabilities. Used in: PageRank algorithm, MCMC sampling for Bayesian inference, hidden Markov models for sequence analysis, text generation, reinforcement learning, and customer journey modelling. Stationary distribution exists for ergodic chains."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Amazon", topic="Survival",
         text="What is survival analysis and when would you use it?",
         answer="Survival analysis models time-to-event data with censoring (some subjects have not experienced the event yet). Key concepts: survival function S(t) = P(T > t), hazard function h(t) = instantaneous event rate. Methods: Kaplan-Meier (non-parametric survival curve), Cox proportional hazards (relates covariates to hazard). Used for: customer churn prediction, medical trial outcomes, equipment failure prediction, and subscription cancellation."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Google", topic="Testing",
         text="What is the Bonferroni correction and what are its alternatives?",
         answer="When performing m hypothesis tests, the probability of at least one false positive increases (family-wise error rate). Bonferroni correction divides alpha by m: reject if p < alpha/m. It is simple but very conservative — reduces power significantly. Alternatives: Holm-Bonferroni (step-down, less conservative), Benjamini-Hochberg (controls False Discovery Rate instead of FWER, more powerful for many tests), and permutation-based corrections."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Meta", topic="Regression",
         text="Explain the assumptions of logistic regression from a statistical perspective.",
         answer="Logistic regression assumes: 1) Binary or ordinal outcome. 2) Linear relationship between log-odds and predictors. 3) Independence of observations. 4) No multicollinearity among predictors. 5) Large sample size (minimum 10-20 events per predictor). It does NOT assume normality of residuals or homoscedasticity. Violations: non-linearity can be addressed with polynomial terms or splines; multicollinearity with VIF analysis and feature removal."),

    dict(subject="Stats", difficulty="Hard", type="Situational", company="Google", topic="Experimentation",
         text="Your A/B test has been running for two weeks but has not reached statistical significance. Your PM wants to either extend the test or declare no effect. What do you advise?",
         answer="First check: was the test properly powered for the expected effect size? If underpowered, extending is valid but calculate the new required duration. Consider if the MDE was realistic — maybe the true effect is smaller than hypothesised. Check for implementation bugs, segment-level effects, and metric validity. If properly powered and no significance, this IS a result — there is likely no meaningful effect. Do not keep extending hoping for significance (that is p-hacking). Report the confidence interval of the effect to show what effect sizes are ruled out."),

    dict(subject="Stats", difficulty="Hard", type="Situational", company="Amazon", topic="Analysis",
         text="You notice that a key metric improved dramatically last week. How would you statistically validate whether this is a real change or noise?",
         answer="Compute confidence intervals for the metric before and after — check if they overlap. Run a hypothesis test comparing the two periods. Check for seasonal effects by comparing to the same period last year. Look for confounding events (marketing campaign, bug fix, external factors). Use change point detection algorithms. Verify data quality — check for logging changes, missing data, or calculation errors. A single week may have high variance — look at the trend."),

    dict(subject="Stats", difficulty="Hard", type="Situational", company="Meta", topic="Design",
         text="You are designing an A/B test for a feature that might have network effects (e.g., a social media feature). Standard randomisation will not work. What do you do?",
         answer="Standard user-level randomisation causes interference (one user's treatment affects another's outcome). Solutions: cluster-based randomisation (randomise at city, region, or social cluster level), switchback experiments (alternate treatment/control over time periods), ego-network randomisation, or use interference-aware causal inference methods. Tradeoffs: cluster randomisation has fewer independent units (lower power); switchback has temporal confounds. Consider simulation to estimate required sample size."),

    # ─────────────────────────────────────────
    # NLP — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="TCS", topic="Preprocessing",
         text="What are the typical steps in a text preprocessing pipeline?",
         answer="Typical steps: lowercasing, removing punctuation/special characters, tokenisation, removing stop words, stemming or lemmatisation, handling contractions, removing HTML tags and URLs. Order matters — tokenise before removing stop words. For deep learning models, minimal preprocessing is often better since models like BERT learn from raw text. Always validate that preprocessing does not remove important signal."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Wipro", topic="Models",
         text="What are N-gram models and what are their limitations?",
         answer="N-gram models predict the next word based on the previous N-1 words. Bigrams use one previous word, trigrams use two. They use conditional probability: P(w_n | w_{n-1}, ..., w_{n-N+1}). Limitations: they cannot capture long-range dependencies, suffer from data sparsity for large N, and the vocabulary explosion problem. Smoothing techniques (Laplace, Kneser-Ney) handle unseen N-grams. Largely replaced by neural language models."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Architectures",
         text="What is the encoder-decoder architecture in NLP?",
         answer="Encoder-decoder consists of two parts: the encoder processes the input sequence into a fixed context representation, and the decoder generates the output sequence from that representation. Originally used with RNNs/LSTMs for machine translation (seq2seq). The bottleneck of fixed-size context was solved by attention mechanism. Transformers use this architecture: BERT is encoder-only, GPT is decoder-only, T5 is encoder-decoder."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Infosys", topic="Tasks",
         text="What is text classification and what are the common approaches?",
         answer="Text classification assigns labels to text documents. Approaches: traditional ML (TF-IDF + logistic regression/SVM — still strong baselines), CNN-based (text convolutions capture n-gram patterns), RNN/LSTM (capture sequential information), and transformer-based (fine-tune BERT, RoBERTa for state-of-the-art). For few labels, zero/few-shot with LLMs works well. Evaluation: accuracy, F1 (especially for imbalanced classes), confusion matrix."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="TCS", topic="Embeddings",
         text="What is the difference between static and contextual word embeddings?",
         answer="Static embeddings (Word2Vec, GloVe) assign a single fixed vector per word regardless of context — 'bank' has the same vector in 'river bank' and 'bank account'. Contextual embeddings (BERT, ELMo, GPT) generate different vectors for the same word based on its context. Contextual embeddings capture polysemy and nuance, leading to significantly better performance on most NLP tasks."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Generation",
         text="What do temperature, top-k, and top-p mean in text generation?",
         answer="Temperature scales logits before softmax: higher temperature (>1) makes outputs more random/creative, lower (<1) makes them more focused/deterministic. Top-k sampling restricts choices to the k most probable tokens. Top-p (nucleus sampling) restricts to the smallest set of tokens whose cumulative probability exceeds p. These are decoding strategies that trade off diversity vs coherence in generated text."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Wipro", topic="Evaluation",
         text="What are BLEU and ROUGE scores?",
         answer="BLEU (Bilingual Evaluation Understudy) measures how many n-grams in generated text match the reference — used for machine translation. ROUGE (Recall-Oriented Understudy) measures overlap between generated and reference summaries, focusing on recall — used for summarisation. BLEU emphasises precision; ROUGE emphasises recall. Both are imperfect: they miss semantic similarity and penalise valid paraphrases."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Tokenisation",
         text="What is Byte Pair Encoding (BPE) and why is it used for tokenisation?",
         answer="BPE starts with individual characters and iteratively merges the most frequent adjacent pairs to form subword tokens. It balances between character-level (handles any word) and word-level (captures semantics) tokenisation. It handles out-of-vocabulary words by breaking them into known subwords. Used by GPT models. SentencePiece (used by BERT, T5) is a similar subword tokenisation algorithm."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Infosys", topic="Tasks",
         text="What is the difference between information extraction and information retrieval?",
         answer="Information retrieval (IR) finds relevant documents from a collection given a query (search engines). Information extraction (IE) identifies structured information from unstructured text — named entities, relationships, events. IR returns documents; IE returns structured data. Example: searching for 'Apple CEO' is IR; extracting 'CEO(Apple, Tim Cook)' from a news article is IE. They are complementary in modern NLP systems."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Transformers",
         text="What is positional encoding in transformers and why is it needed?",
         answer="Transformers process all tokens in parallel (no recurrence), so they have no inherent notion of position. Positional encoding adds position information to token embeddings. Original transformers use sinusoidal functions of different frequencies for each dimension. BERT uses learned positional embeddings. RoPE (Rotary Position Embedding) is used in modern LLMs for better length generalisation. Without positional encoding, 'dog bites man' and 'man bites dog' would have the same representation."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Transformers",
         text="How does multi-head attention work in transformers?",
         answer="Multi-head attention runs several attention mechanisms in parallel, each with different learned projections (queries Q, keys K, values V). Each head can attend to different aspects of the input (syntactic, semantic, positional). Outputs are concatenated and linearly transformed. Formula per head: Attention(Q,K,V) = softmax(QK^T/sqrt(d_k))V. Typically 8-16 heads. It is richer than single attention because it captures multiple types of relationships simultaneously."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Amazon", topic="Topic Modelling",
         text="What is topic modelling and compare LDA with BERTopic.",
         answer="Topic modelling discovers abstract topics in a document collection. LDA (Latent Dirichlet Allocation) is a probabilistic generative model that assumes documents are mixtures of topics, and topics are distributions over words. BERTopic uses transformer embeddings, UMAP for dimensionality reduction, and HDBSCAN for clustering, then extracts topic words using c-TF-IDF. BERTopic produces more coherent topics and handles short texts better. LDA is simpler and more interpretable."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="LLMs",
         text="What is prompt engineering and what are key strategies?",
         answer="Prompt engineering crafts input prompts to elicit desired LLM behaviour. Strategies: be specific and explicit, provide examples (few-shot), use role-playing ('You are an expert...'), chain-of-thought prompting ('Think step by step'), output format specification (JSON, bullet points), negative instructions ('Do not...'), and temperature/token limit tuning. Effective prompting can dramatically improve LLM performance without any fine-tuning."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Meta", topic="LLMs",
         text="What is chain-of-thought prompting and why does it improve LLM reasoning?",
         answer="Chain-of-thought (CoT) prompting instructs the LLM to show intermediate reasoning steps before giving the final answer. 'Let's think step by step' or providing worked examples with reasoning. It improves performance on math, logic, and multi-step reasoning tasks by breaking complex problems into manageable steps. Zero-shot CoT (just adding 'think step by step') works surprisingly well. It works because it keeps intermediate results in context."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="LLMs",
         text="What is RLHF (Reinforcement Learning from Human Feedback) and why is it important?",
         answer="RLHF fine-tunes language models to align with human preferences. Process: 1) Collect human rankings of model outputs. 2) Train a reward model to predict human preferences. 3) Use PPO (Proximal Policy Optimisation) to fine-tune the LM to maximise the reward model's score. It makes models more helpful, harmless, and honest. Used in ChatGPT, Claude, and other aligned models. Alternatives: DPO (Direct Preference Optimisation) skips the reward model."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Amazon", topic="Tasks",
         text="What is coreference resolution and why is it important?",
         answer="Coreference resolution identifies when different expressions refer to the same entity. Example: 'John went to the store. He bought milk.' — 'He' refers to 'John'. It is crucial for: document understanding, information extraction, question answering, and summarisation. Without it, NLP systems lose track of who/what is being discussed. Modern approaches use span-based neural models and transformer representations."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Evaluation",
         text="What is BERTScore and why is it better than BLEU for evaluating text generation?",
         answer="BERTScore computes similarity between generated and reference text using contextual BERT embeddings, matching tokens greedily and computing precision, recall and F1 in embedding space. Unlike BLEU (which uses exact n-gram matching), BERTScore captures semantic similarity — 'happy' and 'joyful' score highly even though they share no n-grams. It correlates better with human judgments but is more computationally expensive."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Any", topic="Multilingual",
         text="What are multilingual models like mBERT and XLM-R, and how do they work?",
         answer="mBERT is BERT trained on Wikipedia in 104 languages with shared vocabulary and no explicit cross-lingual signal. XLM-R is trained on CommonCrawl data in 100 languages using a larger model and more data. Both learn cross-lingual representations — you can fine-tune on English and apply to other languages (zero-shot transfer). XLM-R generally outperforms mBERT. They enable NLP for low-resource languages without language-specific training data."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Tasks",
         text="How do modern question answering systems work?",
         answer="Extractive QA: given a passage and question, the model predicts start and end positions of the answer span (BERT-based). Generative QA: the model generates the answer text (T5, GPT). Open-domain QA combines retrieval (find relevant passages from a corpus) with a reader (extract/generate answer). RAG extends this by using retrieved passages as context for generation. Evaluation metrics: Exact Match and F1 (token overlap)."),

    dict(subject="NLP", difficulty="Medium", type="Coding", company="Google", topic="Preprocessing",
         text="How would you build a custom text preprocessing pipeline in Python?",
         answer="Use a function chain: 1) re.sub() for regex-based cleaning (URLs, HTML, special chars). 2) .lower() for lowercasing. 3) Tokenise with nltk.word_tokenize or spaCy. 4) Remove stop words using nltk.corpus.stopwords. 5) Lemmatise with spaCy or WordNetLemmatizer. Wrap in a class with a transform() method for sklearn pipeline compatibility. For production, use spaCy's pipeline which handles tokenisation, POS tagging, and lemmatisation efficiently."),

    dict(subject="NLP", difficulty="Medium", type="Coding", company="Amazon", topic="Similarity",
         text="How would you compute semantic similarity between two sentences?",
         answer="1) Encode both sentences using a sentence transformer model (sentence-transformers library, e.g., 'all-MiniLM-L6-v2'). 2) Compute cosine similarity between the two embedding vectors. Code: from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); embeddings = model.encode([sent1, sent2]); similarity = cosine_similarity([embeddings[0]], [embeddings[1]]). For large-scale search, use FAISS for efficient nearest-neighbour lookup."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Google", topic="LLMs",
         text="How does instruction tuning differ from standard fine-tuning, and why is it effective?",
         answer="Standard fine-tuning trains on task-specific input-output pairs (e.g., sentiment labelled data). Instruction tuning trains on diverse tasks formatted as natural language instructions ('Classify the sentiment of: ...', 'Summarise: ...', 'Translate to French: ...'). It teaches the model to follow instructions generalising to unseen tasks. FLAN, InstructGPT and Alpaca use this approach. Combined with RLHF, it produces models that are both capable and aligned."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Meta", topic="Architecture",
         text="What are the key differences between BERT, GPT, and T5 architectures?",
         answer="BERT: encoder-only, bidirectional, trained with masked language modelling. Best for understanding tasks (classification, NER, QA). GPT: decoder-only, autoregressive (left-to-right), trained with next-token prediction. Best for generation. T5: encoder-decoder, treats every task as text-to-text. Versatile for both understanding and generation. Each has spawned many variants: RoBERTa, DeBERTa (BERT family); GPT-2/3/4 (GPT family); FLAN-T5, UL2 (T5 family)."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Google", topic="Augmentation",
         text="What are text data augmentation techniques and when are they effective?",
         answer="Techniques: synonym replacement (WordNet), random insertion/deletion/swap, back-translation (translate to another language and back), paraphrasing with LLMs, contextual augmentation (use BERT to replace words), mixup in embedding space, and EDA (Easy Data Augmentation). Effective when training data is limited. Less impactful for large pretrained models. Always validate that augmentation preserves labels and does not introduce noise."),

    dict(subject="NLP", difficulty="Hard", type="Situational", company="Google", topic="Design",
         text="You need to build a document search system over 10 million internal company documents. What architecture would you design?",
         answer="Two-stage retrieval: 1) First stage: BM25 or dense retrieval (encode documents with a bi-encoder, store in FAISS/Milvus vector database, retrieve top-100 candidates). 2) Second stage: re-rank with a cross-encoder for higher accuracy on the candidates. Add metadata filtering, faceted search, and query expansion. For hybrid: combine sparse (BM25) and dense retrieval scores. Use incremental indexing for new documents. Monitor search quality with NDCG and user click-through metrics."),

    dict(subject="NLP", difficulty="Hard", type="Situational", company="Amazon", topic="Deployment",
         text="Your NLP model needs to support 15 languages but you only have labelled data in English. How would you approach this?",
         answer="Use multilingual pretrained models (XLM-R, mBERT). Fine-tune on English labelled data and evaluate zero-shot transfer to other languages. For critical languages, use translate-train: machine-translate English training data to target languages and fine-tune. Collect a small evaluation set in each target language for proper assessment. Consider language-specific adapters for languages where zero-shot transfer is poor. Monitor per-language performance in production."),

    dict(subject="NLP", difficulty="Hard", type="Situational", company="Meta", topic="Safety",
         text="You are deploying an LLM-powered customer service chatbot. What safety measures would you implement?",
         answer="Input guardrails: content moderation filter, prompt injection detection, PII redaction. Output guardrails: toxicity filter, factual grounding (RAG with verified knowledge base), confidence-based fallback to human agents. System design: restrict model capabilities (no code execution, no external API calls), log all conversations for audit, implement rate limiting, add user feedback mechanism. Regular red-teaming and adversarial testing. Human-in-the-loop for high-stakes decisions."),

    # ─────────────────────────────────────────
    # COMPUTER VISION — 35 new questions
    # ─────────────────────────────────────────

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What are the common color spaces used in computer vision?",
         answer="RGB: default for displays, three channels (Red, Green, Blue). HSV: Hue (color), Saturation, Value (brightness) — better for color-based segmentation. LAB: L (lightness), A and B (color opponents) — perceptually uniform, good for color comparison. Grayscale: single channel, used when color is not important. Converting between color spaces is common in preprocessing pipelines. OpenCV uses BGR by default."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Wipro", topic="Image Processing",
         text="What is edge detection and how do Canny and Sobel differ?",
         answer="Edge detection identifies boundaries in images where pixel intensity changes sharply. Sobel applies directional gradient filters (horizontal and vertical) to detect edges, outputting gradient magnitude. Canny is a multi-stage algorithm: Gaussian smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding. Canny produces cleaner, thinner edges and is more robust than Sobel. Both are foundational in traditional CV."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Infosys", topic="Image Processing",
         text="What are morphological operations in image processing?",
         answer="Morphological operations process binary/grayscale images using a structuring element (kernel). Erosion: shrinks bright regions, removes small noise. Dilation: expands bright regions, fills small holes. Opening (erosion then dilation): removes small noise while preserving shape. Closing (dilation then erosion): fills small holes. Used for: noise removal, shape analysis, connected component extraction. Applied in OCR, medical imaging, and object detection preprocessing."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Detection",
         text="What is the difference between face detection and face recognition?",
         answer="Face detection locates faces in an image — it answers 'where are the faces?' (bounding boxes). Face recognition identifies who the face belongs to — it answers 'whose face is this?' Detection is easier and comes first in the pipeline. Detection methods: Haar cascades, HOG+SVM, MTCNN, RetinaFace. Recognition methods: FaceNet (triplet loss), ArcFace (additive angular margin). Recognition requires a database of known faces."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="TCS", topic="Tasks",
         text="What is Optical Character Recognition (OCR) and what are modern approaches?",
         answer="OCR converts images of text into machine-readable text. Traditional: binarise, segment characters, classify each (template matching or SVM). Modern: end-to-end deep learning — CRNN (CNN for features + RNN for sequence) with CTC loss, or transformer-based models (TrOCR). Tesseract is a popular open-source OCR engine. Challenges: handwritten text, curved text, low resolution, and multilingual documents."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Wipro", topic="Fundamentals",
         text="What is image resolution and how does it affect model performance?",
         answer="Image resolution is the number of pixels (width × height). Higher resolution provides more detail but increases computation and memory. Most CNN models resize inputs to a fixed size (224×224, 384×384). Too low resolution loses important details (small objects). Too high adds noise and computational cost. The optimal resolution depends on the task — object detection needs higher resolution than classification. Multi-scale approaches process at multiple resolutions."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Segmentation",
         text="What is the difference between semantic, instance, and panoptic segmentation?",
         answer="Semantic segmentation labels every pixel with a class (all cars are 'car' — no distinction between individual cars). Instance segmentation distinguishes individual objects (car-1, car-2). Panoptic segmentation combines both: stuff classes (sky, road) get semantic labels, thing classes (cars, people) get instance labels. Models: U-Net for semantic, Mask R-CNN for instance, Panoptic FPN for panoptic."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Infosys", topic="Tasks",
         text="What is pose estimation in computer vision?",
         answer="Pose estimation detects the position of body keypoints (joints, landmarks) from images or video. Top-down: detect person first, then estimate keypoints. Bottom-up: detect all keypoints first, then group by person (faster for multiple people). Models: OpenPose, HRNet, MediaPipe. Applications: sports analytics, fitness apps, gesture recognition, AR/VR, and physiotherapy. Outputs are typically 17-25 keypoints with x,y coordinates and confidence scores."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Features",
         text="What are SIFT, SURF, and ORB feature detectors?",
         answer="These detect and describe distinctive local features in images. SIFT (Scale-Invariant Feature Transform): robust to scale and rotation, but slow and patented (patent expired). SURF: faster version of SIFT using integral images. ORB (Oriented FAST and Rotated BRIEF): fast, free, good for real-time applications. Used for image matching, stitching, SLAM, and object recognition. Largely replaced by learned features (SuperPoint) in modern applications."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="TCS", topic="Video",
         text="What is optical flow and what is it used for?",
         answer="Optical flow estimates the motion of pixels between consecutive video frames, producing a vector field showing how each pixel moved. Methods: Lucas-Kanade (sparse, fast), Farneback (dense), FlowNet/RAFT (deep learning). Used for: motion detection, video stabilisation, action recognition, autonomous driving, and video interpolation. It assumes brightness constancy and small motion between frames."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Google", topic="Detection",
         text="What is the difference between anchor-based and anchor-free object detectors?",
         answer="Anchor-based detectors (Faster R-CNN, SSD, YOLOv3) predefine a set of reference boxes (anchors) at each location and predict offsets from these anchors. They require careful anchor design. Anchor-free detectors (CenterNet, FCOS, YOLOv8) directly predict object centres and sizes without predefined anchors. Anchor-free methods are simpler, have fewer hyperparameters, and often achieve competitive or better performance. Modern YOLO versions are anchor-free."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Amazon", topic="Architectures",
         text="What is a Feature Pyramid Network (FPN) and why is it important?",
         answer="FPN builds a multi-scale feature pyramid from a backbone CNN by combining high-resolution low-level features (edges, textures) with low-resolution high-level features (semantic meaning) through top-down pathway and lateral connections. This enables detecting objects at multiple scales — small objects use high-resolution features, large objects use low-resolution features. FPN is a standard component in modern object detectors (Faster R-CNN, RetinaNet, Mask R-CNN)."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Google", topic="3D Vision",
         text="What is depth estimation and what are monocular vs stereo approaches?",
         answer="Depth estimation predicts distance from the camera to each pixel. Stereo depth uses two cameras (like human eyes) and computes disparity between matched pixels — depth is inversely proportional to disparity. Monocular depth estimation uses a single image and deep learning to predict depth from learned cues (size, texture gradients, occlusion). Monocular is more practical (single camera) but less accurate. Models: MiDaS, DPT. Used in AR, robotics, and autonomous driving."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Generation",
         text="What is image super-resolution and how do modern approaches work?",
         answer="Super-resolution reconstructs high-resolution images from low-resolution inputs. Classical: interpolation (bicubic). Deep learning: SRCNN (first CNN approach), ESRGAN (GAN-based, produces realistic textures), SwinIR (transformer-based). GAN-based methods produce sharper results but may hallucinate details. Perceptual loss and adversarial loss produce more visually pleasing results than pixel-wise MSE. Applications: satellite imagery, medical imaging, video enhancement, and photo upscaling."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Generation",
         text="What is neural style transfer and how does it work?",
         answer="Style transfer applies the artistic style of one image to the content of another. Original approach (Gatys et al.): optimise a generated image to match content features (high-level CNN activations) of one image and style features (Gram matrices of activations) of another. Feed-forward methods (Johnson et al.) train a network for real-time transfer. AdaIN (Adaptive Instance Normalisation) enables arbitrary style transfer. Used in apps like Prisma."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Google", topic="Tasks",
         text="What is image retrieval and how do modern systems work?",
         answer="Image retrieval finds similar images in a database given a query image. Modern approach: encode images into compact embeddings using a trained CNN/ViT, store embeddings in a vector database (FAISS, Milvus), and find nearest neighbours at query time. Training uses metric learning (contrastive/triplet loss) or ArcFace. Techniques: global descriptors (GeM pooling), re-ranking, and query expansion. Used in reverse image search, product matching, and duplicate detection."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Amazon", topic="Robustness",
         text="What are adversarial attacks on vision models and how do you defend against them?",
         answer="Adversarial attacks add imperceptible perturbations to images that cause misclassification. FGSM (Fast Gradient Sign Method) follows the gradient to maximise loss. PGD is an iterative version. Physical-world attacks use printed patches. Defences: adversarial training (train on adversarial examples), input preprocessing (JPEG compression, denoising), certified defences (randomised smoothing), and ensemble methods. No defence is foolproof — it is an ongoing arms race."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Any", topic="Data",
         text="What is synthetic data for training vision models and when is it useful?",
         answer="Synthetic data is generated programmatically (3D rendering, simulation, GANs, diffusion models) rather than collected from the real world. Useful when: real data is scarce, expensive to label, or privacy-sensitive. Examples: synthetic faces for face recognition, rendered objects for detection, simulated driving scenes. Domain gap (difference between synthetic and real data) is the main challenge — addressed by domain randomisation and domain adaptation techniques."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Video",
         text="What is action recognition in video and what are the common approaches?",
         answer="Action recognition classifies human activities in video clips. Approaches: 2D CNN + temporal pooling (extract frame features, aggregate), 3D CNNs (C3D, I3D — convolve across space and time), Two-stream networks (separate RGB and optical flow), and Video Transformers (TimeSformer, ViViT — apply attention across space-time tokens). SlowFast networks use two pathways at different frame rates. Challenges: temporal reasoning, computational cost, and dataset bias."),

    dict(subject="CV", difficulty="Medium", type="Coding", company="Google", topic="Image Processing",
         text="How would you build an image preprocessing pipeline using OpenCV?",
         answer="1) Read image: cv2.imread(path). 2) Resize: cv2.resize(img, (width, height)). 3) Convert colour: cv2.cvtColor(img, cv2.COLOR_BGR2RGB). 4) Normalise: img = img / 255.0 or ImageNet normalisation. 5) Apply augmentations: cv2.flip(), rotation with cv2.getRotationMatrix2D(). 6) Blur/denoise: cv2.GaussianBlur(). For deep learning, use torchvision.transforms or albumentations for composable, GPU-accelerated augmentation pipelines."),

    dict(subject="CV", difficulty="Medium", type="Coding", company="Amazon", topic="Detection",
         text="How would you build a simple object detection pipeline using a pretrained model?",
         answer="Use a pretrained model from torchvision: model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True). Preprocess image: convert to tensor, normalise. Run inference: predictions = model([image_tensor]). Post-process: filter by confidence threshold, apply NMS (non-maximum suppression). Visualise: draw bounding boxes with labels and scores using matplotlib or OpenCV. For custom classes, fine-tune on your dataset using transfer learning."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Google", topic="3D Vision",
         text="What are point clouds and how are they processed in deep learning?",
         answer="Point clouds are sets of 3D points (x,y,z coordinates, optionally with colour/intensity) from LiDAR or depth sensors. Unlike images, they are unordered and sparse. PointNet processes each point independently then aggregates with max pooling (invariant to order). PointNet++ adds local structure with hierarchical grouping. Voxel-based methods (VoxelNet) discretise into 3D grids. Used in autonomous driving, robotics, and AR. Challenges: irregular structure, varying density, computational cost."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Meta", topic="Generation",
         text="What is image inpainting and how do modern deep learning approaches work?",
         answer="Image inpainting fills in missing or damaged regions of an image. Modern approaches: encoder-decoder networks with partial convolutions (ignore missing pixels), gated convolutions (learn soft masks), and transformer-based models that capture long-range context. GAN-based methods (DeepFill, LaMa) produce realistic textures. Recent diffusion model-based inpainting (Stable Diffusion inpainting) achieves the best quality. Applications: photo editing, object removal, image restoration, and cultural heritage preservation."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="How do deformable convolutions work and what problem do they solve?",
         answer="Standard convolutions sample input at fixed grid locations. Deformable convolutions learn 2D offsets for each sampling position, allowing the receptive field to adapt to object shape and scale. An additional conv layer predicts offsets from the input features. This enables modelling geometric transformations without explicit data augmentation. Particularly useful for: irregular object shapes, varying scales, and dense prediction tasks. Used in DCN (Deformable Convolutional Networks) and modern detectors."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Any", topic="Calibration",
         text="What is camera calibration and why is it important in computer vision?",
         answer="Camera calibration determines intrinsic parameters (focal length, principal point, distortion coefficients) and extrinsic parameters (camera position and orientation in world coordinates). It maps 3D world points to 2D image points. Done using a calibration pattern (checkerboard) and Zhang's method (implemented in cv2.calibrateCamera). Essential for: 3D reconstruction, AR, stereo vision, measurement applications, and undistorting images. Without calibration, geometric measurements from images are inaccurate."),

    dict(subject="CV", difficulty="Hard", type="Situational", company="Google", topic="Deployment",
         text="You need to deploy a real-time object detection system on an edge device with limited compute. How would you approach this?",
         answer="Model selection: use efficient architectures (YOLOv8-nano, MobileNet-SSD, EfficientDet-Lite). Optimise: quantise to INT8 (TensorRT, TFLite), prune unimportant channels, use knowledge distillation from a larger model. Framework: deploy with TensorRT on NVIDIA Jetson, TFLite on mobile, or ONNX Runtime. Reduce input resolution to the minimum needed. Benchmark latency and accuracy tradeoffs. Consider hardware-specific optimisations and batching. Monitor inference time, memory, and power consumption in production."),

    dict(subject="CV", difficulty="Hard", type="Situational", company="Amazon", topic="Quality",
         text="You are building a product image quality detection system for an e-commerce platform. What approach would you take?",
         answer="Define quality criteria: resolution, blur, lighting, background consistency, watermarks, text overlay. Train a multi-label classifier on manually labelled examples for each defect type. Use a backbone like EfficientNet with multiple classification heads. For blur detection, combine learned features with traditional metrics (Laplacian variance). Create an automated pipeline: ingest → quality check → accept/flag/reject. Set thresholds per category (jewellery needs higher quality than electronics). A/B test the impact on conversion rates."),

    dict(subject="CV", difficulty="Hard", type="Situational", company="Meta", topic="Ethics",
         text="Your team is asked to build a system that estimates age and gender from photos for targeted advertising. What technical and ethical concerns would you raise?",
         answer="Technical concerns: accuracy varies across demographics (worse for underrepresented groups), lighting and angle sensitivity, adversarial robustness. Ethical concerns: privacy (processing biometric data requires consent under GDPR), potential for discrimination (age/gender-based targeting can be discriminatory), consent (users may not know their photos are being analysed), bias amplification, and regulatory compliance. Recommend: privacy-preserving approaches, clear user consent, bias audits, opt-out mechanisms, and consulting legal/ethics teams before deployment."),

    dict(subject="CV", difficulty="Hard", type="Situational", company="Google", topic="Scale",
         text="You need to build an image similarity search system that handles 100 million images with sub-second query time. How would you design it?",
         answer="Extract embeddings using a trained vision model (ViT or EfficientNet with metric learning). Store embeddings in an approximate nearest-neighbour index: FAISS with IVF (Inverted File) + PQ (Product Quantisation) for memory efficiency, or ScaNN. Shard the index across multiple machines for 100M scale. Use a two-stage approach: fast ANN retrieval (top-1000), then precise re-ranking with a more expensive model. Cache popular queries. Index supports incremental updates. Monitor recall@K and query latency."),

])

# ══════════════════════════════════════════════════════════════
# BATCH 3 — Extra Conceptual Questions (deepening coverage)
# ══════════════════════════════════════════════════════════════

QUESTIONS.extend([

    # ── ML Conceptual ──────────────────────────────────────────

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Any", topic="Evaluation",
         text="What is the F1 score and when is it more useful than accuracy?",
         answer="F1 score is the harmonic mean of precision and recall: 2*(P*R)/(P+R). It is more useful than accuracy when classes are imbalanced. For example, in a dataset with 95% negatives, a model predicting all negative gets 95% accuracy but 0% F1 for the positive class. F1 penalises models that sacrifice either precision or recall."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="Wipro", topic="Fundamentals",
         text="What is the curse of dimensionality?",
         answer="As the number of features grows, the volume of the feature space increases exponentially, making data sparse. Distances between points become nearly equal, hurting distance-based algorithms like KNN. More features also increase overfitting risk and training time. Solutions: feature selection, PCA, autoencoders, or domain-driven feature engineering to reduce dimensions."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Algorithms",
         text="How does a Random Forest make predictions and why is it better than a single Decision Tree?",
         answer="Random Forest builds many decision trees on random bootstrap samples and random feature subsets, then aggregates their predictions (majority vote for classification, average for regression). It is better than a single tree because averaging reduces variance and overfitting while maintaining low bias. The randomness decorrelates the trees, making the ensemble more robust. Feature importance can be derived from mean decrease in impurity across trees."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Amazon", topic="Evaluation",
         text="What is stratified sampling and why is it important in train-test splits?",
         answer="Stratified sampling ensures each split has the same class proportions as the full dataset. Without it, a random split could put most of a minority class into one set, giving misleading evaluation results. It is especially critical for imbalanced datasets. In sklearn, use train_test_split with stratify=y or StratifiedKFold for cross-validation."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Infosys", topic="Algorithms",
         text="What is the difference between hard and soft voting in ensemble methods?",
         answer="Hard voting takes the majority class predicted by individual models. Soft voting averages the predicted probabilities and picks the class with the highest average probability. Soft voting is usually better because it accounts for prediction confidence — a model 90% sure should carry more weight than one that is 51% sure. Soft voting requires models that output calibrated probabilities."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Google", topic="Preprocessing",
         text="What is target encoding and when would you use it instead of one-hot encoding?",
         answer="Target encoding replaces each category with the mean of the target variable for that category. Use it for high-cardinality categorical features (like zip code or user ID) where one-hot encoding creates too many columns. Risk: it can leak target information and cause overfitting. Mitigate with smoothing (blend category mean with global mean) and cross-validation-based encoding."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Google", topic="Theory",
         text="What is the VC dimension and why does it matter in learning theory?",
         answer="VC (Vapnik-Chervonenkis) dimension measures the capacity of a model — the largest set of points it can shatter (classify in all possible ways). A linear classifier in 2D has VC dimension 3. Higher VC dimension means the model can fit more complex patterns but also overfits more easily. It provides theoretical bounds on generalisation error: more training data is needed for higher VC dimension models."),

    dict(subject="ML", difficulty="Hard", type="Conceptual", company="Amazon", topic="Algorithms",
         text="Explain how Gradient Boosted Trees (GBT) work step by step.",
         answer="GBT builds trees sequentially. Step 1: start with a simple prediction (e.g., mean). Step 2: compute residuals (errors). Step 3: fit a new shallow tree to predict the residuals. Step 4: add this tree's predictions (scaled by learning rate) to the running prediction. Step 5: repeat with new residuals. Each tree corrects previous errors. Regularisation via learning rate, max depth, subsampling, and L1/L2 penalties prevents overfitting. XGBoost adds second-order gradients for efficiency."),

    dict(subject="ML", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Fundamentals",
         text="What is the difference between online learning and batch learning?",
         answer="Batch learning trains on the entire dataset at once — the model is retrained from scratch when new data arrives. Online learning updates the model incrementally with each new data point or mini-batch. Online learning is useful for streaming data, very large datasets that do not fit in memory, and environments where the data distribution shifts over time. SGD naturally supports online learning."),

    dict(subject="ML", difficulty="Easy", type="Conceptual", company="TCS", topic="Evaluation",
         text="What is a learning curve and what does it tell you?",
         answer="A learning curve plots training and validation performance against the number of training samples. If both scores are low, the model underfits (high bias) — try a more complex model. If training score is high but validation is low, the model overfits (high variance) — get more data or regularise. If both converge to a high score, the model is well-fitted. It helps decide whether to collect more data or change the model."),

    # ── DL Conceptual ──────────────────────────────────────────

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="Any", topic="Architectures",
         text="What is a Recurrent Neural Network (RNN) and what problem does it solve?",
         answer="RNNs process sequential data by maintaining a hidden state that carries information from previous time steps. At each step, the hidden state is updated based on the current input and previous hidden state. They solve problems where order matters: text, speech, time series. Vanilla RNNs suffer from vanishing gradients for long sequences, which is why LSTMs and GRUs were developed."),

    dict(subject="DL", difficulty="Easy", type="Conceptual", company="TCS", topic="Training",
         text="What is the difference between online, batch, and mini-batch gradient descent?",
         answer="Batch GD computes gradients on the entire dataset — stable but slow for large data. Online (stochastic) GD uses one sample at a time — fast and noisy, can escape local minima. Mini-batch GD uses small batches (32-256 samples) — balances speed and stability, enables GPU parallelism. Mini-batch is the standard in deep learning. Batch size affects generalisation: smaller batches often generalise better."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Google", topic="Architectures",
         text="What is a U-Net and why is it popular for image segmentation?",
         answer="U-Net has an encoder (downsampling) path and a decoder (upsampling) path connected by skip connections that pass high-resolution features directly to the decoder. This preserves spatial details crucial for pixel-level predictions. It works well with small datasets (originally designed for medical imaging with ~30 images). Variants include U-Net++, Attention U-Net, and nnU-Net which auto-configures for different tasks."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Amazon", topic="Training",
         text="What is label smoothing and why does it help?",
         answer="Instead of using hard labels (0 or 1), label smoothing uses soft targets like 0.1 and 0.9. This prevents the model from becoming overconfident and improves calibration. The model learns that no prediction should be 100% certain. It acts as a regulariser, reducing overfitting. Common in image classification and machine translation. Typically use a smoothing factor of 0.1."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Fundamentals",
         text="What is the difference between weight decay and L2 regularisation?",
         answer="For standard SGD, weight decay and L2 regularisation are mathematically equivalent — both shrink weights towards zero. However, for adaptive optimisers like Adam, they differ. L2 regularisation adds the penalty to the loss, which gets scaled by the adaptive learning rate. Weight decay (AdamW) directly shrinks weights regardless of the adaptive rate, providing more consistent regularisation. AdamW is preferred over Adam with L2 for this reason."),

    dict(subject="DL", difficulty="Medium", type="Conceptual", company="Any", topic="Architectures",
         text="What is the difference between 1x1, 3x3 and dilated convolutions?",
         answer="1x1 convolutions change the number of channels without altering spatial dimensions — used for channel mixing and dimensionality reduction (Network-in-Network, Inception). 3x3 is the standard spatial convolution capturing local patterns. Dilated (atrous) convolutions insert gaps between kernel elements, expanding the receptive field without increasing parameters — used in semantic segmentation (DeepLab) and WaveNet for audio."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="What is Flash Attention and why is it important for transformers?",
         answer="Standard self-attention is O(n²) in both time and memory for sequence length n. Flash Attention is an IO-aware algorithm that computes exact attention by tiling the computation to fit in fast GPU SRAM, avoiding reading/writing the full n×n attention matrix to slow GPU HBM. It reduces memory from O(n²) to O(n) and is 2-4x faster. It enables training with much longer sequences. Flash Attention 2 further optimises parallelism."),

    dict(subject="DL", difficulty="Hard", type="Conceptual", company="Meta", topic="Fine-Tuning",
         text="What is the difference between full fine-tuning, LoRA, prefix tuning and prompt tuning?",
         answer="Full fine-tuning updates all model parameters — best accuracy but high cost. LoRA adds trainable low-rank matrices to attention layers (~0.1-1% params). Prefix tuning prepends learnable virtual tokens to each layer's hidden states. Prompt tuning only prepends learnable tokens to the input embedding. Trade-off: full > LoRA > prefix > prompt tuning in accuracy but reverse in efficiency. LoRA is the most popular balance of quality and cost."),

    # ── DSA Conceptual ─────────────────────────────────────────

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is amortised time complexity? Give an example.",
         answer="Amortised analysis averages the cost of an operation over a sequence of operations, even if individual operations are expensive. Example: ArrayList/dynamic array appending is O(1) amortised. Most appends are O(1), but occasionally the array doubles in size (O(n) copy). Over n appends, total work is O(n), so each append is O(1) amortised. It is different from average case — amortised guarantees hold for any sequence."),

    dict(subject="DSA", difficulty="Easy", type="Conceptual", company="TCS", topic="Hashing",
         text="What are the common collision resolution strategies in hash tables?",
         answer="Chaining: each bucket stores a linked list of colliding entries — simple, handles high load. Open addressing: on collision, probe for the next empty slot. Linear probing: check next slot (causes clustering). Quadratic probing: check i² slots ahead (reduces clustering). Double hashing: use a second hash function for step size (best distribution). Python dicts use open addressing with perturbation."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Google", topic="Graphs",
         text="What is the difference between a tree, a forest, and a graph?",
         answer="A graph is a set of vertices and edges (can have cycles, be directed/undirected). A tree is a connected acyclic undirected graph — n vertices, n-1 edges, exactly one path between any two vertices. A forest is a collection of disjoint trees (acyclic but not necessarily connected). Every tree is a graph, but not every graph is a tree. Binary trees, BSTs, and heaps are special cases of trees."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Amazon", topic="Complexity",
         text="What is the Master Theorem and how is it used?",
         answer="The Master Theorem solves recurrences of the form T(n) = aT(n/b) + O(n^d), common in divide-and-conquer algorithms. Three cases: if d < log_b(a), T(n) = O(n^log_b(a)). If d = log_b(a), T(n) = O(n^d log n). If d > log_b(a), T(n) = O(n^d). Example: merge sort T(n) = 2T(n/2) + O(n) → a=2, b=2, d=1, case 2 → O(n log n). It provides quick complexity analysis without solving the full recurrence."),

    dict(subject="DSA", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Strings",
         text="What is the Rabin-Karp algorithm and when would you use it?",
         answer="Rabin-Karp uses rolling hash to find pattern matches in text. Compute hash of the pattern and slide a window across the text, updating the hash in O(1) using rolling hash. On hash match, verify with character comparison to handle collisions. Average O(n+m), worst O(nm). Best for multi-pattern search (search for many patterns simultaneously) — each pattern's hash is checked in O(1) against the window hash."),

    dict(subject="DSA", difficulty="Hard", type="Conceptual", company="Google", topic="Advanced",
         text="What is a Bloom filter and where is it used?",
         answer="A Bloom filter is a space-efficient probabilistic data structure that tests set membership. It uses k hash functions mapping elements to k positions in a bit array. Query: if all k bits are set, the element is 'probably in the set' (false positives possible). If any bit is 0, the element is 'definitely not in the set' (no false negatives). Used in: database query optimisation, cache lookups, spell checkers, and network routers. Cannot delete elements (use Counting Bloom filter for that)."),

    # ── Python Conceptual ──────────────────────────────────────

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is the difference between a module, a package, and a library in Python?",
         answer="A module is a single .py file containing functions, classes and variables. A package is a directory of modules with an __init__.py file, enabling hierarchical organisation. A library is a collection of packages distributed together (e.g., NumPy, pandas). You import modules with 'import', packages with 'from package import module'. The terms are sometimes used loosely — 'library' and 'package' are often interchangeable in casual usage."),

    dict(subject="Python", difficulty="Easy", type="Conceptual", company="TCS", topic="Fundamentals",
         text="What does 'if __name__ == \"__main__\"' do in Python?",
         answer="It checks whether the script is being run directly (not imported). When a script runs directly, __name__ is set to '__main__'. When imported as a module, __name__ is the module's name. This idiom lets you write code that executes only when the file is run directly — useful for putting test code, CLI entry points, or examples that should not run on import."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Google", topic="Advanced",
         text="What is the difference between @staticmethod and @classmethod in practice?",
         answer="@staticmethod takes no implicit first argument — it is essentially a regular function namespaced under the class. @classmethod receives the class itself as the first argument (cls), enabling it to access class-level attributes and create instances of subclasses. Use @classmethod for factory methods (alternative constructors like dict.fromkeys()). Use @staticmethod for utility functions logically grouped with the class but not needing class or instance state."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Amazon", topic="Modules",
         text="What is the difference between NumPy and Pandas, and when do you use each?",
         answer="NumPy provides fast n-dimensional arrays and vectorised mathematical operations — use for numerical computation, linear algebra, and when you need raw performance on homogeneous data. Pandas provides DataFrames with labelled rows/columns, handling mixed types, missing data, groupby, merging, and time series — use for data manipulation, cleaning, and analysis. Pandas is built on NumPy. For pure computation, NumPy is faster; for data wrangling, Pandas is more convenient."),

    dict(subject="Python", difficulty="Medium", type="Conceptual", company="Microsoft", topic="Advanced",
         text="How does Python's dictionary work internally?",
         answer="Python dicts use a hash table with open addressing. When inserting a key, Python computes its hash, finds a slot in the internal array, and stores the key-value pair. Collisions are resolved by probing. Since Python 3.7, dicts maintain insertion order by using a compact array of indices into a separate entries array. Average O(1) for get/set/delete. The table resizes (doubles) when 2/3 full. Keys must be hashable (immutable)."),

    dict(subject="Python", difficulty="Hard", type="Conceptual", company="Google", topic="Advanced",
         text="What is the Method Resolution Order (MRO) in Python and how does it handle multiple inheritance?",
         answer="MRO determines the order in which base classes are searched when calling a method. Python uses the C3 linearisation algorithm which ensures: a class is checked before its parents, and the order of parents is preserved. Access it via ClassName.__mro__ or ClassName.mro(). super() follows the MRO, not just the immediate parent. This prevents the diamond problem where a method could be ambiguous with multiple inheritance paths."),

    # ── Stats Conceptual ───────────────────────────────────────

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Any", topic="Probability",
         text="What is the difference between independent and mutually exclusive events?",
         answer="Independent events: the occurrence of one does not affect the other. P(A and B) = P(A) * P(B). Example: two coin flips. Mutually exclusive events: they cannot occur simultaneously. P(A and B) = 0. Example: rolling a 3 and a 5 on one die. Mutually exclusive events are never independent (unless one has probability 0), because if one occurs, the other definitely does not."),

    dict(subject="Stats", difficulty="Easy", type="Conceptual", company="Infosys", topic="Fundamentals",
         text="What is variance and how does it relate to standard deviation?",
         answer="Variance measures the average squared deviation from the mean: Var(X) = E[(X-mu)²]. Standard deviation is the square root of variance, bringing the measure back to the original units. If heights vary with variance 25 cm², the standard deviation is 5 cm — much more interpretable. Variance is easier to work with mathematically (additive for independent variables), but standard deviation is more intuitive for communication."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Google", topic="Testing",
         text="What is a t-test and what are its different types?",
         answer="A t-test compares means when the population standard deviation is unknown and sample size is small. One-sample t-test: is the sample mean different from a known value? Independent two-sample t-test: are two group means different? Paired t-test: are means different for the same subjects measured twice? Assumptions: normality (relaxed for large n by CLT), independence, equal variances (use Welch's t-test if not). Reports t-statistic and p-value."),

    dict(subject="Stats", difficulty="Medium", type="Conceptual", company="Amazon", topic="Regression",
         text="What is the difference between correlation and regression?",
         answer="Correlation measures the strength and direction of a linear relationship between two variables (-1 to +1). It is symmetric — correlation of X with Y equals Y with X. Regression models the relationship to predict one variable from another. It is asymmetric — predicting Y from X is different from predicting X from Y. Correlation does not imply a predictive model; regression provides one. Both assume linearity in their basic forms."),

    dict(subject="Stats", difficulty="Hard", type="Conceptual", company="Google", topic="Inference",
         text="What is the difference between frequentist and Bayesian confidence/credible intervals?",
         answer="Frequentist confidence interval: if you repeated the experiment many times, 95% of the computed intervals would contain the true parameter. It says nothing about the probability of the parameter being in this specific interval. Bayesian credible interval: there is a 95% probability that the parameter lies in this interval, given the data and prior. Bayesian intervals directly answer what we usually want to know but require specifying a prior distribution."),

    # ── NLP Conceptual ─────────────────────────────────────────

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What are stop words and should you always remove them?",
         answer="Stop words are common words (the, is, at, a) that appear frequently but carry little semantic meaning on their own. Removing them reduces noise and dimensionality for bag-of-words and TF-IDF models. However, do NOT remove them for: transformer models (BERT needs them for context), sentiment analysis ('not good' loses meaning without 'not'), and language models. The trend in modern NLP is minimal preprocessing."),

    dict(subject="NLP", difficulty="Easy", type="Conceptual", company="TCS", topic="Tasks",
         text="What is the difference between NER and POS tagging?",
         answer="POS (Part-of-Speech) tagging labels each word with its grammatical role: noun, verb, adjective, etc. NER (Named Entity Recognition) identifies and classifies named entities: person names, organisations, locations, dates, etc. POS tagging is about grammar; NER is about real-world entities. POS tagging is often a preprocessing step that helps NER. Both can be done with sequence labelling models (BiLSTM-CRF, BERT)."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Google", topic="Embeddings",
         text="How does Word2Vec learn word embeddings?",
         answer="Word2Vec learns embeddings by training a shallow neural network on word co-occurrence. Two architectures: CBOW (predicts a word from its context) and Skip-gram (predicts context from a word). Skip-gram with negative sampling is most common. The trained weight matrix becomes the embedding. Words in similar contexts get similar vectors, capturing semantic relationships like king - man + woman ≈ queen. Training is efficient with negative sampling."),

    dict(subject="NLP", difficulty="Medium", type="Conceptual", company="Amazon", topic="Tasks",
         text="What is dependency parsing and how does it differ from constituency parsing?",
         answer="Constituency parsing breaks a sentence into nested phrases (NP, VP, PP) forming a tree — shows phrase structure. Dependency parsing connects words with directed edges showing grammatical relationships (subject, object, modifier) — shows who does what to whom. Dependency parsing is more popular in modern NLP because it directly captures semantic relationships and works better across languages. SpaCy uses dependency parsing by default."),

    dict(subject="NLP", difficulty="Hard", type="Conceptual", company="Meta", topic="LLMs",
         text="What is the difference between autoregressive and masked language modelling?",
         answer="Autoregressive LM (GPT): predicts the next token given all previous tokens, left-to-right. Cannot see future context. Natural for text generation. Masked LM (BERT): masks random tokens and predicts them using both left and right context. Better for understanding tasks but not naturally generative. T5 bridges both: encoder uses bidirectional context, decoder is autoregressive. The choice determines what tasks the model excels at."),

    # ── CV Conceptual ──────────────────────────────────────────

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Any", topic="Fundamentals",
         text="What is a convolution operation in image processing?",
         answer="Convolution slides a small filter (kernel) over an image, computing the element-wise product and sum at each position. Different kernels detect different features: edge detection (Sobel), blurring (Gaussian), sharpening. In CNNs, the kernel values are learned during training. A 3x3 kernel on a 5x5 image produces a 3x3 output (without padding). Padding and stride control the output size."),

    dict(subject="CV", difficulty="Easy", type="Conceptual", company="Wipro", topic="Fundamentals",
         text="What is the difference between stride and padding in CNNs?",
         answer="Stride is the step size when sliding the filter — stride 1 moves one pixel at a time, stride 2 skips every other position (halving spatial dimensions). Padding adds extra pixels (usually zeros) around the input border. 'Same' padding keeps output size equal to input. 'Valid' padding uses no padding (output shrinks). Stride reduces spatial dimensions for efficiency; padding preserves spatial information at the edges."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Google", topic="Architectures",
         text="How does the Inception (GoogLeNet) module work?",
         answer="Inception modules apply multiple filter sizes (1x1, 3x3, 5x5) and max pooling in parallel on the same input, then concatenate the outputs. This captures features at multiple scales simultaneously. 1x1 convolutions are used before larger filters to reduce channel dimensions (bottleneck), keeping computation manageable. This architecture won ImageNet 2014 and inspired multi-scale feature extraction in modern networks."),

    dict(subject="CV", difficulty="Medium", type="Conceptual", company="Amazon", topic="Detection",
         text="How does Faster R-CNN work for object detection?",
         answer="Faster R-CNN has three components: 1) A backbone CNN extracts feature maps from the image. 2) A Region Proposal Network (RPN) generates candidate bounding boxes (anchors) with objectness scores. 3) An ROI (Region of Interest) pooling layer extracts fixed-size features for each proposal, which are classified and refined by fully connected layers. It is a two-stage detector — slower but more accurate than single-stage detectors like YOLO for small objects."),

    dict(subject="CV", difficulty="Hard", type="Conceptual", company="Google", topic="Architectures",
         text="How do Vision Transformers (ViT) process images differently from CNNs?",
         answer="ViT splits an image into fixed-size patches (e.g., 16x16), linearly embeds each patch, adds positional embeddings, and processes the sequence with a standard transformer encoder. Unlike CNNs, ViT has no inductive bias for locality or translation invariance — it learns these from data. ViT needs large datasets to outperform CNNs but scales better with data and compute. Hybrid models (CNN backbone + transformer) combine the strengths of both."),

])

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
        print(f"✅ Seeded {len(QUESTIONS)} questions successfully (400+ question bank).")

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
