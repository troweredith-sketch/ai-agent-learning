# Week 1 Day 4｜Python 项目结构 / 模块导入 / `.env` / 工程化入门笔记

## **今日主题**

- Python 项目目录结构
- `main.py`
- `utils.py`
- `config.py`
- 模块导入
- `if __name__ == "__main__"`
- 什么是环境变量
- 为什么项目里会有 `.env`
- `BaseModel` 的作用
- `python -m src.main` 和 `python main.py` 的区别

---

## **一、今天在学什么**

今天的核心不是“再写一个 `.py` 文件”，而是开始学习：

> **如何把 Python 代码组织成一个可维护的小项目。**
> 

以前你写的代码更像是：

- 一个单独脚本
- 代码都放在一个文件里
- 配置直接写死在代码中
- 只要能跑就行

现在开始接触的是：

- 目录结构
- 配置管理
- 模块拆分
- 测试目录
- 虚拟环境
- `.env`
- 更像真实项目的写法

---

## **二、脚本代码和工程化代码的区别**

### **1. 以前的简单脚本**

以前常见的写法像这样：

```python
url = "https://api.example.com"
api_key = "123456"

print("开始请求")
```

特点：

- 代码简单直接
- 所有内容写在一个文件里
- 配置写死在代码中
- 适合练习、小工具、一次性脚本

---

### 2. 工程化代码

工程化代码更关注：

- 配置和代码分离
- 目录结构清晰
- 文件职责明确
- 方便维护
- 方便扩展
- 方便测试
- 方便给别人使用

一句话理解：

> **脚本是“能跑就行”，工程化是“以后还能继续维护”。**
> 

---

## 三、Day 4 推荐的项目结构

```
projects/python_template/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests/
│   └── test_smoke.py
├── .env.example
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 四、每个文件分别负责什么

### `src/main.py`

程序入口文件，负责主流程。

它通常负责：

- 调用配置
- 调用工具函数
- 组织程序执行顺序
- 输出结果

一句话理解：

> `main.py` 是“总指挥”。
> 

---

### `src/utils.py`

放通用工具函数。

比如：

- 格式化字符串
- 数据处理
- 小的辅助函数

一句话理解：

> `utils.py` 是“工具箱”。
> 

---

### `src/config.py`

负责配置相关逻辑。

比如：

- 读取环境变量
- 读取 `.env`
- 整理配置对象

一句话理解：

> `config.py` 是“设置中心”。
> 

---

### `tests/test_smoke.py`

负责最基本的测试。

它的作用是：

- 验证代码是否按预期工作
- 做最小功能检查

一句话理解：

> `test_smoke.py` 是“质检员”。
> 

---

## 五、`config.py` 代码讲解

示例代码：

```
from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()


class AppConfig(BaseModel):
    app_name: str = "Python Template"
    app_env: str = "development"
    author: str = "we"


def load_config() -> AppConfig:
    return AppConfig(
        app_name=os.getenv("APP_NAME", "Python Template"),
        app_env=os.getenv("APP_ENV", "development"),
        author=os.getenv("AUTHOR", "we"),
    )
```

---

### 1. `load_dotenv()`

作用：

> 读取 `.env` 文件，把里面的内容加载成环境变量。
> 

如果 `.env` 里有：

```
APP_NAME=My App
APP_ENV=local
AUTHOR=we
```

那么后面就可以通过 `os.getenv()` 读取。

---

### 2. `BaseModel`

`BaseModel` 是 `pydantic` 提供的基类。

这句：

```
class AppConfig(BaseModel):
```

意思是：

> 定义一个叫 `AppConfig` 的配置模型类，并继承 Pydantic 的能力。
> 

作用：

- 让配置结构更清晰
- 有类型提示
- 更适合表示“结构化数据”
- 比普通类更简洁

---

### 3. `AppConfig`

```
class AppConfig(BaseModel):
    app_name: str = "Python Template"
    app_env: str = "development"
    author: str = "we"
