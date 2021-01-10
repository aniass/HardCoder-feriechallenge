
"""
Napisz program, który prosi użytkownika o podanie dowolnego napisu. Następnie program wyświetla na ekranie to słowo
wspak (od prawej do lewej) i wyświetla komunikat czy to wyrażenie jest palindromem (czyli czytane wspak daje do samo
wyrażenie np. “ala”, “Kobyła ma mały bok” (inne przykłady: http://www.palindromy.pl/pal_kr.php).
Podczas sprawdzania ignoruj wielkość liter oraz znaki niebędące literami.
Następnie wywołaj dowolną stronę internetową, która pokaże anagramy oraz słowa utworzone po usunięciu liter, np.
https://poocoo.pl/scrabble-slowa-z-liter/hardcoder
Propozycja rozszerzenia: samodzielnie wyszukaj anagramy i słowa utworzone po usunięciu liter z podanego słowa,
na przykład wykorzystując słownik wspomniany na stronie https://anagramy.wybornie.com/
"""

import re
import webbrowser


def palindrom(phrase):
    input_text = phrase.lower().replace(" ", "")
    input_text = re.sub('[^a-zA-Z łęóąśżźćń]+', "", input_text)
    word = input_text[::-1]
    return input_text == word


words = input('Give a word to check if it is a palindrome:\n')

if palindrom(words):
    print('Your word is a palindrome!')
else:
    print('No, your word is not a palindrome!')

print('Now look at the anagrams create from your words')
website = "https://poocoo.pl/scrabble-slowa-z-liter/" + words
webbrowser.open(website)
