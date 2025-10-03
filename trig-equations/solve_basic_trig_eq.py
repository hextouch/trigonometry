import math

def solve_basic_trig_eq():
    # Solve sin(x) = 0.5 for x in [0, 2π]
    solutions = []
    for k in range(2):
        x = math.asin(0.5) + 2*math.pi*k
        solutions.append(x)
        x = math.pi - math.asin(0.5) + 2*math.pi*k
        solutions.append(x)
    print("Solutions to sin(x) = 0.5 in [0, 2π]:")
    for sol in solutions:
        print(f"x = {sol:.2f} radians")

if __name__ == "__main__":
    solve_basic_trig_eq()