```

表示这个配置对象有 3 个字段：

- `app_name`
- `app_env`
- `author`

并且它们都是字符串类型。

默认值分别是：

- `"Python Template"`
- `"development"`
- `"we"`

---

### 4. `load_config()`

```
def load_config() -> AppConfig:
```

表示定义一个函数，这个函数返回一个 `AppConfig` 对象。

函数内部做的事是：

- 从环境变量里读取配置
- 如果没有，就使用默认值
- 把这些值整理成一个 `AppConfig` 对象返回

---

### 5. `os.getenv()`

例如：

```
os.getenv("APP_ENV","development")
```

意思是：

> 读取环境变量 `APP_ENV`，如果没有，就使用 `"development"`。
> 

---

### 6. `config.py` 的整体作用

一句话总结：

> `config.py` 负责从外部读取配置，并把它整理成一个结构清晰的配置对象。
> 

---

## 六、`utils.py` 代码讲解

示例代码：

```
def build_message(app_name: str, app_env: str, author: str) -> str:
    return f"应用：{app_name} | 环境：{app_env} | 作者：{author}"
```

---

### 1. 这个函数做什么

它接收 3 个字符串参数：

- `app_name`
- `app_env`
- `author`

然后把它们拼成一条字符串返回。

例如：

```
build_message("DemoApp","dev","we")
```

返回：

```
应用：DemoApp | 环境：dev | 作者：we
```

---

### 2. 为什么要放在 `utils.py`

因为它只是一个“可复用的小工具函数”，不属于主流程，也不属于配置管理。

一句话总结：

> `utils.py` 负责提供通用工具函数。
> 

---

## 七、`main.py` 代码讲解

示例代码：

```
from src.config import load_config
from src.utils import build_message


def main() -> None:
    config = load_config()
    message = build_message(config.app_name, config.app_env, config.author)
    print(message)


if __name__ == "__main__":
    main()
```

---

### 1. 导入

```
from src.config import load_config
from src.utils import build_message
```

意思是：

- 从 `src.config` 导入 `load_config`
- 从 `src.utils` 导入 `build_message`

也就是说：

> `main.py` 自己不做配置读取，也不做字符串拼接，而是调用其他模块完成这些工作。
> 

---

### 2. `main()` 函数

```
def main() -> None:
```

表示定义程序主流程函数。

函数内部做的事：

1. 调用 `load_config()` 获取配置
2. 调用 `build_message()` 生成消息
3. 打印消息

---

### 3. 执行流程

```
config = load_config()
```

从 `config.py` 获取配置对象。

```
message = build_message(config.app_name, config.app_env, config.author)
```

把配置对象中的值交给工具函数。

```
print(message)
```

输出结果。

---

### 4. `if __name__ == "__main__"`

```
if __name__ == "__main__":
    main()
```

意思是：

> 如果这个文件是直接运行的，就执行 `main()`。
> 

作用：

- 直接运行时执行主逻辑
- 被别的文件导入时，不会自动执行

一句话理解：

> 让这个文件既可以被导入，也可以单独运行。
> 

---

## 八、`test_smoke.py` 代码讲解

示例代码：

```
import unittest
from src.utils import build_message


class TestUtils(unittest.TestCase):
    def test_build_message(self):
        message = build_message("DemoApp", "dev", "we")
        self.assertIn("DemoApp", message)
        self.assertIn("dev", message)
        self.assertIn("we", message)


if __name__ == "__main__":
    unittest.main()
```

---

### 1. `unittest`

`unittest` 是 Python 自带的测试框架。

---

### 2. `TestUtils`

```
class TestUtils(unittest.TestCase):
```

定义一个测试类，继承 `unittest.TestCase`。

---

### 3. `test_build_message`

```
def test_build_message(self):
```

这是一个测试方法。

在 `unittest` 中，以 `test_` 开头的方法会被识别为测试用例。

---

### 4. 测试内容

```
message = build_message("DemoApp", "dev", "we")
```

调用 `build_message()`，生成结果。

然后检查：

```
self.assertIn("DemoApp", message)
self.assertIn("dev", message)
self.assertIn("we", message)
```

意思是：

- 检查 `"DemoApp"` 是否在结果中
- 检查 `"dev"` 是否在结果中
- 检查 `"we"` 是否在结果中

如果都在，测试通过。

---

### 5. `test_smoke.py` 的作用

一句话总结：

> 它用最简单的方式验证工具函数是否正常工作。
> 

---

## 九、4 个文件的整体配合关系

整个执行流程可以理解为：

1. 运行 `main.py`
2. `main.py` 去 `config.py` 读取配置
3. `main.py` 去 `utils.py` 调用工具函数
4. 最后把结果打印出来
5. `test_smoke.py` 用来检查工具函数是否工作正常

一句话总结：

> `config.py` 提供数据，`utils.py` 处理数据，`main.py` 组织流程，`test_smoke.py` 负责验证。
> 

---

## 十、什么是环境变量

环境变量可以理解成：

> **程序运行时会读取的一组“名字 = 值”的外部配置。**
> 

例如：

```
APP_ENV=development
HOME=/home/mr
PATH=/usr/local/bin:/usr/bin:/bin
```

左边是变量名，右边是变量值。

---

## 十一、环境变量有什么用

### 1. 给程序提供配置

比如：

- 当前环境是什么
- API Key 是什么
- 数据库地址是什么
- 应用名字是什么

---

### 2. 避免把敏感信息写死在代码里

例如：

- API Key
- 数据库密码
- Token

这些不应该直接写在 `.py` 文件里。

---

### 3. 让同一份代码适应不同环境

例如：

- 开发环境
- 测试环境
- 生产环境

代码可以不变，只修改环境变量。

---

### 4. 系统本身也依赖环境变量

最典型的就是：

- `PATH`
- `HOME`
- `USER`
- `PWD`

---

## 十二、什么是 `.env`

`.env` 是一个普通文本文件，用来集中写环境变量。

例如：

```
APP_NAME=My Python Template
APP_ENV=local
AUTHOR=we
API_KEY=abc123
```

然后 Python 程序通过：

```
from dotenv import load_dotenv

