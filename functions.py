# All the functions related to the widgets

import pygame
from tkinter import *
from tkinter import ttk
from datetime import timedelta
from PIL import ImageTk, Image
from ttkthemes import ThemedTk
from audios import audios, paths, playing_audios

from time import sleep


SCREEN = ThemedTk(themebg=True)
SCREEN.config(bg='gray13')

STYLE = ttk.Style()
STYLE.configure('BW.TButton', font=('TkIconFont', 13, 'bold'), foreground='#116562', background='gray')

BG_IMAGE_PATH = "C:\\Users\\User\\Desktop\\wallpaper(copy).png"
IMAGE = ImageTk.PhotoImage(Image.open(BG_IMAGE_PATH))

ICON = PhotoImage(file="C:\\Users\\User\\Desktop\\beat-music-player-2013-04-22.png")
SCREEN.iconphoto(False, ICON)

DEFAULT_VOLUME = 50
IS_PAUSED = False


SCREEN.wm_title('music_player')
panel = Label(SCREEN, image = IMAGE)
panel.place(x=-5, y=-10)
pygame.mixer.init()


def play_the_audio(audio) :

    for path in paths:
        if audio in path:
            audio = path

    for widget in SCREEN.winfo_children():
        if 'scale' in str(widget):
            widget.set(1000)  
            # stop the audio when the song is nearly over.
            # make_play_button()


    pygame.mixer.music.load(open(audio, 'rb'))

    def show_music_pos(pos):

        delta = timedelta(seconds=pos)
        delta_label = Label(SCREEN, text=str(delta), fg='#000066', bg='#b3b3b3', width=8)
        delta_label.place(x=220,y=580)

    def change_pos(current_pos):

        current_pos = int(current_pos)
        print(current_pos)
        pygame.mixer.music.play(start=current_pos)
        show_music_pos(current_pos)


    audio_length = pygame.mixer.Sound(audio).get_length()
    position_slider = Scale(SCREEN, from_=0, to=audio_length, sliderrelief='flat', 
    orient='horizontal', troughcolor='black', length=400,
    highlightbackground='#6C3483',
    showvalue=False, command=change_pos)
        
    position_slider.place(x=55, y=550)


    def increase_pos():

        if IS_PAUSED == False:
            position_slider.set(position_slider.get() + 1)
            SCREEN.after(1000, increase_pos)
    increase_pos()

    def change_the_volume(volume):

        global DEFAULT_VOLUME
        DEFAULT_VOLUME = volume
        volume = int(volume) / 100
        pygame.mixer.music.set_volume(volume)


    def make_volume_scale():

        scale_widget = Scale(SCREEN, from_=0, to=100, sliderrelief='flat',
                        troughcolor='black',width=11 ,length=110, highlightbackground='#6C3483',command=change_the_volume)
        scale_widget.set(DEFAULT_VOLUME)
        scale_widget.place(x=445, y=240)


    make_volume_scale()

            








    

    def make_play_button() :
  
        def unpause_music():

            global IS_PAUSED
            IS_PAUSED = False
            pygame.mixer.music.unpause()
            make_stop_button()
            increase_pos()
            

        resume = ttk.Button(SCREEN, text='▶',style='BW.TButton' ,command=unpause_music)
        resume.place(x=185, y=510)

    def make_stop_button() :

        def pause_music():
            
            global IS_PAUSED
            IS_PAUSED = True
            pygame.mixer.music.pause()
            make_play_button()

        pygame.mixer.music.unpause()
        stop = ttk.Button(SCREEN, text='||',style='BW.TButton' ,command=pause_music)
        stop.place(x=185, y=510)   
    
    make_stop_button()

# Creating widgets for songs and bringing them onto the SCREEN
def make_buttons(window,files) :
    global current_time

    try :
        audio_1 = Button(window,text=files[0],height=4,width=40,bg='#31314f',fg='white',command=lambda : play_the_audio(files[0]))
        audio_1.config(font='TkIconFont')
        audio_1.place(x=90,y=190)

    
    except :
        pass

    try :
        audio_2 = Button(window,text=files[1],height=4,width=40,bg='#31314f',fg='white',command=lambda : play_the_audio(files[1]))
        audio_2.config(font='TkIconFont')
        audio_2.place(x=90,y=270)

    except :
        pass

    try :
        audio_3 = Button(window,text=files[2],height=4,width=40,bg='#31314f',fg='white',command=lambda : play_the_audio(files[2]))
        audio_3.config(font='TkIconFont')
        audio_3.place(x=90,y=350)
    except :
        pass

    try :
        audio_4 = Button(window,text=files[3],height=4,width=40,bg='#31314f',fg='white',command=lambda : play_the_audio(files[3]))
        audio_4.config(font='TkIconFont')
        audio_4.place(x=90,y=430)
    except :
        pass




    # Creating another window either the "next page" button is clicked or the "previous page" button
    def open_another_window() :

        
        for i in SCREEN.winfo_children() :
            i.destroy()
        panel = Label(SCREEN, image = IMAGE)
        panel.place(x=-5, y=-10)
        if pygame.mixer.music.get_busy() :
            pygame.mixer.music.pause()
        for i in audios  :
            if files[len(files) - 1] in i :
                try :
                        make_buttons(SCREEN,audios[audios.index(i)-1]) 
                except :
                    pass
                

    next_page = ttk.Button(text='<=',style='BW.TButton',width=13, command=open_another_window)
    next_page.place(x=75,y=510)

    previous_page = ttk.Button(SCREEN,text='=>',style='BW.TButton',command=open_another_window)
    previous_page.place(x=280,y=510)


def create_SCREEN() :

    SCREEN.geometry("500x630")
    SCREEN.resizable(False, False)

    make_buttons(SCREEN,playing_audios)
    SCREEN.mainloop()

create_SCREEN()
