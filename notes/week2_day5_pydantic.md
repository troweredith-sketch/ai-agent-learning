# Week 2 Day 5 - Pydantic 基础、数据校验、schema 概念

## 今天的学习目标

今天这节不是单独学一个新库，而是在为后面的命令行 Todo 项目提前打基础。

学完之后，你应该能做到：

- 知道 `Pydantic` 是用来做什么的
- 理解什么叫“数据校验”
- 理解什么叫 `schema`
- 能自己写一个最小可用的 `TodoItem` 数据模型
- 知道这个模型后面可以怎么接到 Day 6 的 Todo 项目里

---

## 一、先把今天放回你的学习上下文

你昨天学的是配置管理和环境变量，今天这节已经单独落成一个新的练手项目：

- `projects/10_Pydantic_Todo_Practice`

今天不再借旧模板项目过渡，而是直接围绕一个真实一点的业务对象来练：

- `TodoItem`

昨天更偏向：

- 配置从哪里来
- 配置应该怎么组织

今天则往前走一步：

- 用 Pydantic 表达业务数据结构

所以今天的重点不是“再学一遍配置”，而是把昨天的工程化思路扩展到业务模型：

> 昨天是“配置长什么样”，今天是“一个 Todo 任务长什么样”。

这也正好为 Day 6 的命令行 Todo 项目做铺垫。

---

## 二、Pydantic 是什么

可以先用一句话理解：

> Pydantic 是一个基于 Python 类型标注来做数据校验和数据结构定义的库。

它最适合解决这类问题：

- 我希望一份数据必须符合固定结构
- 我希望字段类型明确
- 我希望创建对象时自动做校验
- 我希望后面还能把这个结构导出成字典、JSON、schema

如果只用普通 `dict`，通常会遇到几个问题：

- 字段名容易写错
- 值的类型不稳定
- 缺字段时不容易第一时间发现
- 后面要转成 JSON 或做接口约束时不够清晰

Pydantic 的核心入口通常是 `BaseModel`。

最小例子：

```python
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


user = User(id="1", name="mr")

print(user)
print(user.id, type(user.id))
```

你可以重点观察：

- `id` 明明传入的是字符串 `"1"`
- 但 Pydantic 会尝试把它转换成 `int`

这说明 Pydantic 不只是“存数据”，还会“检查并尽量转换数据”。

---

## 三、什么是数据校验

数据校验可以简单理解成：

> 检查传进来的数据，是否符合我们预先定义好的规则。

这些规则包括：

- 有没有缺少必填字段
- 字段类型对不对
- 字段值是否满足约束
- 某些默认值该如何自动生成

例如，一个 Todo 项目里的任务：

- `id` 应该是整数
- `title` 应该是字符串
- `completed` 应该是布尔值
- `created_at` 应该是时间

如果传进来的数据不符合要求，Pydantic 会抛出 `ValidationError`。

这比等到程序跑很久之后才发现问题要好得多。

---

## 四、今天的核心练习：设计 `TodoItem`

下面这个模型，就是今天最重要的练习结果。

```python
from datetime import datetime

from pydantic import BaseModel, Field


class TodoItem(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100, description="任务标题")
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
```

### 逐个字段理解

#### `id: int`

表示任务 id 必须是整数。

例如：

- `1` 可以
- `"1"` 通常也会被转换成 `1`
- `"abc"` 不行

#### `title: str`

表示标题必须是字符串。

这里又加了一个 `Field(...)`：

```python
title: str = Field(min_length=1, max_length=100)
```

它的意思是：

- 最少 1 个字符
- 最多 100 个字符

所以空字符串 `""` 不应该通过校验。

#### `completed: bool = False`

表示任务默认未完成。

如果创建对象时不传这个字段，就自动使用 `False`。

#### `created_at: datetime = Field(default_factory=datetime.now)`

表示创建时间默认使用“当前时间”。

这里要注意一个非常重要的点：

我们用的是 `default_factory=datetime.now`，而不是：

```python
created_at: datetime = datetime.now()
```

原因是：

- `datetime.now()` 会在类定义时立刻执行一次
- `default_factory=datetime.now` 会在每次创建实例时再执行

也就是说，`default_factory` 才能保证每个 Todo 的创建时间是各自独立生成的。

---

## 五、把这个模型跑起来看

### 1. 正常创建

```python
todo = TodoItem(
    id=1,
    title="学习 Pydantic",
)

print(todo)
print(todo.model_dump())
```

你应该能看到：

- `completed` 自动补成 `False`
- `created_at` 自动补成当前时间
- `model_dump()` 可以把模型转成普通字典

### 2. 看类型转换

```python
todo = TodoItem(
    id="1",
    title="继续练习",
)

print(todo.id, type(todo.id))
```

重点观察：

- 传进去的是字符串
- 出来时已经变成了整数

这说明 Pydantic 做了数据解析和转换。

### 3. 看校验失败

```python
from pydantic import ValidationError

try:
    todo = TodoItem(
        id=1,
        title="",
    )
except ValidationError as exc:
    print(exc)
```

这次会失败，因为：

- `title` 的最小长度要求是 1
- 空字符串不满足这个规则

---

## 六、什么是 schema

`schema` 可以先用一句人话理解：

> schema 就是“这份数据应该长什么样”的结构说明书。

它通常会描述这些信息：

