init python:

    # Generate seperate audio channel from voice for beeps.
    renpy.music.register_channel(name='beeps', mixer='voice')

    # Character callback that generates the sound.
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

# -------------------------------------------------------------------------
# DEKLARASI GAMBAR (ASSETS)
# -------------------------------------------------------------------------
image bg blck = "images/bg/blck.png"
image bg landmark = "images/bg/landmark.png"
image bg omori = "images/bg/omori.png"
image bg class = "images/bg/f06_03a03.png"

# Sprite Member (Sesuai nama file kamu)
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

# Sprite Gimi (Maskot)
image gimi_happy_buka = "images/Gimi 1.png" 
image gimi_chat_buka = "images/Gimi 2.png" 
image gimi_happy_tunjuk = "images/Gimi 3.png"
image gimi_chat_tunjuk = "images/Gimi 4.png" 
image gimi_shock = "images/Gimi 5.png"

# -------------------------------------------------------------------------
# DEKLARASI KARAKTER
# -------------------------------------------------------------------------
# Note: Callback 'cwo' dan 'cwe' akan mentrigger suara Animalese dari speak.rpy

define gim = Character('GIMI', color="#00ff00", callback=cwo) # Maskot (Hijau)
define mc = Character('YOU', color="#aaaaaa", callback=cwo)   # Player (Abu-abu)

# Core Team & Member
define raz = Character('RAZAAN', color="#ffaa00", callback=cwo) # Orange
define fir = Character('FIRDI', color="#00ccff", callback=cwo)  # Biru
define lis = Character('LISYA', color="#ff99cc", callback=cwe)  # Pink
define chi = Character('CHIA', color="#ffff00", callback=cwe)   # Kuning
define bim = Character('BIMO', color="#9999ff", callback=cwo)   # Ungu
define faj = Character('AJIK', color="#00ffcc", callback=cwo)   # Cyan
define hai = Character('HAIDAR', color="#ff5555", callback=cwo) # Merah
define nas = Character('NASTITI', color="#ffccff", callback=cwe) # Ungu Muda
define dhi = Character('DHIKA', color="#ccff00", callback=cwo)  # Lime
define dje = Character('DJERICO', color="#ffffff", callback=cwo)# Putih

# -------------------------------------------------------------------------
# START GAME
# -------------------------------------------------------------------------
label start:
    play music "OMORI OST - 003 Lost At A Sleepover.flac" loop fadein 1.0 fadeout 1.0

    # Scene 1: Intro Glitch
    scene bg blck with dissolve
    
    # Efek suara glitch manual (opsional) atau teks sistem
    "System" "Booting up... GDGoC_Gemdep.exe loaded."
    
    scene bg class with dissolve
    
    # Scene 2: Gimi Muncul
    show gimi_chat_buka at center with moveinbottom
    gim "Yoo! Selamat datang, Player 1! Kamu sudah masuk ke server GDGoC Game Development Division."
    hide gimi_chat_buka
    
    mc "Hah? Dimana ini?"
    
    show gimi_happy_tunjuk
    gim "Di Markas Game Dev! Timing login kamu pas banget."
    
    mc "Pas buat apa? Buat gacha?"
    hide gimi_happy_tunjuk
    
    show gimi_chat_buka at center 
    gim "Bukan. Buat SKIP TUTORIAL! Eh bercanda."
    gim "Buat kenalan sama Party Member kita tahun ini."
    hide gimi_chat_buka 
    
    show gimi_happy_tunjuk
    gim "Oke, buka Party Menu. Hati-hati, build member di sini aneh-aneh!"
    hide gimi_happy_tunjuk with moveoutbottom

    show gimi_happy_tunjuk at left with moveinbottom

    # ---------------------------------------------------------------------
    # START MEMBER ROSTER (Perkenalan)
    # ---------------------------------------------------------------------

    # --- 1. RAZAAN ---
    show razan at right with moveinbottom
    gim "Pertama, ada Core Team alias Boss-nya. Razaan (TI '23)."
    gim "Game favoritnya Zelda BOTW, makanya hobi manjat tebing."
    
    raz "It is what it is."
    gim "Pasrah banget ya..."
    hide razan with dissolve

    # --- 2. FIRDI ---
    show firdi at right with moveinbottom
    gim "Lanjut, ada Firdi (TI '23). Fanboy Kingdom Hearts."
    gim "Kalau bingung coding, tanya hatimu. Kalau masih bingung, tanya Firdi."
    
    fir "May your heart be your guiding key."
    hide firdi with dissolve

    # --- 3. LISYA ---
    show lisya at right with moveinbottom
    gim "Terus ada Lisya. Game-nya story driven banget, Edith Finch."
    gim "Sangat berguna kalau nyasar di Indralaya."
    
    lis "When nothing goes right, go left."
    hide lisya with dissolve

    # --- 4. CHIA ---
    show chia at right with moveinbottom
    gim "Nah, ini Chia (TI '23). Perhatiin sprite aku sekarang..."
    gim "Yang gambar sprite aku ini tuh dia! Wibu Persona garis keras."
    
    chi "Yare yare da wa."
    hide chia with dissolve

    # --- 5. BIMO ---
    show bimo at right with moveinbottom
    gim "Masuk ke angkatan '24. Ada Bimo. Mainnya Omori."
    gim "Quotes-nya dalem banget. Awas jangan ikut depresi."
    
    bim "If all I can do is believe... My God, My Universe."
    hide bimo with dissolve

    # --- 6. AJIK ---
    show ajik at right with moveinbottom
    gim "Ada Ajik. Anak TI tapi map-nya jauh di Indralaya. Hii~"
    gim "Dia cuma takut sama satu hal..."
    
    faj "Respect everyone, Fear no one, Except Herobrine."
    hide ajik with dissolve

    # --- 7. HAIDAR ---
    show haidar at right with moveinbottom
    gim "Next, Haidar. Suka siksa diri main Cuphead."
    gim "Motto-nya disponsori Nike."
    
    hai "Just Do It."
    hide haidar with dissolve

    # --- 8. NASTITI ---
    show titi at right with moveinbottom
    gim "Ada Nastiti. Selera game-nya vintage abis, Suikoden!"
    gim "Member paling berbudaya dan puitis."
    
    nas "To exist is a fact, To live is an art."
    hide titi with dissolve

    # --- 9. ANDHIKA ---
    show andhika at right with moveinbottom
    gim "Ada Andhika. Pemain Elden Ring."
    gim "Sabar banget orangnya, soalnya udah biasa mati di game."
    
    dhi "Whatever happens, happens."
    hide andhika with dissolve

    # --- 10. DJERICO ---
    show djerico at right with moveinbottom
    gim "TERAKHIR! Plot twist kita. Djerico!"
    gim "Satu-satunya ALCHEMIST (Teknik Kimia) di antara anak Komputer."
    
    dje "Do your..."
    gim "Kayaknya quotes-nya kepotong, tapi biarin lah biar misterius."
    hide djerico with dissolve

    hide gimi_happy_tunjuk with moveoutbottom

    # ---------------------------------------------------------------------
    # CLOSING PERKENALAN
    # ---------------------------------------------------------------------
    
    show gimi_happy_tunjuk at center with moveinbottom
    gim "Itulah Party Member kita. Solid kan?"
    gim "Sekarang kamu udah kenal muka-mukanya."
    
    # Placeholder untuk next scene
    gim "Mau lanjut ke materi?"
    mc "Gasss!"

    return