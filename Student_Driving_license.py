

from tkinter import *
root = Tk()
root.title("Driver's Liscence")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Driver's License")
label_name_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_grade_tag = canvas.create_text(40,205, font=('Times', '16', 'bold') ,text="Birthday :")
label_subjects_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="no. :")
label_address_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="Address :")
label_vehicles_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="Authorisation to drive :")

label_name = Label(root)
label_grade = Label(root)
label_subjects = Label(root)
label_address = Label(root)
label_vehicles = Label(root)

def myCardDetails():
    name = "Winnie the Pooh"
    print(type(name))   
    grade = "January 27, 1823"
    print(type(grade))
    subjects = "451578"
    print(type(subjects))
    address = "Gilbert Lane"
    print(type(address))
    vehicles = "two four"
    print(type(vehicles))
    
    label_name['text'] = name
    label_grade['text'] = grade
    label_subjects['text'] = subjects
    label_address['text'] = address
    label_vehicles['text'] = vehicles
    
    
button1 = Button(root, text = "Show my ID Card", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=label_grade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
label_address_window = canvas.create_window(155, 252, anchor=CENTER, window=label_address)
label_vehicles_window = canvas.create_window(155, 252, anchor=CENTER, window=label_vehicles)
canvas.pack()

root.mainloop()



# tkinter basic template end statement
