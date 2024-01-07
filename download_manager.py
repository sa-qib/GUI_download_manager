
import requests
import tkinter as tk
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *
from tkinter import filedialog as fd

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master, width=20)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


def switch():
    fd.askdirectory()
    download_button['state'] = 'enable'

    

def download():
    url = url_entry.get()  
    fname = fname_entry.get()

    res = requests.get(url, stream=True)
    with open(fname, mode='wb') as f:
        for chunk in res.iter_content(chunk_size=128):
            f.write(chunk)


theme_names = ['morph', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']


# window
window = ttk.Window(themename='cyborg')
window.title("Linkedin Job Finder")
window.geometry("400x200")


# widgets
frame = ttk.Frame(master=window)

fname_label = ttk.Label(master=frame, text="File Name")
fname_entry = EntryWithPlaceholder(frame, 'file Name', 'gray')

url_label = ttk.Label(master=frame, text="URL")
url_entry = EntryWithPlaceholder(frame, 'URL', 'gray')


# file dialogue
button_frame = ttk.Frame(master=window)
file_location = ttk.Button(master=button_frame, text="Browse Location", bootstyle=DARK, command=switch)

# button
download_button = ttk.Button(master=button_frame, text="Download", state=DISABLED, bootstyle=DANGER, command=download)

# message
output_frame = ttk.Frame(master=window)
message_var = ttk.StringVar(master=output_frame, )
message = ttk.Label(master=frame, textvariable='')


# layout 
frame.grid(padx=50, pady=10)

fname_label.grid(row=0, column=0)
fname_entry.grid(row=1, column=0, pady=3, padx=5)


url_label.grid(row=0, column=1)
url_entry.grid(row=1, column=1)


button_frame.grid(padx=10, pady=10)
file_location.grid(row=2, column=0, padx=5)
download_button.grid(row=2, column=1)


# run 
window.mainloop()


