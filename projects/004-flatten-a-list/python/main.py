def flatten_a_list(data: list) -> list:

    """
    Recursively flattens a list containing nested lists to any depth.

    Parameters:
    data (list): A potentially nested list.

    Returns:
    list: A new list containing all elements from the original list, with all levels of nesting removed.
    """

    if len(data) == 0:
        return []

    if isinstance(data[0], list):
        return flatten_a_list(data[0]) + flatten_a_list(data[1:])
    
    else:
        return [data[0]] + flatten_a_list(data[1:])
    

def main():

    print(flatten_a_list([[1], [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))


if __name__ == "__main__":

    main()