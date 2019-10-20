import json


data = json.load(open("data.json"))


def translation(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        return "This word does not exist." \


print(translation(  input("Type a word: ")))

