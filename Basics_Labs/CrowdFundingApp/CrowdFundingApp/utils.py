
import re           # re module for regex validation, used here for phone number validation using regex
from datetime import datetime     # for date time validation

def validate_name(message):   # for user name validation or any other input string
    value = input(message)
    if value.isdigit() or value.isspace() or not value:
        print("---------------- please enter correct value for name -------")
        return validate_name(message)     # note here: recurseve function requires passing the required parameter
    return value
 
# def validate_integer(message):    # for validating integer only, not required here
#     value = input(message)
#     if value.isdigit():
#         return int(value)
#     print("---------------- please enter correct value for int -------")
#     return validate_integer(message)


def validate_password(message_pass, message_confirm):    # validate password match 
    password = input(message_pass)
    confirm_password = input(message_confirm)
    
    if password == confirm_password:
        return password  # Passwords match, return the valid password
    print("------------------ Passwords do not match ------------------------")
    return validate_password(message_pass, message_confirm)        # don't match, recursivly re-run the function. and note here: recurseve function requires passing the required parameters


def validate_email(message):    # be careful in variables naming, get away from names like: email, pass, etc..
     value = input(message)
     if "@" in value:
        return value
     print("----------------- Invalid email. It must contain '@' --------------")
     return validate_email(message)     


def validate_phone(message):  # for phone number validation or any other integer input
    value = input(message)
    # Check if phone is integer value and confirm number noting that Egyptian phone numbers start with 010, 011, 012, or 015 and are 11 digits
    if value.isdigit() and bool(re.match(r"^(010|011|012|015)[0-9]{8}$", value)):
            return int(value)
    print("---------------- please enter correct phone number -------")
    return validate_phone(message)



def validate_date(message):
    date_format = "%Y-%m-%d"
    date_str = input(message)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return validate_date(message)
