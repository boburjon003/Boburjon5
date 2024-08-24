# ism = input("Ismingiz  nima ")
# savol = f"Salom , {ism.title()}.Yoshingiz nechchida?"
# yosh = int(input(savol))
# height = float(input("Bo'yingiz necha metr"))

# son=1
# while son<=5:
#     print(son, )
#     son+=1

# savol = ("istalgan sonni kiriting")
# savol += "(dasturni to'xtatish uchun 'exit' deb yozin ):"
# qiymat = ' '
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat !='exit':
#         print(int(qiymat)**2)
# savol =("istalgan sonni kiriting ")
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing )"
# qiymat =''
# ishora = True
# while ishora :
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(int(qiymat)**2)
# savol =("istalgan sonni kiriting ")
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing )"
# qiymat =''
# ishora = True
# while ishora :
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(int(qiymat)**2)
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(son**2)
    
# savol = ("yaxshi ko'rgan kasbingizni kiriting :\n")
# savol += "(dasturni to'xtatish uchun 'stop' so'zini kiriting  ) >>"
# ishora = True
# qiymat = ''
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'stop':
#      ishora = False
#     else:
#         print(qiymat)

# savol = ("yoshingizni kiriting ")
# savol += "(chiqishni hohlasez 'quit' yoki 'exit' ni yozing)>>"
# ishora = True
# qiymat = ' '

# while ishora:
#     qiymat=input(savol)
    
#     if qiymat == 'exit' or qiymat == 'quit':
#        ishora = False
#     else:
      
#          yosh=int(qiymat)
       
#          if yosh>0 and yosh<7:
#            print("chipta narxi 2000 so'm")
#          elif yosh>=7 and yosh<18:
#           print("chipta narxi 3000 so'm")
#          elif yosh>=18 and yosh<65:
#           print("chipta narxi 10000 so'm")
#          elif yosh>=65:
#           print("chipta narxi 0 so'm")
savol = ("Yoshingizni kiriting ")
# savol += "(chiqishni hohlasez 'quit' yoki 'exit' ni yozing)>>"
# ishora = True
# qiymat = ''
# while True:
#     qiymat=input(savol)
#     if qiymat == 'quit' or qiymat == 'exit':
#         break
#     else:
#         yosh=int(qiymat)
#         if yosh<7:
#           narh=2000
#         elif yosh>=7 and yosh<18:
#             narh=3000
#         elif yosh>=18 and yosh<65:
#             narh=1000
#         elif yosh>65:
#             narh=0
#         if narh==0:
#             print("sizga chipta bepul")
#         else:
#             print(f"siz uchun chipta {narh} so'm")
        
        
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat =(input(savol))
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
            
            
            
            
            
            
            
            
            
            
            
            
            

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")
    




# while ishora:
#     qiymat = input(savol)
    
#     if qiymat.lower() == 'exit' or qiymat.lower() == 'quit':
#         ishora = False
#     else:
#         try:
#             yosh = int(qiymat)
            
#             if yosh > 0 and yosh < 7:
#                 print("Chipta narxi 2000 so'm")
#             elif yosh >= 7 and yosh < 18:
#                 print("Chipta narxi 3000 so'm")
#             elif yosh >= 18 and yosh < 65:
#                 print("Chipta narxi 10000 so'm")
#             elif yosh >= 65:
#                 print("Chipta narxi 0 so'm")
#         except ValueError:
#             print("Iltimos, yaroqli yosh kiriting!")

   
        
        
        
        
        
        
 