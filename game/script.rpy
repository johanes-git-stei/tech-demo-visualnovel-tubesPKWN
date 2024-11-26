# The script of the game goes in this file.

# Character definition and image
define Furina = Character("Furina", color="#4f82bb")
define Raiden = Character("Raiden Ei", color="#37316d")
define FurRai = Character("Furina & Raiden", color="#435b94")
define Narrator = Character("Random Narrator", color="#44ad49")

# Position and short, reusable animations definition
define furina_def_pos = Position(xalign=0.1, yalign=0.58)
define raiden_def_pos = Position(xalign=0.9, yalign=0.58)

# variable definition
default furina_point = 0
default raiden_point = 0
default countdown = 4

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
    with dissolve


    # These display lines of dialogue.

    # furina default center
    Furina "Halo semuanya!"
    Furina "It is I! Furina!"
    # raiden default center, furina left
    show furina_default at furina_def_pos
    with moveinright
    show raiden_default at Position(xalign=0.5, yalign=0.61)
    with dissolve
    Raiden "...dan aku Raiden Ei." 
    # raiden right
    show raiden_default at raiden_def_pos    
    with moveinleft
    Furina "Disini kita akan memperkenalkan kalian mengenai RenPy!" 
    Raiden "Bagaimana cara gameplay RenPy berjalan pada dasarnya.." 
    Furina "tentang background dan sprite image, transisi..." 
    # raiden happy
    hide raiden_default
    show raiden_happy at raiden_def_pos
    Raiden "...minigames dan multiple ending choice!" 
    # raiden default
    hide raiden_happy
    show raiden_default at raiden_def_pos
    Raiden "Nah sebelum kita mulai..." 
    Raiden "boleh tahu tidak, namamu siapa?" 
    
    # pemain memasukkan namanya, nama default dari MC adalah Rusdi.
    $ player_name = renpy.input("Masukkan nama yang ingin anda gunakan:", default="Rusdi")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Rusdi"


    # Furina happy, Raiden happy
    hide furina_default
    show furina_happy at furina_def_pos
    Furina "Halo, [player_name]!" 
    hide raiden_default
    show raiden_happy at raiden_def_pos
    Raiden "Senang bertemu dengan anda, [player_name].." 

    # Furina default, Raiden default
    hide furina_happy
    show furina_default at furina_def_pos
    hide raiden_happy
    show raiden_default at raiden_def_pos
    Furina "Mari kita..." 
    # Furina happy, Raiden happy
    hide furina_default
    show furina_happy at furina_def_pos
    hide raiden_default
    show raiden_happy at raiden_def_pos
    FurRai "Mulai!"

label background_sprite:
    scene bg_sunkencourt with fade:
        blur 20

    # raiden default
    show furina_default at furina_def_pos
    show raiden_default at raiden_def_pos
    Raiden "baik! mari kita bahas mengenai background dan sprite image!"
    # Furina confused
    hide furina_default
    show furina_confused at furina_def_pos
    Furina "Hm... apa itu background dan sprite, Raiden?"
    Raiden "Nah background adalah latar belakang yang muncul dalam suatu scene dalam visual novel!"
    hide furina_confused
    show furina_default at furina_def_pos
    Raiden "..seperti gambar yang ada di belakang ini!"
    Raiden "[player_name], kamu kenal nggak dengan tempat di belakang kita?"

    menu:
        "hm.. Sunken Court, nggak sih?":
            # Raiden happy
            hide raiden_default
            show raiden_happy at raiden_def_pos
            Raiden "benar! ini adalah Sunken Court!"
            hide raiden_happy
            show raiden_default at raiden_def_pos

        "aku lupa, Raiden...":
            # Raiden sad
            hide raiden_default
            show raiden_sad at raiden_def_pos
            Raiden "Yah, rupanya kamu kurang perhatian terhadap lingkunganmu, [player_name].."
            # Raiden default
            hide raiden_sad
            show raiden_default at raiden_def_pos
            Raiden "ini adalah sunken court ya!"
    
    Raiden "Mari kita lanjut!"
    Raiden "Background bisa digunakan untuk menentukan setting cerita, suasana, dan waktu!"
    Raiden "pastikan background yang digunakan memiliki resolusi yang bagus dan aspek rasio yang sesuai dengan visual novelmu"
    # Furina confused
    hide furina_default
    show furina_confused at furina_def_pos
    Furina "seperti 1920 x 1080?"
    # Raiden happy
    hide raiden_default
    show raiden_happy at raiden_def_pos
    Raiden "benar, Furina!"
    hide furina_confused
    show furina_default at furina_def_pos
    # Raiden default
    hide raiden_happy
    show raiden_default at raiden_def_pos
    Raiden "selanjutnya adalah sprite!"
    Raiden "Kamu tahu tidak, apa itu sprite, Furina?"
    Furina "hmm, apa itu Raiden?"
    Raiden "Sprite adalah karakter yang muncul dalam visual novel!"
    Raiden "atau singkatnya, sprite adalah avatar dari masing-masing karakter dalam visual novel tersebut."
    # Furina confused
    hide furina_default
    show furina_annoyed at furina_def_pos
    Furina "s- seperti kita berdua?!"
    Raiden "benar, Furina!"
    # Furina annoyed
    hide furina_annoyed
    show furina_confused at furina_def_pos
    Furina "damn..."
    hide raiden_default
    show raiden_sad at raiden_def_pos
    Raiden "..."
    Furina "..."
    Raiden "..."
    hide raiden_sad
    show raiden_default at raiden_def_pos
    Raiden "Anyway..."
    hide furina_confused
    show furina_default at furina_def_pos
    Raiden "sprite juga bisa digunakan untuk menunjukkan emosi dari karakter tersebut!"
    Raiden "contohnya.."
    # Furina confused
    hide furina_default
    show furina_confused at furina_def_pos
    # Raiden happy
    hide raiden_default
    show raiden_happy at raiden_def_pos
    Raiden "Sprite ekspresi happy"
    # Raiden sad
    hide raiden_happy
    show raiden_sad at raiden_def_pos
    Raiden "Sprite ekspresi sad atau sedih"
    # Raiden confused
    hide raiden_sad
    show raiden_confused at raiden_def_pos
    Raiden "Sprite ekspresi confused atau kebingungan"
    # Raiden annoyed
    hide raiden_confused
    show raiden_annoyed at raiden_def_pos
    Raiden "Sprite ekspresi annoyed"
    # Raiden default
    hide raiden_annoyed
    show raiden_default at raiden_def_pos
    Raiden "last but not least, sprite expresi default atau biasa sering digunakan jika karakter memiliki emosi netral."
    # Furina default
    hide furina_confused
    show furina_default at furina_def_pos
    Furina "Wow... jadi background dan sprite itu penting ya, Raiden?"
    Raiden "Benar, terutama jika kamu ingin visual novelmu memiliki latar dan karakter yang unik!"

