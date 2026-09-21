dictionary = {
    "happy": {
        "meaning": "Feeling good or pleased",
        "synonyms": "joyful, cheerful",
        "antonyms": "sad, unhappy",
        "example": "She is happy today."
    },
    "brave": {
        "meaning": "Not afraid of danger",
        "synonyms": "bold, fearless",
        "antonyms": "cowardly, afraid",
        "example": "He is a brave boy."
    },
    "beautiful": {
        "meaning": "Very attractive",
        "synonyms": "pretty, lovely",
        "antonyms": "ugly",
        "example": "The flower is beautiful."
    }
}

def search(word):
    data = dictionary.get(word.lower())

    if data:
        for key, value in data.items():
            print(f"{key.title()}: {value}")
    else:
        print("Word not found!")

word = input("Enter a word: ")
search(word)