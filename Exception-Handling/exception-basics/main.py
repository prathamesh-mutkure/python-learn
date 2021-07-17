
try:
    file = open("a_file.txt")
    dictionary = {"key": "value"}
    print(dictionary["abc"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Exception Handling")
    print("File Created")
except KeyError as key_error:
    print(f"Key not found: {key_error}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File closed")
