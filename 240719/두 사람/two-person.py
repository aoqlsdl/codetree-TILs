age1, gender1 = map(str, input().split())
age1 = int(age1)

age2, gender2 = map(str, input().split())
age2 = int(age2)

if (((age1 > 19) and (gender1 == 'M')) or ((age2 > 19) and (gender2 == 'M'))):
    print(1)
else: 
    print(0)