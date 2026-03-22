'''for var in seq:
    #stmts

seq:list,tuple,set,dict,str,range'''

'''products = ['bread','fruits','vegtables','milk'] #it can be in list or in tuple or in set or in any sequence
for item in products:
    print(item)'''

'''products = {'bread':30,'fruits':60,'vegtables':45,'milk':87}
for item in products:
    print(item, products[item])'''

'''products = {'bread':30,'fruits':60,'vegtables':45,'milk':87}
for item in products:
    print('products name:',item)
    print('products price:',products[item])
    print('buy now | add to cart')
    print('-----------------------')'''


'''s = 'python programming'
for ch in s:
    print(ch)'''

'''range: seq of numeric
range(start,stop+1,step) = (0,step+1,1)'''

'''for i in range(10,1,-2):
    print(i)'''

'''n = int(input("enter the number: "))
for i in range(1,21):
        print(f'{n}*{i}={n*i}')'''
'''for i in range(10):
    if i==5:
        continue #skip that value continue
    print(i)'''
        
for i in range(10): #if i is in range
    if i==15:
        break #terminate
    print(i)
else:
    print("end of the numbers")

pin = 1234
for i in range(5):
    user_pin = int(input('enter the pin:'))
    if user_pin == pin:
        print("login successful")
        break
    else:
        print("invalid password, try again")
else:
    print("you have reached the max attempts, try again after 5 mins")
    
