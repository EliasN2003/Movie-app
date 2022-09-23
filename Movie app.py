
# MOVIE APP

from tkinter import *

root = Tk()
root.config(bg="#121212")
root.title("Login interface")
width = 1000
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)


# Top menu variables
search = StringVar()
search.set("Search for a movie")


# Top menu frame
top_menu = Frame(root, bg="gray")
top_menu.grid(row=0, column=0, columnspan=3, rowspan=1, sticky=NSEW, ipadx=10, ipady=10)
top_menu.grid_columnconfigure(1, weight=1)
top_menu.grid_columnconfigure(2, weight=1)
top_menu.grid_rowconfigure(0, weight=1)

search_bar = Entry(top_menu, textvariable=search, font=("Doppio One", 16), borderwidth=5)
search_bar.grid(row=0, column=0, sticky=W, padx=15)
search_btn = Button(top_menu, text="Search", font=("Doppio One", 15), bg="orange", fg="black")
search_btn.grid(row=0, column=1, sticky=W)
advanced_search_btn = Button(top_menu, text="Advanced search", font=("Doppio One", 16), bg="orange", fg="black")
advanced_search_btn.grid(row=0, column=2, sticky=E, padx=15)

# Root window
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

upcoming_lbl = Label(root, text="Upcoming movies in 2022", font=("Doppio One", 22, "bold"), bg="#121212", fg="orange")
upcoming_lbl.grid(row=1, column=0, columnspan=3, sticky=N, pady=(20, 0))
action_lbl = Label(root, text="Action", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
action_lbl.grid(row=2, column=0, sticky=NW, padx=(125, 0), ipadx=15, ipady=6, pady=(40, 0))
horror_lbl = Label(root, text="Horror", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
horror_lbl.grid(row=2, column=1, sticky=N, ipadx=15, ipady=6, pady=(40, 0))
drama_lbl = Label(root, text="Drama", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
drama_lbl.grid(row=2, column=2, sticky=NE, padx=(0, 125), ipadx=15, ipady=6, pady=(40, 0))


root.mainloop()
