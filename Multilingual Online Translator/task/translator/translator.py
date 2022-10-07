"""
Project: Multilingual Online Translator
Stage 5/7: Simultaneous translation


Description
Perfect! Your program already became a convenient tool. There are just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better: add the feature of translating the word to all the languages at once, and also save the search results to a text file so that the user could read the translations later.

Objectives
Add the following functionality to your program:

Before taking an input specifying the target language, output the message Type the number of a language you want to translate to or '0' to translate to all languages:
If the user inputs 0 as the target language, translate the word to all available languages.
Output results to the terminal, as in the previous stage. At this stage, it's enough to print just one translation and one sentence pair per target language.
Save results of the search to a file named word.txt, where word is the word that was being translated.
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
Type the number of a language you want to translate to or '0' to translate to all languages:
> 0
Type the word you want to translate:
> hello
This will result in the following output and a file called hello.txt with the same content:

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


def net(ad0, ad1, w):
    address = rf'https://context.reverso.net/translation/' + trans_lang[ad0].lower() + '-' \
              + trans_lang[ad1].lower() + '/' + w
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

        print(f'{trans_lang[ad1].title()} Translations:')
        print(*[w for i, w in enumerate(out_words[:-1]) if i < 5], sep='\n')

        print()

        print(f'{trans_lang[ad1].title()} Examples:')
        print(*[out_texts[i * 2] + '\n' + out_texts[i * 2 + 1] + '\n' for i in range(5) if i < len(out_texts) // 2],
              sep='\n')
    else:
        print(r.status_code, 'Fail')


trans_lang = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French', '6': 'Hebrew',
              '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese', '11': 'Romanian',
              '12': 'Russian', '13': 'Turkish'}

print('Hello, welcome to the translator. Translator supports:')
print(*[key + '. ' + val for key, val in trans_lang.items()], sep='\n')
print('Type the number of your language: ')
address_0 = input()

print("Type the number of a language you want to translate to or '0' to translate to all languages:")
address_1 = input()

print('Type the word you want to translate:')
word = input().lower()

print()

if address_1 in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
    net(address_0, address_1, word)
elif address_1 == '0':
    ...
else:
    ...
