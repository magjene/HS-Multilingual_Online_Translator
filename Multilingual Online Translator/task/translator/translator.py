"""
Project: Multilingual Online Translator
Stage 4/7: All of them


Description
Great job! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will finally make our translator a multilingual one!

The maximum number of languages our translator can support is 13. They are:

Arabic
German
English
Spanish
French
Hebrew
Japanese
Dutch
Polish
Portuguese
Romanian
Russian
Turkish
They should be enumerated in the program. A great idea is to present them with relevant numbers so that the user can choose the first as the original language and the second as a translation.

Objectives
At this stage, your program should:

Output the welcoming message (let's update it a bit): Hello, welcome to the translator. Translator supports:
Output an enumerated list of languages. The enumeration should start from 1. The order of languages should be exactly as in the list above.
Take input (a number from the list) specifying the source language (the language from which the translation should be performed).
Take input (a number from the list) specifying the target language (the language to which the translation should be performed).
Take input specifying the word that should be translated.
Output the results as in the previous stage. At this stage, you don't need to print 200 OK anymore.
Tip 1: just place the listed languages into the URL depending on the user’s choice!

Tip 2: Try to convert the input to lower case: it may cause an error if the user's input is in upper case or mixed.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Hello, welcome to the translator. Translator supports:
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language:
> 3
Type the number of language you want to translate to:
> 4
Type the word you want to translate:
> hello

Spanish Translations:
hola
buenos días
qué tal
saludo
buen día

Spanish Examples:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.

He didn't introduce us, so hello.:
No nos presentó, así que hola.

Well, hello, Prince Charming.:
Vaya, hola, Príncipe Azul.

In addition, fast delivery. hello Laura.:
Además, la entrega rápida. hola Laura.

L: Well, hello, my dear secretary.:
A: Bien, hola, mi querida secretaria.
"""


import requests
from bs4 import BeautifulSoup


translate = input('Type "en" if you want to translate from French into English, '
                  'or "fr" if you want to translate from English into French:\n')
word = input('Type the word you want to translate:\n')
print(f'You chose "{translate}" as the language to translate "{word}".')

address = rf'https://context.reverso.net/translation/'
if translate == 'fr':
    address += r'english-french/' + f'{word}'
elif translate == 'en':
    address += r'french-english/' + f'{word}'

out_words, out_texts = [], []
r = requests.get(address, headers={'User-Agent': 'Mozilla/5.0'})
if r:
    print(r.status_code, 'OK\n')

    soup = BeautifulSoup(r.content, 'html.parser')
    display_term = soup.find_all('span', {'class': 'display-term'})
    for trans in display_term:
        out_words.append(trans.text)

    display_texts = soup.find('section', {'id': 'examples-content'}).find_all('span', {'class': 'text'})
    for t in display_texts:
        out_texts.append(t.text.strip())

    name = 'French' if translate == 'fr' else 'English'
    print(f'{name} Translations:')
    print(*[w for i, w in enumerate(out_words[:-1]) if i < 5], sep='\n')

    print()

    print(f'{name} Examples:')
    print(*[out_texts[i * 2] + '\n' + out_texts[i * 2 + 1] + '\n' for i in range(5) if i < len(out_texts) // 2], sep='\n')
else:
    print(r.status_code, 'Fail')
