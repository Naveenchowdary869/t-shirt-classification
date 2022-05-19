"""
NO FUNCTIONS SHOULD BE ADDED OR REMOVED FROM THIS MODULE. SIMPLY COMPLETE EACH FUNCTION AS DESCRIBED.
YOU SHOULD ALSO NOT REMOVE ANY OF THE COMMENTS OR CHANGE THE STRUCTURE IN ANY WAY OTHER THAN AS INSTRUCTED.

TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters it receives and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately and as specified.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import datetime
import re
file_path = 'data/sales.csv'
import csv

records = []
#headings = []


# def load_data(file_path):
#     print("Loading data...", end="")

with open(file_path, encoding="utf8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file)
    headings = next(csv_reader)

    for line in csv_reader:
        records.append(line)

    print("Done!")
print(records)



def greeting():
    greet ="------------------Sales and Profit Data------------------"
    print(greet)
    return

    # """
    # Task 3: Display a greeting
    #
    # The welcome message should display the title 'Sales and Profit Data'.
    # The welcome message should contain dashes to the left and right of the title i.e. is of the form ----- title -----
    # The number of dashes on either side of the title should be equivalent to the number of characters in the title.
    #
    # :return: Does not return anything.
    # """

greeting()

def error(msg):
    print(f'Error! {  { msg }  }.')
    return

error('this is an error ')
    # """
    # Task 4: Display an error message.
    #
    # The function should display a message in the following format:
    # 'Error! {error_msg}.'
    # Where {error_msg} is the value of the parameter 'msg' passed to this function
    #
    # :param msg: A string containing an error message.
    # :return: Does not return anything.
    # """



def status(operation, progress=15):
    if progress == 0:
        print(f'>> PROCESS STARTED: {operation}')
    elif 0 > progress or progress < 100:
        print(f'>> PROCESS IN PROGRESS: {operation} ({progress}%)')
    elif progress == 100:
        print(f'>> PROCESS ENDED: {operation}')
    elif progress > 100:
        print(f'>> STATUS: {operation}')
        return

#status('task1',14)


    # """
    # Task 5: Display a message to indicate the progress of an operation.
    #
    # The function should display a message in the following format:
    # '>> PROCESS STARTED: {operation}'
    # if the value of the parameter 'progress' is equal to 0.
    #
    # The function should display a message in the following format:
    # '>> PROCESS IN PROGRESS: {operation} ({progress}%)'
    # if the value of the parameter 'progress' is between, but not including, 0 and 100
    #
    # The function should display a message in the following format:
    # '>> PROCESS ENDED: {operation}'
    # if the value of the parameter 'progress' is equal to 100.
    #
    # The function should display a message in the following format:
    # '>> STATUS: {operation}'
    # if the value of the parameter 'progress' is outside the range 0 - 100.
    #
    # Note:
    # {operation} is the value of the parameter 'operation' passed to this function.
    # {progress} is the value of the parameter 'progress' passed to this function.
    #
    #
    # :param operation: A string indicating what operation is being executed.
    # :param progress: An integer indicating the progress made by the process.
    # :return: Does not return anything.
    # """



def main_menu():
    print("please select an option:")
    print("\n[1] Process Data")
    print("\n[2] Query Database")
    print("\n[3] Visualise Data")
    print("\n[4] Exit")
    number = int(input("Your selection: "))
    return number
#main_menu()
    # """
    # Task 6: Display the main menu of options and read the user's response.
    #
    # First, a menu should be displayed starting with the message 'Please select an option:' and then followed
    # by the options:
    #
    # '[1] Process Data',
    # '[2] Query Database',
    # '[3] Visualise Data' and
    # '[4] Exit'
    #
    # Each option should be displayed on a new line with no blank lines or extra spaces before or after the option.
    # The single quotes and commas should not be displayed.
    #
    # The function should then display the message 'Your selection: ' (note the space) and read in the user's response.
    # Th function should return the user's response as an integer.
    #
    # For higher marks (advanced task):
    #     - The user's response should be returned if it is valid.
    #     - The function should display the error message 'Invalid selection.' using the tui error function
    #     if the user's selected option is invalid. The function should also return -1 in this case.
    #
    # :return: An integer indicating what menu option has been selected or -1 if the selected option is invalid.
    # """
    #
    # pass


def sub_menu(menu_id=0):

    if 0 == menu_id or menu_id > 3:
        print(f"{error('menu id should be between 1 and 3.')}")

    print("Please select an option:")
    if menu_id == 1:
        print("\n[1] Record By Id")
        print("\n[2] Records by Customers")
        print("\n[3] Group Records by Shipment Mode")
        print("\n[4] Summarise Records")
    elif menu_id == 2:
        print("\n[1] Setup database")
        print('\n[2] Retrieve all customers in alphabetical order from the database')
        print('\n[3] Retrieve the total sales of each product from the database')
        print('\n[4] Retrieve the top 3 product categories in terms of profit from the database')
        print('\n[5] Retrieve the top 3 product sub-categories in terms of sales for specific dates from the database')
    elif menu_id ==3:
        print('\n[1] Static Summary')
        print('\n[2] Animated Summary')
    number1 = int(input("Your selection: "))
    return number1
