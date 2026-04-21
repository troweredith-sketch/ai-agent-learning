# Week 2 Day 3 - logging 基础、日志级别、日志输出到文件

## 今天的学习目标

今天先不追求“像工程项目那样完整使用 logging”，而是先把最基础的东西学明白：

- 什么是 `logging`
- 为什么不要只用 `print()`
- `info` / `warning` / `error` 的区别
- 如何把日志输出到控制台
- 如何把日志写入文件
- 如何让日志同时输出到屏幕和文件
- 如何在一个最简单的小程序里使用日志

---

## 一、什么是 logging

`logging` 是 Python 自带的日志模块。

它的作用可以简单理解成：

- `print()` 更偏“给用户看”
- `logging` 更偏“记录程序运行过程”

例如：

- 程序开始运行了
- 用户输入错了
- 某一步失败了
- 程序正常结束了

这些内容都很适合用 `logging` 来记录。

---

## 二、为什么不要只用 `print()`

`print()` 当然能输出内容，但它有几个问题。

### 1. `print()` 没有级别

下面两句看起来差不多：

```python
print("程序启动成功")
print("保存文件失败")
```

但它们的重要程度完全不同。

`logging` 可以把它们区分开：

- `info`：正常信息
- `warning`：有问题，但还能继续
- `error`：真的发生失败

### 2. `print()` 不方便写入文件

如果程序出问题了，只看终端里的 `print()` 不方便回头排查。  
日志写进文件后，可以之后再打开看。

### 3. `print()` 不适合记录程序过程

比如下面这些更像“程序内部记录”：

- 程序什么时候启动
- 用户输入为什么失败
- 文件保存有没有成功

这类信息更适合用日志。

---

## 三、`info` / `warning` / `error` 是什么

这是今天最核心的内容。

### `logging.info()`

表示：普通信息，程序正在正常运行。

例如：

```python
logging.info("程序开始运行。")
```

适合记录：

- 程序开始
- 程序结束
- 某一步执行成功

### `logging.warning()`

表示：有问题，但程序还能继续。

例如：

```python
logging.warning("用户输入为空。")
```

适合记录：

- 用户输入不合法
- 某个值不太对
- 程序用了默认值继续运行

### `logging.error()`

表示：真的出错了。

例如：

```python
logging.error("保存文件失败。")
```

适合记录：

- 文件写入失败
- 程序运行中出现严重问题
- 捕获到异常

### 一个最简单的判断方法

- 正常记录：`info`
- 有问题但还能继续：`warning`
- 已经失败了：`error`

---

## 四、最简单的控制台日志

今天先学最简单的写法，不引入太多新概念。

示例文件：`projects/08_Logging_Practice_CLI/logging_basic_simple.py`

代码：

```python
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)

print("这是 print 输出，主要是给用户看的。")

logging.info("程序开始运行。")
logging.warning("这是一个 warning 示例。")
logging.error("这是一个 error 示例。")

print("程序结束。")
```

### 这段代码里最重要的是哪几行

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)
```

含义：

- `level=logging.INFO`
  表示显示 `INFO` 及以上级别
- `format="%(levelname)s: %(message)s"`
  表示日志显示成“级别: 内容”
- `stream=sys.stdout`
  表示把日志输出到屏幕

### 运行效果

```text
这是 print 输出，主要是给用户看的。
INFO: 程序开始运行。
WARNING: 这是一个 warning 示例。
ERROR: 这是一个 error 示例。
程序结束。
```

---

## 五、把日志写入文件

示例文件：`projects/08_Logging_Practice_CLI/logging_to_file_simple.py`

代码：

```python
import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    filename=str(LOG_FILE),
    filemode="a",
    encoding="utf-8",
)

print("程序开始运行。")

logging.info("这是一条 info 日志。")
logging.warning("这是一条 warning 日志。")
logging.error("这是一条 error 日志。")

print(f"日志已经写入 {LOG_FILE}")
```

### 新增的 3 个关键参数

- `filename=str(LOG_FILE)`
  表示把日志写入脚本所在目录里的 `app.log`
- `filemode="a"`
  表示追加写入，不覆盖旧内容
- `encoding="utf-8"`
  表示支持中文，避免乱码

这里多加了两行：

```python
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"
```

作用是：

- 先拿到当前脚本所在目录
- 再把日志固定写到这个目录里

这样即使你在仓库根目录运行脚本，也不会把日志误写到别的地方。

### 文件里会看到什么

运行后，当前目录会生成 `app.log`，内容类似这样：

```text
INFO: 这是一条 info 日志。
WARNING: 这是一条 warning 日志。
ERROR: 这是一条 error 日志。
```

---

## 六、同时输出到屏幕和文件

示例文件：`projects/08_Logging_Practice_CLI/logging_console_and_file_simple.py`

代码：

```python
import logging
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app_both.log"


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)

