import numpy as np

def p1():
    array = np.random.randint(0, 100, size=20)

    mean_value = np.mean(array)
    min_value = np.min(array)
    max_value = np.max(array)
    min_index = np.argmin(array)

    # print("array", array)
    print("mean:", mean_value)
    print("min:", min_value)
    print("max:", max_value)
    print("index of min:", min_index)

def p2():
    array1 = np.arange(2, 15, 2)

    array2 = np.array([7, 11, 17, 18, 23, 30, 45])

    combined_array = (array1 + array2[:len(array1)]) ** 2

    condition = (array2 > 12) & (array2 % 5 == 3)
    elements_by_condition = array1[condition[:len(array1)]]

    mod_elements1 = array1 % 2
    mod_elements2 = array2 % 3

    print("array1:", array1)
    print("array2:", array2)
    print("combined_array:", combined_array)
    print("elements_by_condition:", elements_by_condition)
    print("mod_elements1:", mod_elements1)
    print("mod_elements2:", mod_elements2)

def p3():
    b = np.random.rand(3, 1)
    C = np.random.rand(3, 3)

    # Решение системы Cx = b
    try:
        x = np.linalg.solve(C, b)
        print("Solvation of equation Cx = b: ", x)
    except np.linalg.LinAlgError as e:
        print("Exception while solving equation:", e)

    # Случай, когда будет брошено исключение LinAlgError
    C_exc = np.array([[1, 2, 3], [1, 2, 3], [4, 5, 6]])
    b_exc = np.random.rand(3, 1)

    try:
        x_exc = np.linalg.solve(C_exc, b_exc)
        print("Solvation of equation Cx = b: ", x_exc)
    except np.linalg.LinAlgError as e:
        print("Exception while solving equation:", e)

p1()
p2()
p3()