ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
min = ages[0]
max = ages[(len(ages))-1]
print(min)
print(max)
ages.append(min)
ages.append(max)
print(ages)
sum = 0
if (len(ages)%2 == 0):
    t1 = int(ages[int(len(ages)/2)] + ages[int((len(ages)/2) - 1)])/2
    print(t1)
else:
    print(ages[int(len(ages)/2)])
for i in range(0,(len(ages))-1):
    sum = sum + ages[i]
avg = sum/len(ages)
print(avg)
ran = (ages[len(ages)-1] - ages[0])
print(ran)