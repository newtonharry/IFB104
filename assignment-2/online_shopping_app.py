# -----Statement of Authorship----------------------------------------#
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
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
# --------------------------------------------------------------------#


# -----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
# --------------------------------------------------------------------#


# -----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(
    url="http://www.wikipedia.org/",
    target_filename="download",
    filename_extension="html",
):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception(
            "Download error - Access denied to document at URL '" + url + "'"
        )
    except:
        raise Exception(
            "Download error - Something went wrong when trying to download "
            + "the document at URL '"
            + url
            + "'"
        )

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode("UTF-8")
    except UnicodeDecodeError:
        raise Exception(
            "Download error - Unable to decode document at URL '"
            + url
            + "' as Unicode text"
        )

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(
            target_filename + "." + filename_extension, "w", encoding="UTF-8"
        )
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception(
            "Download error - Unable to write to file '" + target_file + "'"
        )

    # Return the downloaded document to the caller
    return web_page_contents


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#


# Setup variables
website = "https://www.amazon.com.au/gp/rss/bestsellers/"
web_content = {"electronics": [], "home": [], "pc": [], "shoes": []
}
selected_category = ""
cart = []


# regular expression used to find xml components
information_extractor = re.compile(
    r"<item>\s*<title([^<]+)</title>(?:[^<]|<(?!/item>))*?"
    '<img src="([^"]+)"[^>]*>(?:[^<]|<(?!/item>))*?'
    "</span>(?:[^<]|<(?!/item>))*?"
    "<b>(\$[\d.]+(?: - \$[\d.]+)?)</b>"
)


# Download up to date files
def download_info(category):
    webpage_contents = download(website + category, category)
    products = information_extractor.findall(webpage_contents)
    return products


# function to get already archived files
def get_archived_info(category):
    with open(f"{category}.html", "r") as f:
        info = f.read()
        products = information_extractor.findall(info)
        return products


# Function to create a new window for each category
def create_window(title, products):
    window = Toplevel(master)
    window.title(title)
    window.geometry("1000x400")
    window.configure(bg="forest green")

    for product in products:
        frame = Frame(window, bg="forest green", pady=4)
        frame.grid(stick=W)

        product = Label(
            frame,
            text="{}({})".format(product[0][1:], product[2]),
            bg="forest green",
            font=("Arial Bold", 9),
        )

        product.grid(column=0, row=0, sticky="W")

    txtframe = Frame(window, bd=2, bg="white")
    txtframe.pack()

    products_infomation = Label(txtframe, text=product)
    products_infomation.pack()

    window.mainloop()


# Define functions to view different types of products


def select_electronics():
    global selected_category

    selected_category = "electronics"
    text = get_archived_info("electronics")
    web_content[selected_category] = text
    window = create_window("Electronics", text)


def select_home():
    global selected_category

    selected_category = "home"
    text = get_archived_info("home")
    web_content[selected_category] = text
    create_window("Home", text)


def select_pc():
    global selected_category

    selected_category = "pc"
    text = download_info("pc")
    web_content[selected_category] = text
    window = create_window("PC", text)


def select_shoes():
    global selected_category

    selected_category = "shoes"
    text = download_info("shoes")
    web_content[selected_category] = text
    window = create_window("Shoes", text)


# Add information about the product to the cart array
def add_to_cart():
    global web_content
    global cart

    cart.append(web_content[selected_category][int(item_selector.get()) - 1])


# Generate an invoice html file based upon the cart array
def invoice():
    global cart

    with open("invoice.html", "w") as f:
        f.write("<html>")

        f.write("<body>")

        f.write("<center><h1>Your Electronics Store Invoice</h1></center>")

        for product in cart:
            f.write(f"<center><p>{product[0][1:]}({product[2]})</p></center>")
            f.write(f'<center><img src="{product[1]}"></center>')

        f.write("<center>")
        f.write("<h3>Bargain Bin stocked from:</h3>")
        f.write("<li>https://www.amazon.com.au/gp/rss/bestsellers/electronics</li>")
        f.write("<li>https://www.amazon.com.au/gp/rss/bestsellers/home</li>")
        f.write("</center>")

        f.write("<center>")
        f.write("<h3>Todays Specials stocked from:</h3>")
        f.write("<li>https://www.amazon.com.au/gp/rss/bestsellers/pc</li>")
        f.write("<li>https://www.amazon.com.au/gp/rss/bestsellers/shoes</li>")
        f.write("</center>")

        f.write("</body>")

        f.write("</html>")

    write_to_database()


# Write all the purchased items to the database
def write_to_database():
    with connect("shopping_cart.db") as d:
        db = d.cursor()

        for product in cart:
            title, _, price = product
            sql = f"INSERT INTO ShoppingCart(Item,Price) VALUES ('{title}' , '{price}')"
            db.execute(sql)


# Create the tk window
master = Tk()
master.title("Hot Electronics")
master.geometry("600x600")
master.configure(bg="white")

title = Label(
    master, text="Welcome to Hot Electronics Tech Store!", font=("Arial Bold", 20)
)

# Logo
img = PhotoImage(file="logo.gif")
logo = Label(master, image=img)
logo.image = logo
logo.place(x=250, y=140)  # Image positioning

# Bargains and specials grame and label
Bargains_label = Label(master, font=("Arial Bold", 12), text=("Bargian Bin!"))

Bargains_frame = Frame(
    master, bd=2, bg="blue"
)  # frame holding Electronics and Home radiobuttons
Bargains_frame.pack()

electronics_radio_button = Radiobutton(
    Bargains_frame,
    font=("Arial", 10),
    text=("Electronics"),
    value=1,
    command=select_electronics,
)
electronics_radio_button.pack(side=LEFT)

Home = Radiobutton(
    Bargains_frame, font=("Arial", 10), text=("Home"), value=2, command=select_home
)
Home.pack(side=LEFT)


# pc and shoe frame label
Specials_label = Label(master, font=("Arial Bold", 11), text=("Todays Specials"))


# frame holding PC and Shoes radiobuttons
Specials_frame = Frame(master, bd=2, bg="blue")
Specials_frame.pack()

PC = Radiobutton(
    Specials_frame, font=("Arial", 10), text=("PC"), value=3, command=select_pc
)
PC.pack(side=LEFT)

Shoes = Radiobutton(
    Specials_frame, font=("Arial", 10), text=("Shoes"), value=4, command=select_shoes
)
Shoes.pack(side=LEFT)


# Spin box so user can select product
item_selection = Label(master, text="Item Number")

item_selector = Spinbox(master, from_=1, to=10)
item_selector.pack()

# frame holding cart and invoice buttons
buttons = Frame(master, bd=2, bg="blue")

addcart = Button(buttons, text=("Add to Cart"), command=add_to_cart)
addcart.pack(side=LEFT)

invoice = Button(buttons, text=("Print Invoice"), command=invoice)
invoice.pack(side=RIGHT)


# postioning of all the widgets (just move the x,y co-ords around)
title.place(x=45, y=20)

Bargains_label.place(x=20, y=140)  # Frame Labels
Specials_label.place(x=20, y=70)


Bargains_frame.place(x=40, y=100)  # RadioButton Frames
Specials_frame.place(x=40, y=170)

item_selector.place(x=20, y=235)
item_selection.place(x=20, y=215)

buttons.place(x=20, y=330)

master.mainloop()
