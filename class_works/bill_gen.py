print('------ Welcome to Grocery Store ------')
data={
    1:{'product':'Rice','price':60},
    2:{'product':'Wheat Flour','price':45},
    3:{'product':'Sugar','price':25},
    4:{'product':'Milk','price':70},
    5:{'product':'Eggs (12 pcs)','price':130},
    6:{'product':'Cooking Oil','price':90},
    7:{'product':'Tea Powder','price':20},
    8:{'product':'Salt','price':30},
    9:{'product':'Bread','price':25},
    10:{'product':'Soap','price':120},
    }

print('Here are the available products: ')
for i in data:
    print(f'{i}. {data[i]["product"]} - ${data[i]["price"]}')

print("Enter the product indexes you want to buy (you can repeat indexes)")
ind=list(map(int,input("Enter indexes (e.g. 1 2 2 5): ").split()))


total_amount=0
s=set()
for i in ind:
    if i not in s:
        print(f'{data[i]["product"]}-{data[i]["price"]}* {ind.count(i)}')
        total_amount+=data[i]['price']*ind.count(i)
        s.add(i)
    
        

print("total bill:",total_amount)
  
    