- 有哪些字段
- 每个字段是什么类型
- 哪些字段必填
- 每个字段有哪些约束
- 默认值是什么

对今天这个 `TodoItem` 来说，它的 schema 大概会表达：

- `id` 是整数
- `title` 是字符串，而且长度不能小于 1
- `completed` 是布尔值，默认值是 `False`
- `created_at` 是日期时间

Pydantic 可以直接帮我们生成 schema：

```python
print(TodoItem.model_json_schema())
```

这个输出通常不会拿来手写，但你需要知道它的意义：

- 它是“模型结构的机器可读说明”
- 后面做 API、自动文档、前后端约定、LLM 结构化输出时都很有用

你现在可以先记住：

> model 是“程序里可直接操作的数据对象”，schema 是“描述这个对象结构的说明书”。

---

## 七、为什么今天要学这个

因为从 Day 6 开始，你要做的是命令行 Todo 项目。

到了那一步，`TodoItem` 就不只是练习题了，而会变成真正的项目模型。

而且今天你已经有了一个专门的练习目录：

- `projects/10_Pydantic_Todo_Practice/src/todo_item.py`
- `projects/10_Pydantic_Todo_Practice/src/demo.py`
- `projects/10_Pydantic_Todo_Practice/tests/test_todo_item.py`

例如后面你很可能会做这些事：

- 添加任务时，先把输入组装成 `TodoItem`
- 保存到 JSON 文件前，先用 `model_dump()` 转成字典
- 读取旧数据时，再重新转回模型
- 更新任务状态时，保持字段结构一致

也就是说，今天学的内容，是后面项目分层里 `model` 这一层的起点。

---

## 八、和你这次练习项目的连接

今天建议你不要只停留在笔记里，而是和项目一起看：

- `src/todo_item.py`：看模型定义本身
- `src/demo.py`：看正常输入、自动转换、校验报错、schema 输出
- `tests/test_todo_item.py`：看怎样用测试验证模型行为

这一步你要真正建立起来的感觉是：

> Pydantic 本质上是“定义和校验数据结构”的工具，而不是只能拿来配配置。

---

## 九、关于版本：今天统一按 Pydantic v2 理解

今天这个练习项目里已经固定了版本：

- `projects/10_Pydantic_Todo_Practice/requirements.txt`
- `pydantic==2.10.6`

所以今天最好统一使用 v2 写法。

你看教程时如果看到这些旧写法，不要混淆：

- 旧写法：`.dict()`
- v2 更推荐：`model_dump()`

- 旧写法：`.schema()`
- v2 更推荐：`model_json_schema()`

如果你今天看到网上教程和这份笔记写法不一样，优先先判断它是不是旧版教程。

---

## 十、今天建议你按这个顺序学习

### 第一步：先理解概念，不急着背 API

先抓住 3 句话：

1. `Pydantic` 用来定义和校验数据结构
2. `BaseModel` 是最常见入口
3. `schema` 是“数据结构说明书”

### 第二步：只围绕 `TodoItem` 做最小练习

今天不要贪多，先把这个模型练熟：

```python
class TodoItem(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
```

### 第三步：主动做 4 次试错

你今天至少要自己试这 4 种输入：

1. 正常数据
2. `id="1"` 看自动转换
3. `title=""` 看校验报错
4. 打印 `model_dump()` 和 `model_json_schema()`

如果这 4 个都试过，你对今天内容的理解会扎实很多。

---

## 十一、今天的最小练习脚本

你可以先写一个最小可运行示例：

```python
from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class TodoItem(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)


def main() -> None:
    todo = TodoItem(id="1", title="学习 Pydantic")
    print("todo:", todo)
    print("dump:", todo.model_dump())
    print("schema:", TodoItem.model_json_schema())

    try:
        TodoItem(id=2, title="")
    except ValidationError as exc:
        print("validation error:")
        print(exc)


if __name__ == "__main__":
    main()
```

这个脚本覆盖了今天最重要的 4 个点：

- 建模
- 默认值
- 校验
- schema 输出

---

## 十二、今天的自测题

学完后你可以不看笔记，试着回答下面几个问题：

1. `Pydantic` 和普通 `dict` 的关键区别是什么？
2. `BaseModel` 是做什么的？
3. 为什么 `title=""` 应该校验失败？
4. 为什么 `created_at` 更适合写成 `Field(default_factory=datetime.now)`？
5. `model_dump()` 和 `model_json_schema()` 分别输出什么？
6. 为什么今天的 `TodoItem` 对明天的 Todo 项目有帮助？

如果这 6 个问题你能顺下来讲清楚，今天就不算只是“看过”，而是已经“学会一轮”了。

---

## 十三、今天的小结

今天最核心的收获，不是记住了多少 API，而是建立这条链路：

- 用 `BaseModel` 定义数据结构
- 用类型标注描述字段
- 用 `Field(...)` 添加约束
- 用校验保证输入更可靠
- 用 `schema` 输出结构说明

把这条链路建立起来后，后面的配置管理、接口参数、项目模型、甚至 LLM 结构化输出，都会越来越顺。

---

## 参考资料

- Pydantic 官方文档 Models: https://docs.pydantic.dev/latest/concepts/models/
- Pydantic 官方文档 Fields: https://docs.pydantic.dev/latest/concepts/fields/
- Pydantic 官方文档 JSON Schema: https://docs.pydantic.dev/latest/concepts/json_schema/
