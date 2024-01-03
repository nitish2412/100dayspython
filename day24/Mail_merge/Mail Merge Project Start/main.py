def send_letter(lines, change_name):
    letter_name = "letter_for_"+change_name+".txt"
    file_name = "./Output/ReadyToSend/"+letter_name
    fp_letters = open(file_name, "w")
    for line in lines:
        fp_letters.write(line)
    fp_letters.close()


def create_letter(change_name):
    fp_letters = open("./Input/Letters/starting_letter.txt")
    lines = fp_letters.readlines()
    tmp = lines[0].split(' ')
    tmp[1] = change_name
    header = " ".join(tmp)
    lines[0] = header
    send_letter(lines, change_name.strip())


fp_name = open("./Input/Names/invited_names.txt", "r")
names = fp_name.readlines()
fp_name.close()
print(names)
for name in names:
    print(name.strip())
    create_letter(name)

