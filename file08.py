def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lis = []
    for i in data:
        if i in ('0123456789'):
            lis.append(int(i))

    return max(lis)
# Read data from file