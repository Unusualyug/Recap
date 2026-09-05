"""

PHASE 1: NUMPY FOR DEEP LEARNING
Numpy= Numerical python

it is python library used to effiiently work with the numbers, arrays, matrics and mathamatical operations.

import numpy as np

insted of working with python lists: numbers= [1, 2, 3, 4]

we can use the NumPy array...
numers= np.array([1,2,3,4])

numpy becomes specially important in ML/DL becaue data is usually represented numerically.

For example:

Image
 ↓
Pixel values
 ↓
Numbers
 ↓
NumPy array
 ↓
Neural network

2. Arrays

An array is a collection of vales arranged in one or more dimentions.

Creating an array:
import numpy as np
a= np.array([12, 34, 56, 78])

This is 1-dimentional array

[10, 20, 30, 40]

You can also create a 2D array:
import numpy as np

a = np.array([
    [10, 20, 30],
    [44, 67, 43]
])

print(a)

Visually:

[[10 20 30]
 [44 67 43]]

IT IS ESSENTIAL FOR MATRIX.

WHY THIS IS IMPORTANT FOR DEEP LEARNING
suppose we have 3 stdent and their marks in 3 subjects:

        Math  DBMS  Python
Student1 80    70     90
Student2 60    85     75
Student3 90    95     88

This can be represented as:

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [90, 95, 88]
])

A neural network works with this kind of numerical structure constantly.

3. np.zeros()
create an array filled with 0.

np.zeros(5) #[0. 0. 0. 0. 0.]

You can create matrics:
np.zeros((2, 3))

0  0  0
0  0  0

The (2, 3) means:

2 rows
3 columns

4. np.ones()
Same idea, but fills the array with 1.

np.ones(5)
[1. 1. 1. 1. 1.]

Or:

np.ones((2, 3))
1  1  1
1  1  1

These are useful when we need to initialize data or create starting values.

5. np.random
Used to generate random numbers.

For example: np.random.rand(3)
might produce: [0.31 0.72 0.14]

Every time you run it, the numbers can be different.

Random values are particularly important in deep learning because neural-network weights are commonly initialized using random values.

6. Array properties
Once you have an array:

a= np.array([
    [1,2,3],
    [4,5,6]
])
you can sk several questions about the shape.

(i) shape
a.shape

Output: (2, 3)

Meaning: 2 rows x 3 columns

(ii) ndim
a.ndim

Output: 2
Meaning the array has 2 dimensions.

(iii) size
a.size

Output: 6
There are 6 total elements.

(iv) dtype
a.dtype: Tells you the data type of the elements.

For example: int64 or float64

So:

shape → structure
ndim  → number of dimensions
size  → total elements
dtype → type of elements

7. Array Operations

NumPy allows mathematical operations directly on arrays.

(i) Addition
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b

Result: [5, 7, 9]

It performs:

1 + 4 = 5
2 + 5 = 7
3 + 6 = 9

(ii) Subtraction
a - b
[-3, -3, -3]

(iii) Multiplication
a * b

Important: this is element-wise multiplication.

1 x 4 = 4
2 x 5 = 10
3 x 6 = 18

Result:

[4, 10, 18]

(iv) Division
a / b

Again, element by element.

8. Broadcasting 
This is really important for ML/DL.

Broadcasting allows Numpy to perform operations between array with compatible shapes.

a = np.array([1, 2, 3])
a + 10

NumPy effectively does:

[1, 2, 3]
+
[10,10,10]
-----------
[11,12,13]

You didn't have to manually create [10,10,10].
That's broadcasting.

9. Indexing
Indexing means accessing a perticular elements.

a= np.array([10, 20, 30, 40])
a[0] #10

Remember Python uses zero-based indexing:
Index:   0   1   2   3
Value:  10  20  30  40

For 2D array:
a= np.array([
    [1,2,3],
    [4,5,6]
])

a[0, 1] #2
Meaning: ) row and 1 column

10. SLicing
Slicing means taking a portion of an array.

a= np.array([10, 20, 30, 40, 50])
a[1:4]

Result: [20, 30, 40]

The general idea is: [start: stop]
where stop index is not included

11. Linear Algebra
This is where NumPy become extremely important for nural networks.

Suppose:
A= np.array([
    [1, 2],
    [3, 4]
])

B= np.array([
    [5, 6],
    [7, 8]
])

You can Perform matrix multiplication using
A @ B

This is different from A * B

* → element-wise multiplication
@ → matrix multiplication

This type of operation is fundamental to neural networks.

12. Dot Products

The dot product combines corresponding elements and adds them.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.dot(a, b)

Conceptually: (1x4) + (2x5) + (3x6)
= 4 + 10 + 18
= 32

This is extremely important because neural networks essentially perform operations involving inputs x weights + bias.

For example:

Inputs       Weights
  x1    x       w1
  x2    x       w2
  x3    x       w3
          ↓
       Sum them
          ↓
        + bias
          ↓
       Output

13. Transpose
Transpose changes rows into  column and column into rows.

Suppose:

A =
1  2  3
4  5  6

Transpose: A.T

1  4
2  5
3  6

In NumPy: A.T
This is frequently used in matrix calculations.

14. Scalar → Vector → Matrix → Tensor
This is one of the most important concepts to understand before deep learning.

(i) Scalar
A single number: 5

One value.

(ii) Vector
A collection of numbers in one dimension: [1, 2, 3]

You can think of it as: 3 values

(iii) Matrix

A 2D arrangement:
1  2  3
4  5  6

It has: 2 rows x 3 columns

(iv)Tensor
A generalization of arrays to multiple dimensions.

For example, imagine 3 images, each with height 28 and width 28:

3 x 28 x 28
That's a 3D array/tensor.
For colored images, you might have:

3 x 28 x 28 x 3
where the last 3 can represent:
Red
Green
Blue

In deep learning frameworks such as PyTorch and TensorFlow, tensors are the fundamental data structure.

Note ==> Linear algebra deals with vectors, matrices, linear equations, transformations, dot products, etc.
_________________________________________________________________________________________________

Real-life uses of Scalar, Vector, Matrix and Tensor

1. Scalar → One value
A scalar is simply one number.

Examples:
25°C
₹500
75 kg
0.95 accuracy
In Deep Learning

A scalar can represent:

Loss = 0.35
Learning rate = 0.001

So:
Scalar = one numerical value.

2. Vector → Collection of values

Example: [180, 75, 20]

Could represent:

    Height = 180 cm
    Weight = 75 kg
    Age = 20
Real-life uses

Vectors are used to represent:

A person's features
GPS coordinates
Product characteristics
Student marks
ML input features

For example, a house could be represented as: [1500, 3, 2, 5000000]

where:

    1500 → area
    3    → bedrooms
    2    → bathrooms
    5000000 → price
In Deep Learning

A single input example can be represented as a vector: [feature1, feature2, feature3, ...]
Vector = multiple numerical values representing something.

3. Matrix → Table of values

Example:

80  70  90
60  85  75
90  95  88

This could represent 3 students x 3 subjects.

             Subjects
          Math DBMS Python
Student 1   80   70    90
Student 2   60   85    75
Student 3   90   95    88
Real-life uses

Matrices are everywhere:

Excel-like datasets
Image pixels
Financial data
Scientific calculations
Recommendation systems
Machine-learning datasets

For example, a grayscale image can be represented as a matrix:

0    120   255
30   200   180
90   50    220

Each number represents a pixel intensity.

In Deep Learning: Neural networks perform lots of matrix operations, especially:

Input Matrix x Weight Matrix
Matrix = organized numerical data in rows and columns.

4. Tensor → Multi-dimensional numerical data
A tensor is basically a generalized multi-dimensional array.
Imagine you have 100 grayscale images, each of size 28 x 28.

You could have:

100 x 28 x 28

That's a 3D tensor.
For color images: 100 x 28 x 28 x 3

where:

100 → number of images
28  → height
28  → width
3   → RGB channels
Real-life Deep Learning examples

Tensors are used for:

Images: Batch x Height x Width x Channels

Videos: Batch x Frames x Height x Width x Channels

Text: Batch x Sequence Length x Features

So when you're working with CNNs, computer vision, NLP, etc., you'll encounter tensors constantly.

Easy way to remember
| Type       | Example           | Real-life representation   |
| ---------- | ----------------- | -------------------------- |
| **Scalar** | `5`               | Temperature, loss, price   |
| **Vector** | `[10, 20, 30]`    | Features of one person     |
| **Matrix** | `[[1,2],[3,4]]`   | Dataset / image            |
| **Tensor** | `3 x 28 x 28 x 3` | Collection of color images |

_________________________________________________________________________________________________

"""