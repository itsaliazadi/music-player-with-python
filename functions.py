# All the functions related to the widgets


import os
import pydub
import pygame
import pygame.mixer
from tkinter import *
from tkinter import Tk
from audios import audios, paths, playing_audios

from tkinter import ttk
from ttkthemes import ThemedTk




screen = ThemedTk(theme="default")
def open_music_player() :
    
    screen.wm_title('')
    icon = PhotoImage(file="C:\\Users\\User\\Downloads\\music_player_logo.png")
    screen.iconphoto(False, icon)
    pygame.mixer.init()

# create_resume_button() and create_stop_button() pause and unpause the current audio
    def create_resume_button() :

        if pygame.mixer.music.get_busy() :
            pygame.mixer.music.pause()
            resume = Button(screen, text='resume', height=3, width=10, bg='#49A',command=create_stop_button)
            resume.place(x=200, y=480)

    def create_stop_button() :

        pygame.mixer.music.unpause()
        stop = Button(screen, text='||', height=3, width=10, bg='#49A', command=create_resume_button)
        stop.place(x=200, y=480)

    

    def play_the_audio(audio) :

        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.load(open(audio, 'rb'))
        pygame.mixer.music.play()

    def change_the_volume(volume):

        volume = int(volume) / 100
        pygame.mixer.music.set_volume(volume)
        


    def make_scale_widget():

        scale_widget = Scale(screen, from_=0, to=100, command=change_the_volume)
        scale_widget.set(50)
        scale_widget.place(x=445, y=240)

    def handle_the_audio(audio_name) :

        if pygame.mixer.music.get_busy() : # if some audio's playing, it firstly pauses it and them
            pygame.mixer.music.pause()
        
        # Creating the scale widget
        make_scale_widget()
 
        # Creating all the buttons related to the song
        for i in paths:
            if audio_name in i:
                play_the_audio(i)
                make_scale_widget()
                create_stop_button()
                mainloop()

    # Creating widgets for songs and bringing them onto the screen
    def make_buttons(window,files) :

        try :
            audio_1 = Button(window,text=files[0],height=4,width=40,bg="#6C3483",command=lambda : handle_the_audio(files[0]))
            audio_1.config(font=("Cooper Black",10))
            audio_1.place(x=65,y=160)
        except :
            pass

        try :
            audio_2 = Button(window,text=files[1],height=4,width=40,bg='#6C3483',command=lambda : handle_the_audio(files[1]))
            audio_2.config(font=("Cooper Black",10))
            audio_2.place(x=65,y=240)
        except :
            pass

        try :
            audio_3 = Button(window,text=files[2],height=4,width=40,bg='#6C3483',command=lambda : handle_the_audio(files[2]))
            audio_3.config(font=("Cooper Black", 10))
            audio_3.place(x=65,y=320)
        except :
            pass

        try :
            audio_4 = Button(window,text=files[3],height=4,width=40,bg='#6C3483',command=lambda : handle_the_audio(files[3]))
            audio_4.config(font=("Cooper Black", 10))
            audio_4.place(x=65,y=400)
        except :
            pass



        # Creating another window either the "next page" button is clicked or the "previous page" button
        def open_another_window() :

            for i in screen.winfo_children() :
                i.destroy()
            if pygame.mixer.music.get_busy() :
                pygame.mixer.music.pause()
            for i in audios  :
                if files[len(files) - 1] in i :
                    try :
                         make_buttons(screen,audios[audios.index(i)-1]) 
                    except :
                        pass
                    

        # Making next_page and previous_page buttons         
        next_page = Button(screen,text='next page',height=3,width=10,bg='#116562',command=open_another_window)
        next_page.place(x=120,y=480)

        previous_page = Button(screen,text='previous page',height=3,width=10,bg='#116562',command=open_another_window)
        previous_page.place(x=280,y=480)


    def make_label() :

        screen.geometry("500x600")
        guide_message = "Choose your favourite music!"
        guide = Label(screen,text=guide_message,bg='#0E6655')
        guide.config(width=50,height=5)
        guide.config(font=("Arial CYR",10))
        guide.pack()

        make_buttons(screen,playing_audios)
        screen.mainloop()

    make_label()

open_music_player()
