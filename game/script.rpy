# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define Dev = Character('BEEMO', color="#ffffff")

# Game dimulai disini.
label start:

    scene bg blck with dissolve
    Dev "Prikitiws."

    Dev "Ini game kami bro"

    return
