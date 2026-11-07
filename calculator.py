
from pprint import pprint

pprint("<========== Simple Calculator ==========>")

while True:
    son1 = input("1-sonni kiriting => ")
    son2 = input("2-sonni kiriting => ")
    amal = input("Amalni kiriting (+ , * , - , /) => ")    
    
    if "." or "," in son1:
        son_1 = float(son1)
    else:
        son_1 = int(son1)
        
    if "." or "," in son2:
        son_2 = float(son2)
    else:
        son_2 = int(son2)

    if amal == "+":
        print(f"{son_1} + {son_2} = {son_1 + son_2}")
    elif amal == '*': 
        print(f"{son_1} * {son_2} = {son_1 * son_2}")
    elif amal == '-':
        print(f"{son_1} - {son_2} = {son_1 - son_2}")
    elif amal == '/':
        if son_2 == 0:
            print("Nolga bo'lib bo'lmaydi!")
            break
        else:
            print(f"{son_1} / {son_2} = {son_1 / son_2}")
    else:
        pprint("Matematikada bunday amal yo'q")
         
    print("Davom etasizmi?")
    print("Istalgan narsani kiritsangiz davom etasiz.")
    print("q yoki quit kiritsangiz Canculator to'xtaydi.")
    again_or_no = input("Birini tanlang: ")
    if again_or_no == 'q' or again_or_no == 'quit':
        pprint("Siz Canculator ni to'xtatdingiz.")
        break
    else:
        continue
