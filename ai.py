from tkinter import *
from random import randint

root = Tk()
root.title('Diet commander')

def generate():

    protein = ['Yogurt(1 cup)','Cooked meat(3 Oz)','Cooked fish(4 Oz)','1 whole egg + 4 egg whites','Tofu(5 Oz)']
    fruit = ['Berries(80 Oz)','Apple','Orange','Banana','Dried Fruits(Handfull)','Fruit Juice(125ml)']
    vegetable = ['Any vegetable(80g)']
    grains = ['Cooked Grain(150g)','Whole Grain Bread(1 slice)','Half Large Potato(75g)','Oats(250g)','2 corn tortillas']
    ps = ['Soy nuts(i Oz)','Low fat milk(250ml)','Hummus(4 Tbsp)','Cottage cheese (125g)','Flavored yogurt(125g)']
    taste_en = ['2 TSP (10 ml) olive oil','2 TBSP (30g) reduced-caloriesorie salad dressin','1/4 medium avocado','Small handful of nuts','1/2 ounce  grated Parmesan cheese','1 TBSP (20g) jam, jelly, honey, syrup, sugar']

    weight = v3.get()
    height = v4.get()
    age = v5.get()
    select = str(Lb.get(ACTIVE))
    gender = Lb2.get(ACTIVE)

    if gender == 'Male':
        calories = float()
        calories = 88.362 + (13.397*float(weight)) + (4.799*float(height)) - (5.677*float(age))
        print ("Calories:",calories)
    elif gender == 'Female':
        calories = float()
        calories = 447.593 + (9.247*float(weight)) + (3.098*float(height)) - (4.330*float(age))


    if select == 'Super Light (little or no exercise)':
        calories = calories*1.2

    elif select == 'Lightly active (1-3 days/week)':
        calories = calories*1.375

    elif select == 'Moderately active (3-5 days/week)':
        calories = calories*1.55

    elif select == 'Very active (6-7 days/week)':
        calories = calories*1.725

    elif act == 'Super active (twice/day)':
        calories = calories*1.9

    print ("Calories:",calories)

    result = Tk()
    result.title('Schedule')


    if calories<1500:
        l6 = Label(result, text="%-20s %-50s %-50s"%("Breakfast:",protein[randint(0, 4)],fruit[randint(0, 5)]) ).grid(row=0,column=0,sticky='w')
        l8 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Lunch:",protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=1,column=0,sticky='w')
        l9 = Label(result, text="%-20s %-50s %-50s"%("Snack:",ps[randint(0, 4)],vegetable[0]) ).grid(row=2,column=0,sticky='w')
        l10 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Dinner:",protein[randint(0, 4)],"2 "+vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=3,column=0,sticky='w')
        l11 = Label(result, text="%-20s %-50s"%("Snack:",fruit[randint(0, 5)]) ).grid(row=4,column=0,sticky='w')


    elif calories<1800:
        l6 = Label(result, text="%-20s %-50s %-50s"%("Breakfast:",protein[randint(0, 4)],fruit[randint(0, 5)]) ).grid(row=0,column=0)
        l8 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Lunch:",protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=1,column=0)
        l9 = Label(result, text="%-20s %-50s %-50s"%("Snack:",ps[randint(0, 4)],vegetable[0]) ).grid(row=2,column=0)
        l10 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Dinner:","2 "+protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=3,column=0)
        l11 = Label(result, text="%-20s %-50s"%("Snack:",fruit[randint(0, 5)]) ).grid(row=4,column=0)
        
        
    elif calories<2200:
        l6 = Label(result, text="%-20s %-50s %-50s"%("Breakfast:",protein[randint(0, 4)],fruit[randint(0, 5)]) ).grid(row=0,column=0)
        l8 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Lunch:",protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=1,column=0)
        l9 = Label(result, text="%-20s %-50s %-50s"%("Snack:",ps[randint(0, 4)],vegetable[0]) ).grid(row=2,column=0)
        l10 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Dinner:","2 "+protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=3,column=0)
        l11 = Label(result, text="%-20s %-50s"%("Snack:",fruit[randint(0, 5)]) ).grid(row=4,column=0)
        

    elif calories>=2200:
        l6 = Label(result, text="%-20s %-50s %-50s"%("Breakfast:","2 "+protein[randint(0, 4)],fruit[randint(0, 5)]) ).grid(row=0,column=0)
        l8 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Lunch:",protein[randint(0, 4)],vegetable[0],"Leafy Greens "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=1,column=0)
        l9 = Label(result, text="%-20s %-50s %-50s"%("Snack:",ps[randint(0, 4)],vegetable[0]) ).grid(row=2,column=0)
        l10 = Label(result, text="%-20s %-50s %-50s %-50s %-50s"%("Dinner:","2 "+protein[randint(0, 4)],"2 "+vegetable[0],"Leafy Greens 2 "+grains[randint(0,4)],taste_en[randint(0,5)]) ).grid(row=3,column=0)
        l11 = Label(result, text="%-20s %-50s"%("Snack:",fruit[randint(0, 5)]) ).grid(row=4,column=0)
        
    result.mainloop()


l1 = Label(root, text='Weight')
l2 = Label(root, text='Height(in cms)')
l3 = Label(root, text='Age  ')
l4 = Label(root, text = 'Gender', bg = 'white')
l5 = Label(root, text = 'Activity', bg = 'white')
l7 = Label(root, text = '')


v3=StringVar()
v4=StringVar()
v5=StringVar()


e3 = Entry(root, textvariable=v3, width=30)
e4 = Entry(root, textvariable=v4, width=30)
e5 = Entry(root, textvariable=v5, width=30)

Lb = Listbox(root, height=6, width=30)
Lb.insert(1, 'Super Light (little or no exercise)')
Lb.insert(2, 'Lightly active (1-3 days/week)')
Lb.insert(3, 'Moderately active (3-5 days/week)')
Lb.insert(4, 'Very active (6-7 days/week)')
Lb.insert(5, 'Super active (twice/day)')

Lb2 = Listbox(root, height=2, width=30)
Lb2.insert(1, 'Male')
Lb2.insert(2, 'Female')

var = Lb.get(ACTIVE)
print (var)

l5 = Label(root, text = '')
l5.grid(row=5,column=0)

b1 = Button(root, text = 'Submit', width=25, command = generate)

l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)
l4.grid(row=0,column=0)
l5.grid(row=4,column=0)
l7.grid(row=0,column=2)
e3.grid(row=1, column=1)
e4.grid(row=2, column=1)
e5.grid(row=3, column=1)
Lb.grid(row=4, column = 1)
Lb2.grid(row=0, column = 1)
b1.grid(row=6,columns=3)


root.mainloop()
