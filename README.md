#GLORY AGBOFAME
# Library-Management-System.py
Here's the documentation for the Library Management System code, including explanations for the methods, functions, and modules used:

## Library Management System Documentation

### Overview:
This program implements a simple Library Management System using the Tkinter GUI toolkit. It allows users to manage library membership information and book details. Users can select a book from the list, and the corresponding book details will be displayed. They can enter the membership information, and the data will be displayed in the Text widget. The user can also delete the displayed data, reset the form, or exit the application.

### Modules Used:
1. `tkinter`: The standard GUI (Graphical User Interface) library in Python. It provides classes and functions for creating GUI applications.
2. `random`: This module is imported but not used in the current implementation.
3. `time`: This module is imported but not used in the current implementation.
4. `tkinter.messagebox`: A submodule of `tkinter` that provides methods for creating message boxes (pop-up windows) with various options.

### Class: `Library`
This class represents the main application window and contains the GUI elements and functionality.

#### Attributes:
1. `root` (Tk): The root window of the application. It serves as the main window where all the widgets are placed.
2. `MemberType` (StringVar): A variable to store the selected member type from the combobox.
3. `BookID` (StringVar): A variable to store the selected book ID.
4. `Ref` (StringVar): A variable to store the reference number.
5. `BookTitle` (StringVar): A variable to store the selected book title.
6. `Title` (StringVar): A variable to store the selected title (Mr., Mrs., Ms).
7. `FirstName` (StringVar): A variable to store the entered first name.
8. `LastName` (StringVar): A variable to store the entered last name.
9. `Address` (StringVar): A variable to store the entered address.
10. `PostCode` (StringVar): A variable to store the entered postal code.
11. `PhoneNo` (StringVar): A variable to store the entered phone number.
12. `Author` (StringVar): A variable to store the selected book author.
13. `DateofIssued` (StringVar): A variable to store the entered date of issuance.
14. `DueDate` (StringVar): A variable to store the calculated due date.
15. `ReturnFine` (StringVar): A variable to store the return fine amount.
16. `ReturnDate` (StringVar): A variable to store the return date.
17. `Price` (StringVar): A variable to store the price of the book.

#### Methods:
1. `Reset()`: Clears all the entry fields and resets the form to its default state.
2. `Delete()`: Deletes the data displayed in the right-side text widget (`txtDisplayR`).
3. `Exit()`: Asks the user for confirmation to exit the application and closes the window.
4. `DisplayData()`: Displays the membership information in the right-side text widget (`txtFrameDetail`).
5. `Receipt()`: Displays the selected book and membership information in the right-side text widget (`txtDisplayR`).
6. `SelectedBook(evt)`: Event handler for the book selection. Updates the book details based on the selected book.

#### Functions:
1. `SelectedBook(evt)`: This function is used to handle the event when a book is selected from the listbox (`booklist`). It updates the corresponding book details in the entry fields and displays the membership and book information in the right-side text widget.

#### Widgets:
1. `ComboBox` (`cboMemberType`): A combobox widget to select the member type.
2. `Entry` (`lblBookID`, `lblRef`, `lblBookTitle`, `lblFirstName`, `lblLastName`, `lblAddress`, `lblPostCode`, `lblPhoneNo`, `lblAuthor`, `lblDateIssued`, `lblDueDate`, `lblReturnFine`, `lblReturnDate`, `lblPrice`): Entry widgets to enter various details.
3. `Text` (`txtDisplayR`): A text widget to display book and membership information.
4. `Listbox` (`booklist`): A listbox widget displaying a list of available books.
5. `Buttons` (`btnDisplayData`, `btnDelete`, `btnReset`, `btnExit`): Buttons for various actions like displaying data, deleting data, resetting the form, and exiting the application.

### Execution:
The application is executed by creating an instance of the `Library` class, which initializes the Tkinter root window and sets up the GUI elements and functionality. The `root.mainloop()` method runs the main event loop, allowing the application to respond to user interactions and events.

Please note that the explanations provided here are general overviews of the methods, functions, and modules used. For more detailed information, additional comments and docstrings can be added to the code to provide a more comprehensive understanding of the code logic and functionality.
