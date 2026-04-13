# 解析一条商品字符串
def parse_item(line: str) -> dict:
    parts = line.split(",")
    item = {
        "name": parts[0],
        "quantity": int(parts[1]),
        "price": float(parts[2])
    }
    return item

# 解析整个商品列表
def parse_items(items: list) -> list:
    parsed_items = []
    for item in items:
        parsed_item = parse_item(item)
        parsed_items.append(parsed_item)

    return parsed_items

# 统计总数量
def calculate_total_count(items: list) -> int:
    total_count = 0
    for item in items:
        total_count = total_count + item["quantity"]

    return total_count

# 统计总价
def calculate_total_price(items: list) -> float:
    total_price = 0
    for item in items:
        total_price = total_price + item["quantity"] * item["price"]

    return total_price

# 统计最贵商品
def calculate_most_expensive_item(items: list) -> dict:
    most_expensive_item = items[0]
    for item in items:
        if item["price"] > most_expensive_item["price"]:
            most_expensive_item = item

    return most_expensive_item

# 是否会员
def get_member_input() -> str:
    while True:
        member = input("是否是会员？(y/n): ").lower().strip()
        if member in ("y", "n"):
            return member
        print("输入错误，请输入 y 或 n ")

# 会员优惠
def apply_member_discount(total_price: float, member: str) -> float:
    if member == "y":
        if total_price >= 50:
            total_price = total_price * 0.9

    return total_price

# 优惠券金额
def get_coupon_input() -> float:
    while True:
        try:
            return float(input("请输入优惠券金额: "))
        except ValueError:
            print("输入错误，请输入数字")


# 优惠券优惠
def apply_coupon_discount(total_price: float, coupon: float) -> float:
    total_price = total_price - coupon
    if total_price < 0:
        total_price = 0

    return total_price

# 把参数打包成字典
def build_summary(items: list, member: str, coupon: float) -> dict:
    return {
        "total_count": calculate_total_count(items),
        "total_price": apply_coupon_discount(
            apply_member_discount(calculate_total_price(items), member), coupon
        ),
        "most_expensive_item": calculate_most_expensive_item(items),
    }


# 打印小票
def print_receipt(items: list, summary: dict):
    print("------ 购物小票 ------")
    for item in items:
        print(item["name"], "x", item["quantity"], "单价", item["price"], "小计", item["quantity"] * item["price"])
    print("商品总件数:", summary["total_count"])
    print("最贵商品:", summary["most_expensive_item"]["name"], "单价:", summary["most_expensive_item"]["price"])
    print("最终总价:", round(summary["total_price"], 2))

# 主程序
def main() -> None:
    items = [
        "apple,3,5.5",
        "banana,2,3.0",
        "milk,1,12.8",
        "bread,2,6.5"
    ]

    member = get_member_input()
    

    coupon = get_coupon_input()


    parsed_items = parse_items(items)

    total_count = calculate_total_count(parsed_items)
    total_price = calculate_total_price(parsed_items)
    most_expensive_item = calculate_most_expensive_item(parsed_items)

    total_price = apply_member_discount(total_price, member)
    total_price = apply_coupon_discount(total_price, coupon)

    print_receipt(parsed_items, build_summary(parsed_items, member, coupon))


if __name__ == "__main__":
    main()