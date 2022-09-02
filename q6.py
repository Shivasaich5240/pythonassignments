def uniquewordscount(l):
    sum = 0
    for i in l:
        sum = sum + 1
    print(sum)
str = "I am a teacher and I love to inspire and teach people"
s = set(str.split(" "))
uniquewordscount(s)
