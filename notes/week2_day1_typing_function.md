# Week 2 Day 1 - 函数设计、类型标注、docstring 基础

## 今天的学习目标

从“会写能运行的 Python 脚本”，进步到“会写更清晰、更像工程代码的小程序”。

今天重点学习了：

- 函数设计
- 参数和返回值
- 类型标注
- docstring 基础写法

---

## 一、函数设计

### 1. 什么是函数设计

函数设计不只是会写 `def`，更重要的是：

- 能把一段逻辑拆成多个职责清晰的函数
- 让每个函数都只做一件事
- 让代码更容易读、改、复用和测试

### 2. 好函数的特点

#### 职责单一
一个函数最好只做一件事。

例如：

- `parse_item()`：解析商品数据
- `calculate_total_price()`：计算总价
- `print_receipt()`：打印小票

#### 输入、处理、输出分开
写代码时尽量区分：

- 输入：`input()`
- 处理：计算、判断、转换
- 输出：`print()`

更推荐：

- 外层获取输入
- 中间函数负责处理
- 最外层负责输出

#### 参数清楚
函数要通过参数接收输入，不要把数据写死在函数内部。

#### 返回值明确
函数优先用 `return` 返回结果，而不是直接 `print()`。

因为返回值更容易复用和测试。

#### 函数名要能表达意图
好的函数名应该让人一眼看懂用途，例如：

- `calculate_total_price`
- `apply_coupon_discount`
- `find_most_expensive_item`

### 3. 常见问题

#### 一个函数干太多事
比如一个函数同时负责：

- 获取输入
- 处理数据
- 判断条件
- 打印结果

这种函数通常应该拆开。

#### 只打印，不返回
`print()` 是显示结果，`return` 才是把结果交给其他代码继续使用。

---

## 二、参数和返回值

写函数时先想两个问题：

1. 这个函数需要什么输入？
2. 这个函数应该返回什么结果？

例如：

```python
def add(a: int, b: int) -> int:
    return a + b
```

这里很清楚：

- 参数：`a`、`b`
- 返回值：`int`

### 建议

- 处理逻辑尽量用参数传入数据
- 处理结果尽量用 `return` 返回
- `print()` 尽量放在最外层

---

## 三、类型标注

### 1. 类型标注的作用

类型标注可以让代码更清楚，帮助我们理解：

- 函数接收什么类型的数据
- 函数返回什么类型的结果

例如：

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### 2. 常见基础类型

- `str`
- `int`
- `float`
- `bool`
- `list[str]`
- `list[int]`
- `dict[str, int]`
- `None`

例如：

```python
def show_message(message: str) -> None:
    print(message)
```

这里 `-> None` 表示函数没有返回值。

### 3. 类型标注的重点位置

现阶段最重要的是先给下面这些地方加类型标注：

- 函数参数
- 函数返回值

例如：

```python
def calculate_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)
```

### 4. 类型标注不要写得太宽泛

不推荐只写：

```python
def parse_items(items: list) -> list:
    ...
```

因为这样信息太少。

更好的是写得具体一点，例如：

```python
def parse_items(items: list[str]) -> list[Item]:
    ...
```

这样更容易理解。

### 5. `TypedDict` 的基本认识

当字典结构固定时，可以用 `TypedDict` 让类型更清楚。

例如：

```python
from typing import TypedDict


class Item(TypedDict):
    name: str
    quantity: int
    price: float
```

这样就比直接写 `dict` 更明确。

---

## 四、docstring

### 1. docstring 是什么

docstring 是写在函数、类、模块里的说明文字。

最简单的写法：

```python
def is_adult(age: int) -> bool:
    """判断年龄是否大于等于 18。"""
    return age >= 18
```

### 2. docstring 的作用

- 说明函数是干什么的
- 帮助别人快速理解代码
- 帮助未来的自己回头看代码
- 补充类型标注表达不了的业务含义

### 3. 基础写法

#### 单行 docstring

适合简单函数：

```python
def calculate_total_count(items: list[Item]) -> int:
    """统计商品总数量。"""
```

#### 多行 docstring

适合复杂函数：

```python
def divide(a: float, b: float) -> float:
    """
    计算两个数相除的结果。

    Args:
        a: 被除数
        b: 除数

    Returns:
        相除后的结果
    """
```

### 4. 合格的 docstring

至少要说明：

- 这个函数做什么
- 必要时说明参数含义
- 必要时说明返回值或异常

### 5. 不好的 docstring

这种没有信息量：

```python
def add(a: int, b: int) -> int:
    """这是一个函数。"""
```

