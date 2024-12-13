from tkinter import *
from submit import *

class Gui:
    """
    This is the GUI used to input letter grades which then determines the overall
    GPA of a person
    """
    def __init__(self, window):
        """
        Initializes GUI layout

        :param window: Tkinter window to display the GUI
        """
        self.window = window

        # Name input
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.input_name = Entry(self.frame_name)

        self.label_name.pack(side='left')
        self.input_name.pack(padx=11, side='left')
        self.frame_name.pack(anchor='w', padx=10, pady=10)

        # Letter grade for math input
        self.frame_math = Frame(self.window)
        self.label_math = Label(self.frame_math, text='Math')
        self.input_math = Entry(self.frame_math)

        self.label_math.pack(side='left')
        self.input_math.pack(padx=16, side='left')
        self.frame_math.pack(anchor='w', padx=10, pady=10)

        # Letter grade for science input
        self.frame_science = Frame(self.window)
        self.label_science = Label(self.frame_science, text='Science')
        self.input_science = Entry(self.frame_science)

        self.label_science.pack(side='left')
        self.input_science.pack(padx=5, side='left')
        self.frame_science.pack(anchor='w', padx=10, pady=10)

        # Letter grade for history input
        self.frame_history = Frame(self.window)
        self.label_history = Label(self.frame_history, text='History')
        self.input_history = Entry(self.frame_history)

        self.label_history.pack(side='left')
        self.input_history.pack(padx=7, side='left')
        self.frame_history.pack(anchor='w', padx=10, pady=10)

        # Letter grade for english input
        self.frame_english = Frame(self.window)
        self.label_english = Label(self.frame_english, text='English')
        self.input_english = Entry(self.frame_english)

        self.label_english.pack(side='left')
        self.input_english.pack(padx=7, side='left')
        self.frame_english.pack(anchor='w', padx=10, pady=10)

        # Button used to save the information to data.csv file
        self.save_button = Button(self.window, text='SAVE', command=self.submit)
        self.save_button.pack(pady=10)

        # Message label to let user know somthing has gone wrong
        self.mes_label = Label(self.window, text='')
        self.mes_label.pack()

        # Instruction label
        self.ins_label = Label(self.window, text='Make sure to put in letter grades')
        self.ins_label.pack()

        # Instruction label
        self.ins2_label = Label(self.window, text='Put NA if you do not have that class')
        self.ins2_label.pack()

        # Label to show GPA and changes once saved
        self.gpa_label = Label(self.window, text='GPA: NA')
        self.gpa_label.pack(pady=10)

    def submit(self):
        """
        Used for submit.py
        :return: None
        """
        submit(self)