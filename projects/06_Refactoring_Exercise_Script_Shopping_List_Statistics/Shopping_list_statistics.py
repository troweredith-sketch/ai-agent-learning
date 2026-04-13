items = [
    "apple,3,5.5",
    "banana,2,3.0",
    "milk,1,12.8",
    "bread,2,6.5"
]

member = input("是否是会员？(y/n): ")
coupon_text = input("请输入优惠券金额: ")

coupon = float(coupon_text)

total = 0
count = 0
most_expensive_name = ""
most_expensive_price = 0

for item in items:
    parts = item.split(",")
    name = parts[0]
    quantity = int(parts[1])
    price = float(parts[2])

    subtotal = quantity * price
    total = total + subtotal
    count = count + quantity

    if price > most_expensive_price:
        most_expensive_price = price
        most_expensive_name = name

print("------ 购物小票 ------")
for item in items:
    parts = item.split(",")
    name = parts[0]
    quantity = int(parts[1])
    price = float(parts[2])
    print(name, "x", quantity, "单价", price, "小计", quantity * price)

if member == "y":
    if total >= 50:
        total = total * 0.9

total = total - coupon

if total < 0:
    total = 0

print("商品总件数:", count)
print("最贵商品:", most_expensive_name, "单价:", most_expensive_price)
print("最终总价:", round(total, 2))