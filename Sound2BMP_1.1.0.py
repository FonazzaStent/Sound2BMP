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
    img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AYht+mFUVaBO0g4hCwOlkQFXGUKhbBQmkrtOpgcukfNGlIUlwcBdeCgz+LVQcXZ10dXAVB8AfE0clJ0UVK/C4ptIjx4O4e3vvel7vvAKFRYaoZmABUzTJS8ZiYza2K3a8IIIR+WkckZuqJ9GIGnuPrHj6+30V5lnfdnyOk5E0G+ETiOaYbFvEG8cympXPeJw6zkqQQnxOPG3RB4keuyy6/cS46LPDMsJFJzROHicViB8sdzEqGSjxNHFFUjfKFrMsK5y3OaqXGWvfkLwzmtZU012kOI44lJJCECBk1lFGBhSjtGikmUnQe8/APOf4kuWRylcHIsYAqVEiOH/wPfvfWLExNuknBGND1Ytsfo0D3LtCs2/b3sW03TwD/M3Cltf3VBjD7SXq9rUWOgL5t4OK6rcl7wOUOMPikS4bkSH6aQqEAvJ/RN+WAgVugd83tW+scpw9Ahnq1fAMcHAJjRcpe93h3T2ff/q1p9e8HSB5ylkmT+ZUAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfmBA0SCQ4i+81yAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAsxJREFUSMe1Vr1KM1EQPbkKESR3I1hJRESI2uYBJKSysrCwzgPYbRdYdfNjKaRMowa0sElgn8AXMJhC0CJKMEQE0biYhEB2YjFyvzXqavzWU83Ozp0zO7MzdwJEhL/EOIB0Or23t+e7a13XDcMIEFE4HLZtW0rpo3d22Gq1xvlZSvn09BQIBHzxPhgMpqamWBZK65f3IVdipJOZTCabzY5GxjUA0Gq1vE2bzWYkEhFCtNvtYDDobax8jvAFlUoFABG9vLz8/NQIBKVSiYVOp+M/QbPZPDw8ZPnbZP6G4OzsDEAkEgHw/Pz8vwT9fn9nZyeTyShNuVwGYBjGqAQgIimllJJcOD4+5rePj49E1Gg0ACSTyfPzcwAHBwduY8dxTNM0TdOtVD4/IahUKqpTqtUqEVmWBcCyrHq9DiCXy7l9XVxcsPHDw8NHAuHubzba3NwEsLW1BaBWq6n/JxaLTU5OAri7u3Pn4OTkhIXr6+svU8TjSEo5MTEB4OjoiINNpVIqP0TU7XaFEPF4XEV6c3OjZsP+/r5KmqZp71IEgFVSSsMwer1er9eLRqPRaJQDtCyLD8fjcSFEt9vlx3w+D6BYLAIYGxtjD5qmccT/CDRNcxyH3iOVSgGYn58H0Gg0WMkJ5HTf399LKVdWVjqdjmma0oVhgqG/iKFal/PDyOVyAOr1OhFx4OVyeeig4zifFPkjFhYWWFhfX1fKmZkZbmbbtnd3dxcXFxOJhMe4HvcgmJ2dZSEWiynl9PQ099rp6enV1VWxWAyFQt/cyR4j1zRNFTWDC3h7e1soFEKh0Orq6m862QPVahXA0tISgHw+/5XZj2rgcZNcXl4CWFtb8/M+YHAzc6vPzc39CYEQAsDGxsZPF6+REAwGt7e3B4PB8vKyz5f+L0r17tLnaerX4jWcItu21S7m4+r4VmRd1/1dTHnS6br+VoM/Xd9fAVRROIG1BVk9AAAAAElFTkSuQmCC'
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
    headerbytes= b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9ba0upKNhBxCFDdbIgKuIoVSyChdJWaNXB5NIvaNKQpLg4Cq4FBz8Wqw4uzro6uAqC4AeIo5OToouU+L+k0CLGg+N+vLv3uHsHeJtVphg9E4Cimno6ERdy+VUh8IpehBCEHwMiM7RkZjEL1/F1Dw9f72I8y/3cn6NPLhgM8AjEc0zTTeIN4plNU+O8TxxhZVEmPice1+mCxI9clxx+41yy2cszI3o2PU8cIRZKXSx1MSvrCvE0cVRWVMr35hyWOW9xVqp11r4nf2G4oK5kuE5zBAksIYkUBEioo4IqTMRoVUkxkKb9uIt/2PanyCWRqwJGjgXUoEC0/eB/8Ltbozg16SSF44D/xbI+RoHALtBqWNb3sWW1TgDfM3Cldvy1JjD7SXqjo0WPgP5t4OK6o0l7wOUOMPSkibpoSz6a3mIReD+jb8oDg7dAaM3prb2P0wcgS10t3wAHh8BYibLXXd4d7O7t3zPt/n4A/75yeXvunoQAAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfmBgoICBVHI3igAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAA6VJREFUWMPlV01IMmsUfsYCISKhVEhdiQStJHSltDBDiDIh+hlsEW1y01a3EbQIg9rUPimklYIZbYpplYt+KTRIyFmkQhNo2aJQ5tzV7d75dGzsu9zvu9wDs3rP+8w55znned+XEUWR8AtNhV9s7a1ueHp6QiqVQiqVwvX1NQDAarXC4XDA4XBAp9O1hMcopaBWqyGZTCIcDsPtdsPlckGv14OIIAgCOI7D8fExgsEgvF4v2tsV5iaKIn31VatV2tjYIJZlKZ1Oy/ql02liWZbW19epWq2SEmxFAcRiMWJZlgRB+NJXEARiWZZisZiiABpSUKlUwHEcTk5OcHNzg0qlgu3tbfT390v8Dg4OEI1GMTExgbGxMajVagDA3d0d5ubm0NHRAavViqGhIbhcLnR1dX3dA9lsFqFQCGazGV6vFzqdDiqVqu7nALCzs4NMJoNSqQSz2YxgMAiGYT6D+LM/kskkstkswuEw+vr65HugUCjQ8PAwxWIxRRxGIhGKRCIkCAI5nU7ieb6hX61Wo3g8Tm63m/L5vGRN9WNG4+Pj8Pl8aGtrUzxKPT092Nvbg8FgaCw2KhV8Ph98Ph92d3cbV6BUKpHdbqdcLtc066OjI/L7/eT3+2l+fp4ikYiiZhNFkXieJ5vNRqVSqb4Cz8/PAACj0Sib6e3tLVZWVhAIBBAIBMDzfEuiYzAYwDDM579aVsJ0Oo2ZmRkMDg4CACYnJ0Gk/Chp5PtZAa1WCyJCoVCQBdDr9Tg7O0O5XEa5XMbl5SVMJpPiAIrFIogIWq22PgCNRoPp6WkkEglZAKfTCZPJBI/HA4/HA6PRCKfTqTiARCKBqakpaDSaxmOYz+fJ7XZTPB6nWq0mO1I8z1Mul5P1aWUM64To/v4eoVAIFotFIkTfMVEUIQgC9vf3kc1msba2VidEDaX49fUVHMeB4zhcXV3h4+PjWwGo1WoMDAzA5XIpl+L/943o8PAQy8vLEoelpSWMjIxgcXER5+fnkvJGo1EAwOzsLN7f3z/X7HY7Njc3m+I1pODl5QXFYlGyobe3FxqNBo+Pj3h7e/trI8PAYrGAiPDw8ABRFD/XOjs7YTKZmuL9NAUMw7SkgoooOD09lS3Z6uqqLAULCwsNKWiG99tMgaQCmUwGFxcXEge73d7wNvT3vkkmk5Ie6O7uxujoqCI81Y+8KjnBWumTr/B+Lwq+Y/l8Hn6/XyLXNpsNW1tb/+zLqNmLSU4H/pUA/vNnwR8H97llVEK/YAAAAABJRU5ErkJggg=='

    soundfile=open(soundfilename,'rb')
    tempfile=open("tempfile.bmp",'wb')
    tempfile.write(headerbytes)
    soundfilesize=os.path.getsize(soundfilename)
    for n in range (45, 460800):
        if soundfilesize>460800:
            soundfile.seek(n)
        elif soundfilesize<460800 and n==soundfilesize:
            soundfile.seek(1)
        byteread=soundfile.read(1)
        tempfile.write(byteread)
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
