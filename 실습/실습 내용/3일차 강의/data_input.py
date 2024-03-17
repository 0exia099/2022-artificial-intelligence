from tkinter import *

def process():
    print(f"이름={entry[0].get()}, 직업={entry[1].get()}, 나이={entry[2].get()}")

def reset():
    for x in range(3):
        entry[x].delete(0, END)
    entry[0].focus_set()
    
labels = ["이름", "직업", "나이"]
window = Tk()

entry = []
for x in range(3):
    Label(window, text=labels[x]).grid(row=x, column=0)
    entry.append(Entry(window))
    entry[x].grid(row=x, column=1)

frame = Frame(window)
frame.grid(row=3, column=1)
Button(frame, text="처리", padx=15, command=process).pack(side=LEFT)
Button(frame, text="다시 입력", command=reset).pack(side=LEFT)

window.mainloop()