更好的写法：

```python
def add(a: int, b: int) -> int:
    """返回两个整数之和。"""
```

---

## 五、这三者之间的关系

这三者可以这样理解：

### 函数设计

决定代码怎么拆、每个函数做什么。

### 类型标注

说明函数接收什么、返回什么。

### docstring

解释函数为什么存在、具体做什么。

三者结合起来，代码就会更像工程代码。

---

## 六、购物小票重构练习总结

这次练习是把一个原始脚本重构成多个函数。

### 原始脚本的问题

- 没有函数
- 商品解析重复写了两次
- 输入、处理、输出混在一起
- 折扣逻辑直接写死在主流程里
- 没有类型标注
- 没有 docstring

### 重构后的改进方向

把逻辑拆成多个函数，例如：

- `parse_item()`：解析一条商品数据
- `parse_items()`：解析商品列表
- `calculate_total_count()`：统计总件数
- `calculate_total_price()`：统计总价
- `calculate_most_expensive_item()`：找最贵商品
- `apply_member_discount()`：应用会员折扣
- `apply_coupon_discount()`：应用优惠券
- `build_summary()`：组装汇总信息
- `print_receipt()`：打印小票
- `main()`：主程序入口

### 这次重构中发现的问题

#### 1. 类型标注太宽泛

比如直接写 `dict`、`list`，信息不够清楚。

#### 2. `main()` 里有重复计算

前面算了一遍，后面 `build_summary()` 又算了一遍。

#### 3. 缺少 docstring

虽然函数拆出来了，但还缺说明。

#### 4. 对空列表不安全

比如：

```python
most_expensive_item = items[0]
```

如果列表为空会报错，应该先判断：

```python
if not items:
    raise ValueError("items 不能为空")
```

#### 5. 字段命名要准确

例如汇总里的价格字段，写成 `final_price` 比 `total_price` 更准确，因为它表示折扣后的最终价格。

---

## 七、这次修改后的主要收获

### 1. 主流程应该尽量简洁

理想的 `main()` 应该像这样：

```python
def main() -> None:
    items = [...]
    member = get_member_input()
    coupon = get_coupon_input()
    parsed_items = parse_items(items)
    summary = build_summary(parsed_items, member, coupon)
    print_receipt(parsed_items, summary)
```

这样主流程一眼就能看懂。

### 2. 数据结构清楚后，代码会更容易维护

使用 `TypedDict` 后，商品和汇总信息更明确：

- `Item`
- `Summary`

### 3. docstring 能提升可读性

给核心函数补 docstring 后，代码更容易理解。

---

## 八、今天学到的工程化思维

### 1. 不要只追求“代码能跑”

还要考虑：

- 清不清楚
- 好不好改
- 能不能复用
- 别人能不能看懂

### 2. 函数应该回答明确的问题

比如：

- 总件数是多少？
- 原始总价是多少？
- 最贵商品是谁？
- 折扣后价格是多少？

### 3. 先想职责，再写代码

写函数前先问：

- 这个函数负责什么？
- 它需要什么输入？
- 它应该返回什么结果？

---

## 九、我现在应该做到的最低标准

对于一个小脚本，至少要做到：

- 拆成多个函数
- 每个函数职责尽量单一
- 给函数加参数和返回值类型标注
- 给核心函数加 docstring
- 用 `main()` 管理主流程

---

## 十、今天的复盘

### 今天做了什么

- 学了函数设计、参数和返回值、类型标注、docstring
- 把购物小票脚本重构成多个函数
- 给代码补了更清晰的类型标注
- 学会了 `TypedDict` 的基本用途
- 学会了让 `main()` 更简洁

### 今天的收获

- 明白了“输入、处理、输出分开”的重要性
- 明白了 `return` 比直接 `print()` 更适合复用
- 明白了类型标注不仅是语法，更是“说明书”
- 明白了 docstring 是帮助理解函数的重要工具

### 今天还需要继续练习的地方

- 类型标注写得更具体
- 养成写 docstring 的习惯
- 避免重复计算
- 提前考虑边界情况，比如空列表

---

## 十一、下一步建议

接下来可以继续练习：

1. 再找一个旧脚本重构
2. 每个函数先写输入和返回值
3. 给核心函数补 docstring
4. 尝试继续优化数据结构
5. 开始练习异常处理和 logging

---

## 十二、一句话总结

今天最重要的不是学会几个语法点，而是开始形成一种写代码的习惯：

**先想职责，再设计函数；写清输入输出；补上类型标注；最后用 docstring 说明用途。**