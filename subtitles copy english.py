import os
from selenium import webdriver
import time
import random


def login_chrome():
    link = input('Enter video link ... ')
    link = link[8:]

    browser = webdriver.Chrome('D:\chromedriver.exe')    # link for your folder with "chromedriver"
    browser.implicitly_wait(4)
    browser.get(f'https://downsub.com/?url=https%3A%2F%2F{link}')
    time.sleep(random.randrange(4, 6))

    browser.find_element(value='//*[@id="app"]/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div['
                               '1]/button[2]').click()
    time.sleep(random.randrange(5, 8))


login_chrome()


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    b, c = int(input('Enter the limits of the number of words in the text. Minimum ...')), int(
        input('Enter the limits of the number of words in the text. Maximum ...'))
    folder = os.listdir("C:/Users/kryna/Downloads")
    lastname = folder[-1]
    filename = f'C:/Users/kryna/Downloads/{lastname}'
    print(filename)

    if not os.path.exists(filename):
        print("The specified file does not exist")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        q = 0
        for word in words_dict:
            x, y = (word.ljust(20), words_dict[word])
            if int(y) in range(b, c):
                print(x, y)
                q = q + 1
            else:
                continue
        print("Number of words in the text: %d" % len(words))
        print("Number of words selected:", q)


if __name__ == "__main__":
    main()
pass
