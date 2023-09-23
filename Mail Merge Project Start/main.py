#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
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

