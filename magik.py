from tkinter import *
root=Tk()
root.title("Mutidimensional Arrays")

root.geometry("500x500")
label = Label(root)

array_1d = ["Jimmy", "Billy", "Bob"]
print(array_1d[0])

array_2d = [["Jimmy", "A"], ["Billy", "C"], ["Bob", "didn't take school"]]
print(array_2d[0])
print(array_2d[0][1])

array_3d = [["Jimmy", "A", "Science"],["Billy", "A", "Making burritos"],["Bob","A","being himself"]]
print(array_3d[0])
print(array_3d[0][0])

def report():
    label['text'] = array_3d[0][0] + " got an " + array_3d[0][1] + " in " + array_3d[0][2] + "."
    
btn = Button(root, text = 'show report', command = report)
btn.place(relx=0.5,rely=0.5,anchor = CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()

#this code is totoally not scuffed and totally not copied off of byju's future school