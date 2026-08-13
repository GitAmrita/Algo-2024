def solution(A, B, X, Y):
    if not A or not B:
        raise ValueError("Arrays A and B must not be empty.")
    # question mentions the arrays are both length N, so arrays of different size is incorrect input
    if len(A) != len(B):
        raise ValueError("Arrays A and B must have the same length.")
    # Initialize the first elements of the DP arrays
    t1 = A[0]
    t2 = B[0]
    for i in range(1, len(A)):
        # t1: best time till i-1 position if the i-1 task happens on line A
        # t1i: best time till i position if the i task happens on line A
        t1i = A[i] + min(t1, t2 + Y)
        # t2: best time till i-1 position if the i-1 task happens on line B
        # t2i: best time till i position if the i task happens on line B
        t2i = B[i] + min(t2, t1 + X)
        t1 = t1i 
        t2 = t2i
    return min(t1, t2)

if __name__ == "__main__":
    # Example usage
    A = [5,5] 
    B = [2,2]
    X = 2
    Y = 4
    result = solution(A, B, X, Y)
    print(f"The minimum time to complete all tasks is: {result}")