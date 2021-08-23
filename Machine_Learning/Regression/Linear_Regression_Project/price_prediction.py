import tkinter as tk
from tkinter import font 
import pickle
import pandas as pd
from tkinter import messagebox

root = tk.Tk()
root.config(bg="black")
root.title("Price Prediction Application")
f1 = tk.Frame(bg="black")
f2 = tk.Frame(bg="black")
l = tk.Label(f1, text="California House Price Prediction", fg="grey", bg="black", 
            font=['monospace', 50, 'italic'])

labels = ['housing_median_age',
        'total_rooms',
        'total_bedrooms',
        'population',
        'households',
        'median_income',
        'ocean_proximity',
        'rooms_per_household',
        'population_per_household',
        'bedrooms_per_rooms']
entries = []
i = 0
for row in range(3):
    for col in range(0, 4, 2):
        l1 = tk.Label(f2, text=labels[i].title(), fg="white", bg="black", font=[None, 20])
        e = tk.Entry(f2, font=['sans serif', 15], bg="grey")  # e1.get()
        entries.append(e)
        l1.grid(row=row, column=col, pady=20, padx=8)
        e.grid(row=row, column=col+1, ipadx=5, ipady=5, pady=20, padx=8)
        i += 1
options = ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND']
dd = tk.StringVar()
l1 = tk.Label(f2, text="Ocean_Proximity",fg="white", bg="black", font=[None, 20])
drop = tk.OptionMenu(f2, dd, *options)
dd.set("NEAR BAY")
l1.grid(row=3, column=0, pady=20, padx=8)
drop.grid(row=3, column=1, ipadx=5, ipady=5, pady=20, padx=8)

def load_model_pipe(f1, f2):
    with open(f1, 'rb') as fp:
        model = pickle.load(fp)
    with open(f2, 'rb') as fp:
        pipe = pickle.load(fp)
    return model, pipe

def predict_value():
    values = [eval(e.get()) for e in entries]
    values.append(dd.get())
    r_per_h = (values[1])/(values[4])
    p_per_h = (values[3])/(values[4])
    b_per_r = (values[2])/(values[1])
    values.extend([r_per_h, p_per_h, b_per_r])
    model, pipe = load_model_pipe("linmodel.pkl", "pipe.pkl")
    df = pd.DataFrame([values], columns=labels)
    df = pipe.transform(df)
    price = model.predict(df)
    print(price)
    messagebox.showinfo("PRICE", price[0])


sub = tk.Button(f2, text="Submit", height=2, width=20, command=predict_value, font=[None, 15, 'italic'], 
                bg="#123456", fg="white")
sub.grid(row=3, column=2, columnspan=2)

f1.pack()
f2.pack()
l.pack()
root.minsize(700, 600)
root.resizable(0, 0)
root.mainloop()