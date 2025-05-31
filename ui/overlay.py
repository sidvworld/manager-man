import tkinter as tk

def show_overlay():
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    #tkinter workaround for corners - check https://stackoverflow.com/questions/7068858/tkinter-window-with-transparent-background
    #basically magenta is the transparent color
    root.wm_attributes('-transparentcolor', 'magenta') 

    # change these later if its too fucking big
    window_width = 400
    window_height = 100
    screen_width = root.winfo_screenwidth()
    x = screen_width - window_width - 20

    #hide and starts offscreen - comment this line and use other one if you want to see the window immediately
    # root.geometry(f"{window_width}x{window_height}+{screen_width}+20")

    #other one
    root.geometry(f"{window_width}x{window_height}+{x}+120")

    canvas = tk.Canvas(root,
                       width=window_width,
                       height=window_height,
                       bg='magenta',
                       highlightthickness=0)
    canvas.pack()

    # ye literally copy and pasted from stackoverflow man idk
    radius = 20

    canvas.create_rectangle(radius, 0, window_width - radius, window_height, fill="#222", outline="")
    canvas.create_rectangle(0, radius, window_width, window_height - radius, fill="#222", outline="")

    # top right corner
    canvas.create_arc((window_width - radius * 2, 0, window_width, radius * 2), start=0, extent=90, fill="#222", outline="")

    # bottom left corner
    canvas.create_arc((0, window_height - radius * 2, radius * 2, window_height), start=180, extent=90, fill="#222", outline="")

    # bottom right corner
    canvas.create_arc((window_width - radius * 2, window_height - radius * 2, window_width, window_height), start=270, extent=90, fill="#222", outline="")

    # top left corner
    canvas.create_arc((0, 0, radius * 2, radius * 2), start=90, extent=90, fill="#222", outline="")


    root.mainloop()


show_overlay()


#random rect
# rect = canvas.create_arc((0, 0, radius * 2, radius * 2), start=90, extent=90, fill="#222")
