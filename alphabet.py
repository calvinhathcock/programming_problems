#https://open.kattis.com/contests/r4r5im/problems/alphabetspam

s = input()

ws = 0.0
lc = 0.0
uc = 0.0
sy = 0.0
total = len(s)
lowers = range(97, 123)
uppers = range(65, 91)

for i in s:
    if (ord(i) in lowers):
        lc += 1
    elif (ord(i) in uppers):
        uc += 1
    elif (ord(i) == 95):
        ws += 1
    else:
        sy += 1
        
print(ws/total)
print(lc/total)
print(uc/total)
print(sy/total)

    
