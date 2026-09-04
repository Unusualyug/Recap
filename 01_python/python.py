"""
1. VARIABLE

-- variable is a simple name which w are used to store the value.

Example: 

name: "YUG"
age= 21
learning_d1= True

we use the variables in the deep learning to constantly store the value in the deep learning model.

2. DATA TYPES

-- A data type is a property/type information associated with a variable that tells the compiler what kind of data it can store.

-- python has different types of datatype

name= "YUG"  #str
age= 21  #int
accuracy= 0.99 #float
is_training= False #bool

-- we can check that which type of data it is by the "type function."
Example : print(type(name))  #<class 'str'>

Note ==> we use the datatype in the deep learning to understan which type of data we are using in the deep learning model.

3. CONDITIONS

-- conditions allows our progra to make decision.

Example:
age = 20
if age>= 18:
    print("Allowed")
else:
    print("Not allowed")

4. LOOPS

-- loops allows to repeat something multiple times.

(i) for loop:
for i range(5):
    print(i)

(ii) while loop:

count= 0

while count < 5:
    print(count)
    count+= 1

In deep learning repetation of operation is included

FOR EXAMPLE:

Epotch 1
Epotch 2
Epotch 3
....
Epotch 10

You will see   
for epotch in range(epochs):
    train_model()

so loops are essential in deep learning to repeat the operation multiple times.

QUESTION: 
we are using the loop means we will going to feed the data multiple times, i mean does it makes sense to train the model with the same data for the 8 to 10 times? 

ANSWER:

yes, it make sense.
we train the model with the same data multiple times because in deep learning, we want the model to learn the patterns and features of the data. By feeding the same data multiple times (through epochs), the model can adjust its weights and biases to minimize the loss function and improve its performance. Each pass through the data allows the model to refine its understanding and make better predictions.


Note ==> here weights is numerical value which used by model to decide how important each feature is when we make the prediction. The model learns these weights during training to optimize its performance.

Example:
Input → Weight → Prediction
Height → 0.8
Age    → 0.2

so, by passing each epotch, the model will figer it out that giving more importance to which factor/attribute enhances the accuracy ad reduce the error...

it means kind of by passing each epotch, deciding that which factors or th attrbutes are require to more for reduce the error and enahnce the performance

******************************************************************************************************

IN SHORT:
More precisely, in each epoch the model adjusts the weights (and biases) to determine how strongly different features should influence the prediction, with the goal of reducing the error/loss and improving performance.

👉 Simple:
Epoch → check errors → adjust weights → reduce loss → improve predictions.

******************************************************************************************************
5. FUnctions

Fuction is a reusable block of code.

Example:

def add(a,b):
    return a + b

Use it: 
result= add(2,4)
print(result) #6

WE NEED TO UNDERSTAND def, parameters, argument, return

(i) def: def is a keyword which is used to create/define a function.

(ii) parameters: the variables written inside the function parenthesis are called parameters. Parameters are used to pass the value to the function.
-- formal parameter
-- actual parameter

Example: def add(a, b):
Here, a and b are parameters.

(iii) Argument: the actiual value whch we write inside the function parenthesis while calling the function is called argument.

Example: result= add(2,4)
Here, 2 and 4 are arguments.

(iv) return: used to send the result send back from the function.

Example: 
def add(a,b):
    return a+b

    
# Easy way to remember...

def add(a, b):      # a, b = parameters
    return a + b    # return result

add(10, 20)         # 10, 20 = arguments

6. Lists

A list stores multiple values.
Like, numbers= [1, 2, 3, 4, 5]

- access an item:
print(numbers[0]) #1
Note: in python, the idex start from 0

inbuild methids of the list like,

add: numbers.append(50)
remove: numbers.remove(3)

Loops in list:

for number in list:
    print(number)

DEEP LEARNING CONNECTION:
In deep learning, we often work with datasets that contain multiple samples. Lists can be used to store and manipulate these samples. For example, we can use lists to store the features of each sample, the corresponding labels, or even the predictions made by the model. Lists allow us to easily iterate over the data, apply transformations, and perform operations on multiple samples at once.

we might have:
classes:["cat", "dog", "hourse"]

or

images=["image1.jpg", "image2.jpg", "image3.jpg"]

7. Tuples
A tuple is same as list but it is immutable, which means we cannot change the value of the tuple once it is created.

Example:
image_size= (224, 224, 3) #tuple

Access:
print(image_size[0]) #224

-- ONE IMPORTANT DIFFERENCE:

my_list= [10, 20, 30]
my_list[0] = 100 #allowed

my_tuple= (10, 20, 30)
my_tuple[0] = 100 #not allowed

For Deep Learning, you'll frequently see shapes such as:
(224, 224, 3) for images, where the first two numbers represent the height and width of the image, and the last number represents the number of color channels (e.g., RGB).

meaning:

224 → height
224 → width
3   → color channels

8. Sets

A set is a collection of unique values. It does not allow duplicate values. Additionally, we can not access the value by the index in set.

A set stores unique values.

numbers= {1, 2, 3, 3, 5}
print(numbers) # {1, 2, 3, 5} The duplicate 3 is removed.

itnis useful when we need the unique value.

classes={"cat", "dog", "cat", "horse"}
print(classes) # {'cat', 'dog', 'horse'}

9. Dictionaries

A dictionary is a collection of key-value pairs. Each key is unique and is used to access its corresponding value. This one is very important.

A dictionary stores data as: key -> value

Example: 
student={
    "name":"Yug",
    "age":21,
    "course":"Deep Learning"
}

Access: student["name"] #Yug

Change: student["age"]= 22

Add: student["grade"]= "A"
Remove: del student["course"]

-- why it is important in deep learning?
In deep learning, dictionaries are often used to store and manage various configurations, hyperparameters, and metadata related to the model and training process. 
For example, we can use dictionaries to store the learning rate, batch size, number of epochs, and other settings that control how the model is trained. 
This allows for easy access and modification of these parameters during experimentation and tuning.

config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 20
}

10. Class

class is a blueprint of creatin gthe object. It is a user-defined data type which holds its own data members and member functions, which can be accessed and used by creating an instance of that class.

it means we need to create an object(instance of class) to access the members and member functions of the class.

simple Example:

class Student:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

__init__ is a special method that automatially run when you create an oobject.

class Student:
def __init__(self, name, age):
    self.name= name
    self.age= age

when you do: 

s1= Student("Yug", 21)

python will automatically call the __init__ method and assign the values to the object s1.

__init__("Yug", 21) will be called automatically. its purpose is mainly to initialize/ set up the object's data.

# what is self?

self refers to the current object.
self.name= name

means: Store the given name inside this perticular object.

Example:
s1= Student("Yug", 21)
s2= Student("John", 25)

so you imagine:
s1 → name = Yug,   age = 20
s2 → name = Jhon, age = 25

self makes sure Python knows which object's data you're referring to.

# Why do we need them?

Without __init__, you would have to manually set the data after creating every object.

s1 = Student()
s1.name = "Yug"
s1.age = 20

With __init__:
s1 = Student("Yug", 20)

In one line:

__init__ → initializes an object when it is created.
self → refers to the current object.

EXAMPLE:

def __init__(self, name):
    self.name= name

def introduce(self):
    print(f"Hello, my name is {self.name}.")

student= Student("Yug")
student.introduce()  # Output: Hello, my name is Yug.

***************************************************************************************************************

FINAL Note ==> __init__ is a build in metod in the pytjon which is used to assign the value to the instance of the class when it is created and the "self" is used to make sure that the data is assigned to the correct instance of the class.

***************************************************************************************************************

# Inheritance:

Inheritance means one class can use/reuse the properties and method of the another class.

The existing class is called the parent class, and new class is called the child class.

class Student:
    def introduce(self):
        print("I am a student.")

class CollageStudent(Student):
    pass
    
-- Here:
Student → Parent class
CollegeStudent → Child class
CollegeStudent(Student) → means CollegeStudent inherits from Student

student= CollageStudent()
student.introduce()  # Output: I am a student.

Eve though introduce() is defined inside Student class, the CollageStudent objectcan use it.

11. Exception Handling

Sometime we program to encounter the error.
You handle certain error using the exception handling.

Example:

try:
    number= int(input("Enter number: "))
    print(number)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

The idea is:

try
 ↓
execute code
 ↓
error?
 ↓
except
 ↓
handle error

This become useful when we working with:

-- datasets
-- files
-- images
-- APIs
-- model loading
-- user input

12. File Handling
we need to know how to work with files.

-- Reading the file

with open("daata.txt", "r") as file:
    data= file.read()

print(data)

-- Writing the file

with open("data.txt", "w") as file:
    file.write("Hello deep learning")

WHY IT IS IMPORTANT:

Machine Learning projects contains many files:
dataset/
    train/
    test/
    validation/

You'll need to understand how python intersects with files and dictionary.

13. Modules and Packages

Amodule is basically a pyton file contaning reusable code.

-- for example:

import math

print(math.sqrt(81))


You can also import specific things:

from math import sqrt

print(sqrt(81))

-- Later you'll use:

import numpy as np
import pandas as pd
import torch
import matplotlib.pyplot as plt

This is extremely important because Deep Learning depends heavily on external libraries.


14. Virtual Environment

This is something we must understand before doing serious Deep Learning projects.

Suppose project A needs:
PyTorch 2.X

and project B needs another version.

Installing everything globally can cause conflicts.
A virtual environment creates an isolated pyton environment for projects.

CREATE ONE
python -m venv venv

Activate on Windows
venv\Scripts\activate

ou'll see something like: (venv) C:\project>

THEN INSTALL PACKAGES:

pip install numpy 

When you're finished: deactivate

-- Your project can look like:

deep-learning-project/
│
├── venv/
├── dataset/
├── src/
├── train.py
├── predict.py
└── requirements.txt

You generally don't upload venv/ to GitHub.

________________________________________________________________________________________________________

think of a virtual environment as a saparate, privte box for one python project.

Why do we need it?

Suppose you have two projects:

Project A → needs TensorFlow 2.15
Project B → needs TensorFlow 2.20

If you install TensorFlow globally, the projects can conflict with each other.

A virtual environment keeps them separate:

Computer
│
├── Project A
│   └── Virtual Environment
│       └── TensorFlow 2.15
│
└── Project B
    └── Virtual Environment
        └── TensorFlow 2.20

So each project gets its own Python packages and versions.

-- How do we create one?
python -m venv venv

This creates a folder called venv.

Then activate it on Windows: venv\Scripts\activate

After activation, when you do: pip install pandas

pandas is installed inside that project's environment, not globally.

The main idea

Virtual environment = isolated Python environment for a specific project, so different projects don't interfere with each other. ✅

This becomes especially important in ML/deep-learning projects, because libraries like TensorFlow, PyTorch, NumPy, etc. can require specific versions.

EXAMPLE:

You use a separate venv whenever different projects need different library versions or dependencies.

For example:

Project 1 → ML model
            TensorFlow 2.15
            NumPy 1.x

Project 2 → Another ML model
            TensorFlow 2.20
            NumPy 2.x

If both projects use the same global Python environment, the versions can conflict.

So you create:

Project 1/
└── venv/ → TensorFlow 2.15

Project 2/
└── venv/ → TensorFlow 2.20

Important point

It's not because you're training two models at the same time.

It's because the two projects/models may require different library versions or dependencies.

👉 Simple rule:
One project → usually one virtual environment → install that project's libraries inside it.


Note ==> MERN:

project/
├── node_modules/      ← installed dependencies
├── package.json
└── src/
    └── code

In Python:

project/
├── venv/              ← isolated environment + packages
├── requirements.txt
└── main.py            ← your code

The main difference is:

node_modules mainly stores project dependencies, while a Python venv also provides an isolated Python environment/interpreter.

So for your understanding, you can think:

venv ≈ Python's project-isolation equivalent of node_modules + its own Python environment.


************************************************************************************
Basically, when we want to create a separate environment for a project and install only the required packages or specific versions of those packages without affecting other projects, we create a virtual environment (`venv`). It provides an isolated environment where the project's dependencies and their versions are stored.


Question : why we need to create the saparate environment

We create a separate environment mainly to prevent dependency conflicts between projects.

For example:

Project A → needs NumPy 1.x
Project B → needs NumPy 2.x

If both use the same global environment, installing/updating NumPy for Project B might break Project A.

With separate environments:

Project A
└── venv → NumPy 1.x

Project B
└── venv → NumPy 2.x

Now they are completely independent. ✅

Simple real-life analogy

Think of two kitchens:

Kitchen A → ingredients needed for Recipe A
Kitchen B → ingredients needed for Recipe B

Changing an ingredient in Kitchen B doesn't affect Kitchen A.

👉 So, separate environment = isolation + no dependency/version conflicts between projects.

************************************************************************************
________________________________________________________________________________________________________


"""