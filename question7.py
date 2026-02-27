# Question 7 — Find the longest word starting with "un"

import requests


def download_book(url):
    """
    Downloads a book from a URL and saves it
    :param url: the url for the book
    :return: None
    """
    response = requests.get(url)
    print(response.status_code)
    with open("book.txt", "w", encoding="utf-8") as f:
        f.write(response.text)


def longest_un_word(filename):
    """
    Finds the longest word that starts with "un" in a text file
    :param filename: the text file to search
    :return: the longest word starting with "un"
    """
    longest = ""
    special_chars = ",.?!;:'\"\n()"

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.lower()
            line = line.replace("—", " ")  # em-dash becomes space
            line = line.replace("-", " ")   # hyphen becomes space
            for c in special_chars:
                line = line.replace(c, "")
            words = line.split()
            for word in words:
                if word[:2] == "un" and len(word) > len(longest):
                    longest = word

    return longest


# Download a book from Gutenberg
download_book("https://www.gutenberg.org/cache/epub/2701/pg2701.txt")

# Find the longest word starting with "un"
result = longest_un_word("book.txt")
print(f"Longest word starting with 'un': {result}")

# Answer: uninterpenetratingly (20 letters)