label transisi:
    scene bg_campuscenter with fade:
        blur 20

    # Furina default, Raiden default
    show furina_default at furina_def_pos
    with dissolve
    show raiden_default at raiden_def_pos
    with dissolve
    Raiden "Kali ini, kita akan bahas mengenai transisi~"
    Furina "Transisi memiliki banyak fungsi dalam visual novel, terutama pada pergantian scene dan posisi karakter!"
    Raiden "Benar sekali, Furina! Coba jelaskan transisi apa saja yang dapat kita gunakan dalam visual novel!"
    # Furina annoyed
    hide furina_default
    show furina_annoyed at furina_def_pos
    Furina "cih nyuruh-nyuruh kowe..."
    Raiden "..."
    Furina "..."
    # Raiden furious, Furina happy
    hide raiden_default
    show raiden_furious at raiden_def_pos
    Raiden "tak keplak rai kowe-"
    hide furina_annoyed
    show furina_happy at furina_def_pos
    Furina "BAIK! Transisi pertama yang ingin aku bahas transisi dalam scene!"
    # change bg scene
    scene bg_its with pixellate:
        blur 20
    hide bg_campuscenter with dissolve

    show furina_happy at furina_def_pos
    with dissolve
    hide raiden_furious
    show raiden_default at raiden_def_pos
    with dissolve
    Furina "Scene seperti yang ada dibelakang kita sebenernya dapat diubah kapan saja dan kita menggunakan transisi untuk membuat perubahan scene menjadi lebih halus!"
    # change bg scene
    scene bg_ui with slideleft:
        blur 20
    hide bg_campuscenter with dissolve

    show furina_default at furina_def_pos
    with dissolve
    hide raiden_furious
    show raiden_default at raiden_def_pos
    with dissolve
    Furina "Transisi scene dapat digunakan sebagai cara yang kreatif..."
    # change bg scene, Raiden confused
    scene bg_collosaltitan with blinds:
        blur 10
    hide bg_ui with dissolve

    show furina_default at furina_def_pos
    with dissolve
    hide raiden_default
    show raiden_confused at raiden_def_pos
    with hpunch
    Furina "...untuk memperlihatkan perubahan suasana atau waktu..."
    # change bg scene
    scene bg_minecraft with irisin:
        blur 10
    hide bg_collosaltitan with dissolve

    show furina_default at furina_def_pos
    with dissolve
    show raiden_confused at raiden_def_pos
    with dissolve
    Furina "...dalam cerita atau visual novel!"
    # reset bg scene, Raiden default
    scene bg_campuscenter with irisout:
        blur 10
    hide bg_minecraft with dissolve

    show furina_default at furina_def_pos
    with dissolve
    show raiden_confused at raiden_def_pos
    with dissolve
    Furina "Selanjutnya adalah tansisi dalam karakter atau biasa disebut sprite!"
    
    hide raiden_confused
    show raiden_default at raiden_def_pos
    Furina "Transisi sprite digunakan untuk mengubah posisi karakter atau mengeluarkan karakter dari scene!"
    Furina "misalnya..."
    # Furina dissolved away
    hide furina_default
    with dissolve
    Furina "Dissolved"
    show furina_default at furina_def_pos
    with dissolve
    hide furina_default
    with fade
    Furina "Fade"
    show furina_default at furina_def_pos
    with dissolve
    hide furina_default
    with slideawayleft
    Furina "move"
    show furina_default at furina_def_pos
    with dissolve
    hide furina_default
    with pixellate
    Furina "pixelated"
    Furina "atau bahkan animasi khusus..."
    # Furina spinning animation
    Furina "seperti ini!"
    Raiden "..."
    hide raiden_default
    show raiden_annoyed at raiden_def_pos
    with dissolve
    Raiden "Baik... sekian dari kami mengenai transisi!"
    # Furina still spinning
    hide raiden_annoyed
    show raiden_happy at raiden_def_pos
    with dissolve
    Raiden "Ingat [player_name], transisi dapat digunakan untuk membuat scene dan karaktermu menjadi lebih hidup!"
    # scene fade in, Furina still spinning

