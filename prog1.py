# Demonstrating basic data types in Python

def main():
    # Integer
    int_var = 42
    print("Integer:", int_var, type(int_var))

    # Float
    float_var = 3.14
    print("Float:", float_var, type(float_var))

    # String
    string_var = "Python Programming"
    print("String:", string_var, type(string_var))

    # Boolean
    bool_var = False
    print("Boolean:", bool_var, type(bool_var))

    # List (mutable sequence)
    list_var = [10, 20, 30, 40, 50]
    print("List:", list_var, type(list_var))

    # Tuple (immutable sequence)
    tuple_var = (100, 200, 300, 400, 500)
    print("Tuple:", tuple_var, type(tuple_var))

    # Set (unordered collection with unique elements)
    set_var = {1, 2, 3, 4, 5, 6}
    print("Set:", set_var, type(set_var))

    # Dictionary (key-value pairs)
    dict_var = {"language": "Python", "version": 3.9}
    print("Dictionary:", dict_var, type(dict_var))

if __name__ == "__main__":
    main()