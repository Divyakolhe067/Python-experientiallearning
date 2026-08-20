# English Dictionary

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

word = input("Enter a word: ").lower()

if word in dictionary:
    print("\nMeaning:", dictionary[word]["meaning"])
    print("Synonyms:", dictionary[word]["synonyms"])
    print("Antonyms:", dictionary[word]["antonyms"])
    print("Example:", dictionary[word]["example"])
else:
    print("Word not found.")