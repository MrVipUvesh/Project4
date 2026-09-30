print("Welcome to the Data Analyzer and Transformer Program")
choice = None
Data = None

def input_data(*args):
    """This function takes multiple elements as an input from the user
       and stores them into a list(array) format by splitting them wherever
       ' '(blank space) appears."""
    global Data
    args = input("\nEnter data for a 1D array (separated by spaces):\n")
    real_data = list(args.split(" "))
    for i in range(len(real_data)):
        real_data[i] = int(real_data[i])
    Data = real_data
    print("\nData has been stored successfully!")

def data_summary():
    """This function gives statistic summary of data which includes
       total elements, minimum value, maximum value, sum of all values
       and average value."""
    print("Data Summary:")
    print(f"- Total elements: {len(Data)}")
    print(f"- Minimum value: {min(Data)}")
    print(f"- Maximum value: {max(Data)}")
    print(f"- Sum of all values: {sum(Data)}")
    print("- Average value: %.2f"% (sum(Data)/len(Data)))

def factorial(x):
    """This function is a recursive function which call itself
       to find factorial of given argument."""
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

def threshold(value):
    """This function is like a filter function which takes 1 argument
       and filter outs all the value greater than equals to it."""
    threshold_value = list(filter(lambda x: x >= value, Data))
    print(f"\nFiltered Data (values >= {value}):")
    print(threshold_value)
    
def sort_data():
    """This function gives user 2 choices to sort the data in two orders
       ascending order and descending order."""
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = int(input("\nEnter your choice: "))

    if(choice == 1):
        return sorted(Data)
        #The results of this won't be stored as we have used 'sorted' function
    elif(choice == 2):
        return sorted(Data, reverse= True)
        #The results of this won't be stored as we have used 'sorted' function

def data_statistics():
    """This function gives statistic summary of data which includes
       minimum value, maximum value, sum of all values and average value."""
    return min(Data), max(Data), sum(Data), (sum(Data)/len(Data))

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    choice = input("Please enter your choice: ")
    choice = int(choice)

    if(choice == 1):
        input_data() #Hover over function name or use .__doc__ to see its docstring
    elif(choice == 2):
        data_summary() #Hover over function name or use .__doc__ to see its docstring
    elif(choice == 3):
        n = int(input("Enter a number to calculate its factorial: "))
        fact = factorial(n) #Hover over function name or use .__doc__ to see its docstring
        print(f"Factorial of {n} is: {fact}")
    elif(choice == 4):
        value = int(input("Enter a threshold value to filter out data above this value:\n"))
        threshold(value) #Hover over function name or use .__doc__ to see its docstring
    elif(choice == 5):
        sort = sort_data() #Hover over function name or use .__doc__ to see its docstring
        print(sort)
    elif(choice == 6):
        mini, maxi, add, avg = data_statistics() #Hover over function name or use .__doc__ to see its docstring
        print("\nDataset Statistics:")
        print(f"- Minimum value: {mini}")
        print(f"- Maximum value: {maxi}")
        print(f"- Sum of all values: {add}")
        print("- Average value: %.2f"%(avg))
    elif(choice == 7):
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break
    else:
        print("Invalid option!")
        continue