s1 = input()
s2 = input()

s1 = s1.replace(s2, '', s1.count(s2) - 1)

print(s1)
