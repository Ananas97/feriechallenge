import re
from selenium import webdriver


def reverse_string(name):
    return name[::-1]


def is_palindrome(string):
    return re.match(string, reverse_string(string))


def remove_none_alphabetical_chars(string):
    return re.sub("[^a-z]+", "", string)


if __name__ == '__main__':
    _input = remove_none_alphabetical_chars(input("Please name a string: ").lower())

    print("{0} written backwords is: {1}".format(_input, reverse_string(_input)))
    if is_palindrome(_input):
        print("{0} is a palindrome".format(_input))
    else:
        print("{0} is not a palindrome".format(_input))

    _to_open = input("Want to see a list of anagrams derived from the given string? Type Y or N ")
    if _to_open == "N":
        print("The end of program!")
    else:
        print("HERE I AM")
        URL = "https://anagramy.wybornie.com/" + _input
        print(URL)
        browser = webdriver.Chrome(r"C:\webdrivers\chromedriver.exe")
        page = browser.get(URL)