#sub_menu(1)

    # """
    # Task 7: Display a sub menu of options and read and return the user's response.
    #
    # If no value, a zero or an invalid value is supplied for the parameter 'id' then the an error containing
    # the following message should be displayed using the tui error function:
    # 'menu id should be between 1 and 3.'
    #
    # The message 'Please select an option:' should be displayed.
    #
    # If the value of the parameter 'menu_id' is 1 then a menu with the following options should be displayed:
    # '[1] Record By Id',
    # '[2] Records by Customers',
    # '[3] Group Records by Shipment Mode', and
    # '[4] Summarise Records'
    #
    # If the value of the parameter 'menu_id' is 2 then a menu with the following options should be displayed:
    # '[1] Setup database',
    # '[2] Retrieve all customers in alphabetical order from the database',
    # '[3] Retrieve the total sales of each product from the database',
    # '[4] Retrieve the top 3 product categories in terms of profit from the database',
    # '[5] Retrieve the top 3 product sub-categories in terms of sales for specific dates from the database'
    #
    # If the value of the parameter 'menu_id' is 3 then a menu with the following options should be displayed:
    # '[1] Static Summary', and
    # '[2] Animated Summary'
    #
    # Each option should be displayed on a new line with no blank lines or extra spaces before of after the option.
    # The single quotes and commas should not be displayed.
    #
    # After displaying the relevant menu above, the message 'Your selection: ' should be displayed
    # and the user's response should be read in and returned as an integer.
    #
    # For higher marks (advanced task):
    #     - The user's response should be returned if it is valid.
    #     - The function should display the error message 'Invalid selection.' (note the space) using tui error
    #     function if the user's selected option is invalid. The function should also return -1 in this case.
    #
    # :param menu_id: An integer indicating what menu should be displayed.
    # :return: An integer indicating what menu option has been selected or -1 if the selected option is invalid.
    # """
    # #
    # pass


def total_records(num_records):
    print(f'There are {num_records} records in the data set.')
    return

    # f"""
    # Task 8: Display the total number of records in the data set.
    #
    # The function should display a message in the following format:
    #
    # "There are {num_records} records in the data set."
    #
    # Where {num_records} is the value of the parameter passed to this function
    #
    # :param num_records: The total number of records in the data set.
    # :return: Does not return anything.
    # """
    # #


total_records(9)


def record_id(valid_ids=None):
    id = int(input("Enter a valid integer record id : "))
    if 2 >= valid_ids <= 7000:
        id == valid_ids
    elif print(f"{error('Invalid record id.')}"):
        return -1
    else:
        return id
# print(record_id(27))

    # """
    # Task 9: Prompt the user to enter a record id and return it.
    #
    # The function should ask the user to enter a record id e.g. 7
    # The function should then read in and return the user's response as an integer.
    #
    # For higher marks (advanced task):
    #     - The function should return the user's response if it is valid.
    #     - If a non-empty list of valid ids is supplied then this should be used to check if the user's value is valid.
    #     - The function should display the error message 'Invalid record id.' using the tui error function
    #     if the value entered by the user is an invalid record id. The function should also return -1 in this case.
    #
    # :param valid_ids: A list of valid record id values.
    # :return: The id for a record or -1 if invalid.
    # """


def customers():
    n =input(print("please enter a coustomer id : "))
    n_split = n.split()
    # convert each item to int type
    for i in range(len(n_split)):
    # convert each item to int type
        n_split[i] = int(n_split[i])
    return n_split

    # """
    # Task 10: Read in and return a list of customer id.
    #
    # The function should ask the user to enter a customer id.
    # The function should return a list containing the specified customer id.
    #
    # For higher marks (advance task):
    #     - The user should be able to enter as many customer ids as desired.
    #     - The function should return a list containing the specified customer ids.
    #
    # For even higher marks (advance task):
    #     - The format of the customer id should match that in the data file.
    #     - The function should check the validity of each customer id entered by the user.
    #     - An error message should be displayed for each invalid customer id.
    #     - The error message 'Invalid customer id: {X}' should be displayed where 'X' is the invalid customer id.
    #     - Only valid customer ids should be included in the list returned by the function.
    #
    # :return: A list of valid customer ids
    # """



