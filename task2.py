k = int(input('Введіть кількість кредитів:'))
if k > 0 and k <= 23:
    print('Student')
if k >= 24 and k <= 53:
    print('Sophomore')
if k >= 54 and k <= 83:
    print('Junior')
if k >= 84:
    print('Senior')
