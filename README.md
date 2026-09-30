# Data Analyzer and Transformer Program 📊

A simple menu-driven Python program for analyzing and transforming a 1D dataset.

This project is made to practice some important Python concepts like **functions, recursion, lambda functions, filtering, sorting, built-in functions, docstrings, and returning multiple values**.

## 📌 Features

The program provides a simple main menu with these options:

- Input a 1D array of numbers
- Display a complete data summary
- Calculate factorial using recursion
- Filter data using a threshold value
- Sort data in ascending or descending order
- Display dataset statistics using multiple return values
- Exit the program

## 🛠️ Concepts Used

This project demonstrates:

- Variables
- Lists
- User input
- Type conversion using `int()`
- Functions
- Function arguments
- Global variables
- Docstrings
- Built-in functions
- `len()`
- `min()`
- `max()`
- `sum()`
- `sorted()`
- `filter()`
- Lambda functions
- Recursion
- `while` loops
- `if-elif-else`
- Multiple return values
- Tuple unpacking
- F-strings

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

    python Project4.py

## 💻 Complete Example

Here is an example of how the program can be used:

    Welcome to the Data Analyzer and Transformer Program

    Main Menu:
    1. Input Data
    2. Display Data Summary (Built-in Functions)
    3. Calculate Factorial (Recursion)
    4. Filter Data by Threshold (Lambda Function)
    5. Sort Data
    6. Display Dataset Statistics (Return Multiple Values)
    7. Exit Program

    Please enter your choice: 1

    Enter data for a 1D array (separated by spaces):
    10 25 5 40 15 30

    Data has been stored successfully!

### 1. Display Data Summary

    Main Menu:
    1. Input Data
    2. Display Data Summary (Built-in Functions)
    3. Calculate Factorial (Recursion)
    4. Filter Data by Threshold (Lambda Function)
    5. Sort Data
    6. Display Dataset Statistics (Return Multiple Values)
    7. Exit Program

    Please enter your choice: 2

    Data Summary:
    - Total elements: 6
    - Minimum value: 5
    - Maximum value: 40
    - Sum of all values: 125
    - Average value: 20.83

### 2. Calculate Factorial

    Please enter your choice: 3

    Enter a number to calculate its factorial: 5
    Factorial of 5 is: 120

The factorial is calculated using a recursive function:

    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x - 1)

### 3. Filter Data by Threshold

    Please enter your choice: 4

    Enter a threshold value to filter out data above this value:
    20

    Filtered Data (values >= 20):
    [25, 40, 30]

The filtering is performed using `filter()` and a lambda function:

    threshold_value = list(filter(lambda x: x >= value, Data))

### 4. Sort Data

The program provides two sorting options.

#### Ascending Order

    Please enter your choice: 5

    Choose sorting option:
    1. Ascending
    2. Descending

    Enter your choice: 1

    [5, 10, 15, 25, 30, 40]

#### Descending Order

    Please enter your choice: 5

    Choose sorting option:
    1. Ascending
    2. Descending

    Enter your choice: 2

    [40, 30, 25, 15, 10, 5]

### 5. Display Dataset Statistics

    Please enter your choice: 6

    Dataset Statistics:
    - Minimum value: 5
    - Maximum value: 40
    - Sum: 125
    - Average value: 20.83

The function returns multiple values:

    def data_statistics():
        return min(Data), max(Data), sum(Data), (sum(Data) / len(Data))

These values are then unpacked into separate variables:

    mini, maxi, add, avg = data_statistics()

### 6. Exit the Program

    Please enter your choice: 7

    Thank you for using the Data Analyzer and Transformer Program. Goodbye!

## 📂 Project Structure

    Data-Analyzer-and-Transformer/
    │
    ├── Project4.py
    └── README.md

## 🧠 Function Overview

### `input_data()`

Takes space-separated numbers from the user, converts them into integers, and stores them in the `Data` list.

### `data_summary()`

Displays the total number of elements, minimum value, maximum value, sum, and average using Python's built-in functions.

### `factorial(x)`

Calculates the factorial of a number using recursion.

### `threshold(value)`

Filters the dataset and displays values greater than or equal to the given threshold using `filter()` and a lambda function.

### `sort_data()`

Allows the user to sort the dataset in ascending or descending order using `sorted()`.

### `data_statistics()`

Returns the minimum value, maximum value, sum, and average of the current dataset.

## ⚠️ Note

The program expects the dataset to contain valid integer values separated by spaces.

For example:

    10 25 5 40 15 30

Also, options that work with `Data` should be used after entering the dataset through **Input Data**.

## 🎯 Purpose

This project is mainly for learning and practicing Python fundamentals by putting multiple concepts together in one interactive program.

It is a small project, but it covers several useful concepts that can later be used in larger Python programs.

---

Made by Uvesh Ansari
