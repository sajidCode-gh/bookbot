path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents  = f.read()
        printReport(file_contents)


def wordCount(file_contents):
    words = file_contents.split()
    return len(words)

def countLetters(file_contents):
    lettersCount = {}
    for letter in file_contents:
        letterLowerCase = letter.lower()
        if letterLowerCase in lettersCount:
            lettersCount[letterLowerCase] += 1
        else:
            lettersCount[letterLowerCase] = 1

    letterCountList = []
    for letter in lettersCount:
        letterCountList.append({"name": letter, "num": lettersCount[letter]})
    
    return letterCountList

def sort_on(dict):
    return dict["num"]

def printReport(file_contents):
    lettersList = countLetters(file_contents)
    lettersList.sort(reverse=True, key=sort_on)

    words = wordCount(file_contents)

    print(f"--- Begin report of {path_to_file} ---", "\n")
    print(f"{words} words found in the document")
    for k in lettersList:
        if k["name"] != " ":
            print(f"The {k["name"]} characters was found {k["num"]} times")
    print("--- End report ---")




main()