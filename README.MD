# 🧠 Complete Deep Learning Roadmap

A complete roadmap to learn **Deep Learning from beginner → advanced → production-ready AI systems**.

The roadmap focuses on **understanding concepts, implementing them, and building real-world projects** rather than only watching tutorials.

---

## 🗺️ Overall Roadmap

```text
Python + NumPy
      ↓
Machine Learning Fundamentals
      ↓
Mathematics for Deep Learning
      ↓
Neural Network Fundamentals
      ↓
Backpropagation + Optimization
      ↓
PyTorch
      ↓
CNN + Computer Vision
      ↓
Advanced Computer Vision
      ↓
RNN → LSTM → GRU
      ↓
NLP Fundamentals
      ↓
Attention
      ↓
Transformers
      ↓
LLMs
      ↓
Fine-Tuning
      ↓
Embeddings + Vector Databases
      ↓
RAG
      ↓
Generative AI
      ↓
Multimodal AI
      ↓
Model Optimization
      ↓
Deployment + MLOps
      ↓
Production AI Systems
```

---

# 📚 Phase 0 — Prerequisites

Don't spend too much time here.

## 🐍 Python

Learn:

* Variables
* Data types
* Conditions
* Loops
* Functions
* Lists
* Tuples
* Sets
* Dictionaries
* Classes
* Exception handling
* File handling
* Modules and packages
* Virtual environments

### Important Libraries

```text
NumPy
Pandas
Matplotlib
Seaborn
Scikit-learn
```

> **Goal:** Become comfortable enough with Python to implement ML/DL algorithms without constantly looking up basic syntax.

---

# 🔢 Phase 1 — NumPy

Deep Learning heavily relies on arrays, matrices, and tensors.

## Learn

### Arrays

```python
np.array()
np.zeros()
np.ones()
np.random()
```

### Array Properties

```python
array.shape
array.ndim
array.size
array.dtype
```

### Operations

* Addition
* Subtraction
* Multiplication
* Division
* Broadcasting
* Indexing
* Slicing

### Linear Algebra Operations

```python
A @ B
```

Understand:

* Matrix multiplication
* Dot product
* Transpose
* Vector operations

### Important Concept

```text
Scalar
   ↓
Vector
   ↓
Matrix
   ↓
Tensor
```

> **Goal:** Understand how numerical data is represented and manipulated inside neural networks.

---

# 📐 Phase 2 — Mathematics for Deep Learning

You don't need extremely advanced mathematics.

Learn the mathematics that actually appears in Deep Learning.

---

## 2.1 Linear Algebra

Learn:

* Scalars
* Vectors
* Matrices
* Tensors
* Matrix multiplication
* Dot product
* Transpose
* Dimensions
* Eigenvalues
* Eigenvectors

Focus especially on:

```text
Vector
Matrix
Tensor
Matrix Multiplication
Dot Product
```

---

## 2.2 Calculus

Learn:

* Functions
* Derivatives
* Partial derivatives
* Chain rule
* Gradients

### Most Important Concept

**Gradient**

A gradient tells us how the model's parameters should change to reduce the error.

```text
Loss
 ↓
Gradient
 ↓
Weight Update
```

---

## 2.3 Probability & Statistics

Learn:

* Mean
* Variance
* Standard deviation
* Probability
* Conditional probability
* Expected value
* Bayes theorem
* Normal distribution
* Probability distributions

> **Goal:** Understand the mathematical ideas used by optimization and model evaluation.

---

# 🤖 Phase 3 — Machine Learning Fundamentals

Before going deep into neural networks, understand traditional Machine Learning.

---

## Supervised Learning

### Regression

* Linear Regression
* Polynomial Regression

### Classification

* Logistic Regression
* Decision Tree
* Random Forest
* KNN
* SVM
* Naive Bayes

---

## Unsupervised Learning

Learn:

* K-Means
* Clustering
* PCA

---

## Important ML Concepts

```text
Training Data
Validation Data
Test Data
```

Learn:

