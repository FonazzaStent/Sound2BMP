import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import os
from tkinter import messagebox
import shutil
from PIL import ImageTk, Image

#create main window
def create_main_window():
    global top
    global root
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9ba0upKNhBxCFDdbIgKuIoVSyChdJWaNXB5NIvaNKQpLg4Cq4FBz8Wqw4uzro6uAqC4AeIo5OToouU+L+k0CLGg+N+vLv3uHsHeJtVphg9E4Cimno6ERdy+VUh8IpehBCEHwMiM7RkZjEL1/F1Dw9f72I8y/3cn6NPLhgM8AjEc0zTTeIN4plNU+O8TxxhZVEmPice1+mCxI9clxx+41yy2cszI3o2PU8cIRZKXSx1MSvrCvE0cVRWVMr35hyWOW9xVqp11r4nf2G4oK5kuE5zBAksIYkUBEioo4IqTMRoVUkxkKb9uIt/2PanyCWRqwJGjgXUoEC0/eB/8Ltbozg16SSF44D/xbI+RoHALtBqWNb3sWW1TgDfM3Cldvy1JjD7SXqjo0WPgP5t4OK6o0l7wOUOMPSkibpoSz6a3mIReD+jb8oDg7dAaM3prb2P0wcgS10t3wAHh8BYibLXXd4d7O7t3zPt/n4A/75yeXvunoQAAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfmBgoICBVHI3igAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAA6VJREFUWMPlV01IMmsUfsYCISKhVEhdiQStJHSltDBDiDIh+hlsEW1y01a3EbQIg9rUPimklYIZbYpplYt+KTRIyFmkQhNo2aJQ5tzV7d75dGzsu9zvu9wDs3rP+8w55znned+XEUWR8AtNhV9s7a1ueHp6QiqVQiqVwvX1NQDAarXC4XDA4XBAp9O1hMcopaBWqyGZTCIcDsPtdsPlckGv14OIIAgCOI7D8fExgsEgvF4v2tsV5iaKIn31VatV2tjYIJZlKZ1Oy/ql02liWZbW19epWq2SEmxFAcRiMWJZlgRB+NJXEARiWZZisZiiABpSUKlUwHEcTk5OcHNzg0qlgu3tbfT390v8Dg4OEI1GMTExgbGxMajVagDA3d0d5ubm0NHRAavViqGhIbhcLnR1dX3dA9lsFqFQCGazGV6vFzqdDiqVqu7nALCzs4NMJoNSqQSz2YxgMAiGYT6D+LM/kskkstkswuEw+vr65HugUCjQ8PAwxWIxRRxGIhGKRCIkCAI5nU7ieb6hX61Wo3g8Tm63m/L5vGRN9WNG4+Pj8Pl8aGtrUzxKPT092Nvbg8FgaCw2KhV8Ph98Ph92d3cbV6BUKpHdbqdcLtc066OjI/L7/eT3+2l+fp4ikYiiZhNFkXieJ5vNRqVSqb4Cz8/PAACj0Sib6e3tLVZWVhAIBBAIBMDzfEuiYzAYwDDM579aVsJ0Oo2ZmRkMDg4CACYnJ0Gk/Chp5PtZAa1WCyJCoVCQBdDr9Tg7O0O5XEa5XMbl5SVMJpPiAIrFIogIWq22PgCNRoPp6WkkEglZAKfTCZPJBI/HA4/HA6PRCKfTqTiARCKBqakpaDSaxmOYz+fJ7XZTPB6nWq0mO1I8z1Mul5P1aWUM64To/v4eoVAIFotFIkTfMVEUIQgC9vf3kc1msba2VidEDaX49fUVHMeB4zhcXV3h4+PjWwGo1WoMDAzA5XIpl+L/943o8PAQy8vLEoelpSWMjIxgcXER5+fnkvJGo1EAwOzsLN7f3z/X7HY7Njc3m+I1pODl5QXFYlGyobe3FxqNBo+Pj3h7e/trI8PAYrGAiPDw8ABRFD/XOjs7YTKZmuL9NAUMw7SkgoooOD09lS3Z6uqqLAULCwsNKWiG99tMgaQCmUwGFxcXEge73d7wNvT3vkkmk5Ie6O7uxujoqCI81Y+8KjnBWumTr/B+Lwq+Y/l8Hn6/XyLXNpsNW1tb/+zLqNmLSU4H/pUA/vNnwR8H97llVEK/YAAAAABJRU5ErkJggg=='
    root= tk.Tk()
    top= root
    top.geometry("120x80")
    top.title("Bitrate Reduction")
    top.resizable(0,0)
    favicon=tk.PhotoImage(data=img) 
    root.wm_iconphoto(True, favicon)

#create_buttons
def create_buttons():
    global convert_button
    convert_button=tk.Button(top)
    convert_button.place(x=20,y=20,height=40,width=80)
    convert_button.configure(text="Convert")
    convert_button.bind("<Button-1>",open_file)

#open_file
def open_file(event):
    global soundfilename
    data=[('WAV', '*.wav')]
    soundfilename=askopenfilename(filetypes=data, defaultextension=data)
    #if str(soundfile)!='':
    convert()

#convert_bitrate
def convert():
    headerbytes= b'B'b'M'b'\x92'b'P'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x92'b'\x00'b'\x00'b'\x00'b'|'b'\x00'b'\x00'b'\x00'b'\xf0'b'\x00'b'\x00'b'\x00'b'\x80'b'\x02'b'\x00'b'\x00'b'\x01'b'\x00'b'\x01'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'P'b'\x00'b'\x00'b'\xc4'b'\x0e'b'\x00'b'\x00'b'\xc4'b'\x0e'b'\x00'b'\x00'b'\x02'b'\x00'b'\x00'b'\x00'b'\x02'b'\x00'b'\x00'b'\x00'b'\x00'b'\xf8'b'\x00'b'\x00'b'\xe0'b'\x07'b'\x00'b'\x00'b'\x1f'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'B'b'G'b'R'b's'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x02'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\x00'b'\xff'b'\xff'b'\xff'
    soundfile=open(soundfilename,'rb')
    tempfile=open("tempfile.bmp",'wb')
    tempfile.write(headerbytes)
    soundfilesize=os.path.getsize(soundfilename)
    if soundfilesize>153600:
        multiplier=soundfilesize/153600
    else:
        multiplier=1
    for n in range (45, 153600):
        if soundfilesize>153600:
            soundfile.seek(int((n*multiplier)+1))
        elif soundfilesize<153600 and n==soundfilesize:
            soundfile.seek(1)
        byteread=soundfile.read(1)
        bytevalue=int.from_bytes(byteread,"big")
        #print (bytevalue)
        if bytevalue>128:
            value=0
            #print("ok")
        else:
            value=255
        bytewrite=value.to_bytes(1,"big")
        #print (bytewrite)
        tempfile.write(bytewrite)
    imgfile=Image.open("tempfile.bmp")    
    img=imgfile.convert("L", palette=Image.Palette.ADAPTIVE, dither=Image.Dither.FLOYDSTEINBERG, colors=256)
    data=[('BMP','*.bmp')]
    bmpfilesavename=asksaveasfilename(filetypes=data, defaultextension=data)
    img.save(bmpfilesavename)
    tempfile.close()
    soundfile.close()
    os.remove("tempfile.bmp")
    imgfileshow=Image.open(bmpfilesavename)
    imgfileshow.show()
    
        

#main             
def main():
        create_main_window()
        create_buttons()

main()
root.mainloop()
