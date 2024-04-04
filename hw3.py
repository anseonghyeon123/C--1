def get_price(discount_rate, discounted_price):
    fixed_price = discounted_price / (1 - discount_rate / 100)
    return fixed_price

def main():
    discount_rate = int(input("할인율은? "))
    discounted_a = int(input("A 상품의 할인된 가격은? "))
    discounted_b = int(input("B 상품의 할인된 가격은? "))
    
    fixed_a = get_price(discount_rate, discounted_a)
    fixed_b = get_price(discount_rate, discounted_b)
    
    print(f"A 상품의 정가는 {int(fixed_a)} 원")
    print(f"B 상품의 정가는 {int(fixed_b)} 원")

if __name__ == "__main__":
    main()
