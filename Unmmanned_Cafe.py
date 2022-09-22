import sys
import barista_module

print("Glory coffee에 오신걸 환영합니다.")

menu = barista_module.menu

def show_menu():
    print("==<< 메뉴 >>==")
    for key in sorted(menu):
        print(key + ".",menu[key])
    return

def get_order():
    order = input("무엇을 주문하시겠어요?(q.종료) : ")
    if order == "q":
        print("주문이 취소 되었습니다.")
        sys.exit(0)
    print(order+"번을 주문하셨습니다.")
    return order

recipe = barista_module.recipe

def process_order(order):
    func = recipe.get(order)
    if func != None:
        func()
    else:
        print("다시 주문해주세요")
    return
count = 0
while True:
    count = count + 1
    if count == 1:
        print("주문 하시겠습니까?")
        first = input("yes 아니면 no를 입력하세요> ")
        if first == "yes":
            #메뉴 보여주기
            print("메뉴판을 보여드겠습니다.")
            show_menu()
            #주문 받기
            order=get_order()
            #주문 처리하기
            process_order(order)
        elif first == "no":
            print("주문을 취소합니다.")
            sys.exit(0)
    else:
        print("추가 주문 하시겠습니까?")
        first = input("yes 아니면 no를 입력하세요> ")
        if first == "yes":
            #메뉴 보여주기
            show_menu()
            #주문 받기
            order=get_order()
            #주문 처리하기
            process_order(order)
        elif first == "no":
            print("주문을 취소합니다.")
            sys.exit(0)