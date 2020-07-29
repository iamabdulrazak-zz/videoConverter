try:
    # checking if the modules are installed
    from moviepy.editor import *
    from pytube import *    
    from tkinter import  *
    import os
    
    # printing a message if there is an issue with the packages!
except Exception as e:
    print('Modules are Missing! \n\n {}'.format(e))

# making the canvas
root = Tk()
root.geometry('700x400')
# making the title
root.title('Youtube Video Downloader')

# making labels 
label_1 = Label(root, text='Enter The Link of The Video!', font=('bold',20))
label_1.place(x=120, y=20)

# declaring variables!
myLink = StringVar()

# making the link entry bar!
link_bar = Entry(root, width=60, textVariable=myLink)
link_bar.place(x=140, y=80)

# functions
def downloadVideo():
    x_link = str(myLink.get())
    video_url = YouTube(x_link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # checking if the folder is exists or make one!
    if not os.path.exists('./videos/'):
        os.mkdir('./videos/')
    video_url.download('./videos/')

# making the submiting button
Button(root, text='Download', width=20, bg='green', fg='white', command=downloadVideo).place(x=220, y=110)

# this will run the app!
root.mainloop()