* Features
* Labels
* Overfitting
* Underfitting
* Bias
* Variance
* Data leakage
* Cross-validation
* Feature scaling
* Evaluation metrics

### Important Metrics

Classification:

```text
Accuracy
Precision
Recall
F1 Score
ROC-AUC
Confusion Matrix
```

Regression:

```text
MAE
MSE
RMSE
R²
```

---

# 🧠 Phase 4 — Neural Network Fundamentals

Now Deep Learning begins.

Understand what a neural network actually is.

---

## Basic Neuron

```text
Input
  ↓
Weights
  ↓
Bias
  ↓
Activation
  ↓
Output
```

Mathematically:

```text
y = wx + b
```

With activation:

```text
y = activation(wx + b)
```

---

# ⚡ Phase 5 — Activation Functions

Learn:

### Sigmoid

```text
σ(x)
```

Useful for:

* Binary classification
* Probability output

### Tanh

```text
tanh(x)
```

### ReLU

```text
max(0, x)
```

Very commonly used in hidden layers.

### Leaky ReLU

Understand why it exists and how it differs from ReLU.

### Softmax

Used commonly for multi-class classification.

---

# 📉 Phase 6 — Loss Functions

The model needs a way to measure how wrong its predictions are.

That is the **loss function**.

---

## Regression

Learn:

```text
MSE
MAE
```

---

## Classification

Learn:

```text
Binary Cross Entropy
Categorical Cross Entropy
```

---

## Learning Process

```text
Input
 ↓
Model
 ↓
Prediction
 ↓
Loss
 ↓
Gradient
 ↓
Weight Update
```

---

# ➡️ Phase 7 — Forward Propagation

Understand the complete forward pass.

```text
Input
 ↓
Layer 1
 ↓
Activation
 ↓
Layer 2
 ↓
Activation
 ↓
Output
 ↓
Prediction
 ↓
Loss
```

Understand:

* Weights
* Biases
* Activations
* Layers
* Output

---

# 🔄 Phase 8 — Backpropagation

⭐⭐⭐ **One of the most important Deep Learning concepts**

Understand:

```text
Forward Pass
      ↓
Prediction
      ↓
Loss
      ↓
Backpropagation
      ↓
Gradients
      ↓
Update Weights
      ↓
Repeat
```

Learn:

* Gradient
* Chain rule
* Gradient descent
* Learning rate
* Weight updates

### You should eventually be able to answer:

> How does a neural network learn?

without simply saying:

> "It uses backpropagation."

You should understand what happens during backpropagation.

---

# 🚀 Phase 9 — Optimization

Learn:

## Gradient Descent

```text
Batch Gradient Descent
Mini-Batch Gradient Descent
Stochastic Gradient Descent
```

---

## Optimizers

Learn:

```text
SGD
Momentum
AdaGrad
RMSProp
Adam
AdamW
```

Pay special attention to:

```text
Adam
AdamW
```

---

# 🧪 Phase 10 — Neural Network From Scratch

Before using PyTorch, build a small neural network using:

```text
Python + NumPy
```

Do not start by implementing huge architectures.

Build a simple binary classifier.

---

## Project 1 — Neural Network From Scratch

Architecture:

```text
Input
 ↓
Dense Layer
 ↓
ReLU
 ↓
Dense Layer
 ↓
Sigmoid
 ↓
Prediction
```

Implement manually:

* Forward propagation
* Loss calculation
* Backpropagation
* Gradient calculation
* Gradient descent
* Weight updates

### Goal

Understand what Deep Learning frameworks are doing internally.

---

# 🔥 Phase 11 — PyTorch

Now learn **PyTorch deeply**.

---

## Core PyTorch

Learn:

```python
torch
torch.tensor
torch.nn
torch.optim
torch.utils.data
```

---

## Dataset & DataLoader

Learn:

```text
Dataset
DataLoader
Batching
Shuffling
```

---

## Neural Network

Learn:

```python
nn.Module
```

Understand:

```python
forward()
```

---

## Training Loop

Understand:

