class Check:
    def __init__(self, name, price, quantity, is_member, coupon_code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_member = is_member
        self.coupon_code = coupon_code
    
    def base_price(self):
        return self.price * self.quantity
    
    def discount(self):
        if self.coupon_code in allowed_coupons and self.base_price() > 300:
            return 1.2
        elif self.is_member == True:
            return 1.05
        else:
            return 1

    def promotion(self):
        if "a" in self.name:
            return "(Promotion)"

    def amount_discount(self):
        return int((self.base_price() * self.discount() - self.base_price()) * 100) / 100
    
    def price_after_discount(self):
        return self.base_price() - self.amount_discount()
    
    def tax_total(self):
        return int((self.price_after_discount() * 1.08 - self.price_after_discount()) * 100) / 100
    
    def end_price(self):
        return self.base_price() - self.amount_discount() + self.tax_total()
    
    def bonus_points(self):
        return (self.quantity ** 2) + (int(self.end_price() * 1.80 - self.end_price()))

allowed_coupons = ["SALE10", "NEWYEAR", "VIP"]
check1 = Check("Laptop", 999.90, 2, True, "SALE10")

print(
    f"=== STORE RECEIPT === \
    \nProduct: {check1.name} {check1.promotion()} \
    \nPrice per piece: {str(check1.price) + "$"} \
    \nQuantity: {check1.quantity} \
    \n---------- \
    \nPrice before discount: {str(check1.base_price()) + "$"} \
    \nDiscount: {str(check1.amount_discount()) + "$" } \
    \nPrice after discount: {str(check1.price_after_discount()) + "$"} \
    \nTax (8%): {str(check1.tax_total()) + "$"} \
    \n---------- \
    \nTotal payable: {str(check1.end_price()) + "$"} \
    \n---------- \
    \nPoints awarded: {check1.bonus_points()} (including volume bonus) \
    \nAmount data type: {type(check1.end_price())}")