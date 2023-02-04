def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    s = 0
    for i in data:
        if i in ('0123456789'):
            s += int(i)

    return s
# Read data from file