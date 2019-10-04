# from tkinter import *
#
# P = 0
#
#
# def val(var, v):
#     print(var)
#     var = int(v.get())
#     # print(var)
#     return var
#
#
# class GUI:
#     my_window = Tk()
#
#     def frameP(self):
#         frame_p = Frame(self.my_window)
#         label_p = Label(frame_p, text="Enter Power transmitted (P) in kW : ")
#         entry_p = Entry(frame_p)
#         btn_submit_p = Button(frame_p, text="       Submit      ", command=frame_p.grid_forget())
#         label_p.grid(row=0, column=0)
#         entry_p.grid(row=0, column=1)
#         btn_submit_p.grid(row=1, columnspan=2)
#         frame_p.grid(row=0, column=0)
#         return int(entry_p.get())
#
#     my_window.mainloop()
#
#
# gui = GUI()
# print(gui.frameP())


# import tkinter as tk
#
#
# class Page(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#
#     def show(self):
#         self.lift()
#
#
# class Page1(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is page 1")
#         label.pack(side="top", fill="both", expand=True)
#
#
# class Page2(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is page 2")
#         label.pack(side="top", fill="both", expand=True)
#
#
# class Page3(Page):
#     def __init__(self, *args, **kwargs):
#         Page.__init__(self, *args, **kwargs)
#         label = tk.Label(self, text="This is page 3")
#         label.pack(side="top", fill="both", expand=True)
#         global entry
#         entry = tk.Entry(self)
#         entry.pack(side="bottom", fill="both")
#
#
# class MainView(tk.Frame):
#     def __init__(self, *args, **kwargs):
#         tk.Frame.__init__(self, *args, **kwargs)
#         p1 = Page1(self)
#         p2 = Page2(self)
#         p3 = Page3(self)
#         print(entry.get())
#         buttonframe = tk.Frame(self)
#         container = tk.Frame(self)
#         buttonframe.pack(side="top", fill="x", expand=False)
#         container.pack(side="top", fill="both", expand=True)
#
#         p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#         p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
#
#         b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
#         b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
#         b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
#
#         b1.pack(side="left")
#         b2.pack(side="left")
#         b3.pack(side="left")
#
#         p1.show()
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     main = MainView(root)
#     main.pack(side="top", fill="both", expand=True)
#     root.wm_geometry("400x400")
#     root.mainloop()


import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Begin", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Click Here",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        # button2 = tk.Button(self, text="Visit Page 2",
        #                     command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageOne(tk.Frame):
    def multifunction(*args):
        for function in args:
            function()

    def go_to(self):
        # Add something to do
        self.controller.show_frame("PageTwo")

    def val(self):
        global p
        p = entry_p.get()
        print(p)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Enter Power transmitted (P) in kW : ", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        global entry_p
        entry_p = tk.Entry(self)
        entry_p.pack()
        # button1 = tk.Button(self, text="Back to Home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        cb = lambda: self.multifunction(self.val, self.go_to())
        # button2 = tk.Button(self, text="Next", command=self.val)
        button2 = tk.Button(self, text="Next", command=cb)
        button2.pack()
        # button2.configure(command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        px = tk.Label(self, text=entry_p.get())
        px.pack(pady=10, padx=10)
        # button1 = tk.Button(self, text="Back to Home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()