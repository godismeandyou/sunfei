import random

word_file = "E:\\git-code\\sunfei\\txt\\words.txt"
word_list = []

def generate_password():
    with open(word_file, 'r') as words:
        randomNum = ""
        for line in words:
            word = line.strip().lower()
            word_list.append(word)
        for i in range(3):
            randomNum += random.choice(word_list)
    return randomNum

print (generate_password())

def generate_password1():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

