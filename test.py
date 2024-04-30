
def matrix_sum(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices cannot be multiplied. Inner dimensions must match.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            result[i][j] += matrix1[i][i] + matrix2[i][j]

    return result

if __name__ == "__main__":
    import norch
    a = norch.Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    b = norch.Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    import time
    import random
    import numpy as np

    
    #a = Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])#.to("cuda")
    #b = Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])#.to("cuda")
    #c = Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])#.to("cuda")

    #d = b-c
    print(a ** 2)
    #print(a ** 2)
    
    """#print(a)
    N = 1000
    a = Tensor([[random.uniform(0, 1) for _ in range(N)] for _ in range(N)])
    b = Tensor([[random.uniform(0, 1) for _ in range(N)] for _ in range(N)])
    #b = Tensor([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    #a = Tensor([[[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]]])
    #b = Tensor([[[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]]])
    ini = time.time()
    c = a + b

    print("\n#####2######")
    
    fim = time.time()

    print(fim-ini)

    print("\n\n")

    
    a = [[random.uniform(0, 1) for _ in range(N)] for _ in range(N)]
    b = [[random.uniform(0, 1) for _ in range(N)] for _ in range(N)]
    ini = time.time()
    result_matrix = matrix_sum(a, b)
    fim = time.time()
    print(fim-ini)


    print("\n\n")

    ini = time.time()
    a = np.random.rand(N, N)
    b = np.random.rand(N, N)
    result_matrix = a + b
    fim = time.time()
    print(fim-ini)

"""