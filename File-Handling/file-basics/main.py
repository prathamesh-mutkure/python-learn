
def read_file():
    file = open("file.txt")
    file_contents = file.read()
    print(file_contents)
    print("-----------------------")
    file.close()


# with keyword closes the file
def write_file():
    with open("file.txt", "a") as file:
        file.write("\nWriting to file through Python")


read_file()
write_file()
read_file()
