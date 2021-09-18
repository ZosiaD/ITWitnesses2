s = float(input('Введіть довжину в сантиметрах:'))
if s < 0:
    print("Запис недійсний")
else:
    s = round(s * 0.39, 2)
    print ('В дюймах: ', s)
    
