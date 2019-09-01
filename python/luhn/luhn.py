from re import search


class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = ''.join(self.card_num.split())  # remove all whitespaces

        if len(card_num) <= 1:
            #raise ValueError("card_num should have non-zero length")
            return False
        if search(r'[^0-9]', card_num):
            #raise ValueError('non-integer non-whitespace characters found in card_num')
            return False

        is_even_len = len(card_num) % 2 == 0
        sum = 0
        for i in range(len(card_num)):
            num = int(card_num[i])
            if i % 2 == 0 and is_even_len \
              or i % 2 != 0 and not is_even_len:
                sum += num * 2
                if num * 2 > 9:
                    sum -= 9
            else:
                sum += num
        return sum % 10 == 0