label multiple_choice_ending:
    scene bg_senirupa with fade:
        blur 20

    # Furina default, Raiden default
    show furina_default at furina_def_pos
    with dissolve
    show raiden_default at raiden_def_pos
    with dissolve

    Furina "Mari kita bahas salah satu aspek paling penting dalam suatu visual novel..."
    hide raiden_default
    show raiden_happy at raiden_def_pos
    Raiden "Multiple ending choice!"
    Furina "Seperti yang kita tahu, multiple ending choice adalah pilihan yang diberikan kepada pemain..."
    hide raiden_happy
    show raiden_default at raiden_def_pos
    Furina "..untuk memilih ending yang diinginkan berdasarkan aksinya di suatu visual novel!"
    Raiden "Untuk mendapatkan ending tertentu, perlu dilakukan aksi-aksi spesifik seperti memiliki cukup in-game currency, berinteraksi dengan karakter utama lainnya atau bahkan menemukan Easter Egg untuk mendapatkan secret ending!"
    hide furina_default
    show furina_happy at furina_def_pos
    Raiden "Mari kita mulai dengan contoh sederhana, [player_name]!"

    # ganti scene fade in / out
    scene bg_classroom with irisout:
        blur 10
    hide bg_senirupa with dissolve

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


    while countdown != 0:
        Narrator "Sisa kesempatan hangout: [countdown]\nTotal hangout bersama Furina: [furina_point]\nTotal hangout bersama Raiden: [raiden_point]"
        menu:
            "Hangout bersama Furina":
                $ furina_point += 1
                $ countdown -= 1

            "Hangout bersama Raiden":
                $ raiden_point += 1
                $ countdown -= 1

            "Tidak hangout sama sekali":
                $ countdown -= 1
                pass
    
if furina_point > raiden_point:
    label furina_ending:
        Narrator "Congratulation! Akhirnya kamu pergi berlibur ke Prancis bersama Furina\nTotal hangout bersama Furina: [furina_point]!"

elif raiden_point > furina_point:
    label raiden_ending:
        Narrator "Congratulation! Akhirnya kamu pergi berlibur ke Jepang bersama Raiden!\nTotal hangout bersama Raiden: [raiden_point]"

else:
    label neutral_ending:
        Narrator "sayangnya kamu tidak berlibur sama sekali... mungkin lain kali ya, [player_name]?"


label music:
    Raiden "Suatu visual novel atau game tidak akan lengkap tanpa adanya musik!"
    Furina "Musik dapat digunakan untuk menambahkan emosi dalam scene atau memberikan kesan yang lebih mendalam pada pemain!"
    Furina "Musik dapat digunakan untuk mengidentifikasikan suatu suasana atau perasaan bahkan karakter tertentu!"
    Raiden "Ada beberapa jenis musik yang dapat digunakan dalam visual novel, seperti..."
    Raiden "Musik netral atau bisa dianggap sebagai background music..."
    Furina "Background music biasanya didesain untuk menemani scene atau cerita dalam visual novel!"
    Raiden "selanjutnya ada musik sedih atau sad music..."
    Furina "Sad music biasanya digunakan untuk scene yang menyedihkan atau mengharukan..."
    Raiden "Kemudian ada musik happy!"
    Furina "Happy music biasanya digunakan untuk scene yang ceria atau menyenangkan!"
    Raiden "Sebenarnya ada banyak bentuk musik tergantung suasana dan cerita yang ingin kamu buat!"
    Raiden "Namun ada satu musik yang lumayan unik tidak hanya untuk scene tapi juga untuk minigame!"
    Raiden "contohnya musik battle"
    Furina "Musik battle biasanya digunakan untuk scene pertarungan atau minigame!"
    Furina "...dan didesain untuk menambahkan ketegangan dan semangat dalam scene tersebut!"
    Raiden "Jadi, jangan lupa untuk memilih musik yang tepat untuk scene dan ceritamu, [player_name]!"



label minigame:


    return
