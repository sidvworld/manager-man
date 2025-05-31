# trial 1 lol

import tkinter as tk

def show_overlay_prompt(callback_on_submit):
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.wm_attributes('-transparentcolor', 'magenta') 

    window_width = 400
    window_height = 100
    screen_width = root.winfo_screenwidth()
    x = screen_width - window_width - 20

    root.geometry(f"{window_width}x{window_height}+{screen_width}+20")

    canvas = tk.Canvas(root, width=window_width, height=window_height,
                       bg='magenta', highlightthickness=0)
    canvas.pack()

    radius = 20
    rect = canvas.create_arc((0, 0, radius * 2, radius * 2), start=90, extent=90, fill="#222")
    canvas.create_arc((window_width - radius * 2, 0, window_width, radius * 2), start=0, extent=90, fill="#222")
    canvas.create_arc((0, window_height - radius * 2, radius * 2, window_height), start=180, extent=90, fill="#222")
    canvas.create_arc((window_width - radius * 2, window_height - radius * 2, window_width, window_height),
                      start=270, extent=90, fill="#222")
    canvas.create_rectangle(radius, 0, window_width - radius, window_height, fill="#222", outline="")
    canvas.create_rectangle(0, radius, window_width, window_height - radius, fill="#222", outline="")


    entry = tk.Entry(root, font=("Segoe UI", 14), bg="#333", fg="white", insertbackground="white", borderwidth=0)
    entry.place(x=30, y=35, width=window_width - 60)
    entry.focus()

    def submit(event=None):
        user_input = entry.get()
        callback_on_submit(user_input)
        slide_out()

    entry.bind("<Return>", submit)

    def slide_in():
        for i in range(0, window_width + 1, 40):
            root.geometry(f"{i}x{window_height}+{screen_width - i}+20")
            root.update()
            root.after(5)

    def slide_out():
        for i in range(window_width, -1, -40):
            root.geometry(f"{i}x{window_height}+{screen_width - i}+20")
            root.update()
            root.after(5)
        root.destroy()

    slide_in()
    root.mainloop()