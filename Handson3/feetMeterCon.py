def toMeters(x):
    feet = x * 0.3048
    return round(feet, 2)

def toFeet(x):
    meters = x / 0.3048
    return round(meters, 2)

# the main() function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    for unit in range(1, 3, 10):
        print(unit, "Feet =", toMeters(unit), "Meters")
    for unit in range(1, 3, 10):
        print(unit, "Meter(s) =", toFeet(unit), "Feet")
# if this module is the main module, call the main() function
# to test the other functions
if __name__ == "__main__":
    main()
