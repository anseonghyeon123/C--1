shopping_bag = {}

while True:
    item = input("상품명? ")

    if item == "":
        break
    
    quantity = int(input("수량은? "))
    
    shopping_bag[item] = quantity
   
    print(f"장바구니에 {item} {quantity}개가 담겼습니다.")

print(f">>> 장바구니 보기: {shopping_bag}")

item_to_find = input("[검색]\n장바구니에서 확인하고자 하는 상품은? ")

if item_to_find in shopping_bag:
    print(f"{item_to_find}은(는) {shopping_bag[item_to_find]}개 담겨 있습니다.")
else:
    print(f"{item_to_find}은(는) 장바구니에 없습니다.")
