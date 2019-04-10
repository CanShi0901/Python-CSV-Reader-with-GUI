# This program was created by Can Shi on March 20, 2019
# Assignment 4 19W_CST8333_350

import csv
import author
from Tkinter import *
import matplotlib.pyplot as plt


class ReadData(author.Author):
    """
    This class inherits from Author class and uses the name() method to get the author's name
    """
    filename = "Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv"
    records = []

    def __init__(self, master):
        """
        Calls init method in super class and change the first and last name to my real name
        """
        super(self.__class__, self).__init__("Can", "Shi")

        # Creates a main page with all buttons for user to choose different functions, and displays student's name
        master.title("Assignment 4 by " + self.name() + " 040806036")

        self.label = Label(master, text="Hello user! My name is " + self.name() + ".\n\nPlease choose an option below.")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        self.reload_button = Button(master, text="Reload CSV", command=self.read_csv)
        self.reload_button.pack()

        self.display_all_button = Button(master, text="Show all records in memory", command=self.show_all_records)
        self.display_all_button.pack()

        self.greet_button = Button(master, text="Display Student Name", command=self.display_student_name)
        self.greet_button.pack()

        self.new_rec_button = Button(master, text="Create New Record", command=self.new_record)
        self.new_rec_button.pack()

        self.del_rec_button = Button(master, text="Delete a Record", command=self.delete_record)
        self.del_rec_button.pack()

        self.edit_rec_button = Button(master, text="Edit a Record", command=self.edit_record)
        self.edit_rec_button.pack()

        self.graph_button = Button(master, text="Draw Graph", command=self.draw_graph)
        self.graph_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def new_record(self):
        """
        This method opens a new window,
        which allows user to input a value and save in the current array of strings
        """
        newwin = Toplevel(root)
        newwin.wm_title("New Record by Can Shi")
        show = Label(newwin, text="Please enter the value you want to be saved")
        show.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        entry = Entry(newwin)
        entry.pack()

        save_button = Button(newwin, text="Save", command=lambda: self.save(entry.get()))
        save_button.pack()

        back_button = Button(newwin, text="Back", command=newwin.destroy)
        back_button.pack()

    def draw_graph(self):
        """
        This method uses data in a csv file to draw a graphical plot
        """
        plant_id = []
        number_buds = []
        number_flowers = []
        with open(self.filename) as csvfile:
            next(csvfile)
            next(csvfile)
            plots = csv.reader(csvfile, delimiter=',')
            for column in plots:
                plant_id.append(int(column[2]))
                number_buds.append(int(column[3]))
                number_flowers.append(int(column[4]))

        plt.plot(plant_id, number_flowers, 'ro')
        plt.ylabel('Number of Flowers')
        plt.xlabel('Plant ID')

        plt.title('Can Shi used matplotlib to do this graph')
        plt.legend()
        plt.show()

    def delete_record(self):
        """
        This method opens a new window,
        which allows user to input a number and delete the string at that location from the array
        """
        newwin = Toplevel(root)
        newwin.wm_title("Delete Record by Can Shi")
        show = Label(newwin, text="Please enter the number of the record you want to delete"
                     + "Please choose a number between 0 and " + (len(ReadData.records) - 1).__str__())

        show.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        vcmd = (newwin.register(self.is_number))

        entry = Entry(newwin, validate='all', validatecommand=(vcmd, '%P'))
        entry.pack()

        delete_button = Button(newwin, text="Delete", command=lambda: self.delete(entry.get()))
        delete_button.pack()

        back_button = Button(newwin, text="Back", command=newwin.destroy)
        back_button.pack()

    def edit_record(self):
        """
        This method opens a new window,
        which allows user to input a number and index,
        then replace the value at index from array with new value entered by user
        """
        newwin = Toplevel(root)
        newwin.wm_title("Edit Record by Can Shi")
        show = Label(newwin, text="Please enter the number of the record you want to edit"
                     + "\nPlease choose a number between 0 and " + (len(ReadData.records) - 1).__str__())

        show.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        vcmd = (newwin.register(self.is_number))

        index_entry = Entry(newwin, validate='all', validatecommand=(vcmd, '%P'))
        index_entry.pack()

        data_show = Label(newwin, text="Please enter the new value to be replaced")

        data_show.pack(side="top", fill="both", expand=True, padx=100, pady=100)

        data_entry = Entry(newwin)
        data_entry.pack()

        edit_button = Button(newwin, text="Save Change", command=lambda: self.edit(index_entry.get(), data_entry.get()))
        edit_button.pack()

        back_button = Button(newwin, text="Back", command=newwin.destroy)
        back_button.pack()

    def is_number(self, P):
        """checks if entered value is a number instead of characters"""
        if str.isdigit(P) or P == '':
            return True
        else:
            return False

    def read_csv(self):
        """
        This function reads the first row, skips the second row,
        reads the next 10 rows of data from a csv file,
        then saves the 10 records in an array of strings
        """
        del ReadData.records[:]
        try:
            with open(ReadData.filename) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        print(row)
                        line_count += 1
                    elif line_count == 1:
                        next(csv_reader)
                        line_count += 1
                    elif line_count >= 12:
                        break
                    else:
                        print(row)
                        ReadData.records.append(row)
                        line_count += 1
        except IOError:
            print "Error: can\'t find file or read data"
        else:
            print "10 records were saved in an array of string"
            csv_file.close()

    def getStudentNumber(self):
        """Overriding this inherited method to display correct student number"""
        return "040806036"

    def display_student_name(self):
        """This method displays the student's name by calling inherited name() method"""
        print("Hello, my name is  " + self.name())
        print ("Student number is " + self.getStudentNumber())

    def show_all_records(self):
        """displays all records saved"""
        for x in ReadData.records:
            print(x)

    def save(self, data):
        """add a value to the array of strings"""
        ReadData.records.append(data)
        print(data.__str__() + " was added to the array.")

    def delete(self, number):
        """removes a value from the array using an index number within range"""
        count = len(ReadData.records) - 1
        if 0 <= int(number) <= int(count):
            del ReadData.records[int(number)]
            print("Record deleted.")
        else:
            print("Wrong number was entered")

    def edit(self, index, data):
        """Replaces the data at index with new data passed in"""
        count = len(ReadData.records) - 1
        if 0 <= int(index) <= int(count):
            ReadData.records[int(index)] = data
            print("Record was saved")
        else:
            print("Wrong index was entered")

    def quit(self):
        """Exits the program"""
        sys.exit()


root = Tk()
gui = ReadData(root)
gui.read_csv()
root.mainloop()
