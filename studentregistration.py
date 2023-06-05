from tkinter import *
from tkinter import ttk, messagebox
import backend as db
from datetime import *


class StudentRegistration(Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.backImage = PhotoImage(file="images\\back7.gif")
        self.backButton = PhotoImage(file="images\\backbutton1.png")
        self.insertButton = PhotoImage(file="images\\insert.png")
        self.init_gui()

    def init_gui(self):
        ##############################    many Constants    ##############################
        padxValue = 10
        padyValue = 10
        entryWidth = 280

        ##############################    Fonts    ##############################
        fontStyle = ('Arial', 16)
        fontTop = ('Arial', 20, 'bold')
        entryColor = 'lightgray'
        buttonColor = 'slategrey'
        labelColor = "white"

        ##############################    Containers    ##############################
        containerout1 = Canvas(self, width=900, height=800)
        containerout1.pack(fill=BOTH, expand=True)
        containerout1.create_image(0, 0, image=self.backImage, anchor="nw")

        containerout2 = Canvas(self, width=657, height=617, background='slategrey')
        containerout2.pack(fill=BOTH, expand=True)
        containerout1.create_window(450, 400, window=containerout2)

        container = Canvas(self, width=640, height=600, background='slategray')
        container.pack(fill=BOTH, expand=True)
        containerout2.create_window(330, 310, window=container)
        ##############################    Labels & Entires    ##############################
        # Label title
        container.create_text(35 * padxValue, 4 * padyValue, justify='center', text="Student Registration",
                              font=fontTop,
                              fill=labelColor, )

        # label and entry of ID
        container.create_text(5 * padxValue, 10 * padyValue, text="ID", font=fontStyle, fill=labelColor, anchor='nw')
        enter_id = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 10 * padyValue, window=enter_id, width=entryWidth, anchor='nw')

        # label and entry of name
        container.create_text(5 * padxValue, 15 * padyValue, text="Name", font=fontStyle, fill=labelColor, anchor='nw')
        enter_name = Entry(self, background=entryColor, width=30)
        container.create_window(20 * padxValue, 15 * padyValue, window=enter_name, width=entryWidth, anchor='nw')

        # label and entry of Author
        container.create_text(5 * padxValue, 20 * padyValue, justify='left', text="Academic year", font=fontStyle,
                              fill=labelColor, anchor='nw')
        enter_academic_year = Entry(self, background=entryColor, width=40)
        container.create_window(20 * padxValue, 20 * padyValue, window=enter_academic_year, width=entryWidth,
                                anchor='nw')
        combo1 = ttk.Combobox(enter_academic_year, value=('1st year', '2st year', '3rd year', '4th year'),
                              state='readonly', width=43)
        combo1.place(x=0, y=0)

        # label and entry of category
        container.create_text(5 * padxValue, 25 * padyValue, justify='left', text="Phone", font=fontStyle,
                              fill=labelColor, anchor='nw')
        enter_phone = Entry(self, background=entryColor, width=40)
        container.create_window(20 * padxValue, 25 * padyValue, window=enter_phone, width=entryWidth, anchor='nw')

        # label and entry of Data of purchase
        container.create_text(5 * padxValue, 30 * padyValue, justify='left', text="Book name", font=fontStyle,
                              fill=labelColor,
                              anchor='nw')
        book = db.get_book_data()
        l = []
        for i in book:
            l.append(i[1])
        enter_book = ttk.Combobox(self, values=l, background=entryColor, width=40, state="readonly")
        container.create_window(20 * padxValue, 30 * padyValue, window=enter_book, width=entryWidth, anchor='nw')

        # label and entry of roof
        container.create_text(5 * padxValue, 35 * padyValue, justify='left', text="Reg. date", font=fontStyle,
                              fill=labelColor, anchor='nw')
        enter_today_date = Label(self, text=str(date.today()), background='slategrey', width=40, font=fontStyle)
        container.create_window(20 * padxValue, 35 * padyValue, window=enter_today_date, width=entryWidth, anchor='nw')

        # label and entry of Pages
        container.create_text(5 * padxValue, 40 * padyValue, justify='left', text="Return date", font=fontStyle,
                              fill=labelColor, anchor='nw')
        enter_return_date = Label(self, text=str(date.today() + timedelta(days=7)), background='slategrey', width=40,
                                  font=fontStyle)
        container.create_window(20 * padxValue, 40 * padyValue, window=enter_return_date, width=entryWidth, anchor='nw')

        # Function to take data from entries and send to database
        def onClick():
            try:
                Id = int(enter_id.get())
                name = enter_name.get()
                Academic = combo1.get()
                Phone = enter_phone.get()
                Bookname = enter_book.get()
                TodayDate = str(date.today())
                returnDate = str(date.today() + timedelta(days=7))
                if (Id) and (name) and (Academic) and (Phone) and (Bookname):
                    db.add_student(Id, name, Academic, Phone, TodayDate, returnDate, Bookname)
                    messagebox.showinfo(message='Student was added in database')
                else:
                    messagebox.showerror(message="Please enter data")
            except:
                messagebox.showerror(message='Invalid Data')

        # insert Button
        insertButton = Button(self, image=self.insertButton, anchor='center', relief='flat', border=0,
                              command=lambda: onClick())
        container.create_window(320, 53 * padyValue, anchor='center', window=insertButton)

        # Back Button
        backButton = Button(self, image=self.backButton, anchor='center', relief='flat', border=0,
                            command=lambda: self.app.goToScreen(start_screen))
        container.create_window(22, 28, anchor='center', window=backButton)


from start_screen import start_screen
