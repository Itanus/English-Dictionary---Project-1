import json
import difflib
from difflib import get_close_matches


data = json.load(open("data.json"))


def translation(word):
    if word.lower() in data:
        return data[word.lower()]
    elif get_close_matches(word.lower(), data.keys())[0] in data:
        return data[get_close_matches(word.lower(), data.keys())[0]]
    else:
        return "This word does not exist." 


print(translation(input("Type a word: ")))

