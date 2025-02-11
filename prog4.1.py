# Program to demonstrate list and tuple in Python
def main():
    # List demonstration
    my_list = [1, 2, 3, 4, 5]
    print("List:", my_list)
    print("First element of list:", my_list[0])
    my_list.append(6)
    print("List after appending 6:", my_list)
    my_list.remove(3)
    print("List after removing 3:", my_list)
    
    # Tuple demonstration
    my_tuple = (10, 20, 30, 40, 50)
    print("Tuple:", my_tuple)
    print("First element of tuple:", my_tuple[0])
    print("Tuple slicing (first three elements):", my_tuple[:3])

if __name__ == "__main__":
    main()
