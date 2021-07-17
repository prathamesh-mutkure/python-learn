# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names_path = "./Input/Names/invited_names.txt"
starting_letter_path = "./Input/Letters/starting_letter.txt"
output_path = "./Output/ReadyToSend"


def get_names():
    with open(invited_names_path) as file:
        names_string = file.read()
        name_list = names_string.split("\n")

        return name_list


def read_starting_letter():
    with open(starting_letter_path) as file:
        starting_letter = file.read()

        return starting_letter.strip()


def write_output_file(file_name, text):
    with open(f"{output_path}/{file_name}.txt", "w") as file:
        file.write(text)


names = get_names()
starting_letter_text = read_starting_letter()

for name in names:
    letter_text = starting_letter_text.replace("[name]", name, 1)
    write_output_file(f"letter_for_{name}", letter_text)
