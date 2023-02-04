def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lis = []
    for i in data:
        if i in ('0123456789'):
            lis.append(i)

    return lis
# Read data from file