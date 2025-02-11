# Program to demonstrate list, tuple, looping over a sequence, and countdown using while loop in Python
def main():
    # List demonstration
    my_list = [1, 2, 3, 4, 5]
    print("List:", my_list)
    print("First element of list:", my_list[0])
    my_list.append(6)
    print("List after appending 6:", my_list)
    my_list.remove(3)
    print("List after removing 3:", my_list)
    
    # Looping over a list
    print("Looping over list:")
    for item in my_list:
        print(item, end=" ")
    print()
    
    # Tuple demonstration
    my_tuple = (10, 20, 30, 40, 50)
    print("Tuple:", my_tuple)
    print("First element of tuple:", my_tuple[0])
    print("Tuple slicing (first three elements):", my_tuple[:3])
    
    # Looping over a tuple
    print("Looping over tuple:")
    for item in my_tuple:
        print(item, end=" ")
    print()
    
    # Countdown using while loop
    num = int(input("Enter a number for countdown: "))
    while num >= 0:
        print(num, end=" ")
        num -= 1
    print()

if __name__ == "__main__":
    main()
