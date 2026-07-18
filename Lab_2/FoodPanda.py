s = input("Chose Your Order:\n1.BBQ Chicken Cheese Burger \n2.Beef Burger \n3.Naga Drums\n")


# if s == "1"or s== "2" or s== "3":
if s in ("1", "2" , "3"):
        if s == "1":
          meal_cost = 250
        elif s == "2":
            meal_cost = 170
        elif s == "3":
            meal_cost = 200
           
        location = input("Chose your Location:\n1.Mohakhali\n2.Out side of the Mohakhali\n")
        if location == "1":
            delivery_charge = 40
        else:
            delivery_charge = 60
        
        tax = meal_cost * 0.08
        total_price = meal_cost + delivery_charge + tax
        
        print("Total Price =", total_price)

else: 
    print("It is not Available in list")
    print("Please Enter between listed Order:")