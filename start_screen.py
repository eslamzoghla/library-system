from tkinter import *


class start_screen(Frame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        app.setSize(900, 800)
        self.backImage = PhotoImage(file="images\\back7.gif")
        self.buttonImage1 = PhotoImage(file='images\\button1.png')
        self.buttonImage2 = PhotoImage(file='images\\button2.png')
        self.buttonImage3 = PhotoImage(file='images\\button3.png')
        self.buttonImage4 = PhotoImage(file='images\\button4.png')
        self.exitButton = PhotoImage(file="images\\exit.png")
        self.initGUI()

    def initGUI(self):
        ##############################    many Constants    ##############################
        padxValue = 10
        padyValue = 10
        entryWidth = 300

        ##############################    Fonts    ##############################
        fontStyle = ('Arial', 18, 'bold')
        fontTop = ('Bellota', 40, 'bold')
        # Edwardian Script ITC
        buttonColor = 'white'
        labelColor = "slategrey"

        ##############################    Containers    ##############################
        containerout1 = Canvas(self, width=900, height=800)
        containerout1.pack(fill=BOTH, expand=True)
        containerout1.create_image(0, 0, image=self.backImage, anchor="nw")

        containerout2 = Canvas(self, width=547, height=617, background='slategrey')
        containerout2.pack(fill=BOTH, expand=True)
        containerout1.create_window(450, 400, window=containerout2)

        container = Canvas(self, width=530, height=600, background='slategray')
        container.pack(fill=BOTH, expand=True)
        containerout2.create_window(275, 310, window=container)

        container.create_text(27 * padxValue, 4 * padyValue, justify='center', text="BFCAI library", font=fontTop,
                              fill='white', )

        ##############################    Buttons    #################################
        book_registration_button = Button(container, image=self.buttonImage1, anchor='center', border=0, relief='flat',
                                          command=lambda: self.app.goToScreen(BookRegistration))
        container.create_window(270, 15 * padyValue, anchor='center', window=book_registration_button)

        book_record_button = Button(container, image=self.buttonImage2, anchor='center', border=0, relief='flat',
                                    command=lambda: self.app.goToScreen(BookRecord))
        container.create_window(270, 25 * padyValue, anchor='center', window=book_record_button)

        student_registration_button = Button(container, image=self.buttonImage3, anchor='center', border=0,
                                             relief='flat', command=lambda: self.app.goToScreen(StudentRegistration))
        container.create_window(270, 35 * padyValue, anchor='center', window=student_registration_button)

        student_record_button = Button(container, image=self.buttonImage4, anchor='center', border=0, relief='flat',
                                       command=lambda: self.app.goToScreen(StudentRecord))
        container.create_window(270, 45 * padyValue, anchor='center', window=student_record_button)

        student_record_button = Button(container, image=self.exitButton, anchor='center', border=0, relief='flat',
                                       command=lambda: self.app.destroy())
        container.create_window(270, 55 * padyValue, anchor='center', window=student_record_button)


from bookregistration import BookRegistration
from bookrecord import BookRecord
from studentregistration import StudentRegistration
from studentrecord import StudentRecord
