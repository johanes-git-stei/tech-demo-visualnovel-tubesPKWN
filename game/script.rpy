# The script of the game goes in this file.

# Character definition and image

define Furina = Character("Furina", color="#4f82bb")
define Raiden = Character("Raiden Ei", color="#37316d")
define FurRai = Character("Furina & Raiden", color="#435b94")
define narrator = Character("Random Narrator", color="#44ad49")

# variable definition
default furina_point = 0
default raiden_point = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_itbplawid with dissolve:
        blur 20

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show furina_default at Position(xalign=0.5, yalign=0.61)

    # These display lines of dialogue.

    # furina default center
    Furina "Halo semuanya!"
    Furina "It is I! Furina!"
    # raiden default center, furina left
    Raiden "...dan aku Raiden Ei."
    # raiden right
    Furina "Disini kita akan memperkenalkan kalian mengenai RenPy!"
    Raiden "Bagaimana cara gameplay RenPy berjalan pada dasarnya"
    Furina "tentang background dan sprite image, transisi..."
    # raiden happy
    Raiden "...minigames dan multiple ending choice!"
    # raiden default
    Raiden "Nah sebelum kita mulai..."
    Raiden "boleh tahu tidak, namamu siapa?"
    
    # pemain memasukkan namanya, nama default dari MC adalah Rusdi.
    $ player_name = renpy.input("Masukkan nama yang ingin anda gunakan:", default="Rusdi")
    $ player_name = player_name.strip()

    # Furina happy, Raiden happy
    Furina "Halo, [player_name]!"
    Raiden "Senang bertemu dengan anda, [player_name].."

    # Furina default, Raiden default
    Furina "Mari kita..."
    # Furina happy, Raiden happy
    FurRai "Mulai!"

label background_sprite:
    scene bg_sunkencourt with dissolve:
        blur 20

    # raiden default
    Raiden "baik! mari kita bahas mengenai background dan sprite image!"
    # Furina confused
    Furina "Hm... apa itu background dan sprite, Raiden?"
    Raiden "Nah background adalah latar belakang yang muncul dalam suatu scene dalam visual novel!"
    Raiden "..seperti gambar yang ada di belakang ini!"
    Raiden "[player_name], kamu kenal nggak dengan tempat di belakang kita?"

    menu:
        "hm.. Sunken Court, nggak sih?":
            # Raiden happy
            Raiden "benar! ini adalah Sunken Court!"

        "aku lupa, Raiden...":
            # Raiden sad
            Raiden "Yah, rupanya kamu kurang perhatian terhadap lingkunganmu, [player_name].."
            # Raiden default
            Raiden "ini adalah sunken court ya!"
    
    Raiden "Mari kita lanjut!"
    Raiden "Background bisa digunakan untuk menentukan setting cerita, suasana, dan waktu!"
    Raiden "pastikan background yang digunakan memiliki resolusi yang bagus dan aspek rasio yang sesuai dengan visual novelmu"
    # Furina confused
    Furina "seperti 1920 x 1080?"
    # Raiden happy
    Raiden "benar, Furina!"
    # Raiden default
    Raiden "selanjutnya adalah sprite!"
    Raiden "Kamu tahu tidak, apa itu sprite, Furina?"
    Furina "hmm, apa itu Raiden?"
    Raiden "Sprite adalah karakter yang muncul dalam visual novel!"
    Raiden "atau singkatnya, sprite adalah avatar dari masing-masing karakter dalam visual novel tersebut."
    # Furina confused
    Furina "s- seperti kita berdua?!"
    Raiden "benar, Furina!"
    # Furina annoyed
    Furina "damn..."
    Raiden "..."
    Furina "..."
    Raiden "..."
    Raiden "Anyway..."
    Raiden "sprite juga bisa digunakan untuk menunjukkan emosi dari karakter tersebut!"
    Raiden "contohnya.."
    # Furina confused
    # Raiden happy
    Raiden "Sprite ekspresi happy"
    # Raiden sad
    Raiden "Sprite ekspresi sad"
    # Raiden confused
    Raiden "Sprite ekspresi confused"
    # Raiden annoyed
    Raiden "Sprite ekspresi annoyed"
    # Raiden default
    Raiden "last but not least, sprite expresi default atau biasa sering digunakan jika karakter memiliki emosi netral."
    # Furina default
    Furina "Wow... jadi background dan sprite itu penting ya, Raiden?"
    Raiden "Benar, terutama jika kamu ingin visual novelmu memiliki latar dan karakter yang unik!"

    # This ends the game.

