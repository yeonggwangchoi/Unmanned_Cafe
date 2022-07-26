import sys

print("Glory coffee에 오신걸 환영합니다.")
print("메뉴판을 보여드릴까요?")
menu = input("yes 아니면 no를 입력하세요> ")
if menu == "yes":
    print("")
else:
    print("")

def show_menu():
    print("==<< 메뉴 >>==")
    print("1. 아메리카노")
    print("2. 카페라떼")
    print("3. 에스프레소")
    print("4. 녹차")
    print("5. 망고쥬스")
    return
def get_order():
    order = input("무엇을 주문하시겠어요?(q.종료) : ")
    if order == "q":
        print("주문이 취소 되었습니다!")
        sys.exit(0)
    print(order, "주문하셨습니다.")
    return order
def make_americano():
    print("아메리카노를 만들고 있습니다~")
    return
def make_cafelatte():
    print("카페라떼를 만들고 있습니다~")
    return
def make_espresso():
    print("에스프레소를 만들고 있습니다~")
    return
def make_greentee():
    print("녹차를 만들고 있습니다~")
    return
def make_mangojuice():
    print("망고쥬스를 만들고 있습니다~")
    return

def process_order(order):
    if order == "1":
        make_americano()
    elif order == "2":
        make_cafelatte()
    elif order == "3":
       make_espresso()
    elif order == "4":
       make_greentee()
    elif order == "5":
       make_mangojuice()
    else:
        print("다시 주문해주세요~")
    return

while True:
    #메뉴 보여주기
    show_menu()
    
    #주문 받기
    order=get_order()
    
    #주문 처리하기
    process_order(order)
    
    #영업 종료 기능 추가 할 것