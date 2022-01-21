# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showerror, showwarning, showinfo
# import matplotlib
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg,
#     NavigationToolbar2Tk
# )

from startLoop import initialize

initialize()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# #send 40 bits in tandem with clock signal
#
# # class App(tk.Tk):
# #     root = tk.Tk()
# #     root.title('Tkinter MessageBox')
# #     root.resizable(False, False)
# #     root.geometry('300x150')
# #
# #     #
# #     options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}
# #
# #     ttk.Button(
# #         root,
# #         text='Show an error message',
# #         command=lambda: showerror(
# #             title='Error',
# #             message='This is an error message.')
# #     ).pack(**options)
# #
# #     ttk.Button(
# #         root,
# #         text='Show an information message',
# #         command=lambda: showinfo(
# #             title='Information',
# #             message='This is an information message.')
# #     ).pack(**options)
# #
# #     ttk.Button(
# #         root,
# #         text='Show an warning message',
# #         command=lambda: showwarning(
# #             title='Warning',
# #             message='This is a warning message.')
# #     ).pack(**options)
# #
# #     # run the app
# #     root.mainloop()
# #
# #
# # if __name__ == '__main__':
# #     matplotlib.use('TkAgg')
# #     app = App()
# #     app.mainloop()
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Tkinter Matplotlib Demo')
#
#         # prepare data
#         data = {
#             'Python': 11.27,
#             'C': 11.16,
#             'Java': 10.46,
#             'C++': 7.5,
#             'C#': 5.26
#         }
#         languages = data.keys()
#         popularity = data.values()
#
#         # create a figure
#         figure = Figure(figsize=(6, 4), dpi=100)
#
#         # create FigureCanvasTkAgg object
#         figure_canvas = FigureCanvasTkAgg(figure, self)
#
#         # create the toolbar
#         NavigationToolbar2Tk(figure_canvas, self)
#
#         # create axes
#         axes = figure.add_subplot()
#
#         # create the barchart
#         axes.bar(languages, popularity)
#         axes.set_title('Top 5 Programming Languages')
#         axes.set_ylabel('Popularity')
#
#         figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#
#
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