label transisi:
    # Furina default, Raiden default
    Raiden "Kali ini, kita akan bahas mengenai transisi~"
    Furina "Transisi memiliki banyak fungsi dalam visual novel, terutama pada pergantian scene dan posisi karakter!"
    Raiden "Benar sekali, Furina! Coba jelaskan transisi apa saja yang dapat kita gunakan dalam visual novel!"
    Furina "cih nyuruh-nyuruh kowe..."
    Raiden "..."
    Furina "..."
    # Raiden furious, Furina annoyed
    Raiden "無我の境地へ。"
    Furina "BAIK! Transisi pertama yang ingin aku bahas transisi dalam scene!"
    # change bg scene
    Furina "Scene seperti yang ada dibelakang kita sebenernya dapat diubah kapan saja dan kita menggunakan transisi untuk membuat perubahan scene menjadi lebih halus!"
    # change bg scene
    Furina "Transisi scene dapat digunakan sebagai cara yang kreatif..."
    # change bg scene, Raiden confused
    Furina "...untuk memperlihatkan perubahan suasana atau waktu..."
    # change bg scene
    Furina "...dalam cerita atau visual novel!"
    # reset bg scene, Raiden default
    Furina "Selanjutnya adalah tansisi dalam karakter atau biasa disebut sprite!"
    Furina "Transisi sprite digunakan untuk mengubah posisi karakter atau mengeluarkan karakter dari scene!"
    Furina "misalnya..."
    # Furina dissolved away
    Furina "Dissolved"
    Furina "Fade"
    Furina "move"
    Furina "pixelated"
    Furina "atau bahkan animasi khusus..."
    # Furina spinning animation
    Furina "seperti ini!"
    Raiden "..."
    Raiden "Baik... sekian dari kami mengenai transisi!"
    # Furina still spinning
    Raiden "Ingat [player_name], transisi dapat digunakan untuk membuat scene dan karaktermu menjadi lebih hidup!"
    # scene fade in, Furina still spinning

label multiple_choice_ending:
    #furina default, Raiden default
    Furina "Mari kita bahas salah satu aspek paling penting dalam suatu visual novel..."
    Raiden "Multiple ending choice!"
    Furina "Seperti yang kita tahu, multiple ending choice adalah pilihan yang diberikan kepada pemain..."
    Furina "..untuk memilih ending yang diinginkan berdasarkan aksinya di suatu visual novel!"
    Raiden "Untuk mendapatkan ending tertentu, perlu dilakukan aksi-aksi spesifik seperti memiliki cukup in-game currency, berinteraksi dengan karakter utama lainnya atau bahkan menemukan Easter Egg untuk mendapatkan secret ending!"
    Raiden "Mari kita mulai dengan contoh sederhana, [player_name]!"
    Furina "Mari kita mulai dengan scenario sederhana!"

    # ganti scene fade in / out
    Narrator "dalam scenario ini, kamu diberi 3 ending:"
    Narrator "1. Ending bersama Furina"
    Narrator "2. Ending bersama Raiden"
    Narrator "3. Ending netral"
    Narrator "Ending-ending ini dapat didapatkan berdasarkan pilihan mu dibawah ini!"
    Narrator "Pilihanmu adalah..."
    Narrator "1. Hangout bersama Furina"
    Narrator "2. Hangout bersama Raiden"
    Narrator "3. Tidak hangout sama sekali"
    Narrator "Pilihan ini akan diulang 4 kali, jumlah total kamu hangout dengan karakter ini akan menentukan endingnya"
    Narrator "Semakin sering hangout maka semakin besar kemungkinan kamu mendapatkan ending bersama karakter tersebut!"
    Narrator "Are you ready, [player_name]?"
    Narrator "let's start!"

    menu:
        "Hangout bersama Furina":
            $ furina_point += 1
            jump multiple_choice_ending

        "Hangout bersama Raiden":
            $ raiden_point += 1
            jump multiple_choice_ending

        "Tidak hangout sama sekali":
            jump multiple_choice_ending


label music:

label minigame:


    return
