# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import Image
import math
from math import *

def prod(a,b):
    return a*b #this function finds the product of two inputs

def cos_pi(a):
    return cos(pi*a) #this function finds the value of the cosine of pi multiplied by the input value
    
def sin_pi(a):
    return sin(pi*a) #this function finds the value of the sine of pi multiplied by the input value

def x(a,b):
    return a #this function returns the first of two inputs

def y(a,b):
    return b #this function returns the second of two inputs

def squared(a):
    return a**2 #this function squares the input of the function
    
def cubed(a):
    return a**3 #this function cubes the input of the function


def build_random_function(min_depth, max_depth):
    """This function uses randomint to create a random list of nested strings. 
    min_depth sets the minimum amount of nesting that can occur, while max_depth
    sets the maximum amount of nesting that can occur"""
    
    
    #sets the base condition
    new_list= [["x"], ["y"]] #created a list of just x and y to be randomly selected for when max depth is reached
    if max_depth == 1: #forces the function to pick x or y which are the input argument in a later function when maximum recursion depth is reached
        rand_func = new_list[randint(0,1)] #randomly selects x or y to add to a new list
        return rand_func #the list must be returned
        
        
    c = min_depth -1 #every time I recurse I want the min depth to decrease by 1 so there is not infinite recursion
    d = max_depth -1 #every time I recurese I want max depth to decrease by 1 to prevent infinite recursion
    
    a = build_random_function(c, d) #calls build random function for recursion and subtracts one from min_depth and max_depth each time the function recurses
    b = build_random_function(c, d) #same as previous line but for b which is where nesting occurs in the function (like a)
    
    
    list_of_functions = [["prod", a, b], ["cos_pi", a], ["sin_pi", a], ["squared",a],["cubed",a], ["x"], ["y"]]
        # these are all the possible strings that can be used to create a list which is the output of build_random_function, a and b are the inputs for the recursion
    
    
    if min_depth >= 0: #if min_depth is not reached yet this prevents x or y from being chosen
        rand_func = list_of_functions[(randint(0,4))] #can randomnly select from anything but x and y
        return rand_func
        
    if min_depth < 0: #if min_depth is reached but not max depth any string from the list can be randomly selected
        rand_func = list_of_functions[(randint(0,6))] #randomly pick from any string from list_of_functions
        return rand_func
        
    

def evaluate_random_function(f, x, y):
    """This function evaluates the list of strings from build_random_function
        This function takes in a function f which is build_random_function, and then x and y
        which are number values and will be used to evaluate the random function
        This function converts the nexted strings in the list output from build_random_function
        to actual functions ie cos_pi becomes cos(pi*a) and then computes the result
        
        evaluate_random_function outputs a number (which is the result of build_random_function evaluated for x and y)
          The range of the output is -1 to 1  
    """
    
    
    
    
    list_func = f #renamed the input function for fun
    
    
    #this is the recursion I look and the beginning of the list and then move on to the list until I reach x or y and then it evaluates the function
    if list_func[0] == 'prod': #defined the function prod which takes the product of its two inputs
        value= evaluate_random_function(list_func[1],x,y)*evaluate_random_function(list_func[2],x,y)
        #print 'value', value
        return value #value was created so I could print the result and test my function
    if list_func[0] == 'cos_pi': #this function is cos(pi*a) a is the next entry in the list
        value = cos_pi(evaluate_random_function(list_func[1],x,y))
        #print 'value', value
        return value
    if list_func[0] == 'sin_pi': #this function is sin(pi*a) a is the next entry in the list
        value = sin_pi(evaluate_random_function(list_func[1],x,y))
        #print 'value', value
        return value
    if list_func[0] == 'squared': #this function is a**2 and a is the next entry in the list
        return squared(evaluate_random_function(list_func[1],x,y))
    if list_func[0] == 'cubed': #this function is a**3 and a is the next entry in the list that is being evaluated
        return cubed(evaluate_random_function(list_func[1],x,y))
    if list_func[0] == 'x': #x is an input argument so if it is reached then evaluate_random_function returns the input x which is an number
        #print x        
        return x
    if list_func[0] == 'y':#y is an input argument so if it is reached there is no more nesting below it so evaluate_random_function returns the input y which is a number
        #print y
        return y
            
        
    

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    
       I did not use this function and instead did the remapping in make_art
    """
    # your code goes here
    
def make_art():
    """This function creates computational art
    It has no inputs but it calls from build random function
    It calls build random function to create random values for r,g,b (colors) and then it
    and then converts these numbers to a 0 to 255 scale which correspond to rgb values
    The function than iterates for x being between -1 and 1 and y values for -1 and 1 for each
    pixel in the image    
    
    
    The function outputs a 350 x 350 pixel that combines the images are generated from the
    red, green, and blue channels
    
    """
    red = build_random_function(4,6) #finds a random function to be used to compute the red in the image
    green = build_random_function(5,8) #finds a random function to be used to compute the green in the image
    blue = build_random_function(5,10) #finds a random function to be used to compute the blue in the image
    im = Image.new("RGB",(350,350)) #sets the size of the image produced
    pixels = im.load()
    
    for x in range(0,349): #runs x through every pixel in the image
        for y in range(0,349): #iterates through every pixel in the image for y
            xscale = x/(349/2.0)-1 #rescales x so it goes from -1 to 1
            yscale = y/(349/2.0)-1 #rescales y so it goes from -1 to 1
            r = evaluate_random_function(red,xscale,yscale) #evaluates evaluate_random_function for red for the given x and y values in the loop
            g = evaluate_random_function(green,xscale,yscale) #same as before but for green
            b = evaluate_random_function(blue,xscale,yscale) #same as before but for blue
            rrescale = (r+1)*255/2.0 #scales the found values for red to a 0 to 255 scale
            grescale = (g+1)*255/2.0 #scales the found values for green to a 0 to 255 scale
            brescale = (b+1)*255/2.0 #scales the found values for red to a 0 to 255 scale
            r = int(rrescale) #set the new red value to the rescaled value
            g = int(grescale) #set the new green value to the rescaled value
            b = int(brescale) #set the new blue value to the rescaled value
            pixels[x,y] = (r,g,b) #gives the r,g,b value for each pictures
    im.save("pic33.png") #saves the picture
    im.show()
    