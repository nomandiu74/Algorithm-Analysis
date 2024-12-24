def bisection_method(f, a, b, tol):
    # Check if the initial interval is valid
    if f(a) * f(b) >= 0:
        print("Bisection method fails: f(a) and f(b) must have opposite signs.")
        return None

    # Perform the Bisection Method
    while (b - a) / 2 > tol:
        
        c = (a + b) / 2
        
        
        if f(c) == 0:
            return c
        
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    # Return the approximate root
    return (a + b) / 2

def example_function(x):
    return x**3 - 4*x - 9
a = 2
b = 3
tolerance = 1e-5

root = bisection_method(example_function, a, b, tolerance)

if root is not None:
    print(f"The approximate root is: {root:.5f}")
