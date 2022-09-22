menu = {
    "1" : "아메리카노",
    "2" : "카페라떼",
    "3" : "에스프레소",
    "4" : "녹차",
    "5" : "망고쥬스"
}

def make_americano():
    print("아메리카노를 주문하셨습니다.")

    return
def make_cafelatte():
    print("카페라떼를 주문하셨습니다.")
    return
def make_espresso():
    print("에스프레소를 주문하셨습니다.")
    return
def make_greentee():
    print("녹차를 주문하셨습니다.")
    return
def make_mangojuice():
    print("망고쥬스를 주문하셨습니다.")
    return

recipe = {
    "1" : make_americano,
    "2" : make_cafelatte,
    "3" : make_espresso,
    "4" : make_greentee,
    "5" : make_mangojuice
}