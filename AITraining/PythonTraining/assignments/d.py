for num in range(1, 501):

    if num % 41 == 0:
        break

    if num % 6 == 0:
        continue

    if num % 2 != 0:
        print(num)