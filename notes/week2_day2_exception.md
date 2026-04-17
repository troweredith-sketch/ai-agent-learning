# Week 2 Day 2 - 异常处理、try/except、自定义错误提示

## 今天的学习目标

今天的目标不是“把报错消灭掉”，而是学会：

- 看懂 Python 报错在说什么
- 用 `try/except` 处理预期内的错误
- 给用户更清楚的错误提示
- 分清楚什么情况应该 `raise`，什么情况应该 `except`

---

## 一、什么是异常

异常（exception）就是：程序运行过程中出现了问题，Python 用一种标准方式通知我们。

例如：

- 输入了不能转换成数字的内容
- 除数写成了 `0`
- 访问了不存在的文件
- 调用了不合法的数据

如果不处理，程序通常会直接中断，并显示 traceback。

例如：

```python
age = int("abc")
```

这时会报：

```python
ValueError
```

意思是：`int()` 想把字符串变成整数，但 `"abc"` 不是合法整数。

---

## 二、为什么要做异常处理

异常处理的核心目的不是“隐藏错误”，而是：

- 让程序更稳
- 给用户更友好的提示
- 在能恢复的时候恢复
- 在不能恢复的时候明确停止

比如命令行程序里，如果用户把年龄输入成 `"hello"`，直接让程序崩掉体验很差。  
更好的做法是告诉用户：

```text
年龄必须是整数，例如 18
```

然后让用户重新输入。

---

## 三、`try/except` 基础

最基本的写法：

```python
try:
    age = int(input("请输入年龄: "))
except ValueError:
    print("年龄必须是整数。")
```

含义是：

- `try` 里放“可能出错”的代码
- 如果真的发生了指定错误，就进入 `except`

### 运行流程

1. 先执行 `try`
2. 如果没报错，`except` 不执行
3. 如果发生匹配的异常，就跳到 `except`

### 推荐原则

- 只把“可能出错”的那几行放进 `try`
- `except` 尽量写具体异常类型，不要一上来就写 `except Exception`

不推荐：

```python
try:
    name = input("姓名: ")
    age = int(input("年龄: "))
    score = float(input("成绩: "))
    print(name, age, score)
except Exception:
    print("出错了")
```

因为这样范围太大，不容易判断到底哪里错了。

更推荐：

```python
raw_age = input("年龄: ")

try:
    age = int(raw_age)
except ValueError:
    print("年龄必须是整数。")
```

---

## 四、常见异常类型

现阶段先认识这些最常见的：

- `ValueError`
  数值类型对了，但值不合法  
  例如：`int("abc")`

- `TypeError`
  对象类型不对  
  例如：`"18" + 2`

- `ZeroDivisionError`
  除数为 0  
  例如：`10 / 0`

- `FileNotFoundError`
  文件不存在

- `KeyError`
  字典里没有这个 key

- `IndexError`
  列表下标越界

- `EOFError`
  `input()` 读取输入时，输入流提前结束

---

## 五、自定义错误提示

有两种常见做法。

### 1. 捕获内置异常后，打印更友好的提示

```python
try:
    age = int(input("请输入年龄: "))
except ValueError:
    print("年龄输入错误，请输入整数，例如 18。")
```

这适合简单场景。

### 2. 主动抛出业务错误

当“语法上没错，但业务规则不允许”时，可以主动 `raise`。

例如：

```python
age = 200

if age > 120:
    raise ValueError("年龄不合理，请输入 1 到 120 之间的整数。")
```

这里 `200` 确实是整数，`int()` 不会报错。  
但从业务规则看，它不合理，所以我们自己抛出错误。

---

## 六、自定义异常类

当你想把“用户输入错误”和“程序内部错误”区分开时，可以定义自己的异常类。

例如：

```python
class UserInputError(ValueError):
    """用户输入不符合要求时抛出的异常。"""
```

然后：

```python
def parse_score(raw: str) -> float:
    score = float(raw)
    if not 0 <= score <= 100:
        raise UserInputError("成绩必须在 0 到 100 之间。")
    return score
```

这样做的好处是：

- 错误含义更清楚
- 代码职责更清晰
- `except` 时可以只捕获你关心的那一类错误

---

## 七、什么错误该抛出，什么错误该捕获

这是今天最重要的一部分。

### 应该抛出（`raise`）的情况

当一个函数发现：

- 输入数据不合法
- 当前条件不满足，无法继续处理
- 这层代码不知道怎么恢复

就应该抛出异常，让上层决定怎么处理。

例如：

```python
def parse_age(raw: str) -> int:
    if not raw.strip():
        raise ValueError("年龄不能为空。")
    return int(raw)
```

这个函数的职责是“校验并解析年龄”。  
如果输入不对，它最合理的动作就是抛出异常。

### 应该捕获（`except`）的情况

当你所在的位置：

- 知道怎么给用户提示
- 知道怎么重试
- 知道怎么降级处理

