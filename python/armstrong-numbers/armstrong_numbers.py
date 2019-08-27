def is_armstrong(number):
    if number != int(number):
        raise Exception("Please enter a valid integer")
    digits = []
    _number = number
    while _number > 0:
        digits.append(_number % 10)
        _number = _number // 10
    total = 0
    print(digits)
    for num in digits:
        total += num ** len(digits)
    if total == number:
        return True
    else:
        return False
