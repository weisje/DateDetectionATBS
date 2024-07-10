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

def dateValidator(): # TODO: Function to check provided string & determine if it is a valid date for a Gregorian calendar
    pass


def main():
    finderResult = dateFinder("31/01/2899")
    if not finderResult:
        sys.exit("No possible dates found")
    else:
        print(finderResult)


if __name__ == '__main__':
    main()
