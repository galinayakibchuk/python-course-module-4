"""
Refactor given program code:
* Put reusable code into the functions:
o First - to calculate days in year
o Second – to decide which planet year is bigger
* Put orbital_radius and orbital_speed together in same data structure
Optional: add try/except handlers to avoid entering incorrect planet
"""
def days_in_year(year):
    if year % 4 ==0 and year %100 !=0 or year %400 ==0:
        return 366
    else:
        return 365

try:
    year = int(input('Please, enter the year value:'))
    days_in_given_year = days_in_year(year)
    print('Days in {year} year - {days}'.format(year=year, days=days_in_given_year))

except ValueError:
    print('Incorrect value passed!')

import math

solar_orbital_radius = {
    "Mercury": 58, "Venus": 108,
    "Earth": 150, "Mars": 228,
    "Jupiter": 778, "Saturn": 1429,
    "Uranus": 2871, "Neptune": 4504
}  # millions of kilometres

solar_orbital_speed = {
    "Mercury": 47.87, "Venus": 35.02,
    "Earth": 29.78, "Mars": 24.13,
    "Jupiter": 13.07, "Saturn": 9.69,
    "Uranus": 6.81, "Neptune": 5.43
}  # kilometres per second


def orbital_radius(radius):
    return radius * 1000000


def planet_year(planet):
    radius = orbital_radius(solar_orbital_radius[planet])
    speed = solar_orbital_speed[planet]
    year_in_seconds = 2 * math.pi * radius / speed
    year_in_days = year_in_seconds / (60 * 60 * 24)
    return int(round(year_in_days, 0))


first = input('Please, enter first planet name:')
second = input('Please, enter second planet name:')

is_first_bigger = 'greater' if planet_year(first) > planet_year(second) else 'less'
print('{f_first} planet year is {comparison} than {f_second}'
      .format(f_first=first, f_second=second, comparison=is_first_bigger))


# planet_orbital_radius = orbital_radius[planet] * 1000000
# planet_year = (2 * math.pi * orbital_radius_1 / orbital_speed_1)
#               /(60 * 60 * 24)