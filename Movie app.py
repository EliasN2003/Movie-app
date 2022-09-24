
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
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Advanced search menu variables
toggle = 1
genre = StringVar()
year = StringVar()
rating = StringVar()

# Top menu variables
search = StringVar()
search.set("Search for a movie")


# Reloads the searchbar in case the user doesn't type anything
def focus_in(e):
    if search.get() == "Search for a movie":
        search.set("")


# Clears the searchbar for the user to type
def focus_out(e):
    if search.get() == "":
        search.set("Search for a movie")


# Creates the pop-up filters frame
def filters():
    global toggle
    global filters_frame
    if toggle == 1:
        toggle = toggle - 1
        filters_frame = Frame(root, bg="gray")
        filters_frame.grid(row=1, column=0, columnspan=3, rowspan=3)
        lbl = Label(filters_frame, text="Filters", font=("Doppio One", 16), bg="gray")
        lbl.grid(row=0, column=0, columnspan=3)
        genre_lbl = Label(filters_frame, text="Genre", font=("Doppio One", 16))
        genre_lbl.grid(row=1, column=0)
        year_lbl = Label(filters_frame, text="Release year", font=("Doppio One", 16))
        year_lbl.grid(row=1, column=1)
        rating_lbl = Label(filters_frame, text="Rating", font=("Doppio One", 16))
        rating_lbl.grid(row=1, column=2)
        # Genre buttons
        action_btn = Radiobutton(filters_frame, text="Action", variable=genre, value="action", font=("Doppio One", 16),
                                 bg="gray", indicatoron=False)
        action_btn.grid(row=2, column=0, ipadx=24, pady=1, padx=10)
        drama_btn = Radiobutton(filters_frame, text="Drama", variable=genre, value="drama", font=("Doppio One", 16),
                                bg="gray", indicatoron=False)
        drama_btn.grid(row=3, column=0, ipadx=23, pady=1)
        sci_fi_btn = Radiobutton(filters_frame, text="Sci-Fi", variable=genre, value="sci-fi", font=("Doppio One", 16),
                                 bg="gray", indicatoron=False)
        sci_fi_btn.grid(row=4, column=0, ipadx=29, pady=1)
        romance_btn = Radiobutton(filters_frame, text="Romance", variable=genre, value="romance",
                                  font=("Doppio One", 16), bg="gray", indicatoron=False)
        romance_btn.grid(row=5, column=0, ipadx=11, pady=1)
        horror_btn = Radiobutton(filters_frame, text="Horror", variable=genre, value="horror", font=("Doppio One", 16),
                                 bg="gray", indicatoron=False)
        horror_btn.grid(row=6, column=0, ipadx=24, pady=1)
        crime_btn = Radiobutton(filters_frame, text="Crime", variable=genre, value="crime", font=("Doppio One", 16),
                                bg="gray", indicatoron=False)
        crime_btn.grid(row=7, column=0, ipadx=27, pady=1)
        # Year buttons
        year_2022_lbl = Radiobutton(filters_frame, text="2022", variable=year, value="2022",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2022_lbl.grid(row=2, column=1, ipadx=9, padx=10)
        year_2021_lbl = Radiobutton(filters_frame, text="2021", variable=year, value="2021",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2021_lbl.grid(row=3, column=1, ipadx=11)
        year_2020_lbl = Radiobutton(filters_frame, text="2020", variable=year, value="2020",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2020_lbl.grid(row=4, column=1, ipadx=8)
        year_2019_lbl = Radiobutton(filters_frame, text="2019", variable=year, value="2019",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2019_lbl.grid(row=5, column=1, ipadx=11)
        year_2018_lbl = Radiobutton(filters_frame, text="2018", variable=year, value="2018",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2018_lbl.grid(row=6, column=1, ipadx=11)
        year_2017_lbl = Radiobutton(filters_frame, text="2017", variable=year, value="2017",
                                    font=("Doppio One", 16), bg="gray", indicatoron=False)
        year_2017_lbl.grid(row=7, column=1, ipadx=12)
        # Rating buttons
        rate_10 = Radiobutton(filters_frame, text="10", variable=rating, value="10", font=("Doppio One", 16),
                              bg="gray", indicatoron=False)
        rate_10.grid(row=2, column=2, padx=11, ipadx=5)
        rate_9 = Radiobutton(filters_frame, text="9", variable=rating, value="9", font=("Doppio One", 16),
                             bg="gray", indicatoron=False)
        rate_9.grid(row=3, column=2, ipadx=10)
        rate_8 = Radiobutton(filters_frame, text="8", variable=rating, value="8", font=("Doppio One", 16),
                             bg="gray", indicatoron=False)
        rate_8.grid(row=4, column=2, ipadx=9)
        rate_7 = Radiobutton(filters_frame, text="7", variable=rating, value="7", font=("Doppio One", 16),
                             bg="gray", indicatoron=False)
        rate_7.grid(row=5, column=2, ipadx=10)
        rate_6 = Radiobutton(filters_frame, text="6", variable=rating, value="6", font=("Doppio One", 16),
                             bg="gray", indicatoron=False)
        rate_6.grid(row=6, column=2, ipadx=10)
        rate_5 = Radiobutton(filters_frame, text="5", variable=rating, value="5", font=("Doppio One", 16),
                             bg="gray", indicatoron=False)
        rate_5.grid(row=7, column=2, ipadx=11)

    else:
        filters_frame.destroy()
        toggle = toggle + 1


# Top menu frame
top_menu = Frame(root, bg="gray")
top_menu.grid(row=0, column=0, columnspan=3, sticky=NSEW, ipadx=10, ipady=10)
top_menu.grid_columnconfigure(1, weight=1)
top_menu.grid_columnconfigure(2, weight=1)
top_menu.grid_rowconfigure(0, weight=1)

search_bar = Entry(top_menu, textvariable=search, font=("Doppio One", 16), borderwidth=5)
search_bar.grid(row=0, column=0, sticky=W, padx=15)
search_bar.bind("<FocusIn>", focus_in)
search_bar.bind("<FocusOut>", focus_out)
search_btn = Button(top_menu, text="Search", font=("Doppio One", 15), bg="orange", fg="black")
search_btn.grid(row=0, column=1, sticky=W)
advanced_search_btn = Button(top_menu, text="Advanced search", font=("Doppio One", 16), bg="orange", fg="black",
                             command=filters)
advanced_search_btn.grid(row=0, column=2, sticky=E, padx=15)

# Main frame
main_frame = Frame(root, bg="blue")
main_frame.grid(row=1, column=0, columnspan=3, sticky=NSEW)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)


upcoming_lbl = Label(main_frame, text="Upcoming movies in 2022", font=("Doppio One", 22, "bold"), bg="#121212",
                     fg="orange")
upcoming_lbl.grid(row=0, column=0, columnspan=3, pady=15)
action_lbl = Label(main_frame, text="Action", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
action_lbl.grid(row=1, column=0, ipadx=15, ipady=6, pady=(20, 0))
horror_lbl = Label(main_frame, text="Horror", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
horror_lbl.grid(row=1, column=1, ipadx=15, ipady=6, pady=(20, 0))
drama_lbl = Label(main_frame, text="Drama", font=("Doppio One", 20, "bold"), bg="orange", fg="#121212")
drama_lbl.grid(row=1, column=2, ipadx=15, ipady=6, pady=(20, 0))


root.mainloop()
