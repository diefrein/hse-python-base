import numpy as np
import time
import matplotlib.pyplot as plt

def matrix_multiply(A, B):
    n = len(A)
    C = [[0] * len(B[0]) for _ in range(n)]
    
    for i in range(n):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

sizes = []
numpy_times = []
list_times = []

for n in range(2, 101):
    A = np.random.randint(1, 51, size=(n, n))
    B = np.random.randint(1, 51, size=(n, n))

    start_time = time.time()
    C_numpy = np.dot(A, B)
    numpy_time = time.time() - start_time
    
    A_list = A.tolist()
    B_list = B.tolist()

    start_time = time.time()
    C_list = matrix_multiply(A_list, B_list)
    list_time = time.time() - start_time

    if not np.array_equal(C_numpy, C_list):
        print(f"Result mismatch for n={n}")

    sizes.append(n)
    numpy_times.append(numpy_time)
    list_times.append(list_time)

    print(f"Matrix size: {n}x{n}, NumPy calculation time: {numpy_time:.12f} sec, Pyhton lists calculation time: {list_time:.12f} sec")