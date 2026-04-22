# 09 Env Config Practice

这是一个专门练习配置管理、`.env`、环境变量和 `config.py` 的小项目。

今天这份练习的目标不是做复杂功能，而是把下面这条链路跑通：

`.env` -> `python-dotenv` -> `os.getenv()` -> `config.py` -> `main.py`

## 你会练到什么

- 如何创建并使用 `.env`
- 为什么有了 `.env` 还要有 `.env.example`
- 如何用 `python-dotenv` 加载本地配置
- 如何用 `os.getenv()` 读取环境变量
- 如何理解 `BASE_DIR`、`ENV_FILE` 和 `parse_bool()`
- 如何把配置集中写到 `config.py`
- 为什么不能把敏感 key 直接打印出来

## 项目结构

```text
09_Env_Config_Practice/
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

## 初始化环境

在当前项目目录运行：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 运行项目

```bash
python3 -m src.main
```

你会看到类似输出：

```text
应用名称: Env Config Practice
运行环境: development
调试模式: True
API 超时时间: 30 秒
模型名称: gpt-4.1-mini
OPENAI_API_KEY: your...here
是否已配置密钥: 是
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 建议练习顺序

### 练习 1：修改 `.env`

依次修改下面几个值，然后每改一次就重新运行项目：

- `APP_NAME`
- `APP_ENV`
- `APP_DEBUG`
- `OPENAI_API_KEY`

目标：

- 看见配置变化如何影响程序输出
- 感受“配置和代码分离”的好处

### 练习 2：观察 `config.py`

重点看这几个点：

- `BASE_DIR` 和 `ENV_FILE` 为什么这样写
- `load_dotenv()` 做了什么
- `os.getenv()` 做了什么
- `parse_bool()` 为什么有必要
- 为什么要用 `AppConfig` 集中保存配置

### 练习 3：自己新增一个配置项

请你自己新增：

```text
API_TIMEOUT=30
```

然后完成下面动作：

- 在 `.env.example` 里加入它
- 在 `config.py` 里读取它
- 在 `AppConfig` 里保存它
- 在 `main.py` 里打印它

### 练习 4：增加一个安全规则

请你自己实现下面规则：

> 当 `APP_ENV=production` 且 `OPENAI_API_KEY` 为空时，程序直接报错，不继续运行。

提示：

- 可以在 `load_config()` 里判断
- 也可以写一个单独校验函数

完成后你应该能得到这条规则：

- `development` 环境可以先宽松一点
- `production` 环境必须保证关键配置完整

### 练习 5：再加一个配置项

试着新增：

```text
MODEL_NAME=gpt-4.1-mini
```

再思考：

- 为什么这类模型名也适合放到配置里？
- 如果以后想切模型，改代码和改配置，哪个更合理？

## `.env` 和 `.env.example` 的区别

- `.env`：当前机器真实要用的配置，通常不提交到 Git
- `.env.example`：项目配置模板，告诉别人这个项目需要哪些变量

常见做法：

```bash
cp .env.example .env
```

然后再把自己的真实值填进 `.env`。

## 今天最重要的工程习惯

### 1. 不要把敏感 key 写死在代码里

错误示例：

```python
OPENAI_API_KEY = "sk-xxxx"
```

更推荐：

```python
openai_api_key = os.getenv("OPENAI_API_KEY", "")
```

### 2. 不要把 `.env` 提交到 Git

所以项目里要有：

- `.gitignore`
- `.env.example`

### 3. 配置集中管理，不要散落 everywhere

今天先养成一个最基础的习惯：

> 配置统一从 `config.py` 进入。

## 如果你学完还想继续练

你可以继续加下面这些配置项：

- `BASE_URL`
- `LOG_LEVEL`
- `ENABLE_CACHE`
- `REQUEST_RETRY`

这些都很适合继续练习“环境变量 + 配置管理”的思路。
