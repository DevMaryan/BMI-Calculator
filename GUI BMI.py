from tkinter import *

root = Tk()
root.title('BMI Calculator')
root.geometry('490x250+800+400')
root.resizable(False, False)
root.iconbitmap('iko.ico')

def bmi():
    try:
        val_height = ent_height.get()
        height = int(val_height)
        val_mass = ent_weight.get()
        mass = int(val_mass)

        h = (height * height)/10000
        rez = (mass / h)
        print(rez)
        b = int(rez)
        if rez < 18.5:
            
            result_lbl["text"] = "You are Underwieght: {}".format(b)

        elif rez >= 18.5 and rez < 24.9:
            result_lbl["text"] = "You have Normal Weight: {}".format(b)

        elif rez >= 25 and rez <=29.9:
            result_lbl["text"] = "You are Overweight: {}".format(b)

        elif rez > 30:
            result_lbl["text"] = "You are Obese: {}".format(b)
            
    except ValueError as e:
        print(e)

# Create Frame
frame = Frame(height = 550, bg = "#252526")
frame.pack(fill=X)
# Create Label and Entry for Height
lbl_height = Label(frame, text = 'What is your height(cm) ?', bg = "#252526", fg = "#FFF")
lbl_height.place(x = 10, y = 5)
val_height = IntVar()

ent_height = Entry(frame, width=30, textvariable=val_height, bd = 0)
ent_height.delete(0)
ent_height.place(x = 10, y = 30)

# Create Label and Entry for Weight
lbl_weight = Label(frame, text='What is your weight(kg)?', bg = "#252526", fg = "#FFF")
lbl_weight.place(x = 10, y = 55)
val_weight = IntVar()

ent_weight = Entry(frame, width = 30, textvariable=val_weight, bd = 0)
ent_weight.delete(0)
ent_weight.place(x = 10, y = 80)

# Button to calculate everything
btnCalc = Button(frame, text = 'Calculate', command = lambda : bmi(), bd = 0, padx = 20, bg = "#81B71A", fg = "#FFF", activebackground="#81B71A")
btnCalc.place(x = 10, y = 115)

result_lbl = Label(frame, Variable=bmi(), bg = "#252526", fg = "#FFF")
result_lbl.place(x = 10, y = 140)


uw_lbl = Label(frame, text = 'Underwieght < 18.5', bg = "#1ca1e8", fg = "#FFF", width = 35, height = 3)
uw_lbl.place(x = 230, y = 10)
uw_lbl = Label(frame, text = 'Normal weight 18.5 - 24.9', bg = "#81B71A", fg = "#FFF", width = 35, height = 3)
uw_lbl.place(x = 230, y = 70)
uw_lbl = Label(frame, text = 'Overweight 25 - 29.9', bg = "#e8b51c", fg = "#FFF", width = 35, height = 3)
uw_lbl.place(x = 230, y = 130)
uw_lbl = Label(frame, text = 'Obese > 30', bg = "#e8261c", fg = "#FFF", width = 35, height = 3)
uw_lbl.place(x = 230, y = 190)



root.mainloop()