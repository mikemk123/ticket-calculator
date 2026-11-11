age = 30
tickets = 5
snack = True
if age  < 12:
    price = 300
elif age <= 17:
    price = 400
elif age > 60:
    price = 350
else:
    price = 500
total = price * tickets
if tickets >=5:
    total=round(total * 0.9)
if snack:
    total += 200
print("Price per ticket:", price)
print("Tickets:", tickets)
print("Total:", total)