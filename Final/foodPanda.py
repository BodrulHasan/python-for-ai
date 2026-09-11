meal = input("Select your Order:\n1.Meet box.\n2.French fry.\n3.Biriyani\n")

if meal in ("1","2","3"):

    if meal == "1":
        meal_cost = 180

    elif meal == "2":
        meal_cost = 100
    
    elif meal == "3":
        meal_cost = 250

    location = input("Select your location:\n1.Dhaka\n2.Outside of Dhaka\n")

    if location in ("1","2"):
        if location == 1:
            delivery_charge = 60
    
        else:
            delivery_charge = 100
    tax = meal_cost*0.08

    total_price = meal_cost+delivery_charge+tax

    print("Sir, Your Total Price is:",total_price)

else:
    print("Yor Order not available in the list")
    print("Sir please select order between the list")

