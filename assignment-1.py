
#section 1
name = "Alexis"
age = 28
height = 5.9
is_student = True


#section 2

name = input("What is your name: ")
birth_year = input("What year were you born? ")
current_year = 2026
calculate_age = current_year - int(birth_year)

print(f"Hello {name}! You are approximately {calculate_age} years old.")


#section 3

pizza_price = input("How much does a slice of pizza cost in your city? ")
pizza_price = float(pizza_price)

pizza_slice = input("How many slices of pizza do you normally eat? ")
pizza_slice = float(pizza_slice)

total_pizza_cost = pizza_slice * pizza_price


print(f"Your cost of eating pizza in your city is: $ {total_pizza_cost:.2f} ")

#section 4
item = str("umbrella")
price = float(23.99)
quantity = int(2)

total = price * quantity

print ("============================")
print ("       RECEIPT              ")
print ("============================")
print (f"Item:       {item}")
print (f"Price:     ${price:.2f}")
print (f"Quantity:   {quantity}")
print ("----------------------------")
print (f"Bill:      ${total: .2f}")
print ("============================")



#section 5

name2 = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("What is a fun fact about you? ")
age2 = input("What year where you born? ")

age2 = int(age2)
current_year2 = 2026
student_current_age = current_year2 - age2


print ("============================")
print (f"   Profile {name2}         ")
print ("============================")
print (f"Hometown:    {hometown}")
print (f"Hobby:       {hobby}")
print (f"Fun fact:    {fun_fact}")
print (f"Age:         {age}")
print ("============================")





