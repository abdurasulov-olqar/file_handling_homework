def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
     l = []
    for i in data.split('\n'):
        l.append(len(i))
    return max(l)
# Read data from file