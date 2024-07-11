import re
import sys


def dateFinder(possibleDateStr) -> tuple:
    """
    Uses regex to find potential calendary dates in provided string in format DD/MM/YYYY format.  Leading zero must be
    used as well for single digit entries and years between 1000 and 2999.
    :param possibleDateStr: Value that may contain a date
    :type possibleDateStr: raw string
    :return: tuple
    """
    dateFormat = re.compile(r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/([1|2]\d{3})")
    date = dateFormat.search(possibleDateStr)
    if date:
        return date.groups()


def dateValidator(dateToValidate) -> None:
    """
    Tests provided value to see if it is a valid date by the Gregorian calendar
    :param dateToValidate: Value to see if it is actually a valid date
    :type dateToValidate: tuple
    :return: None
    """
    day = dateToValidate[0]
    month = dateToValidate[1]
    year = dateToValidate[2]
    if month == "04" or month == "06" or month == "09" or month == "11":
        if int(day) > 30:
            sys.exit(f"Invalid date! {month} only has 30 days in it!")

    elif month == "02":
        if int(year) % 4 == 0:
            if int(year) % 100 == 0:
                if int(year) % 400 == 0:
                    if int(day) > 29:
                        sys.exit(f"Invalid date! {month} only has 29 days in it on goofy leap years!")
                else:
                    if int(day) > 28:
                        sys.exit(f"Invalid date! {month} only has 28 days in it on leap years divisible by 100!")
        else:
            if int(day) > 28:
                sys.exit(f"Invalid date! {month} only has 28 days in it on non-leap years!")

    else:
        if int(day) > 31:
            sys.exit(f"{month} only has 31 days in it!")

    print(f"{day}/{month}/{year} is a valid date")


def main(dateToTest) -> None:
    """
    Main function for finding & testing viability of dates in provided string
    :param dateToTest: value to be tested for a potential date
    :type dateToTest: str
    :return: None
    """
    if dateToTest == "":
        sys.exit("Please enter data to test for a date")
    finderResult = dateFinder(dateToTest)
    if not finderResult:
        sys.exit("No possible dates found")
    else:
        print(finderResult)
        dateValidator(finderResult)


if __name__ == '__main__':
    stringToTest = input("String to test\n>")
    main(stringToTest)
