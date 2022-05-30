#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10133810
#    Student name: Harry Newton
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Assignment Description-----------------------------------------#
#
#  CITYSCAPES
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and efficiently repeating multiple actions in
#  order to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "build_city".
#  You are required to complete this function so that when the
#  program is run it draws a city whose plan is determined by
#  randomly-generated data stored in a list which specifies what
#  style of building to erect on particular sites.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#

#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be installed separately, because the markers
# may not have access to such modules.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700  # pixels
canvas_width = 1100  # pixels
grass_depth = 95  # vertical depth of the "grass", in pixels
half_width = canvas_width // 2  # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal')  # font for drawing the grid
grid_size = 50  # gradations for the x and y scales shown on the screen
offset = 5  # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth  # maximum positive y coordinate
max_building_height = 575  # city ordinance maximum building height
site_width = 240  # maximum width of a building site
floor_height = 60
curr_height = 0 # will += using the floor_height value to make floors

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]], ['Site 2', [25, 0]], ['Site 3', [275, 0]], [
    'Site 4', [-375, -25]
], ['Site 5', [-125, -25]], ['Site 6', [125, -25]], ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]], ['Site 9', [-25,
                                              -50]], ['Site 10', [225, -50]]]

#
#--------------------------------------------------------------------#

#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#


