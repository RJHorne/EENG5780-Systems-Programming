import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
def addarc(event):
    arc = C.create_arc(coord, start=0, extent=event.x, fill="red")
    print(event.x)

def clear(event):
    C.delete('all')


C.pack()
C.bind("<B1-Motion>", addarc)
C.bind("<Button-2>", clear)
top.mainloop()