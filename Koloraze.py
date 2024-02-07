import random
import tkinter as tk
from PIL import Image, ImageTk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def deletenode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

def combine_hex_values(color1, color2, color3):
    weights = [0.5, 0.3, 0.2]
    
    # Remove the '#' symbol from color values if present
    color1 = color1.lstrip('#')
    color2 = color2.lstrip('#')
    color3 = color3.lstrip('#')
    
    red = int((int(color1[:2], 16) * weights[0] + int(color2[:2], 16) * weights[1] + int(color3[:2], 16) * weights[2]) / sum(weights))
    green = int((int(color1[2:4], 16) * weights[0] + int(color2[2:4], 16) * weights[1] + int(color3[2:4], 16) * weights[2]) / sum(weights))
    blue = int((int(color1[4:6], 16) * weights[0] + int(color2[4:6], 16) * weights[1] + int(color3[4:6], 16) * weights[2]) / sum(weights))

    zpad = lambda x: x if len(x) == 2 else '0' + x
    return zpad(hex(red)[2:]) + zpad(hex(green)[2:]) + zpad(hex(blue)[2:])

def target():
    colors = {
        'Red': 'FF0000',
        'Green': '008000',
        'Blue': '0000FF',
        'Black': '000000',
        'White': 'FFFFFF',
        'Yellow': 'FFFF00',
        'Purple': '800080'
    }
    target_color = random.sample(list(colors.values()), 3)
    return target_color

color1, color2, color3 = target()

target_hex = combine_hex_values(color1, color2, color3)

# Create the target color linked list
target_list = LinkedList()
target_list.insert(Node(color1))
target_list.insert(Node(color2))
target_list.insert(Node(color3))

# Create the display color linked list
display_list = LinkedList()
colors_to_insert = ["FF0000", "008000", "0000FF", "000000", "FFFFFF", "FFFF00", "800080"]
for color in colors_to_insert:
    display_list.insert(Node(color))

def color_checker(user_list):
    user_color_node = user_list.head
    if user_color_node is None:
        return False  
    
    count = 0  # Initialize a count variable to keep track of correct positions
    for i in range(3):
        user_color = user_color_node.data
        target_color_node = target_list.head  # Start iterating through target colors
        found_in_target = False
        for j in range(3):
            if user_color == target_color_node.data:
                found_in_target = True
                if user_color == target_color_node.data:
                    count += 1
                break
            target_color_node = target_color_node.next
        if not found_in_target:
            display_list.deletenode(user_color)
        user_color_node = user_color_node.next
    
    # Check if the user has won
    user_win = False
    if count == 3:
        user_win = True
    return user_win

user_list1 = LinkedList()
attempts = 0

user_list1 = LinkedList()
attempts = 0

def open_new_window():
    global attempts
    if attempts >= 3:
        window.destroy()  # Close the main window if the user didn't win in 3 attempts
        return
    
    attempts += 1
    window.withdraw()  # Hide the main window
    new_window = tk.Toplevel()
    new_window.configure(bg="#D0FFFC")
    new_window.geometry('1000x650')
    new_window.title("GAME")
    
    # Label for window
    label = tk.Label(new_window, text="LETS PLAY", font="Copperplate 22 bold", background="#f18ab0")
    label.pack(pady=10)

    # Create a label for the square box and set its background color
    target_color = "#"+target_hex
    box_label = tk.Label(new_window, height=8,width=16,bg=target_color)
    box_label.pack(padx=10, pady=10)
    
    output_frame = tk.Frame(new_window, bg="grey")
    output_frame.pack_configure(padx=10, pady=10)
    
    result_label = tk.Label(output_frame, width=30, height=3)
    result_label.pack_configure(padx=10, pady=10)
    
    # Create a canvas to display selected and mixed colors
    canvas = tk.Canvas(new_window, width=400, height=100, bg="white")
    canvas.pack(pady=20)

    user_choices = []

    def select_color(color):
        if len(user_choices) < 3:
            user_choices.append(color)
            label.config(text=color, background=color)
            color_buttons.config(state=tk.DISABLED)

    def update_canvas():
        canvas.delete("all")  # Clear the canvas
        if len(user_choices) >= 3:
            canvas.create_rectangle(10, 10, 110, 90, fill=user_choices[0])
            canvas.create_rectangle(120, 10, 220, 90, fill=user_choices[1])
            canvas.create_rectangle(230, 10, 330, 90, fill=user_choices[2])
            mixed_color = combine_hex_values(*user_choices)
            canvas.create_rectangle(340, 10, 440, 90, fill=f"#{mixed_color}")
            user_win = color_checker(user_list1)
            if user_win:
                result_label.config(text="Congratulations! You won!")
            else:
                result_label.config(text="Sorry, you did not win. Try again!")

    enter_button = tk.Button(new_window, text="ENTER", width=10, height=2, command=update_canvas)
    enter_button.pack(side="bottom")

    # Create buttons for each color in the linked list and place them at the bottom
    current = display_list.head
    while current:
        color = "#" + current.data
        color_buttons = tk.Button(new_window, width=10, height=7, bg=color, command=lambda c=color: select_color(c))
        color_buttons.pack(side=tk.LEFT, padx=30, pady=5)
        current = current.next

# Create the main window (KOLORAZE)
window = tk.Tk()
window.geometry('1000x650')
window.title("KOLORAZE")

# Load and display the background image
original = Image.open('name.jpg').resize((1000, 650))
bg_image = ImageTk.PhotoImage(original)

background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0)

# Create the "Start" button
start_button = tk.Button(window, text="START", width=15, height=3, command=open_new_window, background="blue")
start_button.place(x=455, y=437.5)

window.mainloop()