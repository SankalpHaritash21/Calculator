import tkinter as tk

button={
    '7':(0,0), '8':(0,1), '9':(0,2),
    '4':(1,0), '5':(1,1), '6':(1,2),
    '1':(2,0), '2':(2,1), '3':(2,2),
    '0':(3,1)
}

opreator={
    '/':(0,3), '*':(1,3), '-':(2,3), '+':(3,3),
    'C':(3,0), '=':(3,2),
    '<-':(4,2)

}

operator_set= {'/', '*', '-', '+'}


root= tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.resizable(False, False)


display= tk.Entry(root, font=('Arial',20),justify="right")

display.pack(fill='x', padx=10, pady=10)

def press(key):
    display.config(state="normal")
    current= display.get()

    if not current and key in operator_set:
        display.config(state="readonly")
        return
    
    if current and current[-1] in operator_set and key in operator_set:
        display.config(state="readonly")
        return
    
    display.insert(tk.END, key)
    display.config(state="readonly")


def clear():
    display.config(state="normal")
    display.delete(0, tk.END)
    display.config(state="readonly")

def calculate():
    display.config(state="normal")
    try:
        result= eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
    display.config(state="readonly")

def delete_last():
    display.config(state="normal")
    current= display.get()

    if current:
        display.delete(len(current)-1, tk.END)

    display.config(state="readonly")

def keyboard_handler(event):
    key = event.keysym
    char= event.char

    if char.isdigit() or char in operator_set:
        press(char)
    elif key == "Return":
        calculate()
    elif key == "BackSpace":
        delete_last()
    elif key == "Escape":
        clear()


button_Frame= tk.Frame(root)
button_Frame.pack()

for text, (r,c) in button.items():
    btn=tk.Button(button_Frame, text=text, font=("Arial",18), width=5, height=2,
              command=lambda t=text: press(t))
    
    btn.grid(row=r, column=c, padx=5, pady=5)

for op, (r,c) in opreator.items():
    if op == 'C':
        cmd=clear
    elif op == '=':
        cmd=calculate
    elif op == '<-':
        cmd=delete_last
    else:
        cmd=lambda o=op: press(o)

    btn = tk.Button(
        button_Frame,
        text=op,
        font=("Arial", 18),
        width=5,
        height=2,
        command=cmd
    )
    btn.grid(row=r, column=c, padx=5, pady=5)



root.bind("<Key>", keyboard_handler)
root.mainloop()