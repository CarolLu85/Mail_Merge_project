
# turn the invited+names.txt into a list
names = open("./Input/Names/invited_names.txt", "r")
name_list = names.readlines()
print(name_list)


# replace the [name] in the starting letter.
with open("./Input/Letters/starting_letter.txt") as start:
    start_letter = start.read()
    for name in name_list:
        # below line is to get rid of the "\n" in the list after every name.
        name = name.strip("\n")
        new = start_letter.replace("[name]", name)
        print(new)
        file_name = f"letter_for_{name}.txt"
        with open(f'./Output/ReadyToSend/{file_name}', "w") as new_letter:
            new_letter.write(new)

