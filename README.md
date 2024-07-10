# DateDetectionATBS
Practice project that uses regular expression to detect dates in the DD/MM/YYYY format.

This project is a practice project from chapter 7 of Automate the Boring Stuff by Al Sweigart. 

Date Detection
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the
months range from to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll
have a leading zero.
The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent 
dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write 
additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 
28 days, and the rest of the months have 31 days. February has 29 days in leap years.
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also 
evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression
that can detect a valid date.