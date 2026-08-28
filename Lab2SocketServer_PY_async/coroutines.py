#Генератор 
def counter(n):
    print("Counter")
    i = 1
    while True:
        x = yield i
        if x is not None:
            i = int(x)
        i+=1
        if i > n:
            print("Counter end")
            return
        
gen = counter(7)
print(next(gen))
print(gen.send(None))
