import os

os.environ["TCL_LIBRARY"] = r"C:\Users\berza\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\berza\AppData\Local\Programs\Python\Python313\tcl\tk8.6"



import tkinter as tk


def write_result(bmi):
    if bmi <= 16:
        category = "Severely Thin"
    elif bmi <= 17:
        category = "Moderately Thin"
    elif bmi <= 18.5:
        category = "Mildly Thin"
    elif bmi <= 25:
        category = "Normal"
    elif bmi <= 30:
        category = "Overweight"
    elif bmi <= 35:
        category = "Obese Class 1"
    elif bmi <= 40:
        category = "Obese Class 2"
    else:
        category = "Obese Class 3"

    return f"Your BMI is: {bmi:.2f}\nCategory: {category}"


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if not height or not weight:
        result_label.config(text="Please enter both weight and height.")
        return

    try:
        height = float(height)
        weight = float(weight)

        if height <= 0 or weight <= 0:
            result_label.config(text="Values must be greater than zero.")
            return

        bmi = weight / (height / 100) ** 2

        result_label.config(text=write_result(bmi))

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.config(padx=30, pady=30)

# Weight input
weight_input_label = tk.Label(text="Enter your weight (kg)")
weight_input_label.pack()

weight_input = tk.Entry(width=15)
weight_input.pack()

# Height input
height_input_label = tk.Label(text="Enter your height (cm)")
height_input_label.pack()

height_input = tk.Entry(width=15)
height_input.pack()

# Calculate button
calculate_button = tk.Button(
    text="Calculate",
    command=calculate_bmi
)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label()
result_label.pack()

window.mainloop()