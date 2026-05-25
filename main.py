import random 
while True:
    e = input("Нажмите Enter или выход")
    if e == "выход":
        break
    n = random.randint(0,1)
    if n == 0: print("Орёл")
    else: print("Решка")