def days(n):
    day = 1
    printers = 1
    while printers < n:
        printers = 2**day
        day += 1
    
    return day
    
print(days(int(input())))
