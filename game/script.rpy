define c = Character("Lylia", color="#ffaaaa")
image lylia netral = "lylia_netral.png"
image lylia senyum = "lylia_senyum.png"
define y = Character("Michael", color="#4db8ff")

define slow_dissolve = Dissolve(2.0)
define fade_black = Fade(1.0, 1.0, 1.0)

transform kecil:
    zoom 0.65 

label start:

    # ==========================================
    # BABAK 1: PERMULAAN (Di Rumah / Jalan)
    # ==========================================
    
    scene bg_rumah
    with slow_dissolve

    "Pagi hari yang cerah. Aku sedang menunggu Lylia."
    "Sekarang pukul 09:10. Lylia telat 10 menit dari waktu yang dijanjikan. "

    show lylia netral at center, kecil
    with dissolve

    c "Michael! Maaf telat ya." 
    y "Tumben orang paling disiplin bisa telat juga." 

    show lylia senyum at center, kecil
    with dissolve 

    c "Ahaha... Tadi ibuku meminta tolong untuk menjemur pakaian dulu."

    show lylia netral at center, kecil
    with dissolve
    
    c "Jadi, hari ini kita jadi pergi ke kota kan?"

    y "Iya, ayo kita berangkat sekarang."

    # ==========================================
    # TRANSISI PERJALANAN (Layar Hitam)
    # ==========================================
    scene black
    with fade_black

    "Kami pun naik bus menuju pusat kota..."

    # ==========================================
    # BABAK 2: KONFLIK / KEGIATAN (Di Kota)
    # ==========================================

  
    scene bg_kota3
    with dissolve

    "Suasana kota sangat ramai hari ini."
    
    show lylia_senang at center, kecil
    with dissolve

    c "Wah! Lihat gedung itu! Bagus banget ya."
    c "Desainnya modern banget. Kapan ya aku bisa mendesain gedung kayak gitu?"
    y "Pasti bisa dong. Nanti kalau kamu sukses, jangan lupa desain rumahku ya."

    show lylia_senang at center, kecil 
    
    c "Boleh, asal bayarannya mahal ya! Hehe."
    
    show lylia_netral at center, kecil
    with dissolve
    
    y "Siap, Bos. Eh, mumpung di sini, kita mau kemana?"

    menu:
        "Pilihan A: Cari Makan":
            jump cari_makan

        "Pilihan B: Ke Toko Buku":
            jump toko_buku

# --- CABANG CERITA A ---
label cari_makan:
    y "Kita cari makan dulu yuk, lapar nih."
    
    show lylia_senang at center, kecil
    c "Setuju! Aku juga belum sarapan."
    
    "Kami pun menghabiskan waktu mencari restoran enak."
    
    jump babak_akhir # Lompat ke ending

# --- CABANG CERITA B ---
label toko_buku:
    y "Ke toko buku aja, cari referensi tugas."
    
    show lylia_netral at center, kecil
    c "Hmm, oke deh. Tapi jangan lama-lama ya."
    
    "Kami masuk ke toko buku dan melihat-lihat novel terbaru."
    
    jump babak_akhir # Lompat ke ending

    # ==========================================
    # BABAK 3: ENDING (Di Kota / Sore Hari)
    # ==========================================
label babak_akhir:

    scene black
    with fade_black

    scene bg_kota2_afternoon
    with slow_dissolve

    "Hari sudah sore. Kami duduk istirahat sebentar sebelum pulang."

    show lylia_senang at center, kecil
    with dissolve

    c "Hah... Capek tapi seru ya hari ini."
    c "Kakiku rasanya mau copot. Tapi makasih ya udah nemenin."
    y "Santai aja. Yuk pulang, besok ada kuliah pagi."

    "Kami pun berjalan menuju halte bus untuk pulang ke rumah masing-masing."
    
    # Layar hitam total (Tamat)
    scene black 
    with slow_dissolve

    "TAMAT"

    return