"""
Project: Multilingual Online Translator
Stage 6/7: Faster translation


Description
Let's try to change the way the user interacts with the program to make the process faster. To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.

Objectives
At this stage, your program should:

Instead of all inputs, take command-line arguments. The first argument is the name of the source language, the second argument is the name of the target language, the third argument is the word. If the word should be translated to all languages, the second argument will be all.
The rest of the functionality should remain the same as in the previous stage.
You'll see some significant changes in the usability of the app!

Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1

You can choose the number of translations and sentence pairs for a language. There should be just at least one translation and one sentence pair.

> python translator.py english french hello
French Translations:
bonjour
allô
ohé
coucou
salut

French Examples:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.

Goodbye England and hello the Netherlands...:
Au revoir l'Angleterre et bonjour les Pays-Bas...

Yes, hello. Jackson speaking.:
Oui, allô, Jackson à l'appareil.

Hello, hello, hello, hello.:
Allô, allô, allô, allô.

And began appearing hello kitty games online.:
Et a commencé à apparaître bonjour Kitty jeux en ligne.
Example 2

> python translator.py english all hello
Arabic Translations:
مرحبا

Arabic Example:
Well, hello, old-school racist.:
حسنا، مرحبا يا تلميذة المدرسة العنصريّة - الأمر يسري بدمهم!


German Translations:
hallo

German Example:
We agreedellen wolf is innocent. hello.:
Wir waren einverstanden damit, dass Wolf unschuldig ist. Hallo.


Spanish Translations:
hola

Spanish Example:
Well, hello, Miss Anchor-liar.:
Bien, hola, señorita presentadora de mentiras.


French Translations:
bonjour

French Example:
Well, hello, freedom fighters.:
Et bien, bonjour combattants de la liberté.


Hebrew Translations:
שלום

Hebrew Example:
Is "hello" too bland?:
האם "שלום" יותר מדי מנומס?


Japanese Translations:
こんにちは

Japanese Example:
The little boy said hello to me.:
小さな男の子が私にこんにちはと言った。


Dutch Translations:
dag

Dutch Example:
That was kind of our funny hello.:
Dat vond we een grappige begroeting.


Polish Translations:
cześć

Polish Example:
I guess it's... goodbye car insurance, hello city bus.:
I domyślam się, że to jest... do widzenia ubezpieczenie samochodu, cześć autobus miejski.


Portuguese Translations:
olá

Portuguese Example:
That was my last kiss hello.:
Pois eu garanto que aquele foi o meu último beijo de olá.


Romanian Translations:
salut

Romanian Example:
Well, hello, professor Culbertson.:
Ei bine, salut, profesor universitar Culbertson.


Russian Translations:
привет

Russian Example:
Why, hello, there, Admiral.:
А, Адмирал, привет, что здесь делаешь.


Turkish Translations:
selam

Turkish Example:
So now little Sabina says hello.:
Velhasıl minik Sabina size selam söylüyor.
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
        print(r.status_code, 'Fail')


trans_lang = ('arabic', 'german', 'english', 'spanish', 'french', 'hebrew',
              'japanese', 'dutch', 'polish', 'portuguese', 'romanian',
              'russian', 'turkish')

address_0, address_1, word = sys.argv[1::]

open(f'{word}.txt', 'w', encoding='utf-8').close()
out_words, out_texts = [], []
if address_1 == 'all':
    for val in trans_lang:
        if val != address_0:
            net(address_0, val, word, j=1)
elif address_1 in trans_lang:
    net(address_0, address_1, word)
else:
    ...

print(open(f'{word}.txt', 'r', encoding='utf-8').read())
