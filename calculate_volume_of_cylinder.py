#!/usr/bin/env python3

# Created by: Donggeun Lim
# Created on: Jan 2019
# This program calculates volume of sylinder.


import math


def caculate_volume(radius, height):
    # calculate volume of sylinder

    # process
    volume = math.pi * (radius**2) * height

    return volume


def main():
    # input
    radius = input("Enter the radius of sylinder (integer): ")
    height = input("Enter the height of triangle (integer): ")

    # call functions
    try:
        integer_as_radius = int(radius)
        integer_as_height = int(height)
        if integer_as_radius > 0 and integer_as_height > 0:
            volume = caculate_volume(height=integer_as_height,
                                     radius=integer_as_radius)
            print("The volume of cylinder is {} m³".format(volume))
        else:
            print("Theses number are minus")
    except Exception:
        print("It is not an integer")


if __name__ == "__main__":
    main()
