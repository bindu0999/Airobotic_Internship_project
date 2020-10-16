from tkinter import Canvas
import joblib
import numpy as np
import tkinter as tk

key = ['setosa','versicolor','virginica']

#loading ml model 
sav = joblib.load('iris.ml')

#creating tkinter instance
root = tk.Tk() 
root.title("Iris flower") 
root.iconbitmap("icon.ico")
canv = tk.Canvas(root,width=250,height=240)
canv.pack()

#creating labels 
sL = tk.Label(root,text='Sepal Length')
canv.create_window(50,20,window=sL)
sW = tk.Label(root,text='Sepal Width')
canv.create_window(45,60,window=sW) 
pL = tk.Label(root,text='Petal Length')
canv.create_window(45,100,window=pL)
pW = tk.Label(root,text='Petal Width')
canv.create_window(50,140,window=pW)


#creating input text fields to get data
in_sL = tk.Entry(root)
canv.create_window(150,20,window=in_sL)
in_sW = tk.Entry(root)
canv.create_window(150,60,window=in_sW) 
in_pL = tk.Entry(root)
canv.create_window(150,100,window=in_pL)
in_pW = tk.Entry(root)
canv.create_window(150,140,window=in_pW)
in_insulin = tk.Entry(root)

#creating labels to show output
value1 = tk.Label(root)
canv.create_window(110,220,window=value1)

#submit button function
def cal():
    val = [
        float(in_sL.get()),
        float(in_sW.get()),
        float(in_pL.get()),
        float(in_pW.get())
    ]
    pred_val = np.array([val])
    result = sav.predict(pred_val)
    value1["text"] = "Iris-"+key[result[0]]

#reset button function
def clear(): 
    value1["text"] = ""

#creating buttons 
but = tk.Button(text='Submit',command=cal)
canv.create_window(80,180,window=but) 
but1 = tk.Button(text='Reset',command=clear)
canv.create_window(150,180,window=but1)

#apply loop to app so it not close itself
root.mainloop()