i = 1
had = [2]
till = int(input("till when you want to count: "))
see_prints = input("do you want to see the twins? (no) or (yes): ").lower()
match see_prints:
    case "no":
        is_see = False
    case "yes":
        is_see = True
count = 0
while True:
    i += 1
    if i > till:     # stop
        break

    for j in range(len(had)):
        if i % had[j] == 0:
            had.append(i)
            break
        elif j == len(had) - 1:
            for k in range(len(had)):
                if (i + 2) % had[k] == 0:
                    had.append(i)
                    break
                elif k == len(had) - 1:
                    if is_see:
                        print(i, i + 2)
                    count += 1
                    had.append(i)
print(f"from 0 to {till} exist {count} prime twins.")
