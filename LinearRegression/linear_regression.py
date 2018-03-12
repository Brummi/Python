import numpy as np


def calculate_A_b(sample_pts):
    A = np.array([[0, 0], [0, 0]])
    b = np.array([0, 0])
    for pt in sample_pts:
        x = pt[0]
        y = pt[1]

        A[0][0] += x**2
        A[0][1] += x
        A[1][0] = A[0][1]
        A[1][1] += 1

        b[0] += 2*x*y
        b[1] += 2*y
    A = A * 2
    return A, b


def steepest_descent_step(x_prev, A, b):
    r = b - np.dot(A, x_prev)
    if all([x==0 for x in r]):
        return x_prev
    alpha = np.dot(r.T, r) / (np.dot(r.T, np.dot(A, r)))
    print("x_prev: ", x_prev)
    print("residual: ", r)
    print("alpha: ", alpha)
    return x_prev + alpha * r


def steepest_descent(x_start, sample_pts, steps):
    x = x_start
    A, b = calculate_A_b(sample_pts)
    for i in range(steps):
        x = steepest_descent_step(x, A, b)
    return x