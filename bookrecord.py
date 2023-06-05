from tkinter import *
from tkinter import messagebox, ttk
import backend as db


class BookRecord(Frame):
    showboolean = 0

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        app.setSize(900, 800)
        self.backImage = PhotoImage(file="images\\back1.gif")
        self.backButton = PhotoImage(file="images\\backbutton1.png")
        self.showButton = PhotoImage(file="images\\show.png")
        self.updateButton = PhotoImage(file="images\\update.png")
        self.deleteButton = PhotoImage(file="images\\delete.png")
        self.searchButton = PhotoImage(file="images\\search.png")
        self.initGui()

    def show_date(self):
        self.table
        self.table.delete(*self.table.get_children())
        data = db.get_book_data()
        for date in data:
            self.table.insert('', END, values=date)

    def initGui(self):
        ##############################    many Constants    #######################
        padxValue = 10
        padyValue = 10
        entryWidth = 300

        ##############################    Fonts    ##############################
        fontStyle = ('Arial', 16)
        fontTop = ('Arial', 20, 'bold')
        entryColor = 'lightgray'
        buttonColor = 'darkgoldenrod'
        labelColor = "white"

        ##############################    Containers    ##############################
        containerout = Canvas(self, width=700, height=900)
        containerout.pack(fill=BOTH, expand=True, ipadx=100)
        containerout.create_image(0, 0, image=self.backImage, anchor="nw")

        container_middle = Canvas(containerout, width=600, height=900, background='slategray', relief=RIDGE)
        container_middle.pack(pady=50)

        container = Canvas(container_middle, width=640, height=650, relief=RIDGE, background='slategray')
        container.pack(side=LEFT, padx=8, pady=8)
        ##############################    Labels & Entires    ##############################

        # Label title
        container.create_text(30 * padxValue, 4 * padyValue, justify='center', text='Book Record', font=fontTop,
                              fill=labelColor)

        # label and entry of Book Name
        container.create_text(5 * padxValue, 10 * padyValue, text='Book name', font=fontStyle, fill=labelColor,
                              anchor='nw')
        book = db.get_book_data()
        l = []
        for i in book:
            l.append(i[1])

        self.enterBookname = ttk.Combobox(self, value=l, background=entryColor, width=30, state="readonly")

        container.create_window(20 * padxValue, 10 * padyValue, window=self.enterBookname, width=entryWidth,
                                anchor='nw')

        # label and entry of Author
        container.create_text(5 * padxValue, 15 * padyValue, justify='left', text='Author', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterAuthor = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 15 * padyValue, window=self.enterAuthor, width=entryWidth, anchor='nw')

        # label and entry of Category
        container.create_text(5 * padxValue, 20 * padyValue, justify='left', text='Category', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterCategory = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 20 * padyValue, window=self.enterCategory, width=entryWidth,
                                anchor='nw')

        # label and entry of Data of Book Version
        container.create_text(5 * padxValue, 25 * padyValue, justify='left', text='Book Version', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterBookVersion = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 25 * padyValue, window=self.enterBookVersion, width=entryWidth,
                                anchor='nw')

        # label and entry of Release Book
        container.create_text(5 * padxValue, 30 * padyValue, justify='left', text='Release Book', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterReleaseBook = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 30 * padyValue, window=self.enterReleaseBook, width=entryWidth,
                                anchor='nw')

        # label and entry of Pages
        container.create_text(5 * padxValue, 35 * padyValue, justify='left', text='Pages', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterPages = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 35 * padyValue, window=self.enterPages, width=entryWidth, anchor='nw')

        # label and entry of Copies
        container.create_text(5 * padxValue, 40 * padyValue, justify='left', text='Copies', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterCopies = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 40 * padyValue, window=self.enterCopies, width=entryWidth, anchor='nw')

        # label and entry of Book Shelf
        container.create_text(5 * padxValue, 45 * padyValue, justify='left', text='Book Shelf', font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enterBookShelf = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 45 * padyValue, window=self.enterBookShelf, width=entryWidth,
                                anchor='nw')

        #####################################    function    #################################
        # Return select row from table

        def table_row_click():
            try:
                self.clear_enteries()
                (id, book_name, author, category, book_version, release_date, pages, copy, book_shelf, note) = \
                self.table.item(self.table.focus())['values']
                # self.enterId.insert(0, id)
                self.enterBookname.set(book_name)
                self.enterAuthor.insert(0, author)
                self.enterCategory.insert(0, category)
                self.enterBookVersion.insert(0, book_version)
                self.enterReleaseBook.insert(0, release_date)
                self.enterPages.insert(0, pages)
                self.enterCopies.insert(0, copy)
                self.enterBookShelf.insert(0, book_shelf)
            except:
                x = ""

        def ClickOnCombo(*args):
            self.clear_enteries()
            name = self.enterBookname.get()
            book = db.search_book_data(name)
            self.enterAuthor.insert(0, str(book[0][2]))
            self.enterCategory.insert(0, str(book[0][3]))
            self.enterBookVersion.insert(0, str(book[0][4]))
            self.enterReleaseBook.insert(0, str(book[0][5]))
            self.enterPages.insert(0, str(book[0][6]))
            self.enterCopies.insert(0, str(book[0][7]))
            self.enterBookShelf.insert(0, str(book[0][8]))

        self.enterBookname.bind("<<ComboboxSelected>>", ClickOnCombo)

        def ClickUpdate():
            try:

                book_name = self.enterBookname.get()
                author = self.enterAuthor.get()
                category = self.enterCategory.get()
                book_version = self.enterBookVersion.get()
                release_date = self.enterReleaseBook.get()
                pages = int(self.enterPages.get())
                copy = int(self.enterCopies.get())
                book_shelf = int(self.enterBookShelf.get())
                if (book_name) and (author) and (category) and (book_version) and (release_date) and (
                        pages) and (copy) and (book_shelf):
                    db.update_book(book_name, author, category, book_version, release_date, pages, copy, book_shelf)
                    messagebox.showinfo(message='Data update in database')
                    if self.showboolean == 1:
                        self.show_date()
                else:
                    messagebox.showerror(message="Please enter data")
            except:
                messagebox.showerror(message='Invalid Data')

        def ClickDelete():
            try:
                book_name = self.enterBookname.get()

                if book_name != None:

                    db.delete_book(book_name)
                    if self.showboolean == 1:
                        self.show_date()
                    self.clear_enteries()
                    messagebox.showinfo(message='Data delete from database')
                else:
                    messagebox.showerror(message="Please enter book")
                book = db.get_book_data()
                l = []
                for i in book:
                    l.append(i[1])
                self.enterBookname['values'] = l
                self.enterBookname.set("")
                self.enterBookname.delete(0, "end")
            except:
                messagebox.showerror('Invalid Data')

        def ClickShow():

            self.showboolean += 1
            if self.showboolean == 1:
                ################################# Table ###################################
                self.app.setSize(1600, 750)
                container_right = Canvas(container_middle, relief=RIDGE, background='slategray')
                container_right.pack(side=RIGHT, padx=8, pady=8, fill=BOTH, expand=True)

                # create Scroll bar
                xscroll = Scrollbar(container_right, orient=HORIZONTAL)
                xscroll.pack(side=BOTTOM, fill=X)
                yscroll = Scrollbar(container_right, orient=VERTICAL)
                yscroll.pack(side=RIGHT, fill=Y)

                self.table = ttk.Treeview(container_right, columns=(
                    'id', 'name', 'author', 'category', 'version', 'release_date', 'pages', 'copy', 'book_shelf',
                    'notes'),
                                          show='headings')
                self.table.pack(fill=BOTH, expand=True)

                # column name
                self.table.heading('id', text='ID')
                self.table.heading('name', text='Book name')
                self.table.heading('author', text='Author')
                self.table.heading('category', text='Category')
                self.table.heading('version', text='Book version')
                self.table.heading('release_date', text='Release date')
                self.table.heading('pages', text='Pages')
                self.table.heading('copy', text='Copy')
                self.table.heading('book_shelf', text='Book shelf')
                self.table.heading('notes', text='Notes')

                # Column width
                self.table.column('id', width=20, anchor='center')
                self.table.column('name', width=100, anchor='center')
                self.table.column('author', width=60, anchor='center')
                self.table.column('category', width=120, anchor='center')
                self.table.column('version', width=75, anchor='center')
                self.table.column('release_date', width=80, anchor='center')
                self.table.column('pages', width=40, anchor='center')
                self.table.column('copy', width=40, anchor='center')
                self.table.column('book_shelf', width=65, anchor='center')
                self.table.column('notes', width=120, anchor='center')

                # Scroll conf
                xscroll.configure(command=self.table.xview)
                yscroll.configure(command=self.table.yview)
                self.table.configure(xscrollcommand=xscroll.set)
                self.table.configure(yscrollcommand=yscroll.set)

                self.table.bind('<ButtonRelease-1>', lambda e: table_row_click())
                self.show_date()
            else:
                messagebox.showinfo(message='Sorry, Table is already shown')

        #########################################     Button    ###########################################
        # Back Button
        BackButton = Button(self, image=self.backButton, anchor='center', relief='flat', border=0,
                            command=lambda: self.app.goToScreen(start_screen))
        container.create_window(22, 28, anchor='center', window=BackButton)

        # show Button
        showButton = Button(self, image=self.showButton, anchor='center', relief='flat', border=0,
                            command=lambda: ClickShow())
        container.create_window(125, 57 * padyValue, anchor='center', window=showButton)

        # update Button
        updateButton = Button(self, image=self.updateButton, anchor='center', relief='flat', border=0,
                              command=lambda: ClickUpdate())
        container.create_window(325, 57 * padyValue, anchor='center', window=updateButton)

        # delete Button
        deleteButton = Button(self, image=self.deleteButton, anchor='center', relief='flat', border=0,
                              command=lambda: ClickDelete())
        container.create_window(525, 57 * padyValue, anchor='center', window=deleteButton)

    def clear_enteries(self):

        self.enterAuthor.delete(0, END)
        self.enterCategory.delete(0, END)
        self.enterBookVersion.delete(0, END)
        self.enterReleaseBook.delete(0, END)
        self.enterPages.delete(0, END)
        self.enterCopies.delete(0, END)
        self.enterBookShelf.delete(0, END)


from start_screen import start_screen
