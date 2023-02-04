def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lis = []
    for i in data:
        if i in ('0123456789'):
            lis.append(int(i))

    return min(lis)
# Read data from file