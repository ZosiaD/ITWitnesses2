a = int(input('Кількість одиниць товару: '))
if a < 10:
    s = a*12
    print('Вартість покупки:', s)
if 10 < a < 99:
    s = a*10
    print('Вартість покупки:', s)
if a >= 100:
    s = a*7
    print('Вартість покупки:', s)