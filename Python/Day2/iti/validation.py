

# def validateintinput(message):
#     while True:
#         numm = input(message)
#         if numm.isdigit():
#             numm = int(numm)
#             return numm
#
# validateintinput("please enter age ")


def validateintinput(message):
    numm = input(message)
    if numm.isdigit():
        numm = int(numm)
        return numm

    return validateintinput(message)

# validateintinput("please enter age ")