def dates():
    n = input(print("please enter a date in this formate : "))
    # format
    datetime1 = datetime.datetime.strptime(n, '%m/%d/%Y').date()

    return datetime1

    # """
    # Task 11: Read in and return a list of dates.
    #
    # The function should ask the user to enter a date.
    # The function should return a list containing the specified date.
    #
    # For higher marks (advance task):
    #     - The user should be able to enter as many dates as desired.
    #     - The function should return a list containing the specified dates.
    #
    # For even higher marks (advance task):
    #     - The function should check the validity of each date entered by the user.
    #     - An error message should be displayed for each invalid date.
    #     - The error message 'Invalid date: {X}' should be displayed where 'X' is the invalid date.
    #     - Only valid dates should be included in the list returned by the function.
    #
    # :return: A list of valid dates
    # """


def sample_size(max_records, default_size=5):
    max_records1 = int(input(print("Enter a whole number :")))
    if max_records1 > max_records:
      max_records1 = default_size
    return max_records1
    # """
    # Task 12: Read in and return a sample size.
    #
    # The function should ask the user to enter a whole number which represents the number of records to be sampled.
    # The function should return the number entered by the user.
    # The function check that the value entered by the user is valid.
    #
    # :param default_size: The default number of records to be sampled.
    # :param max_records: The maximum number of records that can be sampled.
    # :return: An integer corresponding to the sample size.
    # """



def display_record(record, cols=None):
    invalid_cols =[]
    if cols == None:
        print(record)
    elif type(cols)==list:
        print(f"cols :{cols}")
        for index in cols.sort():
            print(record[index])
    else:
        error(f"Invalid cols {cols}")


print(display_record(3))

    # """
    # Task 13: Display a record.
    #
    # The function should display the value of the parameter 'record'.
    # This is a list of values which represents a single record.
    #
    # For higher marks (advance task):
    #     - the parameter 'cols' is a list of column indexes.
    #     - the function should check if any column indexes have been supplied.
    #     - if so, the function should sort the list into natural (ascending) order.
    #     - the function should then display a record containing only values corresponding to each column index.
    #
    # For even higher marks (advance task):
    #     - any invalid column indexes should be ignored when displaying the record
    #     - any invalid column indexes should be returned as a list
    #
    # :param record: A list of data values for a record.
    # :param cols: A list of integer values that represent column indexes
    # :return: Does not return anything for basic function or a list of invalid indexes for the advance task
    # """
    # #
    # pass


def display_records(records, cols=None):
    pass


    # """
    # Task 14: Display multiple records
    #
    # The function should display each record in the list of records.
    # Each record should be displayed on a new line.
    # There should be no blank lines or extra spaces before or after the displayed record.
    #
    # For higher marks (advance task):
    #     - records may contain empty record i.e. it will contain no values
    #     - the function should ignore any empty records when displaying each record
    #     - the number of empty records encountered should be returned
    #
    # :param records: A list of records.
    # :param cols: A list of integer values that represent column indexes.
    # :return: Does not return anything for the basic task or a count of empty records encountered for the advance task.
    # """
    # #
    # pass


def display_groups(groups):
    for group in groups :
        print(f"groups:{group}")
    for key, value in groups.items():
        print(f"{key}:{value}")
    return


    # """
    # Task 15: Display groups
    #
    # The function should display each group contained in groups.
    # The parameter 'groups' is a dictionary so both its keys (group names) and values (group members) will need
    # to be displayed.
    # The group will need to be displayed on its own line followed by each record belonging to that group on its own
    # line e.g.
    #
    # {group}:
    # {group record 1}
    # {group record 2}
    # ...
    #
    # There should be no blank lines or extra spaces before or after each line.
    #
    # For higher marks (advance task):
    #     - The function should display the keys in natural (alphabetical and ascending) order.
    #
    # :param groups: A dictionary containing group names as keys and records as values.
    # :return: Does not return anything.
    # """
    # #
    # pass


def display_summary(summary):
    summary = {key: value for key, value in sorted(summary.items())}
    for key,value in summary:
        print(f"{key}:{value}")
    return


    # """
    # Task 16: Display summary
    #
    # The function should display the summary received as an argument for the parameter 'summary'.
    # The parameter 'summary' contains a dictionary where the keys represent names of states and the values are
    # dictionaries that contain sales data.
    #
    # E.g. A key-value pair in the dictionary 'summary' may be as follows:
    # 'New York': {'sales': 157.56, 'quantity': 100, 'discount': 300.14, 'profit': 450.34}
    #
    # The function should display each key with its value in the format: '{key}: {value}'
    #
    # For higher marks (advance task):
    #     - the function should display the keys in natural (alphabetical and ascending) order
    #
    # :param summary: A dictionary containing names as keys and nested dictionaries as values.
    # :return: Does not return anything.
    # """
    # #
    # pass
