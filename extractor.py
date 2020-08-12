try: # checking if the modules are installed
    from pytube import *    
    from tkinter import  *
    import os 
    
except Exception as e: # printing a message if there is an issue with the packages!
    print('Packages are Missing! \n\n {}'.format(e))

app = Tk() # making the canvas
app.iconphoto(FALSE, PhotoImage(file='./images/Youtube-icon.png'))
app.title('Youtube Video Downloader') # making the title
app.geometry('600x200') # sizing the canvas

# making labels and it's place
label_1 = Label(app,text="Enter YouTube Link!", font=("bold",20))
label_1.place(x=180,y=20)

label_2 = Label(app, text="Developed By Abdulrazak Osman", width=80, font=("bold",9))
label_2.place(x=20,y=160)

myLink = StringVar() # link declaration!

# making the link entry bar and it's place!
link_bar = Entry(app, width=60, textvariable=myLink)
link_bar.place(x=120, y=80)

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

app.mainloop() # this will run the app!