```python
loss.backward()
optimizer.step()
optimizer.zero_grad()
```

The training process:

```text
Data
 ↓
Forward Pass
 ↓
Prediction
 ↓
Loss
 ↓
Backward Pass
 ↓
Gradients
 ↓
Optimizer
 ↓
Updated Weights
```

---

# 🔢 Phase 12 — First PyTorch Projects

## Project 2 — MNIST

Build:

**Handwritten Digit Classifier**

Learn:

* Dataset loading
* DataLoader
* Neural networks
* Training loop
* Validation
* Testing
* Accuracy

---

## Project 3 — Fashion-MNIST

Build:

**Clothing Classification Model**

Learn:

* Image tensors
* Classification
* Model evaluation
* Training improvements

---

## Project 4 — Tabular Neural Network

Build:

**Customer Prediction Model**

Learn:

* Numerical features
* Categorical features
* Neural networks for tabular data
* Regression/classification

---

# 👁️ Phase 13 — CNNs

Now enter **Computer Vision**.

---

## Convolution

Understand:

```text
Image
 ↓
Kernel / Filter
 ↓
Feature Map
```

Learn:

* Kernel
* Stride
* Padding
* Channels
* Feature maps
* Receptive field

---

## CNN Architecture

Understand:

```text
Image
 ↓
Conv2D
 ↓
Activation
 ↓
Pooling
 ↓
Conv2D
 ↓
Activation
 ↓
Pooling
 ↓
Flatten
 ↓
Dense
 ↓
Output
```

---

# 🧱 Phase 14 — CNN Components

Learn:

### Convolution

```text
Conv2D
```

### Pooling

```text
Max Pooling
Average Pooling
```

### Other Concepts

* Number of channels
* Feature maps
* Padding
* Stride
* Kernel size
* Receptive field

---

# 🏛️ Phase 15 — Important CNN Architectures

Study the evolution of CNNs.

```text
LeNet
   ↓
AlexNet
   ↓
VGG
   ↓
GoogLeNet / Inception
   ↓
ResNet
   ↓
DenseNet
   ↓
EfficientNet
```

Don't just memorize architectures.

Understand:

> What problem did each architecture solve?

---

# 🖼️ Phase 16 — Computer Vision Projects

## Project 5 — Cats vs Dogs

Learn:

* Image preprocessing
* CNN
* Data augmentation
* Training
* Validation
* Testing

---

## Project 6 — Plant Disease Detection

Learn:

* Multi-class classification
* Data augmentation
* Transfer learning

---

## Project 7 — Fracture Detection

Build a stronger version of your fracture detection project.

Use:

```text
ResNet
Transfer Learning
Data Augmentation
Evaluation
Grad-CAM
```

Don't focus only on accuracy.

Also understand:

```text
Precision
Recall
F1
Confusion Matrix
ROC-AUC
```

---

# 🔄 Phase 17 — Transfer Learning

⭐⭐⭐ **Very important for real-world Computer Vision**

Instead of:

```text
Random Model
     ↓
Train From Scratch
```

Use:

```text
Pretrained Model
      ↓
Your Dataset
      ↓
Fine-Tuning
```

Learn:

* Feature extraction
* Fine-tuning
* Freezing layers
* Unfreezing layers
* Learning-rate scheduling

Study:

```text
ResNet
EfficientNet
ConvNeXt
ViT
```

---

# 🎯 Phase 18 — Object Detection

Move from:

```text
"What is in this image?"
```

to:

```text
"Where is the object?"
```

---

## Learn

* Bounding boxes
* IoU
* Non-Maximum Suppression
* Precision
* Recall
* mAP

---

## Architectures

### R-CNN Family

```text
R-CNN
Fast R-CNN
Faster R-CNN
```

### Modern Detectors

```text
YOLO
SSD
RetinaNet
```

---

# 🚗 Phase 19 — Object Detection Projects

## Project 8

**Vehicle Detection**

---

## Project 9

**Helmet Detection**

---

## Project 10

**Road Object Detection**

---

## Project 11

**Real-Time Object Detection**

