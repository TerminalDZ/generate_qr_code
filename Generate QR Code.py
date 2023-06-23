import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox, colorchooser, Scale, Canvas, Scrollbar, LabelFrame, filedialog
from PIL import ImageTk, Image

def generate_qr():
    data = data_entry.get()

    if not data:
        messagebox.showwarning("Warning", "Please enter text or link")
        return

    qr = qrcode.QRCode(version=1, box_size=box_size_scale.get(), border=border_scale.get())
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color_1, back_color=color_2)
    img_tk = ImageTk.PhotoImage(image=img)

    canvas.config(scrollregion=canvas.bbox("all"), width=min(img.size[0], root.winfo_screenwidth()), height=min(img.size[1], root.winfo_screenheight()))

    qr_label.configure(image=img_tk)
    qr_label.image = img_tk

    global qr_image
    qr_image = img

def select_color_1():
    global color_1
    color_1 = colorchooser.askcolor()[1]

def select_color_2():
    global color_2
    color_2 = colorchooser.askcolor()[1]

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG file", "*.png")])
    if file_path:
        qr_image.save(file_path)

root = Tk()
root.title("QR Code Generator")
root.geometry("800x800")
root.minsize(800, 800)
root.resizable(True, True)

# Create input field and generate button
data_label = Label(root, text="Enter text or link:")
data_label.pack(pady=(20, 5))

data_entry = Entry(root, width=50)
data_entry.pack(pady=5)

generate_button = Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=(5, 20))

# Create canvas with scrollbar to display QR code
canvas = Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(canvas, orient="vertical", command=canvas.yview)
scrollbar.pack(side="left", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

qr_label = Label(canvas)
qr_label.pack()

color_1 = "black"
color_2 = "white"

# Create color customization options
color_options_frame = LabelFrame(root, text="Color options", padx=10, pady=10)
color_options_frame.pack(side="left", fill="y")

color_1_label = Label(color_options_frame, text="QR color:")
color_1_label.pack()

color_1_button = Button(color_options_frame, text="Select", command=select_color_1)
color_1_button.pack(pady=5)

color_2_label = Label(color_options_frame, text="Background color:")
color_2_label.pack()

color_2_button = Button(color_options_frame, text="Select", command=select_color_2)
color_2_button.pack(pady=5)

# Create size customization options
size_options_frame = LabelFrame(root, text="Size options", padx=10, pady=10)
size_options_frame.pack(side="left", fill="y")

box_size_label = Label(size_options_frame, text="Box size:")
box_size_label.pack()

box_size_scale = Scale(size_options_frame, from_=1, to=20, orient="horizontal")
box_size_scale.set(10)
box_size_scale.pack()

border_label = Label(size_options_frame, text="Border size:")
border_label.pack()

border_scale = Scale(size_options_frame, from_=0, to=5, orient="horizontal")
border_scale.set(5)
border_scale.pack()

def save_qr():
    # Get the filename from the user
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

    # If the user doesn't enter a filename, return
    if not filename:
        return

    # Generate the QR code image
    data = data_entry.get()
    qr = qrcode.QRCode(version=1, box_size=box_size_scale.get(), border=border_scale.get())
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color_1, back_color=color_2)

    # Save the image
    img.save(filename)

save_button = Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=(5, 20))


root.mainloop()