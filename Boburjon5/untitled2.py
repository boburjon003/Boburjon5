# Home task 1 Buyurtmalar qabul qiluvchi dastur >>
# yangi_royxat = []
# ishora = True

# while ishora:
#     savol = ("mahsulot nomini kiriting ::")
#     nomi = input(savol)
#     yangi_royxat.append(nomi)
#     javob= input(("yana ma'lumot qo'shaszmi (ha/yoq) ::"))
#     if javob == "yoq":
#         ishora = False
        
# for nomi in yangi_royxat:
#     print(nomi.title())


# e_bozor = {}
# ishora = True
# n=1
# while ishora:
#     nomi=input(f" bozor u/n {n}chi maxsulot nomini kiriting >>")
#     narhi = input("mahsulot narxini kiriting ")
#     e_bozor[nomi]=int(narhi)
#     n+=1
#     javo = input("yana mahsulot qo'shmoqchimisz (ha/yoq)")
#     if javo == 'yoq':
#         ishora = False

# for nomi, narhi in e_bozor.items():
#     print(f"{nomi.title()}  {narhi} sum")
    

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar :
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh= mahsulotlar[buyurtma]
#         # mahsulotlar=int(narh)
#         print(f"{buyurtma.title} - {narh}")
#     else:
#         print("bizda bunday mahsulot yoq")
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")