```text
Camera
 ↓
YOLO
 ↓
Object Detection
 ↓
Bounding Boxes
```

---

# 🎨 Phase 20 — Image Segmentation

Move from:

```text
Classification
```

to:

```text
Object Detection
```

to:

```text
Pixel-Level Prediction
```

---

## Types

### Semantic Segmentation

Classify every pixel.

### Instance Segmentation

Identify every individual object.

---

## Architectures

Learn:

```text
FCN
U-Net
DeepLab
Mask R-CNN
```

---

# 👁️ Phase 21 — Advanced Computer Vision

Learn:

## Vision Transformers

```text
ViT
Swin Transformer
```

Then explore:

```text
CLIP
SAM
DINO
DINOv2
```

Focus on understanding:

* Architecture
* Training objective
* Use cases
* Fine-tuning
* Inference

---

# 🔁 Phase 22 — Sequence Models

Move from images to sequential data.

Learn:

```text
RNN
 ↓
LSTM
 ↓
GRU
```

Understand:

* Hidden state
* Sequence processing
* Vanishing gradients
* Exploding gradients

---

# 📝 Phase 23 — NLP Fundamentals

Understand:

```text
Text
 ↓
Tokenization
 ↓
Numerical Representation
 ↓
Model
 ↓
Prediction
```

Learn:

* Tokenization
* Vocabulary
* Embeddings
* Word embeddings
* Sentence embeddings
* Word2Vec
* GloVe

---

# 👀 Phase 24 — Attention

⭐⭐⭐ **Major milestone**

Understand why models need to focus on different parts of the input.

Learn:

```text
Query
Key
Value
```

Then:

```text
Attention
 ↓
Self-Attention
 ↓
Multi-Head Attention
```

Understand the basic process:

```text
Q × Kᵀ
   ↓
Softmax
   ↓
Attention Weights
   ↓
× V
```

---

# 🤖 Phase 25 — Transformers

⭐⭐⭐⭐⭐ **Essential for modern AI**

Understand:

```text
Embedding
 ↓
Positional Information
 ↓
Self-Attention
 ↓
Feed Forward Network
 ↓
Normalization
 ↓
Output
```

---

## Original Transformer

Understand:

```text
Encoder
Decoder
```

---

# 🧠 Phase 26 — Transformer Models

Study:

```text
BERT
GPT
T5
ViT
```

Understand their differences:

| Model | Main Architecture | Typical Use            |
| ----- | ----------------- | ---------------------- |
| BERT  | Encoder           | Language understanding |
| GPT   | Decoder           | Text generation        |
| T5    | Encoder + Decoder | Text-to-text tasks     |
| ViT   | Transformer       | Computer Vision        |

---

# 🦙 Phase 27 — Large Language Models

⭐⭐⭐⭐⭐

Learn:

```text
Pretraining
     ↓
Instruction Tuning
     ↓
Fine-Tuning
     ↓
Inference
```

Understand:

* Tokens
* Context window
* Parameters
* Embeddings
* Attention
* Positional encoding
* Sampling
* Temperature
* Top-k
* Top-p

---

# 🛠️ Phase 28 — LLM Fine-Tuning

Understand:

```text
Full Fine-Tuning
        ↓
Parameter Efficient Fine-Tuning
        ↓
LoRA / QLoRA
```

Learn:

```text
LoRA
QLoRA
PEFT
```

Understand why fine-tuning large models normally can be expensive.

---

# 🔎 Phase 29 — Embeddings & Vector Databases

Learn:

```text
Text
 ↓
Embedding Model
 ↓
Vector
 ↓
Vector Database
```

Study:

```text
FAISS
Chroma
Qdrant
Milvus
```

Learn:

* Similarity search
* Cosine similarity
* Chunking
* Metadata
* Retrieval

---

# 📚 Phase 30 — RAG

⭐⭐⭐⭐⭐

**Retrieval Augmented Generation**

Architecture:

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
Relevant Context
 ↓
LLM
 ↓