就应该捕获异常。

例如命令行输入循环：

```python
while True:
    try:
        age = parse_age(input("请输入年龄: "))
        break
    except ValueError as exc:
        print(f"输入错误: {exc}")
```

这里最适合捕获，因为它知道下一步该做什么：  
提示用户，然后重新输入。

### 不要乱捕获的情况

像下面这种写法要非常小心：

```python
except Exception:
    print("出错了")
```

问题是它会把很多不该吞掉的错误也一起吞掉，例如：

- 代码写错变量名
- 函数调用参数写错
- 逻辑 bug

结果就是：程序表面上“没崩”，但真正的问题被藏起来了。

一句话记忆：

- 能处理、能恢复，就捕获
- 不能处理、不能恢复，就抛出

---

## 八、`else` 和 `finally`

今天先认识，不要求大量使用。

```python
try:
    number = int(input("请输入数字: "))
except ValueError:
    print("请输入合法整数。")
else:
    print("转换成功。")
finally:
    print("本次输入结束。")
```

含义：

- `else`：只有没报错时才执行
- `finally`：不管有没有报错都会执行

常见用途：

- `else`：放成功后的逻辑
- `finally`：做清理工作，比如关闭文件、释放资源

---

## 九、今天的小脚本设计思路

今天配套脚本位置：

`projects/07_Exception_Handling_CLI/exception_cli.py`

这个脚本练了 4 件事：

- 用 `try/except` 处理输入错误
- 用自定义异常 `UserInputError`
- 对空输入、非数字输入、范围错误做健壮处理
- 区分“验证函数负责抛出错误”和“输入循环负责捕获错误”

你可以故意输入这些错误场景来练习：

- 姓名直接回车
- 年龄输入 `abc`
- 成绩输入 `200`
- 除数输入 `0`
- 除数输入 `hello`
- 在终端里按 `Ctrl + D`，观察 `EOFError` 的退出处理

---

## 十、今天应该重点理解的代码结构

### 1. 验证函数负责 `raise`

例如：

```python
def parse_score(raw: str) -> float:
    try:
        score = float(raw)
    except ValueError:
        raise UserInputError("成绩必须是数字，例如 89.5。")

    if not 0 <= score <= 100:
        raise UserInputError("成绩必须在 0 到 100 之间。")

    return score
```

这个函数不负责“安慰用户”，它只负责：

- 转换数据
- 发现问题
- 抛出明确错误

### 2. 输入循环负责 `except`

```python
while True:
    try:
        score = parse_score(input("请输入成绩: "))
        break
    except UserInputError as exc:
        print(f"[输入错误] {exc}")
```

这里才是最适合处理用户交互的地方。

---

## 十一、运行方式

在仓库根目录执行：

```bash
python3 projects/07_Exception_Handling_CLI/exception_cli.py
```

---

## 十二、今天复盘时你可以回答这几个问题

1. `try` 里应该放哪些代码，为什么不能放太多？
2. `ValueError` 和“业务规则不合法”有什么区别？
3. 为什么验证函数更适合 `raise`，而输入循环更适合 `except`？
4. 为什么不推荐随手写 `except Exception`？
5. 什么叫“能恢复就捕获，不能恢复就抛出”？

---

## 十三、今天的结论

今天你真正要掌握的不是语法本身，而是这套分工：

- 底层函数负责发现问题并抛出异常
- 上层交互负责捕获异常并给出友好提示
- 不要为了“不报错”而乱捕获

如果你把这套思路建立起来，后面做文件处理、接口调用、数据校验时都会轻松很多。

---

## 十四、当天产出回看

今天的代码产出文件：

`projects/07_Exception_Handling_CLI/exception_cli.py`

这个脚本现在是一个完整可运行的异常处理练习脚本，重点包含：

- `parse_name()`：处理姓名为空、长度过短
- `parse_age()`：处理空输入、非整数、范围不合理
- `parse_score()`：处理空输入、非数字、成绩超范围
- `parse_divisor()`：处理空输入、非数字、除数为 `0`
- `prompt_until_valid()`：统一负责捕获 `UserInputError` 并提示用户重试
- 程序入口：负责处理 `EOFError` 和 `KeyboardInterrupt`

### 建议你回看这 3 个位置

1. 解析函数里是怎么 `raise UserInputError(...)` 的
2. 输入循环里为什么只捕获 `UserInputError`
3. 为什么程序入口单独处理 `Ctrl + C` 和 `Ctrl + D`

### 运行方式

```bash
python3 projects/07_Exception_Handling_CLI/exception_cli.py
```

### 继续加练可以做什么

如果你想继续练手，可以自己再加这几种规则：

- 成绩最多保留 1 位小数
- 姓名不能包含数字
- 年龄只能在 `1 ~ 120` 之间
- 给 `try/except/else/finally` 各写一个最小示例
