cp = input("enter cost price: ")
sp = input("enter selling price: ")
 
p = float(sp) - float(cp)

print("Profit: ", p)
 
p1 = p*0.05 + p

print("Selling price to increase the profit by 5%: ", (float(cp) + p1))
