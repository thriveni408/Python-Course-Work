amount=int(input("Enter the amount: "))
actual_amount=amount
if amount>=10000:
    actual_amount=amount- amount*0.5
    
elif 8000<amount<=10000:
    actual_amount=amount- amount*0.3

elif 5000<amount<=8000:
    actual_amount=amount- amount*0.2

elif 2000<amount<=5000:
    actual_amount=amount- amount*0.05

print(f"Amount: {amount}\nAfter discount: {actual_amount}")