Answer
```

---

## RAG Projects

### Project 12

**PDF Question Answering System**

---

### Project 13

**University Knowledge Assistant**

---

### Project 14

**Research Paper Assistant**

---

# 🎨 Phase 31 — Generative AI

Learn the major generative model families.

```text
Autoencoders
      ↓
VAEs
      ↓
GANs
      ↓
Diffusion Models
```

---

## GAN

Understand:

```text
Generator
     ↕
Discriminator
```

---

## Diffusion

Understand:

```text
Image
 ↓
Add Noise
 ↓
Noise
 ↓
Denoising
 ↓
Generated Image
```

---

# 🌐 Phase 32 — Multimodal AI

Now combine different types of data:

```text
Text
+
Image
+
Audio
+
Video
```

Study:

* Vision-Language Models
* Multimodal LLMs
* Image Captioning
* Visual Question Answering
* Speech + Language

---

## Project 15

### Multimodal AI Assistant

```text
Image
 ↓
Vision Model
 ↓
LLM
 ↓
Answer
```

Allow the user to upload an image and ask questions about it.

---

# 🧪 Phase 33 — Advanced Deep Learning

Now study advanced training techniques.

---

## Regularization

Learn:

```text
L1 Regularization
L2 Regularization
Dropout
Weight Decay
```

---

## Normalization

Learn:

```text
Batch Normalization
Layer Normalization
RMSNorm
```

---

## Training Techniques

Learn:

```text
Learning Rate Scheduling
Warmup
Early Stopping
Gradient Clipping
Mixed Precision
Gradient Accumulation
```

---

# ⚡ Phase 34 — Model Optimization

Learn how to make models smaller and faster.

```text
Quantization
Pruning
Knowledge Distillation
Model Compression
```

---

## Numerical Formats

Understand:

```text
FP32
FP16
BF16
INT8
INT4
```

---

# 🖥️ Phase 35 — GPU & Performance

Understand:

```text
CPU
GPU
CUDA
VRAM
Batch Size
GPU Memory
```

Learn how to deal with:

```text
CUDA Out Of Memory
```

Understand techniques such as:

* Smaller batch size
* Mixed precision
* Gradient accumulation
* Smaller models
* Gradient checkpointing

---

# 🚀 Phase 36 — Model Deployment

A model isn't truly useful if you cannot deploy it.

Learn:

```text
Model
 ↓
API
 ↓
Docker
 ↓
Cloud
```

---

## Tools

Learn:

```text
FastAPI
Docker
Git
GitHub
MLflow
Weights & Biases
```

---

## Cloud

Get familiar with at least one cloud platform:

```text
AWS
GCP
Azure
```

Also understand practical deployment platforms such as:

```text
Hugging Face
Render
```

---

# ⚙️ Phase 37 — MLOps

Learn:

* Experiment tracking
* Model versioning
* Data versioning
* Model deployment
* Model monitoring
* Logging
* CI/CD
* Reproducibility

---

## Monitoring

Understand:

```text
Latency
Memory
GPU Usage
Accuracy
Data Drift
Model Drift
```

---

# 🏭 Phase 38 — Production AI

Understand how real AI systems are built.

```text
User
 ↓
Frontend
 ↓
API
 ↓
Model
 ↓
Database / Vector DB
 ↓
Response
```

Learn:

* REST APIs
* Authentication
* Model serving
* Docker
* Cloud deployment
* Logging
* Monitoring
* Scaling
* Caching
* Rate limiting

---

# 🏆 Complete Project Roadmap

Build projects in this order.

| #  | Project                     | Main Skill              |
| -- | --------------------------- | ----------------------- |
| 1  | Neural Network From Scratch | DL Fundamentals         |
| 2  | MNIST Classifier            | PyTorch                 |
| 3  | Fashion-MNIST               | Classification          |
| 4  | Tabular Predictor           | Dense Networks          |
| 5  | Cats vs Dogs                | CNN                     |
| 6  | Plant Disease Detection     | Transfer Learning       |
| 7  | Fracture Detection          | Medical Computer Vision |
| 8  | Vehicle Detection           | Object Detection        |
| 9  | Helmet Detection            | YOLO                    |
| 10 | Road Segmentation           | U-Net                   |
| 11 | Real-Time Object Detection  | CV + Deployment         |
| 12 | PDF Q&A                     | RAG                     |
| 13 | Research Assistant          | Embeddings + RAG        |
| 14 | Fine-Tuned LLM              | LoRA / QLoRA            |
| 15 | Multimodal AI               | Vision + LLM            |
| 16 | Generative AI               | Diffusion               |
| 17 | Production AI System        | MLOps                   |

---

# 🧭 Recommended Learning Order

Follow this order instead of randomly jumping between topics:

```text
01. Python
       ↓
