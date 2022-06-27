with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    letter_file.close()

with open("./Input/Names/invited_names.txt") as names_file:
    names_list = names_file.readlines()
    names_file.close()

for names in names_list:
    new_letter = letter.replace("[name]", names.strip())
    """when is no file, python creates one for you (remember write mode)"""
    with open(f"./Output/ReadyToSend/{names.strip()}.txt", mode="w") as file:
        file.write(new_letter)
