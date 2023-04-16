from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.geometry("300x300")
window.config(pady=20,padx=20)

lbl_height=Label(text="Height (cm)")
lbl_height.config(padx=20,pady=20)
lbl_height.pack()

entryHeight=Entry(width=20)
entryHeight.focus()
entryHeight.pack()

lblWeight=Label(text="Weight (kg)")
lblWeight.config(padx=20,pady=20)
lblWeight.pack()

entryWeight	=Entry(width=20)
entryWeight.pack()



def bmiCalculator():
    height=entryHeight.get()
    weight=entryWeight.get()

    if height=="" or weight=="":
            resultLabel.config(text="Enter both weight and height!")
    else:
            try:
                    bmi=float(weight)/((float(height)/100)**2)
                    if bmi <= 16:
                            resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are severely thin! ")
                    elif 16 < bmi <= 17:
                            resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are moderately thin! ")
                    elif 17 < bmi <= 18.5:
                            resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are mild thin! ")
                    elif 18.5 < bmi <= 25:
                            resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are normal weight ")
                    elif 25 < bmi <= 30:
                            resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are overweight ")
                    elif 30 < bmi <= 35:
                             resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are obese class 1 ")
                    elif 35 < bmi <= 40:
                             resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are obese class 2")
                    else:
                             resultLabel.config(text=f"Your BMI is {round(bmi, 2)}. You are obese class 3 ")
            except:
                    resultLabel.config(text="Enter a valid number!")

buton=Button(text="Calculate",command=bmiCalculator)
buton.config(padx=20,pady=20)
buton.pack()


resultLabel=Label(text="")
resultLabel.pack()

window.mainloop()