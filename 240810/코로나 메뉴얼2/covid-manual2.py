types = [0] * 4

for i in range(3):
    symtom, temperature = map(str, input().split())
    temperature = int(temperature)
    if symtom == "Y" and temperature >= 37:
        types[0] += 1
    elif symtom == "N" and temperature >= 37:
        types[1] += 1
    elif symtom == "Y" and temperature < 37:
        types[2] += 1
    else:
        types[3] += 1

for t in types:
    print(t, end = " ")

if types[0] >= 2:
    print("E")