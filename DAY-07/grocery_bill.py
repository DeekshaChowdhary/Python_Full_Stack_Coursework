products = ['milk','biscuits','bread','coffee','sugar']
prices = [50,80,40,180,220]

print("------------- welcome to the grocery store -----------")
print("available produts")

print('index'.ljust(6,' '), 'products'.ljust(15,' '), 'prices'.ljust(6,' ' ))

for i in range(5):
    print(str(i+1).ljust(6,' '),products[i].ljust(15,' '),str(prices[i]).ljust(6,' ' ))

items = list(map(int,input("enter the indexes: ").split()))
print("selected items:")
total_amount = 0
for i in items:
    print(products[i-1],prices[i-1])
    total_amount += prices[i-1]
      
print(f'total amount to pay: Rs. {total_amount}', 'Thank you for shopping with us!', sep="\n")