print("程序开始运行。")

logging.info("这是一条 info 日志。")
logging.warning("这是一条 warning 日志。")
logging.error("这是一条 error 日志。")

print(f"日志已经同时输出到屏幕和 {LOG_FILE}")
```

### 这里最重要的新东西是 `handlers`

`handlers` 可以理解成：

“一条日志要发到哪些地方”

上面代码里有两个地方：

- `logging.StreamHandler(sys.stdout)`
  发到屏幕
- `logging.FileHandler("app_both.log", encoding="utf-8")`
  写到文件

所以一句话总结就是：

同一条日志，复制两份：

- 一份显示在屏幕上
- 一份写进文件里

---

## 七、在程序里怎么使用日志

你现在先记住一个非常重要的原则：

- `print()` 主要给用户看
- `logging` 主要给程序运行记录看

### 哪些内容适合继续用 `print()`

- 输入提示
- 菜单
- 最终结果展示
- 直接告诉用户的内容

例如：

```python
print("请输入年龄: ")
print("保存成功")
```

### 哪些内容适合用 `logging`

- 程序开始运行
- 程序结束
- 用户输入不合法
- 捕获到异常
- 文件保存失败

例如：

```python
logging.info("程序启动")
logging.warning("用户输入的年龄不是整数")
logging.error("保存文件失败")
```

---

## 八、一个最简单的小程序里怎么放日志

下面是一个最基础的用法：

```python
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)

logging.info("程序启动")

name = input("请输入你的名字: ")

if not name.strip():
    logging.warning("用户输入了空名字")
    print("名字不能为空")
else:
    logging.info("用户输入名字成功: %s", name)
    print(f"你好，{name}")

logging.info("程序结束")
```

这段代码很适合刚开始练。

它体现了 3 个最常见场景：

- 开始运行：`info`
- 输入不合法：`warning`
- 正常结束：`info`

---

## 九、异常里怎么写日志

当程序里有 `try/except` 时，日志特别有用。

例如：

```python
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
    stream=sys.stdout,
)

try:
    age = int(input("请输入年龄: "))
    logging.info("年龄输入成功: %s", age)
except ValueError:
    logging.warning("用户输入的年龄不是整数")
    print("年龄必须是整数")
```

这里：

- 输入正确时，记一条 `info`
- 输入错误时，记一条 `warning`

如果是更严重的失败，例如保存文件失败，就更适合记 `error`。

---

## 十、今天先学到哪里就够了

今天先掌握这些内容就很好：

1. 知道 `logging` 是干什么的
2. 知道 `info` / `warning` / `error` 的区别
3. 会把日志输出到屏幕
4. 会把日志写入文件
5. 会让日志同时输出到屏幕和文件
6. 会在一个最简单的小程序里加日志

今天先不强求这些内容：

- `logger = logging.getLogger(__name__)`
- 更完整的工程化日志配置
- 多个模块共用日志
- 更复杂的 handler / formatter 写法

这些后面再学更合适。

---

## 十一、今天的练习文件

今天已经有 3 个最适合入门练习的脚本：

- `projects/08_Logging_Practice_CLI/logging_basic_simple.py`
- `projects/08_Logging_Practice_CLI/logging_to_file_simple.py`
- `projects/08_Logging_Practice_CLI/logging_console_and_file_simple.py`

如果你想多练一步，这个目录里还有一个更完整的命令行脚本：

- `projects/08_Logging_Practice_CLI/logging_practice.py`

建议练习顺序：

1. 先运行 `logging_basic_simple.py`
2. 再运行 `logging_to_file_simple.py`
3. 最后运行 `logging_console_and_file_simple.py`

每跑完一个，都自己回答两个问题：

- 这条内容为什么适合用 `logging`？
- 这条内容如果是直接给用户看，是不是更适合 `print()`？

---

## 十二、今天要带走的结论

- `logging` 是 Python 里记录程序运行过程的工具
- `print()` 不是不能用，而是用途不同
- `info` 表示正常信息
- `warning` 表示有问题但还能继续
- `error` 表示已经失败
- `filename` 可以把日志写入文件
- `handlers` 可以让日志同时输出到多个地方
- 学日志时，先从最简单的脚本开始最稳

---

## 今天的学习总结

今天从零开始学习了 Python `logging` 的最基础用法。  
先掌握了 `info`、`warning`、`error` 三种级别，再练习了日志输出到控制台、写入文件，以及同时输出到屏幕和文件。

同时也明确了一件很重要的事：  
`print()` 主要是给用户看，`logging` 主要是记录程序运行过程。
