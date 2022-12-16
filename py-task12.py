def test(s, p, step):
    if p%(s-step) == 0:
        x = p//(s-step)
        y = s - x
        if y * x == p:
            return True
        else:
            return False
    else:
        return False

while True:
    try:
        S = int(input("Введите сумму чисел: "))
        P = int(input("Введите произведение двух чисел: "))
        out = False
        for n in range(1,S-1):
            if test(S,P,n):
                print(f"{S} {P} -> {n} {S-n}")
                out = True
                break
        if out:
            break
        else:
            print(f"Числа {S} и {P} не соответствуют условиям задачи")
    except:
        print(f"Числа {S} и {P} не соответствуют условиям задачи")