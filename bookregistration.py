from queue import Empty
from tkinter import *
from tkinter import messagebox


class BookRegistration(Frame):
    def __init__(self, app):
        super().__init__()
        self.app = app
        app.setSize(900, 900)
        self.backImage = PhotoImage(file="images\\back7.gif")
        self.backButton = PhotoImage(file="images\\backbutton1.png")
        self.insertButton = PhotoImage(file="images\\insert.png")
        self.initGUI()

    def clear_enteries(self):
        self.enterBookname.delete(0, END)
        self.enterAuthor.delete(0, END)
        self.enterCategory.delete(0, END)
        self.enterBookVersion.delete(0, END)
        self.enterReleaseBook.delete(0, END)
        self.enterPages.delete(0, END)
        self.enterCopies.delete(0, END)
        self.enterBookShelf.delete(0, END)
        self.notes.delete("1.0", "end")

    def initGUI(self):
        ##############################    many Constants    ##############################
        padxValue = 10
        padyValue = 10
        entryWidth = 300
        ##############################    Fonts    ##############################
        fontStyle = ('Arial', 16)
        fontTop = ('Arial', 20, 'bold')
        entryColor = 'lightgray'
        labelColor = "white"

        ##############################    Containers    ##############################
        containerout1 = Canvas(self, width=900, height=1000)
        containerout1.pack(fill=BOTH, expand=True)
        containerout1.create_image(0, 0, image=self.backImage, anchor="nw")

        containerout2 = Canvas(self, width=547, height=817, background='slategrey')
        containerout2.pack(fill=BOTH, expand=True)
        containerout1.create_window(450, 450, window=containerout2)

        container = Canvas(self, width=530, height=800, background='slategrey')
        container.pack(fill=BOTH, expand=True)
        containerout2.create_window(275, 410, window=container)

        ##############################    Labels & Entry    ##############################
        # Label title
        container.create_text(28 * padxValue, 4 * padyValue, justify='center', text="Registration", font=fontTop,
                              fill=labelColor)

        # label and entry of Book name
        container.create_text(4 * padxValue, 10 * padyValue, text="Book name", font=fontStyle, fill=labelColor,
                              anchor='nw')
        self.enterBookname = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 10 * padyValue, window=self.enterBookname, width=entryWidth,
                                anchor='nw')

        # label and entry of Author
        container.create_text(4 * padxValue, 15 * padyValue, justify='left', text="Author", font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterAuthor = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 15 * padyValue, window=self.enterAuthor, width=entryWidth, anchor='nw')

        # label and entry of category
        container.create_text(4 * padxValue, 20 * padyValue, justify='left', text="Category", font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterCategory = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 20 * padyValue, window=self.enterCategory, width=entryWidth,
                                anchor='nw')

        # label and entry of Book version
        container.create_text(4 * padxValue, 25 * padyValue, justify='left', text="Book version", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.enterBookVersion = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 25 * padyValue, window=self.enterBookVersion, width=entryWidth,
                                anchor='nw')

        # label and entry of Release Date
        container.create_text(4 * padxValue, 30 * padyValue, justify='left', text="Release date", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.enterReleaseBook = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 30 * padyValue, window=self.enterReleaseBook, width=entryWidth,
                                anchor='nw')

        # label and entry of Book shelf
        container.create_text(4 * padxValue, 35 * padyValue, justify='left', text="Book shelf", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.enterBookShelf = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 35 * padyValue, window=self.enterBookShelf, width=entryWidth,
                                anchor='nw')

        # label and entry of Pages
        container.create_text(4 * padxValue, 40 * padyValue, justify='left', text="Pages", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.enterPages = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 40 * padyValue, window=self.enterPages, width=entryWidth, anchor='nw')

        # label and entry of copies
        container.create_text(4 * padxValue, 45 * padyValue, justify='left', text="Copy", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.enterCopies = Entry(self, background=entryColor, width=40)
        container.create_window(19 * padxValue, 45 * padyValue, window=self.enterCopies, width=entryWidth, anchor='nw')

        # Notes
        container.create_text(4 * padxValue, 50 * padyValue, justify='left', text="Notes", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        self.notes = Text(self, width=38, height=8)
        container.create_window(34 * padxValue, 57 * padyValue, window=self.notes)

        # Function to take data from entries and send to database
        def onClick_insert():
            try:
                book_name = self.enterBookname.get()
                author = self.enterAuthor.get()
                category = self.enterCategory.get()
                book_version = self.enterBookVersion.get()
                release_date = self.enterReleaseBook.get()
                pages = int(self.enterPages.get())
                copy = int(self.enterCopies.get())
                book_shelf = int(self.enterBookShelf.get())
                note = self.notes.get("1.0", 'end-1c')
                if (book_name) and (author) and (category) and (book_version) and (release_date) and (pages) and (
                copy) and (book_shelf):
                    # Calling database

                    db.add_book(book_name, author, category, book_version, release_date, pages, copy, book_shelf, note)
                    messagebox.showinfo(message='Data add to database')
                    self.clear_enteries()
                else:
                    messagebox.showerror(message='Please, enter data')
            except:
                messagebox.showerror(message='Invalid Data')

        # insert Button
        insertButton = Button(self, image=self.insertButton, border=0, command=lambda: onClick_insert())
        container.create_window(260, 75 * padyValue, anchor='center', window=insertButton)

        # Back Button
        backButton = Button(self, image=self.backButton, anchor='center', relief='flat', border=0,
                            command=lambda: self.app.goToScreen(start_screen))
        container.create_window(43, 28, anchor='e', window=backButton)


# import database file
import backend as db
from start_screen import start_screen
