import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

while True:
    text = input("Enter a word: ").strip().upper()
    try:
        nato_letters = [nato_dict[char] for char in text]
    except KeyError:
        print("Sorry, please enter letters only")
    else:
        print(nato_letters)
        break