02. NumPy
       ↓
03. Machine Learning Fundamentals
       ↓
04. Linear Algebra
       ↓
05. Calculus + Gradients
       ↓
06. Neural Networks
       ↓
07. Activation Functions
       ↓
08. Loss Functions
       ↓
09. Forward Propagation
       ↓
10. Backpropagation
       ↓
11. Optimization
       ↓
12. Neural Network From Scratch
       ↓
13. PyTorch
       ↓
14. CNN
       ↓
15. Transfer Learning
       ↓
16. Computer Vision
       ↓
17. Object Detection
       ↓
18. Segmentation
       ↓
19. RNN / LSTM / GRU
       ↓
20. NLP
       ↓
21. Attention
       ↓
22. Transformers
       ↓
23. LLMs
       ↓
24. Fine-Tuning
       ↓
25. Embeddings
       ↓
26. Vector Databases
       ↓
27. RAG
       ↓
28. Generative AI
       ↓
29. Multimodal AI
       ↓
30. Model Optimization
       ↓
31. Deployment
       ↓
32. MLOps
       ↓
33. Production AI
```

---

# 🔥 How You Should Study Each Topic

Don't use this approach:

```text
Watch 20 hours of tutorial
        ↓
Take notes
        ↓
Move to next topic
```

Instead:

```text
Learn Concept
     ↓
Implement It
     ↓
Build Small Project
     ↓
Experiment
     ↓
Break the Model
     ↓
Debug
     ↓
Understand Why
     ↓
Build Real Project
     ↓
Move Forward
```

---

# 🧪 Example Learning Cycle

For CNN:

```text
Learn Convolution
       ↓
Implement ConvNet
       ↓
Train on CIFAR-10
       ↓
Analyze Results
       ↓
Learn ResNet
       ↓
Use Pretrained ResNet
       ↓
Fine-Tune
       ↓
Build Real-World Project
```

For Transformers:

```text
Learn Attention
       ↓
Implement Self-Attention
       ↓
Understand Transformer
       ↓
Study BERT/GPT
       ↓
Use Hugging Face
       ↓
Fine-Tune Model
       ↓
Build LLM Application
```

---

# 🎯 Final Goal

By the end of this roadmap, you should understand this complete AI stack:

```text
                         AI / DEEP LEARNING
                                  │
              ┌───────────────────┼───────────────────┐
              ↓                   ↓                   ↓
       Computer Vision       NLP / LLM          Generative AI
              │                   │                   │
        CNN / YOLO              RNN              GAN / VAE
        Segmentation        Transformers          Diffusion
        ViT                 LLMs                  Image Gen
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ↓
                         PyTorch / GPU / CUDA
                                  ↓
                      Training & Optimization
                                  ↓
                       Embeddings / Vector DB
                                  ↓
                                RAG
                                  ↓
                         Multimodal AI
                                  ↓
                         Model Optimization
                                  ↓
                       FastAPI / Docker
                                  ↓
                         Cloud Deployment
                                  ↓
                              MLOps
                                  ↓
                        Production AI Systems
