def deg_to_rad(degrees):
    from math import pi
    return degrees * pi / 180

def rad_to_deg(radians):
    from math import pi
    return radians * 180 / pi

def main():
    deg = 180
    rad = deg_to_rad(deg)
    print(f"{deg} degrees = {rad} radians")
    print(f"{rad} radians = {rad_to_deg(rad)} degrees")

if __name__ == "__main__":
    main()
