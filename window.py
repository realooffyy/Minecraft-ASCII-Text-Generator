import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

from utils import open_howto_link
from const import VERSION
import format_input

txt_formattedtext = None

def init():
    root = tk.Tk()
    
    root.title("Minecraft ASCII Text Generator")
    root.config(bg="black")
    root.attributes('-topmost', 1)

    root.resizable(True,True)
    
    root.geometry('400x350')

    font = {
            "title": tkfont.Font(family="Verdana", size=14),
            "subheading": tkfont.Font(family="Verdana", size=10),
            "label": tkfont.Font(family="Verdana", size=10),
            "code": tkfont.Font(family="Consolas", size=10),
            }
    
    def top_frame(container):
        frame = ttk.Frame(container)
        options = {'padx': 5, 'pady': 5}

        # [0,0] title
        txt_appname = ttk.Label(frame, text="Minecraft ASCII Text Generator", font=font["title"])
        txt_appname.grid(row=0, column=0, **options, sticky=tk.W)

        # [1,0] version + credits
        txt_credits = ttk.Label(frame, text=f"v{VERSION} | by ooffyy", font=font["subheading"])
        txt_credits.grid(row=1, column=0, **options, sticky=tk.W)
        
        # [2,0] github link
        button_github = ttk.Button(frame, text="How to use (GitHub)", command=open_howto_link)
        button_github.grid(row=2, column=0, **options, sticky=tk.W)

        frame.grid(padx=10, pady=10, sticky='w')

    def input_frame(container):

        frame = ttk.Frame(container)
        options = {'padx': 5, 'pady': 5}

        # [3,0] 'Input' text
        txt_input = ttk.Label(frame, text="Input", font=font["label"])
        txt_input.grid(row=3, column=0, **options)

        # [3,1] user input line
        user_input = tk.StringVar()
        entry_input = ttk.Entry(frame, textvariable=user_input)
        entry_input.grid(row=3, column=1, **options)
        entry_input.focus()

        def display_result():
            global txt_formattedtext
            result = format_input.ascii_formatter(entry_input.get())
            txt_formattedtext.config(state='normal')  # Set state to normal to modify the content
            txt_formattedtext.delete(1.0, 'end')  # Clear existing content
            txt_formattedtext.insert('insert', result)  # Insert the new result at the insertion cursor
            txt_formattedtext.config(state='disabled')  # Set state back to disabled

        # [3,2] 'Format' button
        button_format = ttk.Button(frame, text="Format + Copy", command=display_result)
        button_format.grid(row=3, column=2, **options)

        frame.grid(padx=10, pady=10, sticky='w')

    def output_frame(container):
        global txt_formattedtext
        frame = ttk.Frame(container)
        options = {'padx': 5, 'pady': 5}

        # [4,0] 'Preview' text
        txt_result = ttk.Label(frame, text="Preview", font=font["label"])
        txt_result.grid(row=4, column=0, **options, sticky='w')

        # [4,1] the result
        txt_formattedtext = tk.Text(frame, font=font["code"], wrap=tk.WORD, state='disabled', width=35, height=7)
        txt_formattedtext.grid(row=4, column=1, **options, sticky='w')
        txt_formattedtext.bindtags((str(txt_formattedtext), str(root), "all")) # blocks selection


        frame.grid(padx=10, pady=10, sticky='w')

    top_frame(root)
    input_frame(root)
    output_frame(root)

    root.mainloop()


"""
        frame.grid(padx=10, pady=10)



    def output_frame(container):
        frame = ttk.Frame(container)
        options = {'padx': 5, 'pady': 5}
"""