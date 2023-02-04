def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lis = []
    for i in data:
        if i in ('0123456789'):
            lis.append(i)

    return [len(lis), len(data)-len(lis)]
# Read data from file
