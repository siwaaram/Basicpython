number = [12, 75, 150, 180, 145, 525, 50]
for i in number:
    if i>150 and i<500:
        continue
    elif i>500:
        break
    elif i%5==0:
        print(i)
