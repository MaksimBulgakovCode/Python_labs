product_name = "Laptop"
price = 999.90
quantity = 2
is_member = True
coupon_code = "SALE10"

cart = {"name": product_name, "price": price, "quantity": quantity}
allowed_coupons = ["SALE10", "NEWYEAR", "VIP"]

base_price = cart["price"] * cart["quantity"]

def discount():
    if coupon_code in allowed_coupons and base_price > 300:
        return 1.2
    elif is_member == True:
        return 1.05
    else:
        return 1

def promotion():
    if "a" in cart["name"]:
        return "(Promotion)"
    else:
        return ""

amount_discount = int((base_price * discount() - base_price) * 100) / 100
price_after_discount = base_price - amount_discount
tax = int((price_after_discount * 1.08 - price_after_discount) * 100) / 100

end_price = base_price - amount_discount + tax

bonus_points = int((end_price * 1.80 - end_price))
bonus_points = cart["quantity"] ** 2 + bonus_points

print(
    f"=== STORE RECEIPT === \
    \nProduct: {cart['name']} {promotion()} \
    \nPrice per piece: {str(cart['price']) + "$"} \
    \nQuantity: {cart['quantity']} \
    \n---------- \
    \nPrice before discount: {str(base_price) + "$"} \
    \nDiscount: {str((amount_discount) ) + "$" } \
    \nPrice after discount: {str(price_after_discount ) + "$"} \
    \nTax (8%): {str(tax) + "$"} \
    \n---------- \
    \nTotal payable: {str(end_price) + "$"} \
    \n---------- \
    \nPoints awarded: {bonus_points} (including volume bonus) \
    \nAmount data type: {type(end_price)}") 
