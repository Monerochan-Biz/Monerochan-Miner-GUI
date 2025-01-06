import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # For resizing the icon
import threading
import time


def create_window():
    # Initialize the main window
    root = tk.Tk()
    root.title("Monerochan Pool Miner")
    root.geometry("450x350")
    root.config(bg="#c0c0c0")  # Light gray background like Windows 3.1

    # Check for available fonts and set a fallback
    available_fonts = list(font.families())
    retro_font = "MS Sans Serif" if "MS Sans Serif" in available_fonts else "Courier"

    # Create the inner frame for better styling
    inner_frame = tk.Frame(root, bg="#c0c0c0", bd=2, relief="sunken")
    inner_frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    # Helper functions for retro style
    def retro_label(parent, text, fg="black", bg="#c0c0c0"):
        return tk.Label(
            parent,
            text=text,
            font=(retro_font, 10),
            bg=bg,
            fg=fg,
            padx=5,
            pady=5
        )

    def retro_checkbox(parent, text, var, command=None):
        return tk.Checkbutton(
            parent,
            text=text,
            variable=var,
            command=command,
            bg="#c0c0c0",
            fg="black",
            font=(retro_font, 10),
            selectcolor="white",
            anchor="w",
            relief="flat"
        )

    def retro_shadowed_button(parent, text, command=None):
        shadow_frame = tk.Frame(parent, bg="darkgray", relief="raised", bd=1)  # Shadow color
        button = tk.Button(
            shadow_frame,
            text=text,
            relief="raised",  # Raised for a 3D effect
            bg="#e0e0e0",  # Lighter background for button
            fg="black",
            bd=2,
            padx=5,
            pady=2,
            font=(retro_font, 10),
            command=command
        )
        button.pack(padx=1, pady=1)
        return shadow_frame

    # Function to animate the progress bar (rotating)
    def animate_progress_bar():
        progress_bar_width = 0
        progress_direction = 1
        while running:
            if progress_bar_width == 380 or progress_bar_width == 0:
                progress_direction = -progress_direction  # Reverse direction

            progress_bar_width += progress_direction * 5  # Update width incrementally
            progress_bar.config(width=progress_bar_width)
            time.sleep(0.05)

    # Start mining
    def start_mining():
        global running
        running = True
        status_label.config(text="Status: Mining...")
        threading.Thread(target=animate_progress_bar, daemon=True).start()

    # Stop mining
    def stop_mining():
        global running
        running = False
        status_label.config(text="Status: Stopped")
        progress_bar.config(width=0)

    # Variables
    use_tor_var = tk.BooleanVar()
    donate_var = tk.BooleanVar()

    # Icon
    icon_label = tk.Label(inner_frame, bg="#c0c0c0")
    icon_label.place(x=10, y=10)
    try:
        icon_image = Image.open("icon.png").resize((48, 48))  # Resize the image to fit
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo
    except Exception:
        icon_label.config(text="[Icon Missing]")

    # Use Tor checkbox
    use_tor_check = retro_checkbox(inner_frame, "Use Tor", use_tor_var)
    use_tor_check.place(x=80, y=20)

    # Donate to Pool checkbox
    def toggle_eth_entry():
        if donate_var.get():
            eth_entry.config(state=tk.DISABLED)
        else:
            eth_entry.config(state=tk.NORMAL)

    donate_check = retro_checkbox(inner_frame, "Donate to Pool", donate_var, toggle_eth_entry)
    donate_check.place(x=80, y=50)

    # ETH Address label and entry
    eth_label = retro_label(inner_frame, "ETH Address:")
    eth_label.place(x=80, y=80)
    eth_entry = tk.Entry(inner_frame, width=30, font=(retro_font, 10))
    eth_entry.place(x=160, y=80)

    # Buttons
    start_button = retro_shadowed_button(
        inner_frame,
        "Start",
        command=start_mining
    )
    start_button.place(x=80, y=130)

    stop_button = retro_shadowed_button(
        inner_frame,
        "Stop",
        command=stop_mining
    )
    stop_button.place(x=160, y=130)

    # Status label
    status_label = retro_label(inner_frame, "Status: Idle")
    status_label.place(x=80, y=200)

    # Progress bar frame
    progress_frame = tk.Frame(inner_frame, bg="darkgray")
    progress_frame.place(x=80, y=230, width=300, height=20)
    progress_bar = tk.Frame(progress_frame, bg="green", width=0, height=20)
    progress_bar.pack(side="left", fill="y")

    # Start the main loop
    root.mainloop()


# Global variable to control animation
running = False

create_window()

