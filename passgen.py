print("Welcome to Password Generator!")
string = input("Enter in a word you would like modified into a password: ")
while len(string) < 8:
    string = input("Please provide at least 8 characters: ")

string = string.replace("a", "@")
string = string.replace("b", "8")
string = string.replace("e", "3")
string = string.replace("i", "!")
string = string.replace("l", "1")
string = string.replace("o", "0")
string = string.replace("s", "5")
string = string.replace("t", "7")

print(string)
