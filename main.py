from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=300)

label_1 = Label(text="Enter Your Weight (kg)")
label_1.pack()
entry_weight = Entry(width=10)
entry_weight.pack()

label_2 = Label(text="Enter Your Height (cm)")
label_2.pack()
entry_height = Entry(width=10)
entry_height.pack()

result_label = Label(text="")
result_label.pack()

def button_clicked():
    weight = entry_weight.get()
    height = entry_height.get()

    if weight == '' or height == '':
        result_label.config(text="Please enter both weight and height.")
        return

    try:
        weight = float(weight)
        height = float(height) / 100
    except ValueError:
        result_label.config(text="Enter a valid number.")
        return

    bmi = weight / height ** 2

    if bmi <= 18.4:
        result_label.config(text="Your BMI is {:.2f}. You are underweight".format(bmi))
    elif 18.5 <= bmi <= 24.9:
        result_label.config(text="Your BMI is {:.2f}. You are normal".format(bmi))
    elif 25.0 <= bmi <= 39.9:
        result_label.config(text="Your BMI is {:.2f}. You are overweight".format(bmi))
    elif bmi >= 40:
        result_label.config(text="Your BMI is {:.2f}. You are obese".format(bmi))

button = Button(text="Calculate", command=button_clicked)
button.pack()

window.mainloop()