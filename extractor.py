try:
    # checking if the modules are installed
    from pytube import *    
    from tkinter import  *
    import os 
    
    # printing a message if there is an issue with the packages!
except Exception as e:
    print('Modules are Missing! \n\n {}'.format(e))

# making the canvas
app = Tk()
app.geometry('600x200')
# making the title
app.title('Youtube Video Downloader')

# making labels
label_1 = Label(app,text="Enter The Link of The Video!", font=("bold",20))
label_1.place(x=120,y=20)

label_2 = Label(app, text="Developed By Abdulrazak Osman", width=80, font=("bold",9))
label_2.place(x=140,y=150)

# declaring variables
myLink = StringVar()

# making the link entry bar!
link_bar = Entry(app, width=60, textvariable=myLink)
link_bar.place(x=140, y=80)

# main functions!
def downloadVideo():
    link = str(myLink.get())
    video = YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # checking if the folder is exists or make one!
    if not os.path.exists('./videos/'):
        os.makedirs('./videos/')
    video.download('./videos/')

# making the submiting button
Button(app,text="Download", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)

# this will run the app!
app.mainloop()