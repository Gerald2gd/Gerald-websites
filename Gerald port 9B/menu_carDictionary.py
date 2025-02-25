print("Premium Dealership")
print("By Fitzgerald BPL 9B")
print("_____________________________________")
print("Selamat datang di dealer premium! ")
print("Mobil terbaru kami: Porsche 911 GT3, Pagani Huayra, Avanza 1UZ V8 Swap, Isuzu MUX Twin Turbo, Dodge Charger SRT, Toyota Fortuner GR Sport, Hilux GR Sport")

harga = {
    "Pagani Huayra": 54000000000,
    "Dodge Charger SRT":8000000000,
    "Isuzu MUX Twin Turbo":600000000,
    "Porsche 911 GT3": 3000000000,
    "Avanza 1UZ V8 Swap":650000000,
    "Toyota Fortuner GR Sport":755000000,
    "Toyota Hilux GR Sport":540000000,
}

menu_mobil = input("Silahkan pilih mobil yang anda ingin: ")
if menu_mobil in harga:
    print(f"Mobil {menu_mobil} memiliki harga {harga[menu_mobil]}")
    print(f"enjoy your {menu_mobil}")

else:
    print("Selamat datang di dealer premium! ")
print("terima kasih! ")