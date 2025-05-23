def string_edit_distance(s: str, t: str) -> int:

    """
    Recursively computes the edit distance between two strings.

    Parameters:
    s (str): The first string.
    t (str): The second string.

    Returns:
    int: The edit distance between the two input strings.
    """

    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)

    cost = 0 if s[-1] == t[-1] else 1

    d1 = string_edit_distance(s[:-1], t) + 1
    d2 = string_edit_distance(s, t[:-1]) + 1 
    d3 = string_edit_distance(s[:-1], t[:-1]) + cost

    return min(d1, d2, d3)


def main():

    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    
    print(string_edit_distance(s, t))


if __name__ == "__main__":

    main()
