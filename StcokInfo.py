class StockInfo:
    def __init__(self, code_name, price, amount):
        self.code_name = code_name
        self.amount = amount
        self.price = price
        self.total = float(self.price) * int(self.amount)

    def debug_print(self):
        print("code name=>", self.code_name, "amount=>", self.amount,
              "price", self.price, "total", self.total)

    def transfer_to_list(self):
        single_stock = [self.code_name, self.amount, self.price, self.total]
        return single_stock
