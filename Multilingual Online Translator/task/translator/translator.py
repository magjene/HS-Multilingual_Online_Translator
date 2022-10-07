"""
Project: Multilingual Online Translator
Stage 3/7: Translations


Description
To get readable results, you need to clean and format all the data you get from the web. It's a good thing that Python is a rich programming language with powerful text formatting out of the box!

To make the results extracted from the web page easily readable, let's separate sentences and translations by newlines and put titles in front of different sections of the output.

Objectives
At this stage, format the output of results in the following fashion:

Output the line ... Translations:; put the full name of the target language instead of ... (for example, English Translations).
Output found translations, one per line. Make sure there are no commas or quotes, just the word (or the phrase). If there are more than 5 translations, leave only 5 of them to keep the results more compact. Or you can print all of them, it does not affect the testing.
Output the line ... Examples; put the full name of the target language instead of ... .
Output found examples of sentences, one sentence per line. Make sure there are no commas or quotes (apart from those that should be inside the sentence). First, output the sentence in the source language, then output its translation in the target language. Repeat this procedure for every found sentence pair. If there are more than 5 sentence pairs, you can leave only 5 of them for convenience. Or you can print all of them, it does not affect the testing.
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:
> fr
Type the word you want to translate:
> hello
You chose "fr" as a language to translate "hello".
200 OK

French Translations:
bonjour
allô
ohé
coucou
salut

French Examples:
Well, hello, freedom fighters.
Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...
Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.
Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.
Allô, allô, allô, allô.

And began appearing hello kitty games online.
Et a commencé à apparaître bonjour Kitty jeux en ligne.
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
    print(out_texts)
else:
    print(r.status_code, 'Fail')
