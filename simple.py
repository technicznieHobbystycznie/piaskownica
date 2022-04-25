import requests

#cel - lista linków (wszystkich !)

url = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get(url)
text = surowe_info.text

efekt = text.split('</p>')


linki = []
for i in efekt:
    link = i.replace('<p>', '')
    link = link.replace('- ','')
    link = link.strip()
    if ' ' in link or '<' in link:
        continue
    linki.append( link)

def policz_domeny_pl( linki):
    w = 0
    for s in linki:
        if len(s)>6:
            if s[-3:]==".pl" and s[-7]!='.':
                w += 1
            else:
                continue
        else:
            if s[-3:]==".pl":
                w += 1
            else:
                continue
    return w

wynik = policz_domeny_pl(linki)
print(wynik)

def pobierz_strone( weblnk):    
    surowe_info = requests.get( weblnk)
    text = surowe_info.text
    return text

def stworz_liste_flag( weblnk):
    text_strony_www = pobierz_strone( weblnk)
    lista_linii = text_strony_www.split('</p>')
    linki = []
    for linia in lista_linii:
        link = linia.replace('<p>', '')
        link = link.replace('- ', '')
        link = link.strip()
        if ' ' in link or '<' in link:
            continue
        linki.append( link)
    
    return linki

weblnk = 'https://zajecia-programowania-xd.pl/flagi'

lista_flag = stworz_liste_flag(weblnk)

weblnk = 'https://zajecia-programowania-xd.pl/flagi'

lista_flag = stworz_liste_flag(weblnk)

dotpl = policz_domeny_pl( lista_flag)