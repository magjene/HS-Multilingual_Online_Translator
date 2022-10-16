"""
Project: Multilingual Online Translator
Stage 7/7: Unexpected


Description
Your program works as expected! However, there’s a problem you should always keep in mind: the user can always input something that will break your program.

Up to this stage, we considered "perfect" inputs. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? Let's find some way to avoid this.

All these situations are called exceptions because you didn’t expect them to happen, and now your program will have to handle them.

Objectives
Add the following functionality:

If the user inputs a name of a language that isn't available in the program, print the line Sorry, the program doesn't support <language> and quit the program.
If the connection with the website isn't successful, print the line Something wrong with your internet connection
If the user inputs a word that's not present in ReversoContext, print the line Sorry, unable to find <word>
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

> python translator.py english korean hello
Sorry, the program doesn't support korean
Example 2

> python translator.py english all hello
Something wrong with your internet connection
Example 3

> python translator.py english all brrrrrrrrrrr
Sorry, unable to find brrrrrrrrrrr
"""


import requests
from bs4 import BeautifulSoup
import sys


def net(ad0, ad1, w, j=5):
    global out_words, out_texts
    address = rf'https://context.reverso.net/translation/' + ad0 + '-' \
              + ad1 + '/' + w
    out_words, out_texts = [], []
    r = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
    if r:
        soup = BeautifulSoup(r.content, 'html.parser')

        display_term = soup.find_all('span', {'class': 'display-term'})
        for trans in display_term:
            out_words.append(trans.text)

        display_texts = soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})
        for t in display_texts:
            out_texts.append(t.text.strip())

        with open(f'{w}.txt', 'a', encoding='utf-8') as file:
            print(f'{ad1.title()} Translations:', file=file)
            print(*[w for i, w in enumerate(out_words[:-1]) if i < j and i < len(out_words) // 2],
                  sep='\n', file=file)

            print('', file=file)

            print(f'{ad1.title()} Examples:', file=file)
            print(*[out_texts[i * 2] + '\n' + out_texts[i * 2 + 1] + '\n' for i in range(j) if i < len(out_texts) // 2],
                  sep='\n', file=file)
    else:
        # print(r.status_code, 'Fail')
        print('Something wrong with your internet connection')


trans_lang = ('arabic', 'german', 'english', 'spanish', 'french', 'hebrew',
              'japanese', 'dutch', 'polish', 'portuguese', 'romanian',
              'russian', 'turkish')

address_0, address_1, word = sys.argv[1::]

open(f'{word}.txt', 'w', encoding='utf-8').close()
out_words, out_texts = [], []
if address_0 in trans_lang and address_1 in trans_lang:
    net(address_0, address_1, word)
elif address_1 == 'all' and address_0 in trans_lang:
    for val in trans_lang:
        if val != address_0:
            net(address_0, val, word, j=1)
else:
    if address_0 not in trans_lang:
        print(f"Sorry, the program doesn't support {address_0}")
    else:
        print(f"Sorry, the program doesn't support {address_1}")

print(open(f'{word}.txt', 'r', encoding='utf-8').read())
