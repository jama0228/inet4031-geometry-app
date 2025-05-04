import math

# Function to calculate the volume of a sphere
# Formula: Volume = (4/3) * π * r^3
def volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# Function to prompt user for input and display the volume
def prompt():
    print()
    print("-----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME OF A SPHERE")
    print("-----------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))

    print("\nThe Volume of the Sphere = ", volume(radius))

# Call the prompt function only if this file is run directly
if __name__ == "__main__":
    prompt()
