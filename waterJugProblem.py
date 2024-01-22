# def water_jug_problem(capacity_jug1, capacity_jug2, target_amount):
#     state_set = set()

#     def pour_water(jug1, jug2):
#         if (jug1, jug2) in state_set:
#             return False
#         state_set.add((jug1, jug2))
#         print(f"Jug1: {jug1}L, Jug2: {jug2}L")

#         if jug1 == target_amount or jug2 == target_amount:
#             print("Goal reached!")
#             return True

#         # Fill jug1
#         if jug1 < capacity_jug1:
#             if pour_water(capacity_jug1, jug2):
#                 print(f"Pour water from jug2 to jug1 ({jug1 + jug2 - capacity_jug1}L)")
#                 return True

#         # Fill jug2
#         if jug2 < capacity_jug2:
#             if pour_water(jug1, capacity_jug2):
#                 print(f"Pour water from jug1 to jug2 ({jug1 + jug2 - capacity_jug2}L)")
#                 return True

#         # Empty jug1
#         if jug1 > 0:
#             if pour_water(0, jug2):
#                 print("Empty jug1")
#                 return True

#         # Empty jug2
#         if jug2 > 0:
#             if pour_water(jug1, 0):
#                 print("Empty jug2")
#                 return True

#         # Pour water from jug1 to jug2
#         if jug1 > 0 and jug2 < capacity_jug2:
#             pour_amount = min(jug1, capacity_jug2 - jug2)
#             if pour_water(jug1 - pour_amount, jug2 + pour_amount):
#                 print(f"Pour water from jug1 to jug2 ({pour_amount}L)")
#                 return True

#         # Pour water from jug2 to jug1
#         if jug2 > 0 and jug1 < capacity_jug1:
#             pour_amount = min(jug2, capacity_jug1 - jug1)
#             if pour_water(jug1 + pour_amount, jug2 - pour_amount):
#                 print(f"Pour water from jug2 to jug1 ({pour_amount}L)")
#                 return True

#         return False

#     # Start from the initial state (both jugs empty)
#     pour_water(0, 0)

# # Example usage
# water_jug_problem(4, 3, 2)


import tkinter as tk
from tkinter import messagebox

def water_jug_problem(capacity_jug1, capacity_jug2, target_amount):
    state_set = set()

    def pour_water(jug1, jug2):
        if (jug1, jug2) in state_set:
            return False
        state_set.add((jug1, jug2))

        if jug1 == target_amount or jug2 == target_amount:
            return True

        # Fill jug1
        if jug1 < capacity_jug1:
            if pour_water(capacity_jug1, jug2):
                steps.append(f"Fill jug1 ({capacity_jug1}L)")

        # Fill jug2
        if jug2 < capacity_jug2:
            if pour_water(jug1, capacity_jug2):
                steps.append(f"Fill jug2 ({capacity_jug2}L)")

        # Empty jug1
        if jug1 > 0:
            if pour_water(0, jug2):
                steps.append("Empty jug1")

        # Empty jug2
        if jug2 > 0:
            if pour_water(jug1, 0):
                steps.append("Empty jug2")

        # Pour water from jug1 to jug2
        if jug1 > 0 and jug2 < capacity_jug2:
            pour_amount = min(jug1, capacity_jug2 - jug2)
            if pour_water(jug1 - pour_amount, jug2 + pour_amount):
                steps.append(f"Pour {pour_amount}L from jug1 to jug2")

        # Pour water from jug2 to jug1
        if jug2 > 0 and jug1 < capacity_jug1:
            pour_amount = min(jug2, capacity_jug1 - jug1)
            if pour_water(jug1 + pour_amount, jug2 - pour_amount):
                steps.append(f"Pour {pour_amount}L from jug2 to jug1")

        # Check if one jug is completely filled and the other is partially filled
        if jug1 == capacity_jug1 and jug2 < capacity_jug2:
            pour_amount = min(jug2, capacity_jug1)
            if pour_water(jug1 - pour_amount, jug2 + pour_amount):
                steps.append(f"Pour {pour_amount}L from jug1 to jug2 (completely fill jug1)")

        if jug2 == capacity_jug2 and jug1 < capacity_jug1:
            pour_amount = min(jug1, capacity_jug2)
            if pour_water(jug1 + pour_amount, jug2 - pour_amount):
                steps.append(f"Pour {pour_amount}L from jug2 to jug1 (completely fill jug2)")

        return False

    # Start from the initial state (both jugs empty)
    pour_water(0, 0)

# GUI Function to get user input and display the steps
def solve_water_jug_problem():
    capacity_jug1 = int(entry_jug1.get())
    capacity_jug2 = int(entry_jug2.get())
    target_amount = int(entry_target.get())

    steps.clear()
    water_jug_problem(capacity_jug1, capacity_jug2, target_amount)

    if not steps:
        messagebox.showinfo("Result", "No solution exists.")
    else:
        result_text.set("\n".join(steps))
        messagebox.showinfo("Result", "Solution found!")

# Create the main Tkinter window
root = tk.Tk()
root.title("Water Jug Problem Solver")
root.geometry("365x584+300+100")

# Create and place widgets
label_jug1 = tk.Label(root, text="Capacity of Jug 1:")
label_jug1.grid(row=0, column=0, padx=5, pady=5)

entry_jug1 = tk.Entry(root)
entry_jug1.grid(row=0, column=1, padx=5, pady=5)

label_jug2 = tk.Label(root, text="Capacity of Jug 2:")
label_jug2.grid(row=1, column=0, padx=5, pady=5)

entry_jug2 = tk.Entry(root)
entry_jug2.grid(row=1, column=1, padx=5, pady=5)

label_target = tk.Label(root, text="Target Amount:")
label_target.grid(row=2, column=0, padx=5, pady=5)

entry_target = tk.Entry(root)
entry_target.grid(row=2, column=1, padx=5, pady=5)

button_solve = tk.Button(root, text="Solve", command=solve_water_jug_problem)
button_solve.grid(row=3, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
label_result = tk.Label(root, textvariable=result_text, wraplength=300)
label_result.grid(row=4, column=0, columnspan=2, pady=5)

steps = []

# Start the Tkinter event loop
root.mainloop()
