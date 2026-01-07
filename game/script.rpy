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
image bg makoto_normal = "images/b1_1_3.png"
image bg makoto_no_suit = "images/b1_1_1.png"
image bg Razaan = "images/Frame 1.png"
image bg Haidar = "images/Haidar.png"
image bg Djerico = "images/Frame 3.png"
image bg landmark = "images/bg/landmark.png"
image bg omori = "images/bg/omori.png"

#pake kyk gini aja kak buat sprite
image define bimo = "images/b1_1_1.png"

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
    play music "OMORI OST - 003 Lost At A Sleepover.flac" loop fadein 1.0

    scene bg Razaan with dissolve
    raz "hai gueh Razaan kortim kece."

    scene bg Haidar with dissolve
    hai "Hai gueh haidar beredar"

    scene bg Djerico with dissolve
    dje "Hai gueh djerico dari tekkim"

    scene bg omori with dissolve
    show b1_1_1
    bim "hai gueh Bimo gueh suka OMORI."
    bim "gueh Teknik Informatika angkatan '24."
    lis "hai gueh lisya dari angkatan 26."
    return
