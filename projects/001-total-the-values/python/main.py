def total_the_values(values: list, count: int=0) -> float:

    """
    Recursively sums all integer or floating-point values in a list.

    Args:
        values (list): A list containing int or float numbers.
        count (int): The current index in the list, used internally during recursion.

    Returns:
        float: The total sum of all numeric values in the list.

    Raises:
        TypeError: If 'values' is not a list or contains non-numeric elements.
    """
    
    if not isinstance(values, list):
        raise TypeError("Expected a list, got a different type.")

    if count == len(values):
        return 0.0
    
    if not isinstance(values[count], (int, float)):
        raise TypeError("All elements must be numeric.")
    
    return values[count] + total_the_values(values, count + 1)


def main():
    
    values = []

    n = None
    while n != "":
        n = input("Please enter a number or a blank line to stop: ")
        if n.isdigit():
            value = float(n)
            values.append(value)
        elif not n.isdigit() and n != "":
            print("Expected a number or a blank line.")

    print(f"{total_the_values(values):.2f}")


if __name__ == "__main__":
    main()