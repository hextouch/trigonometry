import math

def right_triangle_solver(a=None, b=None, c=None, A=None, B=None):
    # a, b, c: sides; A, B: angles in degrees
    if a and b:
        c = math.hypot(a, b)
        A = math.degrees(math.asin(a/c))
        B = math.degrees(math.asin(b/c))
        print(f"Given legs a={a}, b={b}: hypotenuse c={c:.2f}, angles A={A:.2f}°, B={B:.2f}°")
    else:
        print("Provide at least two sides.")

def main():
    right_triangle_solver(a=3, b=4)

if __name__ == "__main__":
    main()
