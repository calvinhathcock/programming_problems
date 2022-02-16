#https://open.kattis.com/contests/r4r5im/problems/symmetricorder
set = 1
while True:
    lines = [input() for _ in range(int(input()))]
    if (len(lines) == 0):
        break
   
    print("SET", set)
    set += 1
   
    l = []
    walker = 0
   
    for i in range(len(lines)):
        if i % 2 == 0:
            l.insert(len(l)-walker, lines[i])
            walker += 1
        else:
            l.insert(walker, lines[i])
        
    for j in l:
        print(j)
   
    
        
        
    
