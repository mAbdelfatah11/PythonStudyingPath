"""
    any python file is a module
    you can import the module or part of it inside another one
"""
# "1- import the module -----> you can access module elements using modulename "
# import itimodule
# itimodule.sayhello("Ali")

# "2- import part of the module -----"
# from itimodule import sayhello, pi
#
# sayhello("Ahmed")
# print(pi)

""" package ---> set of modules -------"""
# import iti.validation
#
# iti.validation.validateintinput("please enter num1 : ")

# from iti.validation import validateintinput
# validateintinput("please enter num1 : ")


#########################3
# import  iti
# import itipkg.greetingmodule
#
# itipkg.greetingmodule.sayhello("Ahmed")
##########################33
from itipkg import  sayhello
sayhello("test")

""" libraray ---> set of packages -----"""
from django.urls import path
 
# django: A library containing packages and modules for web development.
# django.urls: A package inside the Django library.
# path: A specific function or object (likely from a module inside the django.urls package).
