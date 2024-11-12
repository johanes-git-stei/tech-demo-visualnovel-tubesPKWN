# The script of the game goes in this file.

# Character definition and image

define Furina = Character("Furina", color="#4f82bb")
define Raiden = Character("Raiden Ei", color="#37316d")
define FurRai = Character("Furina & Raiden", color="#435b94")

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
    Raiden "baik! pertama mari kita bahas mengenai background dan sprite image!"
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
    Raiden "sangat!"

    # This ends the game.

    return
