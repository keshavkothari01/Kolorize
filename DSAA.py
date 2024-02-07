import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def combine_hex_values(color1, color2, color3):
    weights = [0.5, 0.3, 0.2]
    
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

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def deletenode(self, node):
        temp = self.head
        if node == self.head.data:
            self.head = temp.next
            del temp
        else:
            prev = None
            while temp is not None and temp.data != node:
                prev = temp
                temp = temp.next
            if temp is not None:
                prev.next = temp.next
                del temp

# Create the target color linked list
target_list = LinkedList()
target_list.insert(Node(color1))
target_list.insert(Node(color2))
target_list.insert(Node(color3))

# Create the display color linked list
display_list = LinkedList()
display_list.insert(Node("FF0000"))
display_list.insert(Node("008000"))
display_list.insert(Node("0000FF"))
display_list.insert(Node("000000"))
display_list.insert(Node("FFFFFF"))
display_list.insert(Node("FFFF00"))
display_list.insert(Node("800080"))

chance = 0

def color_checker(user_list):
    user_color_node = user_list.head
    count = 0  
    for i in range(3):
        user_color = user_color_node.data
        target_color_node = target_list.head  # Start iterating through target colors.
        found_in_target = False
        for j in range(3):
            if user_color == target_color_node.data:
                found_in_target = True
                if user_color == target_color_node.data:
                    print(f'Color {user_color} is correct and at the correct position')
                    count += 1
                else:
                    print(f'Color {user_color} is correct but at the wrong position')
                break
            target_color_node = target_color_node.next
        if not found_in_target:
            print(f'Color {user_color} is not in the target colors')
            display_list.deletenode(user_color)
        user_color_node = user_color_node.next
    
    # Check if the user has won
    user_win = False
    if count == 3:
        user_win = True
        print("Congratulations! You won!")
    return user_win

# User input linked list
user_list1 = LinkedList()
values = []
# print(f'\nTarget color is: {target_hex}')
while chance < 3:  # 3 times
    user_list1 = LinkedList()
    values = []
    print(f'\nTarget color is: {target_hex}')
    for i in range(3):
        display_list.printlist()  
        user_choice = input(f'Choose color {i+1}: ')
        values.append(user_choice)

    # Insert user input colors into the linked list
    for i in values:
        user_list1.insert(Node(i))

    print(f'\nTarget color is: {target_hex}')
    user_mix = combine_hex_values(values[0], values[1], values[2])
    print(f'User Mix: {user_mix}')

    # Check user input against target colors and check for a win
    user_win = color_checker(user_list1)
    
    chance += 1
    if user_win:
        break

if not user_win:
    print("Sorry, you did not win. HAHAHAHA")
# import tkinter as tk

# root = tk.Tk()
# root.title("Button with Filled Color")

# # Set the background color of the button
# button_bg_color = "blue"

# # Create the button with the specified background color
# button = tk.Button(root, text="\t \t", bg=button_bg_color)
# button.pack(pady=20, padx=50)

# root.mainloop()


