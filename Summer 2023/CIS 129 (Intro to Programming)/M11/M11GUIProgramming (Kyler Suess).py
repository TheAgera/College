# Design the wireframes and storyboard, interactivity diagram, object dictionary, and any necessary scripts for an interactive program for customers of Sanderson’s Ice Cream Sundaes.

# Allow customers the option of choosing a three-scoop, two-scoop, or one-scoop creation at a base price of $4.00, $3.00, or $2.20, respectively.
# Let the customer choose chocolate, strawberry, or vanilla as the primary flavor.
# If the customer adds nuts, whipped cream, or cherries to the order, add $0.50 for each to the base price.
# After the customer clicks an Order Now button, display the price of the order.

import tkinter as tk

class Sundae:
    # USed to initialize the object's attributes each time the init function is called
    def __init__(self, flavor, scoops, toppings):
        self.flavor = flavor
        self.scoops = scoops
        self.toppings = toppings

    # If statement used to calculate scoop price
    def calculate_price(self):
        base_price = 0
        if self.scoops == 3:
            base_price = 4.00
        elif self.scoops == 2:
            base_price = 3.00
        elif self.scoops == 1:
            base_price = 2.20

        # Calculates the additional toppings by using len, which essentially counts the number of toppings.
        additional_toppings_price = 0.50 * len(self.toppings)
        total_price = base_price + additional_toppings_price

        return total_price

# This function gets called when the order now button is clicked, grabs each variable from the respective buttons/ checkboxes
# The "pack" argument is built into tkinter that allows each object to properly allign itself with the program. Pack is a bad word, it moreso stacks each object.
def show_price():
    sundae = Sundae(flavor_var.get(), scoops_var.get(), [topping for topping, var in toppings_vars.items() if var.get()])
    price = sundae.calculate_price()
    price_label.config(text=f"Price: ${price:.2f}")
    options_frame.pack_forget()
    price_frame.pack()

# Closses the window, thus exiting the program
def exit_program():
    window.destroy()

# Create the main window and title
window = tk.Tk()
window.title("Sanderson's Ice Cream Sundaes")

# Sets the window resolution
window.geometry ('350x350')

# Options frame widget, holds the options for selecting flavor, scoops, toppings, and the Order Now button
options_frame = tk.Frame(window)
options_frame.pack()

# Flavor selection, works by setting a variable to store the selected flavor, by default it is chocolate. Each radio button (flavor_button) will change that variable
flavor_var = tk.StringVar()
flavor_var.set("Chocolate")
flavor_label = tk.Label(options_frame, text="Select Flavor:")
flavor_label.pack()
flavor_buttons = [
    tk.Radiobutton(options_frame, text="Chocolate", variable=flavor_var, value="Chocolate"),
    tk.Radiobutton(options_frame, text="Strawberry", variable=flavor_var, value="Strawberry"),
    tk.Radiobutton(options_frame, text="Vanilla", variable=flavor_var, value="Vanilla")
]
for button in flavor_buttons:
    button.pack()

# Scoop selection, works the same way as above
scoops_var = tk.IntVar()
scoops_var.set(3)
scoops_label = tk.Label(options_frame, text="Select Scoops:")
scoops_label.pack()
scoop_buttons = [
    tk.Radiobutton(options_frame, text="Three Scoops", variable=scoops_var, value=3),
    tk.Radiobutton(options_frame, text="Two Scoops", variable=scoops_var, value=2),
    tk.Radiobutton(options_frame, text="One Scoop", variable=scoops_var, value=1)
]
for button in scoop_buttons:
    button.pack()

# Toppings selection, works the same as the previous two, except there are checkboxes instead of radiobuttons. The checkboxes are Boolean (True or False)
toppings_vars = {}
toppings_label = tk.Label(options_frame, text="Select Toppings:")
toppings_label.pack()
toppings = ["Nuts", "Whipped Cream", "Cherries"]
for topping in toppings:
    var = tk.BooleanVar()
    var.set(False)
    toppings_vars[topping] = var
    checkbox = tk.Checkbutton(options_frame, text=topping, variable=var)
    checkbox.pack()

# Order Now button, calls the show price function
order_button = tk.Button(options_frame, text="Order Now", command=show_price)
order_button.pack()

# Price frame, starts the second screen
price_frame = tk.Frame(window)

# Price display, creates a label widget
price_label = tk.Label(price_frame, text="Price: $0.00")
price_label.pack()

# Exit button
exit_button = tk.Button(price_frame, text="Exit", command=exit_program)
exit_button.pack()

# Start the GUI event loop
window.mainloop()