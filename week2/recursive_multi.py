def mult(a, b):
    """ 
    Input: 2 intergers: a and b
    Output: The result of multiplying a and b
    """
    if (b == 1):
        return a
    else:
        return a + mult(a, b-1)
