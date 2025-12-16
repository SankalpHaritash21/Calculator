import tkinter as tk

root= tk.Tk()

class Calculator:
    def __init__(self, root):

        self.button={
            '7':(0,0), '8':(0,1), '9':(0,2),
            '4':(1,0), '5':(1,1), '6':(1,2),
            '1':(2,0), '2':(2,1), '3':(2,2),
            '0':(3,1)
        }

        self.opreator={
            '/':(0,3), '*':(1,3), '-':(2,3), '+':(3,3),
            'C':(3,0), '=':(3,2),
            '<-':(4,3)

        }

        self.operator_set= {'/', '*', '-', '+'}

        self.memory_buttons=[
            ("M+", self.memory_add),
            ("M-", self.memory_subtract),
            ("MR", self.memory_recall)
        ]


        self.root=root
        self.memory=0 #State Variable Example
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg="#121212")
        self.display= tk.Entry(root,
            font=("Arial", 20),
            justify="right",
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#333333",
            highlightcolor="#333333",
            readonlybackground="#1E1E1E")
        
        self.display.config(state="readonly")
        self.display.pack(fill='x', padx=10, pady=10)

        self.button_frame= tk.Frame(root, bg='#121212')
        self.button_frame.pack()


        
        
        
        for text, (r,c) in self.button.items():
            btn=tk.Button(self.button_frame, text=text, font=("Arial",18), width=5, height=2, bg='#2A2A2A', fg='white',
                    activebackground='#3A3A3A',
                    activeforeground='white',
                    borderwidth=0,
                command=lambda t=text: self.press(t))
        
            btn.grid(row=r, column=c, padx=5, pady=5)



        for op, (r,c) in self.opreator.items():
            if op == 'C':
                cmd=self.clear
            elif op == '=':
                cmd=self.calculate
            elif op == '<-':
                cmd=self.delete_last
            else:
                cmd=lambda o=op: self.press(o)

            color = "#FF9500" if op in self.operator_set or op in ['=', 'C'] else "#2A2A2A"

            btn = tk.Button(
                self.button_frame,
                text=op,
                font=("Arial", 18),
                width=5,
                height=2,
                bg=color,
                fg="white",
                activebackground="#FFA733",
                activeforeground="white",
                borderwidth=0,
                command=cmd
            )
            btn.grid(row=r, column=c, padx=5, pady=5)

        self.root.bind("<Key>", self.keyboard_handler)

        for i, (text, cmd) in enumerate(self.memory_buttons):
            btn = tk.Button(
                self.button_frame,
                text=text,
                font=("Arial", 18),
                width=5,
                height=2,
                bg="#444444",
                fg="white",
                borderwidth=0,
                command=cmd
                )
            btn.grid(row=4, column=i, padx=5, pady=5)

    def memory_add(self):
        try:
            self.memory += float(self.display.get())
        except:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.display.get())
        except:
            pass

    def memory_recall(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(self.memory))
        self.display.config(state="readonly")






    def press(self, key):
        self.display.config(state="normal")
        current= self.display.get()

        if not current and key in self.operator_set:
            self.display.config(state="readonly")
            return
        
        if current and current[-1] in self.operator_set and key in self.operator_set:
            self.display.config(state="readonly")
            return
        
        self.display.insert(tk.END, key)
        self.display.config(state="readonly")

    def clear(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.config(state="readonly")

    def calculate(self):
        self.display.config(state="normal")
        try:
            result= eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
        self.display.config(state="readonly")

    def delete_last(self):
        self.display.config(state="normal")
        current= self.display.get()

        if current:
            self.display.delete(len(current)-1, tk.END)

        self.display.config(state="readonly")

    def keyboard_handler(self, event):
        key = event.keysym
        char= event.char

        if char.isdigit() or char in self.operator_set:
            self.press(char)
        elif key == "Return":
            self.calculate()
        elif key == "BackSpace":
            self.delete_last()
        elif key == "Escape":
            self.clear()


    

    


app= Calculator(root)

# app.memory_add()  # Example usage of memory function
# app.memory_recall()  # Example usage of memory function
root.mainloop()