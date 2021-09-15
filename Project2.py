import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
win = tk.Tk()
win.title('GUI')
#create labels
name_label = ttk.Label(win,text="Enter your name : ")
name_label.grid(row=0,column=0,sticky=tk.W)
Email_label = ttk.Label(win,text="Enter your E-mail : ")
Email_label.grid(row=1,column=0,sticky=tk.W)
age_label = ttk.Label(win,text="Enter Your Age : ")
age_label.grid(row=2,column=0,sticky=tk.W)
gender_label = ttk.Label(win,text="Enter Your Gender : ")
gender_label.grid(row=3,column=0,sticky=tk.W)
#pack,#grid
#create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=10,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()
email_var = tk.StringVar()
email_entrybox=ttk.Entry(win,width=10,textvariable=email_var)
email_entrybox.grid(row=1,column=1)
age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=10,textvariable=age_var)
age_entrybox.grid(row=2,column=1)
# create combobox
gendervar = tk.StringVar()
gender = ttk.Combobox(win, width=16,textvariable=gendervar,state='readonly')
gender['values']=('Male','Female','Other')
gender.current(0)
gender.grid(row=3,column=1)

# radio button
# student , teacher
usertype = tk.StringVar()
radion1 = ttk.Radiobutton(win,text="Student",value="Student",variable=usertype)
radion1.grid(row=4,column=0) 
radion1 = ttk.Radiobutton(win,text="Teacher",value="Teacher",variable=usertype)
radion1.grid(row=4,column=1) 
# check button
checkbutnvar=tk.IntVar()
checkbtn = ttk.Checkbutton(win, text='check if you want to subscribe to our newsletter',variable=checkbutnvar)
checkbtn.grid(row=5,columnspan=3)

# create button

# def action():
# 	username = name_var.get()
# 	userage = age_var.get()
# 	emailvar = email_var.get()
# 	print(f"{username} has {userage} years old and email-id {emailvar}")
# 	usergender = gendervar.get()
# 	user_type = usertype.get()
# 	if checkbutnvar.get():
# 		subscribed = "Yes"
# 	else:
# 		subscribed = "No"
# 	print(f"{usergender} having type {user_type} and Subscribed : {subscribed}")
# 	with open("file.txt","a") as f:
# 		f.write(f"{username},{userage},{emailvar},{usergender},{user_type},{subscribed}\n")
# 	name_entrybox.delete(0, tk.END)
# 	age_entrybox.delete(0, tk.END)
# 	email_entrybox.delete(0, tk.END)
# 	name_label.configure(foreground='Blue')
# 	Submit_button.configure(foreground='Red')

# write to csv files
def action():
	username = name_var.get()
	userage = age_var.get()
	emailvar = email_var.get()
	print(f"{username} has {userage} years old and email-id {emailvar}")
	usergender = gendervar.get()
	user_type = usertype.get()
	if checkbutnvar.get():
		subscribed = "Yes"
	else:
		subscribed = "No"

	# write to csv
	with open('file.csv','a',newline='') as f:
		dict_writer = DictWriter(f,fieldnames=['UserName','User Email',"User Age","User Type","User Gender",'Subscription'])
		if os.stat('file.csv').st_size==0:
			dict_writer.writeheader()

		dict_writer.writerow({
			'UserName' : username,
			'User Email' : emailvar,
			"User Age" : userage,
			"User Type" : user_type,
			"User Gender" : usergender,
			'Subscription' : subscribed
		})
	name_entrybox.delete(0, tk.END)
	age_entrybox.delete(0, tk.END)
	email_entrybox.delete(0, tk.END)
	name_label.configure(foreground='Blue')
	Submit_button.configure(foreground='Red')
Submit_button = tk.Button(win,text="Submit",command=action)
Submit_button.grid(row=6,column=1,sticky=tk.W)
win.mainloop()
