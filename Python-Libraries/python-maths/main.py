import math


def print_data(a, b):
    print(a + " : " + str(b))
    print("-----------------")


print_data("ceil", math.ceil(10.4))
print_data("floor", math.floor(10.4))
print_data("gcd", math.gcd(16, 36))
print_data("log", math.log(2, 10))
print_data("rad to deg", math.degrees(22/7))
print_data("deg to rad", math.radians(180))
print_data("----CONSTANTS----", "\b\b")
print_data("PI", math.pi)
print_data("E", math.e)
print_data("NAN", math.nan)
print_data("INF", math.inf)




