
mapa_graf = {'Warszawa': [['Lodz', 136], ['Radom', 105], ['Pulawy', 140]],
             'Lodz': [['Warszawa', 136], ['Kielce', 147], ['Czestochowa', 127]],
             'Radom': [['Warszawa', 105], ['Kielce', 82]],
             'Pulawy': [['Warszawa', 140], ['Kielce', 150], ['Sandomierz', 106]],
             'Czestochowa': [['Lodz', 127], ['Katowice', 74], ['Krakow', 124]],
             'Kielce': [['Radom', 82], ['Lodz', 147], ['Krakow', 118], ['Pulawy', 150]],
             'Sandomierz': [['Pulawy', 106], ['Krakow', 120], ['Tarnow', 105]],
             'Katowice': [['Czestochowa', 74], ['Zakopane', 106]],
             'Krakow': [['Kielce', 118], ['Czestochowa', 124], ['Sandomierz', 120], ['Zakopane', 111]],
             'Tarnow': [['Sandomierz', 105], ['Zakopane', 158]]
             }
heurystyka = {'Warszawa': 280, 'Lodz': 220, 'Radom': 225, 'Pulawy': 240, 'Czestochowa': 150, 'Kielce': 180, 'Sandomierz': 130, 'Katowice': 75, 'Krakow': 60, 'Tarnow': 70, 'Zakopane': 0}
odleglosc = {'Warszawa': 0}
def AGwiazdka():
    global mapa_graf, heurystyka
    lista_zamknieta = []
    lista_otwarta = [['Warszawa', 280]]
    while True:
        funkcja = [i[1] for i in lista_otwarta]
        #print('funkcja fn:'+ str(funkcja) + str(lista_otwarta))
        najmniejszy_indeks = funkcja.index(min(funkcja))
        #print('najmniejszy indeks: ' + str(funkcja.index(min(funkcja))))
        wezel = lista_otwarta[najmniejszy_indeks][0]
        #print('Obecny wezel: ' +str(wezel))
        # print('')
        lista_zamknieta.append(lista_otwarta[najmniejszy_indeks])
        del lista_otwarta[najmniejszy_indeks]
        #print(lista_zamknieta[-1][0]) #
        if lista_zamknieta[-1][0] == 'Zakopane':       # zakończ pętle jeśli znajdzie Zakopane
            break
        for miasto in mapa_graf[wezel]:
            # print(miasto[0])
            if miasto[0] in [closed_item[0] for closed_item in lista_zamknieta]:

                continue
            # print(odleglosc[wezel])
            odleglosc.update({miasto[0]: odleglosc[wezel] + miasto[1]})
            # print('PO ' + str(miasto[0]) + ': '+ str(odleglosc[wezel]) +' + ' + str(miasto[1]) + ' = ' + str(miasto[1]) + str(miasto[0]))
            funkcja1 = odleglosc[wezel] + heurystyka[miasto[0]] + miasto[1]
            #print(str(miasto[0]) + ' |' + str(funkcja1) + ' = ' + str(odleglosc[wezel]) + ' + ' + str(heurystyka[miasto[0]]) + ' + ' + str(miasto[1]))
            tymczas = [miasto[0], funkcja1]
            #print(tymczas)
            #print('przed: ' + str(lista_otwarta))
            lista_otwarta.append(tymczas)
            #print('PO: ' + str(lista_otwarta))
            #print('LISTA ZAMKNIETA' + str(lista_zamknieta))

    rejestruj_wezel = 'Zakopane'
    optymalna_trasa = ['Zakopane']
    #print(lista_zamknieta)
    for i in range(len(lista_zamknieta) -2, -1, -1):
        #print(range(len(lista_zamknieta)-2, -1, -1))
        #print(str(i) + str(lista_zamknieta[i]))
        sprawdz_wezel = lista_zamknieta[i][0] #aktualny wezel
        #print(lista_zamknieta[i][0]) # wypisuje miasta w liscie zamknietej
        if rejestruj_wezel in [dziecko[0] for dziecko in mapa_graf[sprawdz_wezel]]:
            #print(mapa_graf[sprawdz_wezel]) #to samo co nizej tylko nie wyodrebnione
            odleglosc_dziecka = [tymczas[1] for tymczas in mapa_graf[sprawdz_wezel]] #
            #print('odleglosc dziecka' + str(odleglosc_dziecka))
            wezel_dziecka = [tymczas[0] for tymczas in mapa_graf[sprawdz_wezel]]
            #print('wezel dziecka: ' + str(wezel_dziecka))
            print('')
            #print('Odleglosc')
            #print(odleglosc)

            if odleglosc[sprawdz_wezel] + odleglosc_dziecka[wezel_dziecka.index(rejestruj_wezel)] == odleglosc[rejestruj_wezel]:
                #print('odleglosc[rejestruj_wezel]: ' +str(odleglosc[rejestruj_wezel]))
                #print('wezel_dziecka.index(rejestruj_wezel): ' +str(wezel_dziecka.index(rejestruj_wezel)))
                optymalna_trasa.append(sprawdz_wezel)
                #print('sprawdz_wezel: ' + str(sprawdz_wezel))
                rejestruj_wezel = sprawdz_wezel

    optymalna_trasa.reverse()

    print('Odwiedzone miasta: ' + str(lista_zamknieta))
    print('Optymalna droga przez miasta: ' + str(optymalna_trasa))
    return lista_zamknieta, optymalna_trasa

if __name__ == '__main__':
    lista_zamknieta, optymalna_trasa = AGwiazdka()




