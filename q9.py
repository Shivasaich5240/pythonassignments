list1 = []
n = int(input("Enter the number of students:"))
for i in range(0,n):
    ele = int(input())
    list1.append(ele)
print(list1)
for i in range(0,n):
    list1[i] = list1[i]*0.454
print(list1)