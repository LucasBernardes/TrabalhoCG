from Tkinter import *
import ttk
from logic import *

def init():
    def quit():
        root.quit()

    def setpersp1():
        global perspective
        perspective = 1
    def setpersp2():
        global perspective
        perspective = 2

    def plot():
        if (perspective == 1):
            pers = True
        else:
            pers = False
        
        C[0] = float(c1_entry.get())
        C[1] = float(c2_entry.get())
        C[2] = float(c3_entry.get())
    
        ponto1[0] = float(p1x_entry.get())
        ponto1[1] = float(p1y_entry.get())
        ponto1[2] = float(p1z_entry.get())

        ponto2[0] = float(p2x_entry.get())
        ponto2[1] = float(p2y_entry.get())
        ponto2[2] = float(p2z_entry.get())

        ponto3[0] = float(p3x_entry.get())
        ponto3[1] = float(p3y_entry.get())
        ponto3[2] = float(p3z_entry.get())

        display(C, ponto1, ponto2, ponto3, pers, fl.get())
        init()
        
    #init
    root = Tk()
    root.title("Plotter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    # variaveis
    ponto1  = [0.0, 0.0, 0.0]
    ponto2  = [0.0, 0.0, 0.0]
    ponto3  = [0.0, 0.0, 0.0]
    C       = [0.0, 0.0, 0.0]

    c1_entry = ttk.Entry(mainframe, width=5)
    c2_entry = ttk.Entry(mainframe, width=5)
    c3_entry = ttk.Entry(mainframe, width=5)

    c1_entry.grid(column=2, row=2, sticky=(W, E))
    c2_entry.grid(column=2, row=3, sticky=(W, E))
    c3_entry.grid(column=2, row=4, sticky=(W, E))

    ttk.Label(mainframe, text="Ponto de Vista").\
            grid(column=1, row=1, columnspan=2)
    ttk.Label(mainframe, text="A").grid(column=1, row=2, sticky=W)
    ttk.Label(mainframe, text="B").grid(column=1, row=3, sticky=W)
    ttk.Label(mainframe, text="C").grid(column=1, row=4, sticky=W)

    p1x_entry = ttk.Entry(mainframe, width=5)
    p1y_entry = ttk.Entry(mainframe, width=5)
    p1z_entry = ttk.Entry(mainframe, width=5)

    p2x_entry = ttk.Entry(mainframe, width=5)
    p2y_entry = ttk.Entry(mainframe, width=5)
    p2z_entry = ttk.Entry(mainframe, width=5)

    p3x_entry = ttk.Entry(mainframe, width=5)
    p3y_entry = ttk.Entry(mainframe, width=5)
    p3z_entry = ttk.Entry(mainframe, width=5)

    p1x_entry.grid(column=4, row=3, sticky=(W, E))
    p1y_entry.grid(column=5, row=3, sticky=(W, E))
    p1z_entry.grid(column=6, row=3, sticky=(W, E))

    p2x_entry.grid(column=4, row=4, sticky=(W, E))
    p2y_entry.grid(column=5, row=4, sticky=(W, E))
    p2z_entry.grid(column=6, row=4, sticky=(W, E))

    p3x_entry.grid(column=4, row=5, sticky=(W, E))
    p3y_entry.grid(column=5, row=5, sticky=(W, E))
    p3z_entry.grid(column=6, row=5, sticky=(W, E))
    
    ttk.Label(mainframe, text="Plano de Projecao").\
            grid(column=3, row=1, columnspan=4)
    ttk.Label(mainframe, text="X").grid(column=4, row=2)
    ttk.Label(mainframe, text="Y").grid(column=5, row=2)
    ttk.Label(mainframe, text="Z").grid(column=6, row=2)

    ttk.Label(mainframe, text="P1").grid(column=3, row=3, sticky=W)
    ttk.Label(mainframe, text="P2").grid(column=3, row=4, sticky=W)
    ttk.Label(mainframe, text="P3").grid(column=3, row=5, sticky=W)

    fl = ttk.Combobox(mainframe)
    fl['values'] = ('carro.txt', 'casa.txt', 'cubo.txt')
    fl.grid(column=2, row=8, columnspan=5, sticky=(W,E))

    ttk.Label(mainframe, text="Objeto").grid(column=1, row=8, sticky=W)

    opt = IntVar()

    perspectiva = ttk.\
            Radiobutton(mainframe, text='Perspectiva', variable=opt,command = setpersp1, \
            value=1).grid(column=2, row=9)

    projetiva = ttk.\
            Radiobutton(mainframe, text='Projetiva', variable=opt, command = setpersp2, \
            value=2).grid(column=4, row=9)
    
    button = ttk.Button(mainframe, text='Plottar', command=plot)
    button.grid(column=2, row=10, columnspan=2)

    exit_button = ttk.Button(mainframe, text='Exit', command=quit)
    exit_button.grid(column=5, row=10, columnspan=2)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

init()
