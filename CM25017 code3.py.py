import random

dictionary = {
    "happy": ["Feeling good", "joyful, cheerful", "sad"],
    "brave": ["Not afraid", "bold, fearless", "afraid"],
    "beautiful": ["Very attractive", "pretty, lovely", "ugly"],
    "intelligent": ["Having good understanding", "smart, clever", "stupid"],
    "honest": ["Truthful", "sincere, fair", "dishonest"],
    "ancient": ["Very old", "old, historic", "modern"],
    "generous": ["Willing to give", "kind, giving", "selfish"],
    "confident": ["Having self-belief", "bold, assured", "insecure"],
    "curious": ["Wanting to know", "inquisitive", "uninterested"],
    "creative": ["Having new ideas", "innovative, imaginative", "uncreative"]
}

def search(word):
    word = word.lower()

    if word in dictionary:
        d = dictionary[word]
        print("\nMeaning:", d[0])
        print("Synonyms:", d[1])
        print("Antonyms:", d[2])
    else:
        print("Word not found!")

def history():
    try:
        with open("history.txt") as f:
            print("\nHistory:\n" + f.read())
    except:
        print("No history found!")

while True:
    print("\n--- ADVANCED ENGLISH DICTIONARY ---")
    print("1.Search  2.Random  3.History  4.Exit")

    choice = input("Choice: ")

    if choice == "1":
        word = input("Enter word: ")
        search(word)
        with open("history.txt", "a") as f:
            f.write(word + "\n")

    elif choice == "2":
        search(random.choice(list(dictionary)))

    elif choice == "3":
        history()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")