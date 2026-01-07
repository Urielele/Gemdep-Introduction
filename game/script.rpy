init python:

    #Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    #Character callback that generates the sound.
    def cwo(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "cowo")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")
    
    def cwe(event, **kwargs):
        if event == "show": #When the text is shown
            build_sentence(_last_say_what, "cewe")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end": #When the text is finished displaying or you open a menu.
            renpy.sound.stop(channel="beeps")

# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"
image bg landmark = "images/bg/landmark.png"
image bg omori = "images/bg/omori.png"
image bg class = "images/bg/f06_03a03.png"

#pake kyk gini aja kak buat sprite
# Sip sip
image razan = "images/Frame 1.png"
image firdi = "images/Frame 2.png"
image djerico = "images/Frame 3.png"
image andhika = "images/Frame 5.png"
image bimo = "images/Frame 7.png"
image haidar = "images/Frame 8.png"
image ajik = "images/Frame 9.png"
image lisya = "images/Frame 10.png"
image titi = "images/Frame 11.png"
image chia = "images/Frame 12.png"

# Deklarasikan karakter yang digunakan di game.
define bim = Character('BIMO', color="#ffffff", callback=cwo) #Karakter Bimo
define raz = Character('RAZAAN',  color="#ffffff", callback=cwo) #Karakter kk Razaan (Kortim)
define lis = Character('LISYA', color="#ffffff", callback=cwe) #Karakter kk Lisya
define fir = Character('FIRID', color="#ffffff", callback=cwo) #Karakter kk Firid
define chi = Character('CHIA', color="#ffffff", callback=cwe) #karakter kk Chia
define hai = Character('HAIDAR', color="#ffffff", callback=cwo) #karakter Haidar
define faj = Character('FAJRI', color="#ffffff", callback=cwo) #karakter Fajri
define nas = Character('NASTITI', color="#ffffff", callback=cwe) #karakter Nastiti
define dhi = Character('DHIKA', color="#ffffff", callback=cwo) #karakter Andhika
define dje = Character('DJERICO', color="#ffffff", callback=cwo) #karakter Djerico

# Game dimulai disini.
label start:
    play music "OMORI OST - 003 Lost At A Sleepover.flac" loop fadein 1.0 fadeout 1.0

    scene bg class with dissolve

    show razan
    raz "hai gueh Razaan kortim kece."
    hide razan

    show firdi
    fir "Hai gueh firdi, bisa dipanggil pirid"
    hide firdi

    show djerico
    dje "Hai gueh djerico dari tekkim"
    hide djerico

    show andhika
    dhi "Hello World"
    hide andhika

    show bimo
    bim "Hello World"
    hide bimo

    show haidar
    hai "Hello World"
    hide haidar

    show ajik
    faj "Hello World"
    hide ajik

    show lisya
    lis "Hello World"
    hide lisya

    show titi
    nas "Hello World"
    hide titi

    show chia
    chi "Hello World"
    hide chia




    # scene bg omori with dissolve
    # show b1_1_1
    # bim "hai gueh Bimo gueh suka OMORI.gueh Teknik Informatika angkatan '24."
    # lis "hai gueh lisya dari angkatan 26. Gueh sangat muda sampai angkatan gueh dibawah 25."
    # return
