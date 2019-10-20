import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translation(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word.lower(), data.keys())) > 0:
        if input("Do you mean " + get_close_matches(word.lower(), data.keys())[0] + "?Y/N :").lower() == 'y':
            return data[get_close_matches(word.lower(), data.keys())[0]]
    else:
        return "This word does not exist."


while True:
    print("Hello to English Dictionary, to learn a definition type a word, to end the program type /end")
    answer = input("Type a word: ")
    if answer == '/end':
        break
    else:
        print(translation(answer))
