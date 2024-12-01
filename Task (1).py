print("İngiltərə Almaniyanın ilk federal kansleri : \n A) K. Adenauer B) L. Erxard C) H. Koll D) H. Ş. Şmidt  ")
cavab1 = input("Duzgun varianti secin: ")
print(cavab1)
if cavab1 == "A" or cavab1 == "a":
    print("Cavabiniz dogrudur.")
    b1 = 1
else:
    print("Cavabiniz yanlisdir. \n Dogru cavab : A")
    b1 = 0
print("2) Sultan II İstanbulu neçənci ildə fəth edildi ? \n A) 1444 B) 1452 C) 1501 D) 1453")
cavab2 = input("Dogru varianti secin: ")
print(cavab2)
if cavab2 == "A" or cavab2 == "a":
    print("Cvabiniz dogrudur.")
    b2 = 1
else:
    print("Cavbiniz yanlisdir. \n Dogru cavab : A")
    b2 = 0
print(" Dehli sultanlığının əsasını qoydu: \n A)Qiyasəddin Balaban B)Əlaəddin Hilçi C)Eltutmuş xan. D)Qütbəddin Aybək")
cavab3 = input("Duzgun varianti secin: ")
print(cavab3)
if cavab3 == "D" or cavab3 == "d":
    print("Cavabiniz dogrudur.")
    b3 = 1
else:
    print("Cvabiniz yanlisdir. \n Dogru cavab : D")
    b3 = 0
print(" Osmanlı dövlətində sultandan sonra əsas vəzifəni kim tuturdu? \n A)Baş vəzir B)Dəftərdar C)Paşa D)Sancaqbəyi E) Bəylərbəyi")
cavab4 = input("Duzgun varianti secin: ")
print(cavab4)
if cavab4 == "C" or cavab4 == "c":
    print("Cavabiniz dogrudur.")
    b4 = 1
else:
    print("Cavabiniz yanlisdir. \n Dogru cavab : C")
    b4 = 0
dogru = (b1 , b2 , b3 , b4 )
bal = sum(dogru)
print("Dogru cavab = " , bal)
print("Yanlis cavab =" , 4 - bal)
print("Yekun bal = " , bal * 10)

