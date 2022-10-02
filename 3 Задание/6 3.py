def Zadanie_6(q1, w1, q2, w2):
    if (q1 > 8 or w1 > 8) or (q2 > 8 or w2 > 8):
        print("Ты играешь не на шахматной доске💀")
    else:
        a=(q1 + w1) % 2
        b=(q2 + w2) % 2
        if a == b:
            print("Да")
        else:
            print("Нет")
