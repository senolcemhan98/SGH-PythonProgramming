#%%
def is_prime(num:int):
    i = num-1
    while i>1:
        if (num%i==0):
            return False
        else: 
            i = i-1
    return True

x = int(input('Enter total prime numbers: '))

y = 2
n_prime = []
while True:
    if is_prime(y):
        n_prime.append(y)
        y+=1
    else:
        y+=1
    if len(n_prime)==x:
        print(n_prime)
        break
    

