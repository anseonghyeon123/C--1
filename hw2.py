def get_integer(prompt):
    return int(input(prompt))


def exchange(money):
    coins = [500, 100, 50, 10]
    counts = []
    
    for coin in coins:
        count = money // coin
        counts.append(count)
        money -= count * coin
    
    print(f"500원 동전의 개수: {counts[0]}")
    print(f"100원 동전의 개수: {counts[1]}")
    print(f"50원 동전의 개수: {counts[2]}")
    print(f"10원 동전의 개수: {counts[3]}")

money = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(money)
