from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

canvas_height = 700 # pixels
canvas_width = 1100 # pixels
grass_depth = 95 # vertical depth of the "grass", in pixels
half_width = canvas_width // 2 # maximum x coordinate in either direction
grid_font = ('Arial', 10, 'normal') # font for drawing the grid
grid_size = 50 # gradations for the x and y scales shown on the screen
offset = 5 # offset of the x-y coordinates from the screen's edge, in pixels
max_height = canvas_height - grass_depth # maximum positive y coordinate
max_building_height = 575 # city ordinance maximum building height
site_width = 240 # maximum width of a building site
transition = []
cur_color = None
building = {
    'base': [],
    'floor': [],
    'roof': []
}

cur_section = 'base'

# Define the locations of building sites approved by the
# city council (arranged from back to front)
sites = [['Site 1', [-225, 0]],
         ['Site 2', [25, 0]],
         ['Site 3', [275, 0]],
         ['Site 4', [-375, -25]],
         ['Site 5', [-125, -25]],
         ['Site 6', [125, -25]],
         ['Site 7', [375, -25]],
         ['Site 8', [-275, -50]],
         ['Site 9', [-25, -50]],
         ['Site 10', [225, -50]]]

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
def create_drawing_canvas(show_grid = True):

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
    overlap = 25 # pixels
    penup()
    goto(-(half_width + overlap), -(grass_depth + overlap)) # bottom-left
    fillcolor('pale green')
    begin_fill()
    setheading(90) # face north
    forward(grass_depth + overlap * 2)
    right(90) # face east
    forward(canvas_width + overlap * 2)
    right(90) # face south
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
            write('| ' + str(x_coord), font = grid_font)

    # Optionally draw y coordinates on the left-hand edge of
    # the screen (to aid debugging and marking)
    if show_grid:
        for y_coord in range(-grid_size, max_height, grid_size):
            goto(-half_width + offset, y_coord - offset)
            write(y_coord, font = grid_font)
        goto(-half_width + offset, max_building_height - 5)
        write('Maximum allowed building height', font = grid_font)

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
            write(site_name + ': ' + str(location), font = grid_font)
     
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
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

def pendown_start():
    pendown()
    begin_fill()
    

def add_pos(*pos):
    goto(*pos)

    if isdown():
        transition.append((xcor(),ycor()))
    
def back():
    building[cur_section][-1].pop()
    undo()

def penup_transition():
    global transition        
    penup()
    end_fill()
    if len(transition) != 0:
        building[cur_section].append({cur_color: transition})
        transition = []
    
def black():
    global cur_color
    color('black')
    cur_color = "black"
        
def yellow():
    global cur_color
    color('yellow')
    cur_color = "yellow"

def pink():
    global cur_color
    color('pink')
    cur_color = "pink"

def blue():
    global cur_color
    color('blue')
    cur_color = "blue"

def green():
    global cur_color
    color('green')
    cur_color = "green"

def orange():
    global cur_color
    color('orange')
    cur_color = "orange"

def cyan():
    global cur_color
    color('cyan')
    cur_color = "cyan"

def base():
    global cur_section
    cur_section = 'base'
    goto(-320,0)
    
def floor():
    global cur_section
    cur_section = 'floor'

def roof():
    global cur_section
    cur_section = 'roof'

def left():
    x,y = position()
    add_pos((x - 100,y))
    
def ri():
    x,y = position()
    add_pos((x + 100,y))

def up():
    x,y = position()
    add_pos((x,y + 60))

def down():
    x,y = position()
    add_pos((x,y - 60))

def window():
    dot(23,cur_color)


    if isdown():
        transition.append(('dot',(xcor(),ycor())))

create_drawing_canvas()

pendown()
onscreenclick(add_pos)

onkeypress(penup_transition,'u') # bringns the pen up, stops drawing
onkeypress(pendown_start,'d') # brings the pen down, starts drawing

onkeypress(clear,'c') # clears the page
# onkeypress(back,'b') # clears the page

onkeypress(black,'1') # sets fill color to red
onkeypress(yellow,'2') # sets fill color to green
onkeypress(pink,'3') # sets fill color to purple
onkeypress(blue,'4') # sets fill color to purple
onkeypress(green,'5') # sets fill color to purple
onkeypress(orange,'6') # sets fill color to purple
onkeypress(cyan,'7') # sets fill color to purple


onkeypress(base,'B') # sets fill color to purple
onkeypress(floor,'F') # sets fill color to purple
onkeypress(roof,'R') # sets fill color to purple
onkeypress(window,'C') # sets fill color to purple


onkeypress(up,'f')
onkeypress(down,'b')
onkeypress(left,'l')
onkeypress(ri,'r')

listen()

release_drawing_canvas()

print(building)

