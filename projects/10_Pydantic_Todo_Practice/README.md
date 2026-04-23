# 10 Pydantic Todo Practice

这是一个专门服务于 Week 2 Day 5 的小项目。

目标不是立刻做完整 Todo 程序，而是先把下面这条链路练明白：

`BaseModel` -> 字段类型 -> `Field(...)` 约束 -> 数据校验 -> `model_dump()` -> `model_json_schema()`

你今天看笔记时，建议同时打开：

- `notes/week2_day5_pydantic.md`
- `projects/10_Pydantic_Todo_Practice/src/todo_item.py`
- `projects/10_Pydantic_Todo_Practice/src/demo.py`

## 你会练到什么

- 如何用 `BaseModel` 定义结构化数据
- 如何用类型标注描述字段类型
- 如何用 `Field(...)` 增加长度约束和默认值规则
- 什么是 `ValidationError`
- `model_dump()` 和 `model_json_schema()` 分别做什么
- 为什么 `TodoItem` 会是后面 Todo 项目的模型起点

## 项目结构

```text
10_Pydantic_Todo_Practice/
├── src/
│   ├── __init__.py
│   ├── demo.py
│   └── todo_item.py
├── tests/
│   └── test_todo_item.py
├── .gitignore
├── README.md
└── requirements.txt
```

## 初始化环境

在当前项目目录运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 运行 demo

```bash
python3 -m src.demo
```

你会依次看到：

- 正常创建的 `TodoItem`
- 字符串 `"2"` 被转换成整数 `2`
- 空标题触发 `ValidationError`
- `TodoItem` 自动生成的 schema

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 建议学习顺序

### 第一步：先看模型

先读：

- `src/todo_item.py`

只盯住 4 个字段：

- `id`
- `title`
- `completed`
- `created_at`

先回答自己两个问题：

1. 哪些字段必须传？
2. 哪些字段会自动补默认值？

### 第二步：再跑 demo

再运行：

```bash
python3 -m src.demo
```

重点观察 4 件事：

1. `id="2"` 为什么最后变成了整数
2. `title=""` 为什么会报错
3. `model_dump()` 输出的是普通字典还是模型对象
4. `model_json_schema()` 输出里有哪些字段信息

### 第三步：改代码做练习

今天建议你按这个顺序练：

#### 练习 1：修改标题规则

把：

```python
title: str = Field(min_length=1, max_length=100, description="任务标题")
```

改成：

- `min_length=3`
- `max_length=50`

然后重新跑 demo 和测试，看看有什么变化。

#### 练习 2：新增 `priority`

请你自己给 `TodoItem` 增加：

```python
priority: int = Field(default=3, ge=1, le=5, description="任务优先级")
```

然后完成这 3 件事：

- 在 `demo.py` 里打印这个字段
- 在测试里补一个关于 `priority` 的断言
- 故意传入 `priority=10` 看看会报什么错

#### 练习 3：故意传错类型

试这几种输入：

- `id="abc"`
- `completed="yes"`
- `created_at="2026-04-23T10:30:00"`

观察哪些能转换，哪些会失败。

#### 练习 4：自己读 schema

运行：

```bash
python3 -m src.demo
```

然后重点找：

- `required`
- `properties`
- `title`
- `created_at`

目标不是背输出，而是看懂：

> schema 到底是怎么描述模型结构的。

## 今天最重要的理解

`TodoItem` 不是为了“炫 API”，而是为了把业务数据先定义清楚。

明天开始做命令行 Todo 项目时，这个模型就可以继续复用，比如：

- 添加任务时做输入校验
- 存 JSON 前统一转成字典
- 读取旧数据时重新转成模型

也就是说，今天这个项目其实是在给明天的项目打地基。
