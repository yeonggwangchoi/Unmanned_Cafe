print("Glory coffee에 오신걸 환영합니다~")

while True:
    #메뉴 보여주기
    print("==<< 메뉴 >>==")
    print("1. 아메리카노")
    print("2. 카페라떼")
    print("3. 에스프레소")
    print("4. 녹차")
    print("5. 망고쥬스")
    
    #주문 받기
    order = input("무엇을 주문하시겠어요?(q.종료) : ")
    if order == "q":
        print("주문이 취소 되었습니다!")
        break;
    print(order, "주문하셨습니다.")
    
    if order == "1":
        print("아메리카노를 만들고 있습니다~")
    elif order == "2":
        print("카페라떼를 만들고 있습니다~")
    elif order == "3":
        print("에스프레소를 만들고 있습니다~")
    elif order == "4":
        print("녹차를 만들고 있습니다~")
    elif order == "5":
        print("망고쥬스를 만들고 있습니다~")
    else:
        print("다시 주문해주세요~")
        
        test!!