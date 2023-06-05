from tkinter import *
from tkinter import messagebox, ttk
import backend as db
from datetime import *


class StudentRecord(Frame):
    showboolean = 0

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.backImage = PhotoImage(file="images\\back1.gif")
        self.backbutton = PhotoImage(file="images\\backbutton1.png")
        self.showButton = PhotoImage(file="images\\show.png")
        self.updateButton = PhotoImage(file="images\\update.png")
        self.deleteButton = PhotoImage(file="images\\delete.png")
        self.searchButton = PhotoImage(file="images\\search.png")
        self.init_gui()

    def show_date(self):
        self.table.delete(*self.table.get_children())
        data = db.get_student_data()
        for date in data:
            self.table.insert('', END, values=date)

    def clear_enteries(self):
        self.enter_id.delete(0, END)
        self.enter_name.delete(0, END)
        self.enter_academic_year.delete(0, END)
        self.enter_phone.delete(0, END)
        self.enter_book.delete(0, END)

    def init_gui(self):
        ##############################    many Constants    ##############################
        padxValue = 10
        padyValue = 10
        entryWidth = 280

        ##############################    Fonts    ##############################
        fontStyle = ('Arial', 16)
        fontTop = ('Arial', 20, 'bold')
        entryColor = 'lightgray'
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
        container.create_text(30 * padxValue, 4 * padyValue, justify='center', text="Student Record", font=fontTop,
                              fill=labelColor, )

        # label and entry of ID
        container.create_text(5 * padxValue, 10 * padyValue, text="ID", font=fontStyle, fill=labelColor, anchor='nw')
        self.enter_id = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 10 * padyValue, window=self.enter_id, width=entryWidth, anchor='nw')

        # label and entry of name
        container.create_text(5 * padxValue, 15 * padyValue, text="Name", font=fontStyle, fill=labelColor, anchor='nw')
        self.enter_name = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 15 * padyValue, window=self.enter_name, width=entryWidth, anchor='nw')

        # label and entry of Author
        container.create_text(5 * padxValue, 20 * padyValue, justify='left', text="Academic year", font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enter_academic_year = Entry(self, background=entryColor, width=40)
        container.create_window(20 * padxValue, 20 * padyValue, window=self.enter_academic_year, width=entryWidth,
                                anchor='nw')
        self.combo1 = ttk.Combobox(self.enter_academic_year, value=('1st year', '2st year', '3rd year', '4th year'),
                                   state='readonly', width=43)
        self.combo1.place(x=0, y=0)
        # label and entry of category
        container.create_text(5 * padxValue, 25 * padyValue, justify='left', text="Phone", font=fontStyle,
                              fill=labelColor, anchor='nw')
        self.enter_phone = Entry(self, background=entryColor, width=40)
        container.create_window(20 * padxValue, 25 * padyValue, window=self.enter_phone, width=entryWidth, anchor='nw')

        # label and entry of Data of purchase
        container.create_text(5 * padxValue, 30 * padyValue, justify='left', text="Book name", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        book = db.get_book_data()
        l = []
        for i in book:
            l.append(i[1])
        self.enter_book = ttk.Combobox(self, values=l, background=entryColor, width=40, state="readonly")
        container.create_window(20 * padxValue, 30 * padyValue, window=self.enter_book, width=entryWidth, anchor='nw')
        # label and entry of roof
        container.create_text(5 * padxValue, 35 * padyValue, justify='left', text="Reg. date", font=fontStyle,
                              fill=labelColor, anchor='nw')

        # label and entry of Pages
        container.create_text(5 * padxValue, 40 * padyValue, justify='left', text="Return date", font=fontStyle,
                              fill=labelColor, anchor='nw')

        #####################################    function    #################################

        def table_row_click():
            try:
                Values = self.table.item(self.table.focus(), 'values')
                self.clear_enteries()
                self.enter_id.insert(0, Values[0])
                self.enter_name.insert(0, Values[1])
                self.combo1.set(Values[2])
                self.enter_phone.insert(0, Values[3])
                dates = str(Values[5])
                self.enter_today_date = Label(self, text=Values[4], foreground='black', background='slategrey',
                                              width=40,
                                              font=fontStyle)
                container.create_window(20 * padxValue, 35 * padyValue, window=self.enter_today_date,
                                        width=entryWidth, anchor='nw')
                if dates <= str(date.today()):
                    self.enter_return_date = Label(self, text=dates, background='slategrey', font=fontStyle,
                                                   foreground='red', width=40)
                    container.create_window(20 * padxValue, 40 * padyValue, window=self.enter_return_date,
                                            width=entryWidth,
                                            anchor='nw')
                else:
                    self.enter_return_date = Label(self, text=dates, background='slategrey', font=fontStyle,
                                                   width=40)
                    container.create_window(20 * padxValue, 40 * padyValue, window=self.enter_return_date,
                                            width=entryWidth,
                                            anchor='nw')
                self.enter_book.set(Values[6])
            except:
                x = ""

        def ClickUpdate():
            try:
                Id = int(self.enter_id.get())
                name = self.enter_name.get()
                Academic = self.combo1.get()
                Phone = self.enter_phone.get()
                Bookname = self.enter_book.get()
                if (Id) and (name) and (Academic) and (Phone) and (Bookname):
                    db.updata_student(Id, name, Academic, Phone, Bookname)
                    if self.showboolean == 1:
                        self.show_date()
                    messagebox.showinfo(message='Data is Updated in database')
                else:
                    messagebox.showerror(message="Please enter data")
            except:
                messagebox.showerror(message='Invalid!')

        def ClickDelete():
            try:
                id = int(self.enter_id.get())
                if id:
                    id = self.enter_id.get()
                    db.delete_student(id)
                    if self.showboolean == 1:
                        self.show_date()
                    messagebox.showinfo(message='Data is deleted from database')
                    self.clear_enteries()
                    self.combo1.set("")
                    self.enter_book.set("")
                else:
                    messagebox.showerror(message="Please enter id")
            except:
                messagebox.showerror('Invalid!')

        def ClickSearch():
            try:
                ida = int(self.enter_id.get())
                self.clear_enteries()
                if ida:
                    # ida = int(self.enter_id.get())
                    book = db.search_student_data(ida)
                    # book = db.get_student_data()
                    self.enter_id.insert(0, str(book[0][0]))
                    self.enter_name.insert(0, str(book[0][1]))
                    self.combo1.set(str(book[0][2]))
                    self.enter_phone.insert(0, str(book[0][3]))
                    dates = str(book[0][5])
                    self.enter_today_date = Label(self, text=str(book[0][4]), foreground='black',
                                                  background='slategrey', width=40,
                                                  font=fontStyle)
                    container.create_window(20 * padxValue, 35 * padyValue, window=self.enter_today_date,
                                            width=entryWidth, anchor='nw')
                    if dates <= str(date.today()):
                        self.enter_return_date = Label(self, text=dates, background='slategrey', font=fontStyle,
                                                       foreground='red', width=40)
                        container.create_window(20 * padxValue, 40 * padyValue, window=self.enter_return_date,
                                                width=entryWidth,
                                                anchor='nw')
                    else:
                        self.enter_return_date = Label(self, text=dates, background='slategrey', font=fontStyle,
                                                       width=40)
                        container.create_window(20 * padxValue, 40 * padyValue, window=self.enter_return_date,
                                                width=entryWidth,
                                                anchor='nw')
                    self.enter_book.set(str(book[0][6]))
                    messagebox.showinfo(message='Data was searched in database')
                    self.enter_book.current()
                    # self.clear_enteries()
                else:
                    messagebox.showerror(message="Please enter data")
            except:
                messagebox.showerror(message='Invalid !')

        def ClickShow():
            self.app.setSize(1400, 750)
            self.showboolean += 1
            if self.showboolean == 1:
                table_container = Canvas(container_middle, relief=RIDGE, background='slategray')
                table_container.pack(side=RIGHT, padx=8, pady=8, fill=BOTH, expand=True)

                xscroll = Scrollbar(table_container, orient=HORIZONTAL)
                xscroll.pack(side=BOTTOM, fill=X)
                yscroll = Scrollbar(table_container, orient=VERTICAL)
                yscroll.pack(side=RIGHT, fill=Y)

                # Column names
                self.table = ttk.Treeview(table_container, height=7, columns=(
                    'id', 'name', 'academic', 'phone', 'today_date', 'return_date', 'book_name'),
                                          show='headings', selectmode='browse')
                self.table.pack(fill=BOTH, expand=True)

                # column name
                self.table.heading('id', text='ID')
                self.table.heading('name', text='Student name')
                self.table.heading('academic', text='Academic')
                self.table.heading('phone', text='Phone')
                self.table.heading('today_date', text='Today date')
                self.table.heading('return_date', text='Return date')
                self.table.heading('book_name', text='Book name')

                # Column width
                self.table.column('id', width=80, anchor='center')
                self.table.column('name', width=100, anchor='center')
                self.table.column('academic', width=70, anchor='center')
                self.table.column('phone', width=120, anchor='center')
                self.table.column('today_date', width=80, anchor='center')
                self.table.column('return_date', width=80, anchor='center')
                self.table.column('book_name', width=140, anchor='center')

                # Scroll conf
                xscroll.configure(command=self.table.xview)
                yscroll.configure(command=self.table.yview)
                self.table.configure(xscrollcommand=xscroll.set)
                self.table.configure(yscrollcommand=yscroll.set)

                self.table.bind('<ButtonRelease-1>', lambda e: table_row_click())
                self.show_date()
            else:
                messagebox.showinfo(message='Sorry, Table is already shown')

        # Back Button
        backButton = Button(self, image=self.backbutton, anchor='center', relief='flat', border=0,
                            command=lambda: self.app.goToScreen(start_screen))
        container.create_window(22, 28, anchor='center', window=backButton)

        # show Button
        showButton = Button(self, image=self.showButton, anchor='center', relief='flat', border=0,
                            command=lambda: ClickShow())
        container.create_window(125, 53 * padyValue, anchor='center', window=showButton)

        # update Button
        updateButton = Button(self, image=self.updateButton, anchor='center', relief='flat', border=0,
                              command=lambda: ClickUpdate())
        container.create_window(325, 53 * padyValue, anchor='center', window=updateButton)

        # delete Button
        deleteButton = Button(self, image=self.deleteButton, anchor='center', relief='flat', border=0,
                              command=lambda: ClickDelete())
        container.create_window(525, 53 * padyValue, anchor='center', window=deleteButton)

        # Search Button
        searchButton = Button(self, image=self.searchButton, border=0, command=lambda: ClickSearch())
        container.create_window(550, 11 * padyValue, anchor='center', window=searchButton)


from start_screen import start_screen
