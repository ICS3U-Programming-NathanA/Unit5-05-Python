#!/usr/bin/env python3

# Created by: Nathan Araujo
# Date: Dec 6, 2022
# This program formats the users address


def address_format(
    full_name, street_num, street_name, city, province, postal_code, user_apartment=None
):
    # If the user entered "y" for apartment
    if user_apartment != None:
        address = (
            full_name
            + "\n"
            + user_apartment
            + "-"
            + street_num
            + " "
            + street_name
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )
    # Otherwise set the address without the apartment number
    else:
        address = (
            full_name
            + "\n"
            + street_num
            + " "
            + street_name
            + "\n"
            + city
            + " "
            + province
            + " "
            + postal_code
        )
    return address


def main():
    # Gets user_full_name from the user
    user_full_name = input("Enter your full name: ")
    # Sets user_full_name to all uppercase
    user_full_name = user_full_name.upper()
    # Sees if the user lives in an apartment
    user_apartment_question = input("Do you live inside of an apartment(y or n): ")
    # If statement to determine if they do live in an apartment
    if user_apartment_question.upper() == "Y":
        # Asks the user for their apartment number
        user_apartment = input("Enter your apartment number: ")

    # Gets user_street_num from the user
    user_street_num = input("Enter your street number: ")

    # Gets user_street_name from the user
    user_street_name = input("Enter your street name and type of: ")
    # Sets user_street_name to all uppercase
    user_street_name = user_street_name.upper()
    # Gets user_city from the user
    user_city = input("Enter your city: ")
    # Sets user_city to all uppercase
    user_city = user_city.upper()
    # Gets user_province from the user
    user_province = input("Enter your province (As an abbreviation): ")
    # Sets user_province to all uppercase
    user_province = user_province.upper()
    # Gets user_postal_code from the user
    user_postal_code = input("Enter your postal code: ")

    # call address_format
    address = address_format(
        user_full_name,
        user_street_num,
        user_street_name,
        user_city,
        user_province,
        user_postal_code,
        user_apartment,
    )

    # prints the address
    print("Your Canadian Mailing address is:\n")
    print(f"{address}")


if __name__ == "__main__":
    main()
