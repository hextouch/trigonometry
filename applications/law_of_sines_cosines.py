import math

def law_of_sines(a, A, B):
    # a/sinA = b/sinB => b = a*sinB/sinA
    A_rad = math.radians(A)
    B_rad = math.radians(B)
    b = a * math.sin(B_rad) / math.sin(A_rad)
    print(f"Given a={a}, A={A}°, B={B}°: b={b:.2f}")

def law_of_cosines(a, b, C):
    # c² = a² + b² - 2ab cosC
    C_rad = math.radians(C)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))
    print(f"Given a={a}, b={b}, C={C}°: c={c:.2f}")

def main():
    law_of_sines(5, 30, 45)
    law_of_cosines(3, 4, 90)

if __name__ == "__main__":
    main()
