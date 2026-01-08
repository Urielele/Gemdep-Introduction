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
    
    # Efek suara glitch manual
    "System" "Booting up... GDGoC_Gemdep.exe loaded."
    
    scene bg class with dissolve
    
    # Scene 2: Gimi Muncul
    show gimi_chat_buka at center with moveinbottom
    gim "Yoo! Selamat datang, Player! Kamu sudah masuk ke server GDGoC Game Development Division."
    
    mc "Hah? Dimana ini?"
    hide gimi_chat_buka
    
    # Intro Gimi (Revisi: Hapus bagian Broke Ass)
    show gimi_happy_tunjuk at center
    gim "Sebelumnya perkenalkan aku Gimi! Maskot magang dari divisi game development nih!"
    gim "Nah pas banget kamu lagi login di markas game development nih."
    
    mc "Pas buat apa? Buat gacha?"
    hide gimi_happy_tunjuk
    
    show gimi_chat_buka at center 
    gim "Bukan. Buat SKIP TUTORIAL!"
    gim "tapi boong!"
    gim "Buat kenalan sama Party Member kita tahun ini dong~"
    hide gimi_chat_buka 
    
    show gimi_happy_tunjuk at center
    gim "Oke, buka Party Menu. Hati-hati, build member di sini aneh-aneh tau..."
    hide gimi_happy_tunjuk with moveoutbottom

    # Pindah Gimi ke KIRI (sesuai request animasi kamu)
    show gimi_happy_tunjuk at left with moveinbottom

    # ---------------------------------------------------------------------
    # START MEMBER ROSTER (Perkenalan)
    # ---------------------------------------------------------------------

    # --- 1. RAZAAN ---
    show razan at right with moveinbottom
    gim "Pertama, ada Core Team alias Boss-nya. Razaan (TI '23)."
    gim "Game favoritnya Zelda BOTW, makanya hobi manjat tebing."
    gim "Nah Core kita punya pesan singkat nih. Apa tuh, Core???"
    raz "It is what it is..."
    gim "Pasrah banget ya... yah begitulah core team kita teman-teman!"
    hide razan with moveoutbottom

    # --- 2. FIRDI ---
    show firdi at right with moveinbottom
    gim "Lanjut, ada Firdi (TI '23). Fanboy Kingdom Hearts."
    gim "Kalau bingung coding, tanya hatimu. Kalau masih bingung, tanya Firdi."
    gim "sama kayak sebelumnya nih, Firdi punya pesan penting untuk kalian!"
    fir "May your heart be your guiding key."
    hide firdi with moveoutbottom

    # --- 3. LISYA ---
    show lisya at right with moveinbottom
    gim "Terus ada Lisya. Game-nya story driven banget, Edith Finch."
    gim "Kalau kalian butuh orang buat projek roblox kalian, udah sih, telpon aja si Lisya ini!"
    gim "Beliau ini juga sangat berguna kalau nyasar di Indralaya yagesya."
    gim "Katanya Lisya punya sesuatu yang mau disampaikan nih, apa tuh kira kira?"
    lis "When nothing goes right, go left."
    hide lisya with moveoutbottom

    # --- 4. CHIA ---
    show chia at right with moveinbottom
    gim "Nah, ini Chia (TI '23). Perhatiin penampilan aku sekarang ya."
    gim "Yang gambar penampilan aku ini tuh dia! fans Persona & JOJO garis keras!"
    gim "Kasih pesan singkat dong Chia!"
    chi "Yare yare da wa."
    hide chia with moveoutbottom

    # --- 5. BIMO ---
    show bimo at right with moveinbottom
    gim "Masuk ke angkatan '24. Ada Bimo. Mainnya Omori. Kalian tidak ada yang bisa menebak next move orang ini."
    gim "Quotes-nya dalem banget. Awas jangan ikut depresi."
    bim "If all I can do is believe... My God, My Universe."
    hide bimo with moveoutbottom

    # --- 6. AJIK ---
    show ajik at right with moveinbottom
    gim "Ada Ajik. Anak TI tapi map-nya jauh di Indralaya. Hii~"
    gim "Dia cuma takut sama satu hal..."
    faj "Respect everyone, Fear no one, Except Herobrine."
    hide ajik with moveoutbottom

    # --- 7. HAIDAR ---
    show haidar at right with moveinbottom
    gim "Next, Haidar. Suka siksa diri main Cuphead."
    gim "Motto-nya disponsori Nike."
    hai "Just Do It."
    hide haidar with moveoutbottom

    # --- 8. NASTITI ---
    show titi at right with moveinbottom
    gim "Ada Nastiti. Selera game-nya vintage abis, Suikoden!"
    gim "Member paling berbudaya dan puitis, quotesnya apalagi!"
    nas "To exist is a fact, To live is an art."
    hide titi with moveoutbottom

    # --- 9. ANDHIKA ---
    show andhika at right with moveinbottom
    gim "Ada Andhika. Pemain Elden Ring."
    gim "Sabar banget orangnya, soalnya udah biasa mati di game."
    gim "Orang sabar motto hidupnya gimana nih?"
    dhi "Whatever happens, happens."
    hide andhika with moveoutbottom

    # --- 10. DJERICO ---
    show djerico at right with moveinbottom
    gim "TERAKHIR! Plot twist kita. Djerico!"
    gim "Satu-satunya ALCHEMIST (Teknik Kimia) di antara para anak Komputer."
    gim "Baik djerico, apa nih kata-kata alchemist kita?"
    
    # REVISI: Menggunakan Full Quote
    dje "Do Your best, and God will do the rest."
    
    gim "Nah, mantap quotes-nya lengkap."
    hide djerico with moveoutbottom

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
