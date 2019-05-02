class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        pass

    def double_num(self, card_num):
        return list(x * 2 - 9 if (x * 2) > 9 else x * 2 for x in card_num[len(card_num)-2::-2])


    def sum_num(self, card_num):
        return sum(card_num[::-2]) + sum(self.double_num(card_num))


    def is_valid(self):

        arr = list(int(x) for x in self.card_num if x.isdigit())

        return self.card_num.isdigit() and self.card_num != "0" and self.sum_num(arr) % 10 == 0
