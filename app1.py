import json


data = json.load(open("data.json"))


def translation(word):
    return data[word]


print(translation("rain"))