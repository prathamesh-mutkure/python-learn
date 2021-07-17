
def print_data(tag, value):
    print(tag + " : " + str(value))


def print_line():
    print("------------------------"*3)


dict1 = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
}

print_line()
print_data("dict1", dict1)

from_keys = dict.fromkeys(["John", "Jane", "Bruno", "Swiggy", "Doggy"], 80)
print_data("from keys", from_keys)

print_line()
print_data("items", dict1.items())
print_data("keys", dict1.keys())
print_data("values", dict1.values())

print_line()
print_data("get", from_keys.get("Joe"))

from_keys.pop("John")
print_data("pop", from_keys)

from_keys.popitem()
print_data("pop item", from_keys)

dict1.setdefault("e", "E")
print_data("set default", dict1)

