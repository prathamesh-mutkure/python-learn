
def print_data(tag, value):
    print(tag + " : " + str(value))


def print_line():
    print("---------------------"*3)


string1 = "hello python!"

print_line()
print_data("string1", string1)

print_line()
print_data("capitalize", string1.capitalize())
print_data("title", string1.title())
print_data("upper", string1.upper())
print_data("lower", string1.lower())

print_line()
print_data("center", string1.center(50, " "))
print_data("encode", string1.encode())
print_data("endswith !", string1.endswith("!"))
print_data("endswith !", list(enumerate(string1)))

print_line()
List = ["h", "e", "l", "l", "o", "!"]
joined = "".join(List)
print_data("joined", joined)

string1 = str(List)
print_data("from list", string1)
