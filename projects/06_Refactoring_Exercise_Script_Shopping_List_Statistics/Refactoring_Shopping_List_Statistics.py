from typing import TypedDict


class Item(TypedDict):
    """商品信息。"""
    name: str
    quantity: int
    price: float


class Summary(TypedDict):
    """购物汇总信息。"""
    total_count: int
    final_price: float
    most_expensive_item: Item


def parse_item(line: str) -> Item:
    """将一条商品字符串解析为商品字典。"""
    parts = line.split(",")
    item: Item = {
        "name": parts[0],
        "quantity": int(parts[1]),
        "price": float(parts[2]),
    }
    return item


def parse_items(items: list[str]) -> list[Item]:
    """将商品字符串列表解析为商品字典列表。"""
    parsed_items: list[Item] = []
    for item in items:
        parsed_item = parse_item(item)
        parsed_items.append(parsed_item)
    return parsed_items


def calculate_total_count(items: list[Item]) -> int:
    """统计商品总数量。"""
    total_count = 0
    for item in items:
        total_count = total_count + item["quantity"]
    return total_count


def calculate_total_price(items: list[Item]) -> float:
    """统计商品原始总价。"""
    total_price = 0.0
    for item in items:
        total_price = total_price + item["quantity"] * item["price"]
    return total_price


def calculate_most_expensive_item(items: list[Item]) -> Item:
    """返回单价最高的商品。"""
    if not items:
        raise ValueError("items 不能为空")

    most_expensive_item = items[0]
    for item in items:
        if item["price"] > most_expensive_item["price"]:
            most_expensive_item = item
    return most_expensive_item


def get_member_input() -> str:
    """获取会员输入，只接受 y 或 n。"""
    while True:
        member = input("是否是会员？(y/n): ").lower().strip()
        if member in ("y", "n"):
            return member
        print("输入错误，请输入 y 或 n")


def apply_member_discount(total_price: float, member: str) -> float:
    """对会员订单应用折扣。满 50 且为会员时打 9 折。"""
    if member == "y" and total_price >= 50:
        total_price = total_price * 0.9
    return total_price


def get_coupon_input() -> float:
    """获取优惠券金额。"""
    while True:
        try:
            return float(input("请输入优惠券金额: "))
        except ValueError:
            print("输入错误，请输入数字")


def apply_coupon_discount(total_price: float, coupon: float) -> float:
    """应用优惠券金额，并保证最终价格不小于 0。"""
    total_price = total_price - coupon
    if total_price < 0:
        total_price = 0
    return total_price


def build_summary(items: list[Item], member: str, coupon: float) -> Summary:
    """构建购物汇总信息。"""
    original_total_price = calculate_total_price(items)
    discounted_price = apply_member_discount(original_total_price, member)
    final_price = apply_coupon_discount(discounted_price, coupon)

    return {
        "total_count": calculate_total_count(items),
        "final_price": final_price,
        "most_expensive_item": calculate_most_expensive_item(items),
    }


def print_receipt(items: list[Item], summary: Summary) -> None:
    """打印购物小票。"""
    print("------ 购物小票 ------")
    for item in items:
        subtotal = item["quantity"] * item["price"]
        print(
            item["name"],
            "x",
            item["quantity"],
            "单价",
            item["price"],
            "小计",
            subtotal,
        )

    print("商品总件数:", summary["total_count"])
    print(
        "最贵商品:",
        summary["most_expensive_item"]["name"],
        "单价:",
        summary["most_expensive_item"]["price"],
    )
    print("最终总价:", round(summary["final_price"], 2))


def main() -> None:
    """程序入口。"""
    items = [
        "apple,3,5.5",
        "banana,2,3.0",
        "milk,1,12.8",
        "bread,2,6.5",
    ]

    member = get_member_input()
    coupon = get_coupon_input()

    parsed_items = parse_items(items)
    summary = build_summary(parsed_items, member, coupon)
    print_receipt(parsed_items, summary)


if __name__ == "__main__":
    main()