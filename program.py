#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This program calculates the area of a rectangle
# where the user gets to enter the length and width in mm

import math


def main():
    # main function
    print("We will be calculating the area of a rectangle. ")
    # input
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))
    # process
    area = length * width
    # output
    print("Area is {} mm²".format(area))


if __name__ == "__main__":
    main()
