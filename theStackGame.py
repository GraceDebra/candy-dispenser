from tkinter import Button, Canvas, LEFT, RIGHT, RAISED, Label, Tk, FLAT, SUNKEN, GROOVE, RIDGE 
from tkinter.messagebox import showerror, showinfo

class Candy_Dispenser:
    #initialize the spring
    def __init__(self, window = Tk):
        self.window = window

        #create an empty stack 
        self.candy_stack = []
        self.max_size = 10   #maximum number of candies

        #set dimensions of the whole spring
        self.spring_right = 287
        self.spring_left = 73
        self.spring_top = 120
        self.spring_bottom = 600

        self.spring_thickness = 5

        self.spring_displacement = 30

        # defining updated spring variables
        self.new_bar_bottom = self.spring_top + 30
        self.new_bar_cx = (self.spring_left + self.spring_right) / 2
        self.new_bar_cy = (self.spring_top + self.spring_bottom) / 2

        #deifining initial spring positions (individual lines forming the spring)
        self.a_y = 120
        self.b_y = 220
        self.c_y = 330
        self.d_y = 430
        self.e_y = 530

        #organizing the GUI
        self.left_panel = Canvas(self.window, width= window_width /2, height = window_height)
        self.left_panel.pack(side=LEFT)
        self.right_panel = Canvas(self.window, width= window_width /2, height = window_height)
        self.right_panel.pack(side=RIGHT)
        self.name_label = Label(self.right_panel, text="GRACE DEBRA OCHIENG SCT211-0006/2021", font = "Arial")
        self.name_label.place(x = 0, y = 10)

        #explicitly drawing the spring
        self.a = self.left_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.a_y,
                                             width = self.spring_thickness, smooth = True)
        self.a_b1 = self.left_panel.create_line(self.spring_left, self.a_y, self.spring_right, self.b_y,
                                             width = self.spring_thickness, smooth = True)
        self.a_b2 = self.left_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.a_y,
                                             width = self.spring_thickness, smooth = True)
        self.b = self.left_panel.create_line(self.spring_left, self.b_y, self.spring_right, self.b_y,
                                             width = self.spring_thickness, smooth = True)
        self.b_c1 = self.left_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.b_y,
                                             width = self.spring_thickness, smooth = True)
        self.b_c2 = self.left_panel.create_line(self.spring_right, self.c_y, self.spring_left, self.b_y,
                                             width = self.spring_thickness, smooth = True)
        self.c = self.left_panel.create_line(self.spring_left, self.c_y, self.spring_right, self.c_y,
                                             width = self.spring_thickness, smooth = True)
        self.c_d1 = self.left_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.c_y,
                                             width = self.spring_thickness, smooth = True)
        self.c_d2 = self.left_panel.create_line(self.spring_right, self.d_y, self.spring_left, self.c_y,
                                             width = self.spring_thickness, smooth = True)
        self.d = self.left_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.e_y,
                                             width = self.spring_thickness, smooth = True)
        self.d_e1 = self.left_panel.create_line(self.spring_left, self.e_y, self.spring_right, self.d_y,
                                             width = self.spring_thickness, smooth = True)
        self.d_e2 = self.left_panel.create_line(self.spring_left, self.d_y, self.spring_right, self.d_y,
                                             width = self.spring_thickness, smooth = True)
        self.left_panel.create_line(self.spring_left, self.e_y, self.spring_right, self.e_y,
                                             width = self.spring_thickness, smooth = True)
        
        #set the positions for the candy dispenser
        self.left_panel.create_line(70,70,70,540, width = 3)
        self.left_panel.create_line(290,70,290,540, width = 3)
        self.left_panel.create_line(290,540,70,540, width = 3)

        #creating the buttons
        Button(self.right_panel, text = "push", fg = "blue", bg = "grey", font =("Arial", 14, "bold"),
               relief = RIDGE, bd = 7, command = self.push).place(x = 52, y = 100)
        Button(self.right_panel, text = "Pop", fg = "blue", bg = "grey", font =("Arial", 14, "bold"),
               relief = RIDGE, bd = 7, command = self.pop).place(x = 52, y = 150)
        Button(self.right_panel, text = "Top", fg = "blue", bg = "grey", font =("Arial", 14, "bold"),
               relief = RIDGE, bd = 7, command = self.peek).place(x = 52, y = 200)
        Button(self.right_panel, text = "Length", fg = "blue", bg = "grey", font =("Arial", 14, "bold"),
               relief = RIDGE, bd = 7, command = self.report_size).place(x = 52, y = 250)
        Button(self.right_panel, text = "Is empty", fg = "blue", bg = "grey", font =("Arial", 14, "bold"),
               relief = RIDGE, bd = 7, command = self.report_empty_stat).place(x = 50, y = 321)
        
        #defining methods for the stack ADT operations
    def push(self):
        if self.size() < self.max_size:
            self.candy_stack.append(self.draw_candy())
            self.update_dispenser('push')
        else:
            showerror("Candy dispenser is full")

    def pop(self):
        if self.size() > 0:
            candy = self.candy_stack.pop()
            self.left_panel.delete(candy['bar'])
            self.left_panel.delete(candy['label'])

            self.update_dispenser('pop')
            showinfo('popped', f'removed"{candy["tag"]}"')

        else:
            showerror('Error: Candy dispenser is empty')

    def draw_candy(self):
        bar = self.left_panel.create_oval(self.spring_left, self.spring_top, self.spring_right,
                                              self.new_bar_bottom, fill = "pink")
        tag = f'Candy {self.size() + 1}'
        label = self.left_panel.create_text(self.new_bar_cx, self.new_bar_cy, text = tag, fill = "white")
        return {'bar': bar, 'label': label, 'tag': tag}
        
    def update_dispenser(self, mode):
        if mode == 'push':
            for i in range(self.size()):
                self.update_candy_pos(self.candy_stack[i], (self.size() - 1) -i)

            self.a_y += self.spring_displacement
            self.b_y += self.spring_displacement / 1.5
            self.c_y += self.spring_displacement / 3
            self.d_y += self.spring_displacement / 6

        elif mode == 'pop':
            stack_size = self.size()
            for i in range(stack_size):
                self.update_candy_pos(self.candy_stack[i], stack_size - (i + 1))

            self.a_y -= self.spring_displacement
            self.b_y -= self.spring_displacement / 1.5
            self.c_y -= self.spring_displacement / 2
            self.d_y -= self.spring_displacement / 3

                
        else:
            raise Exception
            
        self.left_panel.coords(self.a, self.spring_left, self.a_y, self.spring_right, self.a_y)
        self.left_panel.coords(self.a_b1, self.spring_left, self.a_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.a_b2, self.spring_left, self.b_y, self.spring_right, self.a_y)
        self.left_panel.coords(self.b, self.spring_left, self.b_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.b_c1, self.spring_left, self.c_y, self.spring_right, self.b_y)
        self.left_panel.coords(self.b_c2, self.spring_right, self.c_y, self.spring_left, self.b_y)
        self.left_panel.coords(self.c, self.spring_left, self.c_y, self.spring_right, self.c_y)
        self.left_panel.coords(self.c_d1, self.spring_left, self.c_y, self.spring_right, self.d_y)
        self.left_panel.coords(self.c_d2, self.spring_right, self.c_y, self.spring_left, self.d_y)
        self.left_panel.coords(self.d, self.spring_left, self.d_y, self.spring_right, self.d_y)
        self.left_panel.coords(self.d_e1, self.spring_left, self.d_y, self.spring_right, self.e_y)
        self.left_panel.coords(self.d_e2, self.spring_right, self.d_y, self.spring_left, self.e_y)

        self.left_panel.update()

    def update_candy_pos(self, candy, y):
        updated_bar_top = self.spring_top + (self.spring_displacement * y)
        updated_bar_bottom = (self.new_bar_bottom + self.spring_displacement * y)

        self.left_panel.coords(
            candy['bar'], self.spring_left, updated_bar_top, self.spring_right, updated_bar_bottom
        )
        self.left_panel.coords(
                candy['label'], self.new_bar_cx, (updated_bar_top + updated_bar_bottom) / 2
        )
    def size(self):
        return len(self.candy_stack)
        
    def report_size(self):
        showinfo('size', f'The candy dispenser size is {self.size()}')

    def peek(self):
        if self.is_empty():
            showerror('Candy dispenser is empty')
        else:
            showinfo('Top', f'{self.candy_stack[-1]["tag"]}')

    def is_empty(self):
        if self.size() == 0:
            return True
        return False
        
    def report_empty_stat(self):
        message = 'False'
        if self.is_empty():
            message = 'True'
        showinfo(message)

if __name__ == '__main__':
    window_height = 650
    window_width = 750

root = Tk()
root.title('Candy dispenser')
root.maxsize(window_width, window_height)
root.minsize(window_width, window_height)
Candy_Dispenser(root)
root.mainloop()




        



