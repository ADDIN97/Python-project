import json
from difflib import get_close_matches

def separate(lista):
    if type(lista) == list:
        for item in lista:
            print(item)
    else:
        return lista

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Miałeś na myśli, któreś z powyższych wyrażeń?")
        print(separate(get_close_matches(word, data.keys())[:3]))
        yes_or_no = input("Wybierz tak lub nie: ")
        if yes_or_no == 'tak':
            choose = input("Wybierz, który wyraz miałeś na myśli wpisując 1,2,3....: ")
            if choose == '1':
                return translate(get_close_matches(word, data.keys())[0])
            elif choose == '2':
                return translate(get_close_matches(word, data.keys())[1])
            elif choose == '3':
                return translate(get_close_matches(word, data.keys())[2])
            else:
                return 'Brak wyboru'
        else:
            return "Brak słowa w bazie danych, spróbuj jeszcze raz"
    else:
        return "Brak słowa w bazie danych, spróbuj jeszcze raz"

print("Witaj w słowniku języka angielskiego! \nMiłej zabawy :)")
data = json.load(open("C:\\Users\\Paweł\\Desktop\\data.json",'r+'))
word_in = input("Podaj słowo: ")
word = word_in.lower()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)