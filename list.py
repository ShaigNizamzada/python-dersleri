isimler = ["Shaig", "Nizamzada", "John", "Doe"]
karisik = [1, "Shaig", True, 2.5, "Nizamzada"]

# # append fonksiyonu ile listeye eleman eklemek
# isimler.append("Ali")
# print(isimler)
# # insert fonksiyonu ile listeye eleman eklemek
# isimler.insert(1,"Deniz")
# print(isimler)
# # remove fonksiyonu ile listeden eleman silmek
# isimler.remove("Ali")
# print(isimler)
# # pop fonksiyonu ile listeden son elemanı silmek
# isimler.pop()
# print(isimler)

sayilar = [1, 2, 3, 4, 7, 5]

# print(len(sayilar))
# print(sum(sayilar))
# print(max(sayilar))
# print(min(sayilar))
# sayilar.sort()
# print(sayilar)
# sayilar.reverse()
# print(sayilar)
# print(sayilar[1:4])
# print(sayilar[:4])

# isimler2 = ["Shaig", "Nizamzada", "John", "Doe"]

# for i in isimler2:
#     print("merhaba", i)

# for index,isim in enumerate(isimler2):
#     print(index+1, ":",isim)

a= [1,2,3]
b=a  #  not copy, reference
b=a.copy() # copy, copy the list


b.append(4)
print(a)
print(b)