```

---

# 🏁 What You Should Be Able to Do

After completing this roadmap, you should be able to:

* Build neural networks from scratch
* Understand backpropagation
* Train models with PyTorch
* Build CNNs
* Perform image classification
* Use transfer learning
* Build object detection systems
* Build segmentation models
* Understand Transformers
* Work with LLMs
* Fine-tune models using LoRA/QLoRA
* Generate and use embeddings
* Build vector-search systems
* Build RAG applications
* Work with multimodal models
* Understand Generative AI
* Optimize models
* Deploy AI models
* Build production-ready AI applications

---

# ⭐ Most Important Rule

**Don't try to master everything before building projects.**

Use:

```text
                 30% THEORY
                     +
                 70% PRACTICE
```

And for every major topic:

```text
Concept
   ↓
Code
   ↓
Experiment
   ↓
Mini Project
   ↓
Real Project
```

Your **Fracture Detection project** can serve as your first serious Computer Vision project. After strengthening that, progress to **Object Detection → Segmentation → Transformers → LLMs → RAG → Multimodal AI → Production AI**.

---

# 🚀 End Goal

```text
BEGINNER
   ↓
Deep Learning Fundamentals
   ↓
PyTorch Developer
   ↓
Computer Vision Engineer
   ↓
Transformer / NLP Developer
   ↓
LLM Engineer
   ↓
Generative AI Engineer
   ↓
Multimodal AI Engineer
   ↓
AI / Deep Learning Engineer
   ↓
Production AI Engineer
```

> **The objective is not to memorize every architecture.**
>
> The objective is to understand **why models work, how to train them, how to improve them, and how to turn them into useful real-world systems.**

---

## 📌 Suggested Repository Structure

You can also maintain your learning journey like this:

```text
deep-learning-roadmap/
│
├── 01-python/
│
├── 02-numpy/
│
├── 03-machine-learning/
│
├── 04-mathematics/
│
├── 05-neural-networks/
│
├── 06-backpropagation/
│
├── 07-optimization/
│
├── 08-neural-network-from-scratch/
│
├── 09-pytorch/
│
├── 10-cnn/
│
├── 11-transfer-learning/
│
├── 12-computer-vision/
│
├── 13-object-detection/
│
├── 14-segmentation/
│
├── 15-rnn-lstm-gru/
│
├── 16-nlp/
│
├── 17-attention/
│
├── 18-transformers/
│
├── 19-llms/
│
├── 20-fine-tuning/
│
├── 21-embeddings/
│
├── 22-vector-databases/
│
├── 23-rag/
│
├── 24-generative-ai/
│
├── 25-multimodal-ai/
│
├── 26-model-optimization/
│
├── 27-deployment/
│
├── 28-mlops/
│
└── 29-production-ai/
```

# 📅 Progress Tracker

Use this checklist to track your progress:

```text
[ ] Python
[ ] NumPy
[ ] Machine Learning
[ ] Linear Algebra
[ ] Calculus
[ ] Probability & Statistics
[ ] Neural Networks
[ ] Activation Functions
[ ] Loss Functions
[ ] Forward Propagation
[ ] Backpropagation
[ ] Gradient Descent
[ ] Optimizers
[ ] Neural Network From Scratch
[ ] PyTorch
[ ] MNIST
[ ] CNN
[ ] Transfer Learning
[ ] Computer Vision
[ ] Object Detection
[ ] YOLO
[ ] Segmentation
[ ] RNN
[ ] LSTM
[ ] GRU
[ ] NLP
[ ] Attention
[ ] Transformers
[ ] BERT
[ ] GPT
[ ] LLMs
[ ] LoRA
[ ] QLoRA
[ ] Embeddings
[ ] Vector Databases
[ ] RAG
[ ] GANs
[ ] VAEs
[ ] Diffusion Models
[ ] Multimodal AI
[ ] Quantization
[ ] Model Optimization
[ ] FastAPI
[ ] Docker
[ ] Cloud Deployment
[ ] MLOps
[ ] Production AI
```

---

## 🏆 Final Philosophy

```text
Learn → Implement → Build → Debug → Understand → Repeat
```

**Don't chase every new AI model.**

Build strong fundamentals first, then learn the modern architectures on top of those fundamentals.
