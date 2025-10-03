import math

def evaluate_trig_functions(angle_deg):
    angle_rad = math.radians(angle_deg)
    print(f"sin({angle_deg}) = {math.sin(angle_rad):.3f}")
    print(f"cos({angle_deg}) = {math.cos(angle_rad):.3f}")
    print(f"tan({angle_deg}) = {math.tan(angle_rad):.3f}")
    print(f"csc({angle_deg}) = {1/math.sin(angle_rad):.3f}")
    print(f"sec({angle_deg}) = {1/math.cos(angle_rad):.3f}")
    print(f"cot({angle_deg}) = {1/math.tan(angle_rad):.3f}")

def main():
    angle = 30
    evaluate_trig_functions(angle)

if __name__ == "__main__":
    main()
