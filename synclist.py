#https://open.kattis.com/contests/kht2bt/problems/synchronizinglists
iteration = 0
while True:
    #input
    l1 = [int(input()) for _ in range(2 * int(input()))]
    n = len(l1)
    if n == 0:
        break
    if iteration > 0:
        print()
    iteration += 1
    #split lists
    l2 = l1[n//2:n]
    l1 = l1[0:n//2]
    #sorted copies to get pairs
    sort1 = list(l1)
    sort2 = list(l2)
    sort1.sort()
    sort2.sort()
    #dictionary containing corresponding pairs by index of original list
    indices = {}
    for i in range(n//2):
        indices.update({l1.index(sort1[i]) : l2.index(sort2[i])})
    #output
    for i in range(n//2):
        print(str(l2[indices[i]]))