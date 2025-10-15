print("=====  Welcome To Smart Store  =====".center(50))
print(" ")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
print(f" ")
print(f"Hello , {name.upper()}")
print(f"Your name length : {len(name)}")
print(f"Title case : {name.title()}")
print(f"Count of 'a' : {name.count('a')}")
print(f"Replaced name : {name.replace('a' , 'x')}")
print(" ")

balance = 1000
print(f"Your starting balance : {balance}")
balance2 = balance + 200
print(f"After bouns : {balance}")
print(" ")
power = pow(5,2)
minbalance = min(balance2 , balance)
maxbalance = max(balance2 , balance)
total = balance + balance2
print(f"Min product price : {minbalance}")
print(f"Max product price : {maxbalance}")
print(f"Rounded total : {round(total)}")
print(f"Power of (5^2) : {power} ")
print(f"Absolute difference from 2000 : {abs(total - 2000)}")
print(" ")

price = float(input("Enter your price : "))
if balance >= price : 
    print(f"Purchase successful!")
elif balance < price : 
    print(f"Insufficient balance!")  
print(f" ")
product_category = input("Product category : ")
if product_category == 'electronics' :
    print("Discount applied!\nNested check >> Excellent choice")
if product_category == 'clothes' :
    print(f"No discount for clothes\nNested check >> Stylish choice")
if product_category == 'food' :
    print(f"Fresh items only \nNested check >> Healthy selection")     
print(f" ")

Product_list = ['phone' , 'laptop']
print(f"Product list : {Product_list}")
Product_list.append("bag")
Product_list.append("Charger")
print(f"After adding accessories : {Product_list}")
Product_list.remove('bag')
print(f"After removing 'bag' : {Product_list}")
print(f"Total items : {len(Product_list)}")
print(f"Max name length in list : {max(Product_list)}")
print(" ")

from array import array
Array_prices = array('i' , [200 , 500 , 900])
print(f"Prices Array : {Array_prices}")
Array_prices.reverse()
print(f"After reverse : {Array_prices}")
print(" ")

Set_customer = {'Ahmed' , 'Sara', 'Ali'}
Set_customer2 = {'Ahmed' , 'Sara', 'Ali' , 'Lina'}
print(f"VIP Customer Set A : {Set_customer}")
print(f"New Customer Set B : {Set_customer2}")
print(f"Union : {Set_customer.union(Set_customer2)}")
print(f"Intersection : {Set_customer.intersection(Set_customer2)}")
print(f"Difference (A-B) : {Set_customer.difference(Set_customer2)}")
print(" ")

Dict_customer = {
    'name':'mustafa' , 
    'age' : 23 , 
    'city' : 'Dubai',
    'balance':balance,
    'last_Purchase':{'item':'laptop' , 'price':price , }


}
print(f"Customer Info : {Dict_customer}")
print(" ")
Tuple_branches = ('Dubai' , 'AbuDhabi' , 'Sharjah')
print(f"Branches Tuple : {Tuple_branches}")
print(f"Tuple length : {len(Tuple_branches)}")
print(f"Index of 'Sharjah' : {Tuple_branches.index('Sharjah')}")
print(f"Max (alphabetical) : {max(Tuple_branches)}")
print(' ')

while True:
    p = input("Enter product price: ")
    if not p.isdigit():
        print("Invalid input, try again\nPlease write number!")
        continue
    p = int(p)
    if p <= 0:
        print("Invalid input, try again\nPrice must be greater than 0!")
        continue
    print("Product accepted!")
    break
print(" ")

while True :
    item =input("Enter next item (type exit to stop) : ")
    if item == 'exit':
        break
    else :
        print("Added successfuly")
print(" ")
print("Thanks you for shopping with\nSmart Store")