# Set up the canvas and draw the background for the overall image.
# By default the drawing grid is displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_grid=True):

    # Set up the drawing canvas with coordinate (0, 0) in the
    # "grass" area
    setup(canvas_width, canvas_height)
    setworldcoordinates(-half_width, -grass_depth, half_width, max_height)

    # Draw as fast as possible
    tracer(False)

    # Make the sky blue
    bgcolor('sky blue')

    # Draw the "grass" as a big green rectangle (overlapping the
    # edge of the drawing canvas slightly)
    overlap = 25  # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap))  # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90)  # face north
    forward(grass_depth + overlap * 2)
    right(90)  # face east
    forward(canvas_width + overlap * 2)
    right(90)  # face south
    forward(grass_depth + overlap * 2)
    end_fill()

    # Draw a nice warm sun peeking into the image at the top left
    penup()
    goto(-canvas_width // 2, canvas_height - grass_depth)
    pencolor('yellow')
    dot(350)

    # Draw a big fluffy white cloud in the sky
    goto(canvas_width // 3, canvas_height - grass_depth - 100)
    pencolor('white')
    dot(200)
    setheading(200)
    forward(100)
    dot(180)
    setheading(0)
    forward(200)
    dot(160)

    # Optionally draw x coordinates along the bottom of the
    # screen (to aid debugging and marking)
    pencolor('black')
    if show_grid:
        for x_coord in range(-half_width + grid_size, half_width, grid_size):
            goto(x_coord, -grass_depth + offset)
            write('| ' + str(x_coord), font=grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font=grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font=grid_font)

    # Optionally mark each of the building sites approved by
    # the city council
    if show_grid:
        for site_name, location in sites:
            goto(location)
            dot(5)
            goto(location[0] - (site_width // 2), location[1])
            setheading(0)
            pendown()
            forward(site_width)
            penup()
            goto(location[0] - 40, location[1] - 17)
            write(site_name + ': ' + str(location), font=grid_font)

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.
# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
#--------------------------------------------------------------------#

#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the build_city function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_plan function appearing below.  Your
# program must work correctly for any data set generated by the
# random_plan function.
#
# Each of the data sets below is a list specifying a set of
# buildings to be erected.  Each specification consists of the
# following parts:
#
# a) The site on which to erect the building, from Site 1 to 10.
# b) The style of building to be erected, from style 'A' to 'D'.
# c) The number of floors to be constructed, from 1 to 10.
# d) An extra value, either 'X' or 'O', whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#

# Each of these data sets draws just one building in each of the
# four styles
fixed_plan_1 = [[1, 'A', 6, 'O']]
fixed_plan_2 = [[2, 'B', 7, 'O']]
fixed_plan_3 = [[3, 'C', 5, 'O']]
fixed_plan_4 = [[4, 'D', 4, 'O']]
fixed_plan_5 = [[1, 'A', 9, 'X']]
fixed_plan_6 = [[2, 'B', 2, 'X']]
fixed_plan_7 = [[3, 'C', 3, 'X']]
fixed_plan_8 = [[4, 'D', 6, 'X']]

# Each of the following data sets draws just one style of
# building but at three different sizes, including the maximum
# (so that you can check your building's maximum height against
# the height limit imposed by the city council)
fixed_plan_9 = [[1, 'A', 10, 'O'], [2, 'A', 5, 'O'], [3, 'A', 1, 'O']]
fixed_plan_10 = [[1, 'B', 10, 'O'], [2, 'B', 5, 'O'], [3, 'B', 1, 'O']]
fixed_plan_11 = [[1, 'C', 10, 'O'], [2, 'C', 5, 'O'], [3, 'C', 1, 'O']]
fixed_plan_12 = [[1, 'D', 10, 'O'], [2, 'D', 5, 'O'], [3, 'D', 1, 'O']]
fixed_plan_13 = [[1, 'A', 10, 'X'], [2, 'A', 5, 'X'], [3, 'A', 1, 'X']]
fixed_plan_14 = [[1, 'B', 10, 'X'], [2, 'B', 5, 'X'], [3, 'B', 1, 'X']]
fixed_plan_15 = [[1, 'C', 10, 'X'], [2, 'C', 5, 'X'], [3, 'C', 1, 'X']]
fixed_plan_16 = [[1, 'D', 10, 'X'], [2, 'D', 5, 'X'], [3, 'D', 1, 'X']]

# Each of the following data sets draws a complete cityscape
# involving each style of building at least once. There is
# no pattern to them, they are simply specific examples of the
# kind of data returned by the random_plan function which will be
# used to assess your solution. Your program must work for any value
# that can be returned by the random_plan function, not just these
# fixed data sets.
fixed_plan_17 = \
    [[1, 'D', 2, 'O'],
     [2, 'B', 7, 'O'],
     [5, 'C', 6, 'O'],
     [6, 'A', 4, 'O']]
fixed_plan_18 = \
    [[1, 'D', 6, 'O'],
     [3, 'C', 5, 'O'],
     [4, 'B', 3, 'O'],
     [9, 'A', 9, 'O'],
     [10, 'D', 2, 'O']]
fixed_plan_19 = \
    [[5, 'C', 6, 'O'],
     [6, 'B', 9, 'O'],
     [7, 'A', 5, 'O'],
     [8, 'A', 7, 'O'],
     [9, 'D', 4, 'O']]
fixed_plan_20 = \
    [[1, 'A', 4, 'O'],
     [2, 'B', 4, 'O'],
     [3, 'A', 5, 'O'],
     [4, 'D', 7, 'O'],
     [10, 'B', 10, 'O']]
fixed_plan_21 = \
    [[1, 'B', 6, 'O'],
     [3, 'A', 4, 'O'],
     [4, 'C', 4, 'O'],
     [6, 'A', 8, 'O'],
     [8, 'C', 7, 'O'],
     [9, 'B', 5, 'O'],
     [10, 'D', 3, 'O']]
fixed_plan_22 = \
    [[1, 'A', 10, 'O'],
     [2, 'A', 9, 'O'],
     [3, 'C', 10, 'O'],
     [4, 'B', 5, 'O'],
     [5, 'B', 7, 'O'],
     [6, 'B', 9, 'O'],
     [7, 'C', 2, 'O'],
     [8, 'C', 4, 'O'],
     [9, 'A', 6, 'O'],
     [10, 'D', 7, 'O']]
fixed_plan_23 = \
    [[3, 'A', 8, 'O'],
     [4, 'C', 8, 'O'],
     [5, 'B', 4, 'O'],
     [6, 'D', 5, 'O'],
     [7, 'C', 5, 'X'],
     [8, 'A', 3, 'X'],
     [9, 'D', 2, 'X']]
fixed_plan_24 = \
    [[2, 'C', 3, 'O'],
     [3, 'B', 1, 'O'],
     [4, 'C', 3, 'X'],
     [5, 'C', 1, 'O'],
     [6, 'D', 2, 'O'],
     [7, 'B', 1, 'O'],
     [8, 'D', 2, 'O'],
     [9, 'C', 7, 'O'],
     [10, 'A', 1, 'X']]
fixed_plan_25 = \
    [[1, 'B', 7, 'X'],
     [3, 'C', 1, 'O'],
     [6, 'D', 3, 'O'],
     [7, 'A', 7, 'O'],
     [8, 'D', 3, 'X'],
     [9, 'C', 7, 'O'],
     [10, 'C', 9, 'X']]
fixed_plan_26 = \
    [[1, 'A', 6, 'O'],
     [2, 'A', 2, 'O'],
     [3, 'A', 9, 'X'],
     [4, 'D', 1, 'X'],
     [5, 'C', 7, 'O'],
     [6, 'D', 6, 'O'],
     [7, 'B', 5, 'O'],
     [8, 'A', 1, 'O'],
     [9, 'D', 10, 'X'],
     [10, 'A', 6, 'O']]

#
#--------------------------------------------------------------------#

#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a city
# to be built.  Your program must work for any data set returned by
# this function.  The results returned by calling this function will
# be used as the argument to your build_city function during marking.
# For convenience during code development and marking this function
# also prints the plan for the city to be built to the shell window.
#


def random_plan(print_plan=True):
    building_probability = 70  # percent
    option_probability = 20  # percent
    from random import randint, choice
    # Create a random list of building instructions
    city_plan = []
    for site in range(1, len(sites) + 1):  # consider each building site
        if randint(
                1,
                100) <= building_probability:  # decide whether to build here
            style = choice(['A', 'B', 'C', 'D'])  # choose building style
            num_floors = randint(1, 10)  # choose number of floors
            if randint(1,
                       100) <= option_probability:  # decide on option's value
                option = 'X'
            else:
                option = 'O'
            city_plan.append([site, style, num_floors, option])
    # Optionally print the result to the shell window
    if print_plan:
        print('\nBuildings to be constructed\n' +
              '(site, style, no. floors, option):\n\n',
              str(city_plan).replace('],', '],\n '))
    # Return the result to the student's build_city function
    return city_plan


#
#--------------------------------------------------------------------#

#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "build_city" function.
#


def ht(xcor, new_x, cur_x=-225):
    return xcor - (cur_x - new_x)

def vt(ycor, new_y, cur_y=0):
    return ycor - (cur_y - new_y)




# Erect buildings as per the provided city plan


def build_city(plans, buildings):

    for plan in plans:
        site, style, height, is_finished = plan  # unpack all the plan values into several variables
        new_x, new_y = sites[site - 1][ 1]  # unpack the list contining the x and y coordinate of the site
        for section, instructions in buildings[style].items():
            for transition in instructions:

                colour, positions = list(transition.items())[0]

                if positions[0][0] == 'dot':
                    penup()
                    goto(
                        ht(positions[0][1][0], new_x), # generate the new x value based upon the site
                        vt(positions[0][1][1], new_y)) # generate the new y value based upon the site
                    pendown()
                    dot(23, colour)
                else:
                    x = ht(
                        positions[0][0],
                        new_x)  # generate the new x value based upon the site
                    y = vt(
                        positions[0][1],
                        new_y)  # generate the new y value based upon the site

                penup()
                color(colour)
                setpos((x, y))
                begin_fill()
                pendown()

                for position in positions:

                    if position[0] == 'dot': # checks if it needs to create a dot
                        penup()
                        goto(
                            ht(position[1][0], new_x), # generate the new x value based upon the site
                            vt(position[1][1], new_y)) # generate the new y value based upon the site

                        pendown()
                        dot(23, colour)
                    else:
                        goto(ht(position[0], new_x), vt(position[1], new_y))
                

                end_fill()


#
#--------------------------------------------------------------------#

#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# building your city.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and building sites
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with your name and/or a description of
# ***** your city
title("Harry's City")

building_styles = {
    'A': {'base': [{'green': [(-220, 0), (-120, 0), (-120, 60), (-220, 60), (-320, 60), (-320, 0)]}, {'pink': [(-246.4814814814815, -2.058823529411765), (-246.4814814814815, 21.61764705882353), (-206.75925925925927, 21.61764705882353), (-206.75925925925927, -0.0)]}, {'pink': [(-186.38888888888889, 50.44117647058824), (-185.37037037037038, 35.0), (-165.0, 35.0), (-165.0, 48.38235294117647), (-185.37037037037038, 48.38235294117647)]}, {'pink': [(-265.8333333333333, 33.970588235294116), (-242.40740740740742, 33.970588235294116), (-242.40740740740742, 48.38235294117647), (-264.81481481481484, 45.294117647058826), (-264.81481481481484, 33.970588235294116)]}, {'black': [(-227.12962962962962, 20.58823529411765), (-226.11111111111111, -1.0294117647058825)]}], 'floor': [{'blue': [(-218.7962962962963, 58.6764705882353), (-118.7962962962963, 58.6764705882353), (-118.7962962962963, 118.6764705882353), (-218.7962962962963, 118.6764705882353), (-318.7962962962963, 118.6764705882353), (-318.7962962962963, 58.676470588235304)]}], 'roof': [{'orange': [(-317.77777777777777, 116.32352941176471), (-217.77777777777777, 116.32352941176471), (-117.77777777777777, 116.32352941176471), (-117.77777777777777, 176.3235294117647), (-217.77777777777777, 176.3235294117647), (-317.77777777777777, 176.3235294117647), (-317.77777777777777, 116.3235294117647)]}, {'cyan': [(-244.44444444444446, 140.0), (-215.92592592592592, 156.47058823529412), (-194.53703703703704, 140.0), (-242.40740740740742, 137.94117647058823)]}]},
    'B': {'base': [{'pink': [(-220, 0), (-120, 0), (-120, 60), (-220, 60), (-320, 60), (-320, 0)]}, {'green': [(-256.6666666666667, -1.0294117647058825), (-253.61111111111111, 30.88235294117647), (-193.51851851851853, 24.705882352941178), (-196.57407407407408, -1.0294117647058825)]}], 'floor': [{'black': [(-217.77777777777777, 58.6764705882353), (-117.77777777777777, 58.6764705882353), (-117.77777777777777, 118.6764705882353), (-217.77777777777777, 118.6764705882353), (-317.77777777777777, 118.6764705882353), (-317.77777777777777, 58.676470588235304)]}, {'cyan': [(-316.75925925925924, 108.08823529411765), (-117.12962962962963, 105.0), (-116.11111111111111, 93.67647058823529), (-315.74074074074076, 94.70588235294117)]}, {'cyan': [(-316.75925925925924, 82.3529411764706), (-118.14814814814815, 80.29411764705883), (-117.12962962962963, 68.97058823529412), (-316.75925925925924, 71.02941176470588)]}], 'roof': [{'yellow': [(-316.75925925925924, 117.3529411764706), (-225.09259259259258, 184.26470588235296), (-118.14814814814815, 118.38235294117648)]}]}, 
    'C': {'base': [{'black': [(-220, 0), (-120, 0), (-120, 60), (-220, 60), (-320, 60), (-320, 0)]}, {'pink': [(-248.51851851851853, 1.0294117647058825), (-248.51851851851853, 32.94117647058824), (-203.7037037037037, 33.970588235294116), (-203.7037037037037, 1.0294117647058825)]}], 'floor': [{'orange': [(-220, 60), (-120, 60), (-120, 120), (-220, 120), (-320, 120), (-320, 60)]}, {'blue': [(-283.14814814814815, 116.32352941176471), (-283.14814814814815, 58.6764705882353), (-261.75925925925924, 59.705882352941174), (-261.75925925925924, 118.38235294117648)]}, {'blue': [(-180.27777777777777, 116.32352941176471), (-177.22222222222223, 58.6764705882353), (-151.75925925925927, 58.6764705882353), (-151.75925925925927, 118.38235294117648)]}], 'roof': [{'cyan': [(-220, 120), (-120, 120), (-120, 180), (-220, 180), (-320, 180), (-320, 120)]}]},
    'D': {'base': [{'pink': [(-220, 0), (-120, 0), (-120, 60), (-220, 60), (-320, 60), (-320, 0)]}, {'blue': [(-252.59259259259258, -1.0294117647058825), (-252.59259259259258, 27.794117647058822), (-203.7037037037037, 27.794117647058822), (-203.7037037037037, -2.058823529411765)]}], 'floor': [{'green': [(-220, 60), (-120, 60), (-120, 120), (-220, 120), (-320, 120), (-320, 60)]}, {'yellow': [(-291.2962962962963, 119.41176470588235), (-227.12962962962962, 58.6764705882353), (-175.1851851851852, 119.41176470588235), (-198.61111111111111, 119.41176470588235), (-228.14814814814815, 76.17647058823529), (-271.94444444444446, 117.3529411764706)]}], 'roof': [{'black': [(-220, 120), (-120, 120), (-120, 180), (-220, 180), (-320, 180), (-320, 120)]}]},
    'E': {'base': [{'blue': [(-220, 0), (-120, 0), (-120, 60), (-220, 60), (-320, 60), (-320, 0)]}, {'pink': [(-255.64814814814815, -1.0294117647058825), (-255.64814814814815, 35.0), (-191.4814814814815, 35.0), (-191.4814814814815, 1.0294117647058825)]}, {'black': [(-223.05555555555554, 35.0), (-223.05555555555554, -2.058823529411765)]}, {'black': [('dot', (-292.31481481481484, 40.14705882352941))]}, {'black': [('dot', (-153.7962962962963, 41.1764705882353))]}], 'floor': [{'orange': [(-220, 60), (-120, 60), (-120, 120), (-220, 120), (-320, 120), (-320, 60)]}, {'cyan': [(-318.7962962962963, 110.1470588235294), (-130.37037037037038, 59.705882352941174), (-120.18518518518519, 71.02941176470588), (-305.55555555555554, 118.38235294117648), (-316.75925925925924, 106.02941176470588)]}, {'cyan': [(-133.42592592592592, 118.38235294117648), (-119.16666666666667, 108.08823529411765), (-307.5925925925926, 58.6764705882353), (-317.77777777777777, 68.97058823529412), (-131.38888888888889, 117.3529411764706)]}], 'roof': [{'green': [(-220, 120), (-120, 120), (-120, 180), (-220, 180), (-320, 180), (-320, 120)]}, {'pink': [(-286.2037037037037, 151.3235294117647), ('dot', (-286.2037037037037, 151.3235294117647))]}, {'pink': [('dot', (-233.24074074074073, 149.26470588235296))]}]}
}

# Call the student's function to build the city
# ***** While developing your program you can call the build_city
# ***** function with one of the "fixed" data sets, but your
# ***** final solution must work with "random_plan()" as the
# ***** argument to the build_city function.  Your program must
# ***** work for any data set that can be returned by the
# ***** random_plan function.
# build_city(fixed_plan_1) # <-- used for code development only, not marking
build_city(
    random_plan(print_plan=True), building_styles)  # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#