def run_len_decoding(data: list) -> list:

    """
    Decodes a list using run-length encoding.

    This function takes a list where elements are in pairs [value, count] and
    returns a decoded list where each value appears `count` times consecutively.

    Parameters:
        data (list): A list of elements encoded as [value1, count1, value2, count2, ...].

    Returns:
        list: The decoded list with values expanded according to their counts.
    """
    
    if len(data) == 0:
        return []
    
    val = data[0]
    count = data[1]

    return [val] * count + run_len_decoding(data[2:])


print(run_len_decoding(["A",12,"B",4,"A",6,"B",1]))