import pyinputplus as pyip
pricetoPay=0
print("Bread type?")
bread=pyip.inputMenu(["wheat","white","sourdough"])
if bread=="wheat":
    pricetoPay+=3
if bread=="white":
    pricetoPay+=9
if bread=="sourdough":
    pricetoPay+=2
cheeseYesNo=pyip.inputYesNo(prompt="Do u want cheese? ")
if cheeseYesNo== "yes":
    pricetoPay+=2.10
    print("Cheese Type? ")
    cheeseType=pyip.inputMenu(["mayo","mustard","lettuce","tomato"],numbered=True)
    if (cheeseType)=="mayo"or"mustard"or"lettuce"or"tomato"or"1"or"2"or"3"or"4":
        pricetoPay+=0.50
else:
    pricetoPay+=0
numberofsandwhiches=pyip.inputInt(prompt="Number of Sandwhiches do u wanna get? ")
pricetoPay =pricetoPay*numberofsandwhiches
print("Total Cost: $",+pricetoPay)