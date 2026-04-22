# Week 2 Day 4 - 配置管理、`.env`、环境变量、不要把 key 写死在代码里

## 今天的学习目标

今天的重点不是做一个复杂配置系统，而是先把这条最核心的链路学明白：

- 什么是配置管理
- 什么是环境变量
- `.env` 和 `.env.example` 分别做什么
- `python-dotenv` 如何配合 `os.getenv()` 使用
- 为什么不能把 key 写死在代码里
- 如何把配置集中放进 `config.py`
- 如何在不同环境下做不同强度的校验

---

## 一、什么是配置管理

配置管理可以简单理解成：

> 把“会变化的参数”从业务代码里分离出来。

这些内容通常都属于配置，而不是业务逻辑：

- 应用名称
- 当前运行环境
- 是否开启 debug
- API key
- 请求超时时间
- 模型名称

为什么要分离？

- 本地开发和生产环境的值往往不同
- 同一份代码可能要跑在不同机器上
- 这些值比代码逻辑更容易变化

一句话理解：

> 业务逻辑负责“程序做什么”，配置负责“程序运行时用什么参数”。

---

## 二、什么是环境变量

环境变量就是：

> 操作系统或当前进程提供的一组键值对。

Python 可以在运行时读取这些值。

最常见的读取方式：

```python
import os

app_env = os.getenv("APP_ENV", "development")
```

这里：

- `APP_ENV` 是变量名
- `"development"` 是默认值

如果系统里存在 `APP_ENV`，就读取它；如果没有，就使用默认值。

常见适合放进环境变量的内容：

- `APP_ENV`
- `APP_DEBUG`
- `OPENAI_API_KEY`
- `API_TIMEOUT`
- `MODEL_NAME`

---

## 三、`.env` 和 `.env.example` 分别是什么

### `.env`

`.env` 是本机实际使用的配置文件。

例如：

```env
APP_NAME=Env Config Practice
APP_ENV=development
APP_DEBUG=true
API_TIMEOUT=30
MODEL_NAME=gpt-4.1-mini
OPENAI_API_KEY=your_api_key_here
```

它的特点是：

- 给当前机器实际运行使用
- 里面可能有真实敏感信息
- 一般不提交到 Git

### `.env.example`

`.env.example` 是配置模板文件。

它的作用是：

- 告诉别人这个项目需要哪些环境变量
- 提供示例值或占位值
- 可以安全地提交到 Git

### 为什么有了 `.env` 还要有 `.env.example`

因为 `.env` 通常会被 `.gitignore` 忽略，别人拿到仓库时看不到你的本地配置。

所以项目里通常是这两个一起存在：

- `.env`：你自己本机真实要用的值
- `.env.example`：告诉别人应该怎么配

常见流程：

```bash
cp .env.example .env
```

然后再把自己的真实值填进 `.env`。

---

## 四、`python-dotenv` 是做什么的

`python-dotenv` 的作用是：

> 把 `.env` 文件里的键值对加载到环境变量里。

最基础的写法：

```python
from dotenv import load_dotenv

load_dotenv()
```

加载之后，再用 `os.getenv()` 读取：

```python
import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME", "Demo App")
```

可以这样理解：

1. `load_dotenv()` 负责“把 `.env` 读进来”
2. `os.getenv()` 负责“按名字把值取出来”

---

## 五、为什么不能把 key 写死在代码里

不推荐这样写：

```python
OPENAI_API_KEY = "sk-1234567890"
```

主要原因有 4 个：

### 1. 不安全

代码一旦提交到 Git 或发给别人，key 很容易泄露。

### 2. 不方便切换环境

本地、测试、生产环境可能要用不同 key。

### 3. 不利于协作

每个人本地环境都可能不同，配置应该跟代码分离。

### 4. 配置和逻辑会混在一起

key 是运行参数，不是业务逻辑。

一句话总结：

> key 属于配置，不属于代码逻辑。

---

## 六、今天练习项目的结构

今天的练习项目是：

`projects/09_Env_Config_Practice`

最小结构如下：

```text
projects/09_Env_Config_Practice/
├── src/
│   ├── config.py
│   ├── main.py
│   └── utils.py
├── tests/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

各部分职责：

- `config.py`：统一读取和校验配置
- `main.py`：程序入口
- `utils.py`：放辅助函数，比如隐藏密钥
- `.env.example`：配置模板
- `.gitignore`：避免把 `.env`、`.venv` 提交到 Git

---

## 七、`BASE_DIR` 和 `ENV_FILE` 是做什么的

在当前练习项目里，有这样两行：

```python
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"
```

它们的作用是：

- `BASE_DIR`：找到项目根目录
- `ENV_FILE`：拼出 `.env` 文件的完整路径

逐步理解：

```python
Path(__file__)
```

表示当前这个文件自己的路径，也就是 `src/config.py`。

```python
.resolve()
```

把路径变成标准的绝对路径。

```python
.parent
```

表示上一层目录，也就是 `src/`。

```python
.parent.parent
```

再往上一层，就是项目根目录 `09_Env_Config_Practice/`。

然后：

```python
ENV_FILE = BASE_DIR / ".env"
```

这里的 `/` 在 `pathlib` 里表示拼接路径，不是除法。

所以最终得到的是：

```python
/home/mr/src/ai-agent-learning/projects/09_Env_Config_Practice/.env
```

这样写的好处是：

- 不依赖当前终端所在目录
- 程序总能准确找到项目自己的 `.env`
- 路径表达更清晰、更稳定

---

## 八、`parse_bool()` 是做什么的

当前项目里有这个函数：

```python
def parse_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default

    normalized = value.strip().lower()
    return normalized in {"1", "true", "yes", "on"}
