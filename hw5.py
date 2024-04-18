def read_single_digit(digit):
    korean_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return korean_digits[digit]

def read_number(number):
   
    if number < 10:
        return read_single_digit(number)
    elif number < 100:
        tens, ones = divmod(number, 10)
        return read_single_digit(tens) + " " + read_single_digit(ones)
    else:
        hundreds, remainder = divmod(number, 100)
        tens, ones = divmod(remainder, 10)
        return (read_single_digit(hundreds) + " " +
                read_single_digit(tens) + " " +
                read_single_digit(ones))


number = int(input("세 자리 정수 입력: "))
print(read_number(number))
