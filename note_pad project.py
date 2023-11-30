from tkinter import*

# Create the main window
root = Tk()
root.title("Note Pad App By Abass.")

# Create a text area
text_area = Text(root)
text_area.pack()

# Create a menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create a file menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add options to the file menu
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create an edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add options to the edit menu
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")

# Create a help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add options to the help menu
help_menu.add_command(label="About")

# create contact us menu
contact_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="contact us", menu=contact_menu)

# Add function to the contact us menu
contact_menu.add_command(label="phone number: 09161200351")
contact_menu.add_command(label="Gmail address: muhammedabass757@gmail.com")


root.mainloop()

