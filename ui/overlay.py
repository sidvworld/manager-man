import tkinter as tk

overlay_open = False

def show_overlay(callback):
    global overlay_open
    if overlay_open:
        return
    overlay_open = True
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.wm_attributes('-transparentcolor', 'magenta')

    #sizing boi
    entry_width = 320
    entry_height = 36

    border_thickness = 6
    border_radius = 22

    window_width = entry_width + border_thickness * 2 + 16
    window_height = entry_height + border_thickness * 2 + 16

    screen_width = root.winfo_screenwidth()
    pos_x = screen_width - window_width - 20
    pos_y = 200 #adjust just to move it down

    root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")

    canvas = tk.Canvas(
        root,
        width=window_width,
        height=window_height,
        bg='magenta',
        highlightthickness=0
    )
    canvas.pack()

    def create_rounded_rect(canvas, x1, y1, x2, y2, r=16, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        return canvas.create_polygon(points, smooth=True, **kwargs)


    create_rounded_rect(
        canvas,
        border_thickness, border_thickness,
        window_width - border_thickness, window_height - border_thickness,
        r=border_radius,
        fill="#222",
        outline="#444",
        width=border_thickness
    )

    entry_x = (window_width - entry_width) // 2
    entry_y = (window_height - entry_height) // 2
    font_e = ("Ubuntu", 14)

    entry = tk.Entry(
        root,
        font=font_e,
        bg="#222",
        fg="white",
        insertbackground="white",
        borderwidth=0,
        relief="flat",
        highlightthickness=0
    )
    entry_pad = 5
    entry.place(x=entry_x + entry_pad, y=entry_y, width=entry_width - entry_pad, height=entry_height)
    entry.focus()

    # escape key to close
    root.bind("<Escape>", lambda e: slide_out())

    user_input = ""
    def submit(event=None):
        user_input = entry.get()
        callback(user_input)
        slide_out()

    entry.bind("<Return>", submit)

    #slide in slide out animation off stack overflow too lol
    def slide_in():
        start_x = screen_width
        end_x = pos_x
        steps = 15
        dx = (end_x - start_x) // steps
        for i in range(steps + 1):
            x = start_x + dx * i
            root.geometry(f"{window_width}x{window_height}+{x}+{pos_y}")
            root.update()
            root.after(1)
        root.geometry(f"{window_width}x{window_height}+{end_x}+{pos_y}")

    def slide_out():
        global overlay_open
        start_x = pos_x
        end_x = screen_width
        steps = 15
        dx = (end_x - start_x) // steps
        for i in range(steps + 1):
            x = start_x + dx * i
            root.geometry(f"{window_width}x{window_height}+{x}+{pos_y}")
            root.update()
            root.after(1)
        root.destroy()
        overlay_open = False

    slide_in()
    root.mainloop()

    if not user_input.strip:
        user_input = None

    return user_input

if __name__ == "__main__":
    show_overlay(callback=lambda user_input: print(f"callback: {user_input}"))

# test callback 
# show_overlay(callback=lambda user_input: print(f"callback: {user_input}"))


#random rect
# rect = canvas.create_arc((0, 0, radius * 2, radius * 2), start=90, extent=90, fill="#222")
