import time


class StockInfo:
    def __init__(self, code_name, price, amount, flag):
        self.datetime = time.strftime("%Y%m%d %H:%M", time.localtime())
        self.code_name = code_name
        self.amount = amount
        self.price = price
        self.total = float(self.price) * int(self.amount)
        if flag == '0':
            self.total = -(self.total + self.total*0.0008 + self.total * 0.00002)

        elif flag == '1':
            self.total = self.total - self.total*0.0008 - self.total * 0.00002 - self.total * 0.001
        else:
            print("error")
        self.total = round(self.total, 2)

    def debug_print(self):
        print("code name=>", self.code_name, "amount=>", self.amount,
              "price", self.price, "total", self.total)

    def transfer_to_list(self):
        single_stock = [self.datetime, self.code_name, self.amount, self.price, self.total]
        return single_stock