load_dotenv()
```

把它加载进来。

---

## 十三、为什么项目里会有 `.env`

因为真实项目里经常有一些内容：

- 不适合写死在代码里
- 不同环境下会变化
- 可能比较敏感
- 需要本地单独配置

例如：

- `API_KEY`
- `DATABASE_URL`
- `APP_ENV`
- `APP_NAME`

所以更好的做法是：

- 代码里只写“读取配置”
- 真实值写在 `.env`
- `.env` 不提交到 Git

---

## 十四、`.env` 和 `.env.example` 的区别

### `.env`

放真实配置值。

例如：

```
API_KEY=real_secret_key
APP_ENV=local
```

通常 **不提交到 Git**。

---

### `.env.example`

放示例模板。

例如：

```
API_KEY=your_api_key_here
APP_ENV=development
```

可以提交到 Git。

一句话理解：

- `.env`：真实配置
- `.env.example`：配置模板

---

## 十五、为什么以前的小脚本没有 `.env`

因为以前的脚本通常：

- 很简单
- 只自己本地跑
- 没有敏感配置
- 不区分不同环境
- 只是练习或一次性使用

所以直接写死在代码里也能接受。

但项目一旦开始变复杂，就需要：

- 配置分离
- 结构拆分
- 依赖管理
- 测试
- 更规范的运行方式

于是 `.env` 就会自然出现。

---

## 十六、`python main.py` 和 `python -m src.main` 的区别

### 1. `python main.py`

表示：

> 直接运行一个文件。
> 

适合：

- 简单脚本
- 单文件程序
- 临时练习

---

### 2. `python -m src.main`

表示：

> 按模块路径运行 `src.main`。
> 

适合：

- 有项目结构
- 有 `src/`
- 有模块导入
- 需要更稳定的导入方式

---

### 3. 为什么 Day 4 更推荐 `python -m src.main`

因为现在你的代码已经不是单个文件，而是：

- `src/main.py`
- `src/config.py`
- `src/utils.py`

这时更适合按项目模块方式运行。

一句话记忆：

> **简单脚本用 `python xxx.py`，项目模块用 `python -m 包名.模块名`。**
> 

---

## 十七、今天最重要的理解

1. 项目结构的目标是让代码更清晰、更容易维护
2. `main.py` 是程序入口
3. `utils.py` 是工具函数文件
4. `config.py` 是配置管理中心
5. `test_smoke.py` 是最基础的测试文件
6. 环境变量是程序运行时读取的外部配置
7. `.env` 是本地管理配置的文件
8. `.env` 的出现是为了让代码更安全、更灵活、更像真实项目
9. `BaseModel` 让配置类更规范
10. 项目结构下更推荐使用 `python -m src.main`

---

## 十八、最短总结版

### 文件职责

- `config.py`：读取配置
- `utils.py`：处理小工具逻辑
- `main.py`：组织程序执行流程
- `test_smoke.py`：做基础测试

### `.env` 的作用

- 存放外部配置
- 避免把敏感信息写死在代码里
- 支持不同环境下的不同配置

### 运行方式

- 小脚本：`python main.py`
- 项目模块：`python -m src.main`

### 工程化代码的本质

> 从“代码能跑”走向“代码能长期维护”。
>