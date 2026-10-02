# secim= int(input("bir sayıyı giriniz: "))

# match secim:
#     case 1:
#         print("sectiginiz sayi 1 ")
#     case 2:
#         print("sectiginiz sayi 2 ")
#     case 3:
#         print("sectiginiz sayi 3 ")
#     case 4:
#         print("sectiginiz sayi 4 ")
#     case 5 | 6:
#         print("sectiginiz sayi 5 ")
#     case _:
#         print("geçersiz seçim")

user = ("Shaig",30)

match user:
    case (name,age):
        print(f"merhaba {name}, {age} yaşındasınız.")