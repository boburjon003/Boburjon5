# def salom_ber(ism,yil):
#     """Salom beruvchi funksiya :"""
#     print(f"Assalomu alekum, {ism.title()},siz {2024-yil}yoshdasiz!")
    
    
    
# ism=input("ismingizni Kiriting>>")
# yil=int(input("yoshingizni kiriting>>"))
# salom_ber(ism, yil)

# def kvadrat_kub(x):
#     print(f"sonni kvadrati {x*x}, kubi esa {x**3} ga teng")
    
    
# x=int(input("istalgan sonni kiriting >>"))
# kvadrat_kub(x)

# def to_juft(x):
#     if x%2==0:
#         print(f"{x} bu juf son")
#     else:
#         print(f"{x} bu toq son")
        
# x=int(input("istalgan sonni kiriting >>"))
# to_juft(x)

# def katta_son(x,y):
#     if x>y:
#         print(f"{x} katta {y} dan")
#     elif y>x:
#         print(f"{y}  katta {x} dan")
#     else:
#         print("sonlar teng")
        
        
# x=int(input("birinchi sonni kiriting >>"))
# y=int(input("ikkinchi sonni kiriting >>"))
# katta_son(x, y)


# def x_y(x,y=2):
#     print(x)
#     print(y)
    

# x=int(input("x ni qiymatini kiriting >>"))
# x_y(x, 2) 

def bolinishi(son):
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsz bo'linadi")

bolinishi(20)
        
        
    
 
       
        
    
    