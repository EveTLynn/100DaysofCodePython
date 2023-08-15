PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as name_file:
    names = name_file.readlines() # return the names in list

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip("\n")
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)

# https://stackoverflow.com/questions/1347791/unicode-error-unicodeescape-codec-cant-decode-bytes-cannot-open-text-file
