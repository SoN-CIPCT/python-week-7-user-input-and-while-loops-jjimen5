"""
Week 7 Python Homework: User Input and While Loops
Pizza Order Tracker for Restaurant
"""

# 1. Make a list called pizza_orders and populate it with names of pizzas that have been ordered
pizza_orders = ['Pepperoni', 'Margherita', 'Hawaiian', 'Veggie Supreme', 'Meat Lovers']

# 2. Make an empty list called finished_pizzas
finished_pizzas = []

# 3. Loop through the list of pizza orders and print a message for each order
print("=" * 50)
print("PIZZA ORDER TRACKER")
print("=" * 50)
print()

while pizza_orders:
    # Get the current pizza being made (first in the list)
    current_pizza = pizza_orders[0]
    
    # Print message that pizza is finished
    print(f"Your {current_pizza} pizza pie is finished!")
    
    # 4. Move that pizza to the finished_pizzas list
    finished_pizzas.append(pizza_orders.pop(0))

print()
print("=" * 50)
print("ALL PIZZAS COMPLETED!")
print("=" * 50)
print()

# 5. After all pizzas have been made, print a message for each finished pizza
for pizza in finished_pizzas:
    print(f"The {pizza} pizza was made.")

print()
print("=" * 50)
print(f"Total pizzas made today: {len(finished_pizzas)}")
print("=" * 50)