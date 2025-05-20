def decimal_to_binary(n: int) -> str: 

    """
    Converts a non-negative integer to its binary representation as a string using recursion.

    Args:
        n (int): A non-negative integer to be converted.

    Returns:
        str: The binary representation of the input integer.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is a negative number.
    """

    if not isinstance(n, int):
        raise TypeError("Expected an integer, got a different value.")
    
    if n < 0:
        raise ValueError("The number must be a positive number.")
    
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    
    return decimal_to_binary(n // 2) + str(n % 2)


def main():

    print(decimal_to_binary(150))
    print(decimal_to_binary(16))
    print(decimal_to_binary(1))
    print(decimal_to_binary(25))


if __name__ == "__main__":
    main()