```

它的作用是：

> 把环境变量里读出来的字符串，转换成真正的 `True` 或 `False`。

为什么要这样做？

因为环境变量读出来通常是字符串：

```python
"true"
"false"
"1"
"0"
```

但程序真正想用的是布尔值：

```python
True
False
```

逐行理解：

```python
if value is None:
    return default
```

如果这个环境变量根本没设置，就返回默认值。

```python
normalized = value.strip().lower()
```

这一步做了两件事：

- `.strip()`：去掉前后空格
- `.lower()`：统一转成小写

所以：

- `" TRUE "` 会变成 `"true"`
- `"Yes"` 会变成 `"yes"`

最后这句：

```python
return normalized in {"1", "true", "yes", "on"}
```

如果值在这组“真值集合”里，就返回 `True`；否则返回 `False`。

例如：

- `parse_bool("true")` -> `True`
- `parse_bool("YES")` -> `True`
- `parse_bool("1")` -> `True`
- `parse_bool("false")` -> `False`
- `parse_bool("0")` -> `False`
- `parse_bool(None)` -> 返回默认值

为什么不能直接写：

```python
bool(os.getenv("APP_DEBUG"))
```

因为：

```python
bool("false")
```

结果仍然是 `True`。  
只要字符串非空，`bool(...)` 就会变成 `True`，这不是我们想要的配置行为。

---

## 九、当前练习项目的最终版配置思路

经过今天的练习，当前项目已经支持这些配置项：

- `APP_NAME`
- `APP_ENV`
- `APP_DEBUG`
- `API_TIMEOUT`
- `MODEL_NAME`
- `OPENAI_API_KEY`

在 `config.py` 里的思路是：

1. 先定位并加载 `.env`
2. 再通过 `os.getenv()` 读取各个配置项
3. 对布尔值做转换
4. 对字符串做 `strip()`
5. 在进入主程序前完成必要校验

这就是“把配置读取和配置校验集中到一个入口”的最小做法。

---

## 十、练习 3：新增 `API_TIMEOUT`

练习 3 做的是：

```env
API_TIMEOUT=30
```

你完成的动作包括：

- 在 `.env.example` 里加入 `API_TIMEOUT`
- 在 `config.py` 里用 `os.getenv("API_TIMEOUT", "30")` 读取它
- 用 `int(...)` 把字符串转成整数
- 在 `AppConfig` 里保存它
- 在程序输出里显示出来

这里最关键的一点是：

> 环境变量读出来默认是字符串，数字要自己做类型转换。

---

## 十一、练习 4：给生产环境增加安全规则

练习 4 的要求是：

> 当 `APP_ENV=production` 且 `OPENAI_API_KEY` 为空时，程序直接报错，不继续运行。

当前实现思路是：

```python
if app_env == "production" and not openai_api_key:
    raise ValueError("APP_ENV=production 时，必须配置 OPENAI_API_KEY。")
```

为什么这条规则要放在 `load_config()` 里？

因为这里是配置的统一入口。

好处是：

- 配置一加载就能发现问题
- 错误不会拖到业务逻辑里才暴露
- 程序可以做到“尽早失败”

这也是工程里很常见的思路：

- `development` 可以相对宽松
- `production` 需要更严格的配置校验

---

## 十二、练习 5：新增 `MODEL_NAME`

练习 5 做的是：

```env
MODEL_NAME=gpt-4.1-mini
```

你完成的动作包括：

- 在 `.env.example` 里加入 `MODEL_NAME`
- 在 `config.py` 里读取它
- 在 `AppConfig` 里保存它
- 在程序输出里显示模型名称

为什么 `MODEL_NAME` 也适合放到配置里？

因为它也是“会变化的参数”：

- 有时你想换更快的模型
- 有时你想换更便宜的模型
- 有时你想按环境切不同模型

如果把模型名写死在代码里，以后每次切模型都要改代码。  
更合理的做法是改配置，不改逻辑。

---

## 十三、当前程序的运行流程

可以把当前项目理解成这样一条链路：

```text
.env
  -> load_dotenv()
  -> os.getenv()
  -> parse_bool() / int() / strip()
  -> AppConfig
  -> build_summary()
  -> main.py 输出
```

也可以换成一句话：

> 先把配置从文件读进来，再做必要转换和校验，最后交给主程序使用。

---

## 十四、今天最重要的工程习惯

1. 不要把敏感 key 写死在代码里。
2. `.env` 用于本机真实配置，`.env.example` 用于共享配置模板。
3. 配置应该集中到 `config.py`，不要散落在多个业务文件中。
4. 环境变量读出来默认是字符串，需要自己做类型转换。
5. 关键配置应该在程序启动时尽早校验，不要等程序跑到一半才报错。

---

## 十五、今天最小完成标准

如果你已经做到下面这些，就说明 Day 4 达标了：

- 能解释什么是配置管理
- 能说清环境变量、`.env`、`.env.example` 的区别
- 会用 `python-dotenv` 和 `os.getenv()` 读取配置
- 能解释 `BASE_DIR`、`ENV_FILE` 的作用
- 能解释 `parse_bool()` 为什么有必要
- 能在项目里增加新配置项
- 能给生产环境加一条最小安全规则

---

## 十六、下一步还能继续练什么

如果你想继续把这套思路练扎实，可以再加这些配置项：

- `BASE_URL`
- `LOG_LEVEL`
- `ENABLE_CACHE`
- `REQUEST_RETRY`

也可以继续做两类进阶练习：

- 限制 `APP_ENV` 只能是 `development / test / production`
- 当 `API_TIMEOUT <= 0` 时，直接报错

这样你就会开始真正进入“配置校验”而不只是“读取配置”。
