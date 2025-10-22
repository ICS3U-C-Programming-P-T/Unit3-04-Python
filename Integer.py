#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/16/2025
# This program ask user for a integer saying if its positive negative or zero


def main():
    # Ask the user for an integer
    user_input = int(input("Give me a Number: "))

    # Checks if number is positive
    if user_input > 0:
        print("This number is positive.")

    # Checks if number is negative
    elif user_input < 0:
        print("This number is negative.")

    # Checks if number is zero
    elif user_input == 0:
        print("The is a zero.")

    # If its not a number
    else:
        print("No idea.")


if __name__ == "__main__":
    main()
