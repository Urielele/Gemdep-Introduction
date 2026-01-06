# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define bim = Character('BIMO', color="#ffffff") #Karakter Bimo
define raz = Character('RAZAAN',  color="#ffffff") #Karakter kk Razaan (Kortim)
define lis = Character('LISYA', color="#ffffff") #Karakter kk Lisya
define fir = Character('FIRID', color="#ffffff") #Karakter kk Firid
define chi = Character('CHIA', color="#ffffff") #karakter kk Chia
define hai = Character('HAIDAR', color="#ffffff") #karakter Haidar
define faj = Character('FAJRI', color="#ffffff") #karakter Fajri
define nas = Character('NASTITI', color="#ffffff") #karakter Nastiti
define dhi = Character('DHIKA', color="#ffffff") #karakter Andhika
define dje = Character('DJERICO', color="#ffffff") #karakter Djerico

# Game dimulai disini.
label start:

    scene bg blck with dissolve
    raz "hai gueh Razaan kortim kece."
    bim "hai gueh Bimo."
    faj "hai gueh fajri."
    return
