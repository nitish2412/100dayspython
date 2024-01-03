file = open("my_file.txt", "r")
contents = file.read()
print(contents)
file.close()

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:
    file.write("\nwelcome to python world.")

