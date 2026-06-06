def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # recall that f = ax^2 + bx + c
    # df/dx = 2ax + b
    x = x0
    for t in range(steps):
        x = x - lr * (2 * a * x + b)
    return x