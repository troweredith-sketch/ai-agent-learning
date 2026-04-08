# Week 1 Day 3｜Python 虚拟环境 / venv / pip 学习笔记

---


## 今日学习主题

- Python 虚拟环境
- `venv`
- `pip`
- `requirements.txt`
- 为什么项目要隔离环境
- 搭建一个可复用的 Python 项目模板

---

## 一、今天主要学了什么

今天的核心目标是：

> 学会给每个 Python 项目创建独立环境，并用规范方式管理依赖。
> 

一句话总结：

> 每个 Python 项目都应该有自己独立的运行环境，不要把所有包都装到系统全局环境里。
> 

---

## 二、为什么项目要隔离环境

如果所有 Python 项目都共用同一个全局环境，很容易出现下面这些问题：

1. 包版本冲突
比如项目 A 需要一个版本的 `pydantic`，项目 B 需要另一个版本。
2. 环境混乱
时间久了会忘记自己装过哪些包，哪些项目依赖哪些版本。
3. 项目不可复现
别人拿到你的代码后，无法快速还原出和你一样的运行环境。
4. 修改一个项目可能影响另一个项目
你在全局环境升级一个包，其他项目可能就跑不起来了。

所以更好的做法是：

> 每个项目一个独立虚拟环境。
> 

一句话理解：

> 虚拟环境就是给项目单独准备一个“自己的 Python 房间”。
> 

---

## 三、什么是 Python 虚拟环境

虚拟环境的作用是：

> 给当前项目提供一套独立的 Python 和 `pip` 环境。
> 

这样在这个环境里安装的包，只影响当前项目，不影响系统全局 Python，也不影响其他项目。

常见做法是使用 Python 自带的 `venv`。

---

## 四、`venv` 是什么

`venv` 是 Python 自带的虚拟环境工具。

最常见的命令是：

```
python3-m venv .venv
```

这条命令的意思是：

- 用 `python3`
- 调用 `venv` 模块
- 在当前目录下创建一个名为 `.venv` 的虚拟环境

### 为什么常命名为 `.venv`

1. 一眼就能看出这是虚拟环境
2. 通常会被 `.gitignore` 忽略
3. 编辑器更容易自动识别

---

## 五、`pip` 是什么

`pip` 是 Python 的包管理工具。

它的作用包括：

- 安装包
- 卸载包
- 查看已安装包
- 导出当前环境依赖

### 常用命令

```
pip install 包名
pip uninstall 包名
pip list
pip freeze
```

例如：

```
pip install requests
```

表示安装 `requests` 包。

---

## 六、`requirements.txt` 是什么

`requirements.txt` 是项目依赖清单文件。

它的作用是：

> 记录这个项目当前依赖了哪些 Python 包和对应版本。
> 

这样别人拿到项目后，只要执行：

```
pip install-r requirements.txt
```

就可以快速安装项目依赖。

### 生成方式

```
pip freeze > requirements.txt
```

这条命令的意思是：

- `pip freeze` 输出当前虚拟环境中的依赖列表
- `>` 把输出写入 `requirements.txt`

一句话理解：

> `requirements.txt` 是项目依赖说明书。
> 

---

## 七、今天实际做了什么

今天的练习目标是：

> 在 `projects/python_template/` 下搭建一个可复用的 Python 项目模板。
> 

### 建议项目结构

```
ai-agent-learning/
└── projects/
    └── python_template/
        ├── app/
        │   └── main.py
        ├── .venv/
        ├── .env.example
        ├── README.md
        ├── requirements.txt
        └── .gitignore
```

### 各部分作用

- `app/main.py`：项目主程序入口
- `.venv/`：当前项目的虚拟环境
- `requirements.txt`：项目依赖列表
- `.env.example`：环境变量示例文件
- `README.md`：项目说明文件
- `.gitignore`：忽略不应该提交到 Git 的内容

---

## 八、Day 3 实操流程

### 第一步：进入项目目录

```
cd ~/ai-agent-learning/projects
```

### 第二步：创建模板项目目录

```
mkdir-p python_template/app
cd python_template
```

### 第三步：创建虚拟环境

```
python3-m venv .venv
```

### 第四步：激活虚拟环境

```
source .venv/bin/activate
```

激活成功后，终端前面通常会出现：

```
(.venv)
```

这说明你已经进入当前项目的虚拟环境。

### 第五步：确认当前使用的是虚拟环境里的 Python 和 `pip`

```
which python
which pip
```

正常情况下会显示路径指向当前项目里的 `.venv/bin/`。

这一步的意义是：

> 确认你安装包时，不会装到系统全局，而是装到当前项目的独立环境里。
> 

### 第六步：安装基础依赖包

```
pip install requests python-dotenv pydantic
```

今天安装的三个包分别是：

- `requests`：用于发送 HTTP 请求
- `python-dotenv`：用于从 `.env` 文件读取环境变量
- `pydantic`：用于定义配置结构、数据结构和做数据校验

### 第七步：导出依赖文件

```
pip freeze > requirements.txt
```

### 第八步：查看依赖内容

```
cat requirements.txt
```

---

## 九、今天搭建的 Python 模板项目应该具备什么

一个可复用的 Python 模板项目，至少应该包含这些内容：

1. 独立虚拟环境
2. 依赖安装方式明确
3. `requirements.txt`
4. 一个最小可运行程序
5. `.env.example`
6. `.gitignore`
7. `README.md` 说明

这意味着以后新建 Python 项目时，你可以直接复制这套模板，再按项目需求改内容，而不是每次从零开始。

---

## 十、关于 `.gitignore` 的补充理解

如果你在仓库根目录 `ai-agent-learning/` 已经有 `.gitignore`，通常不需要在 `python_template/` 里面再写一个新的。

因为根目录 `.gitignore` 会对子目录生效。

### 建议至少包含这些规则

```
.venv/
__pycache__/
*.pyc
.env
```

这样就可以避免把虚拟环境、缓存文件和真实环境变量文件提交到 Git。

### 注意

- `.env` 不应该提交
- `.env.example` 可以提交

一句话理解：

- `.env.example` 是模板
- `.env` 是真实配置

---

## 十一、今天最重要的命令

### 创建虚拟环境

```
python3-m venv .venv
```

### 激活虚拟环境

```
source .venv/bin/activate
```

### 查看当前 Python 路径

```
which python
```

### 查看当前 `pip` 路径

```
which pip
```

### 安装包

```
pip install requests python-dotenv pydantic
```

### 查看已安装包

```
pip list
```

### 导出依赖

```
pip freeze > requirements.txt
```

### 退出虚拟环境

```
deactivate
```

---

## 十二、今天最重要的理解

1. 每个 Python 项目都应该隔离环境
2. `venv` 用来创建项目独立虚拟环境
3. `pip` 用来安装和管理 Python 包
4. `requirements.txt` 用来记录项目依赖
5. 激活虚拟环境后再安装包，包才会装到当前项目里
6. `.venv` 不应该提交到 Git
7. `.env` 不应该提交，但 `.env.example` 可以提交

---

## 十三、今天的一个最小工作流

以后你新建一个 Python 项目，最基础的流程可以照这个走：

### 1. 创建目录

```
mkdir my_project
cd my_project
```

### 2. 创建虚拟环境

```
python3-m venv .venv
```

### 3. 激活虚拟环境

```
source .venv/bin/activate
```

### 4. 安装依赖

```
pip install requests python-dotenv pydantic
```

### 5. 导出依赖文件

```
pip freeze > requirements.txt
```

---

## 十四、今天的产出

今天的产出应该包括：

1. 一个可复用的 Python 项目模板
2. `projects/python_template/` 目录结构
3. 虚拟环境 `.venv`
4. 已安装的基础依赖
5. `requirements.txt`
6. 学习笔记 `notes/week1_day3_python_env.md`

---

## 十五、今天学完后要能回答的问题

1. 为什么 Python 项目要隔离环境？
2. `venv` 是干什么的？
3. `pip` 是干什么的？
4. `requirements.txt` 有什么作用？
5. 为什么 `.venv` 不应该提交到 Git？
6. 为什么 `.env` 不应该提交，但 `.env.example` 可以提交？
7. 如何确认你当前用的是虚拟环境里的 Python？

如果这些问题你都能自己说清楚，说明 Day 3 已经学到位了。

---

## 十六、明天可以继续学什么

建议下一步继续学习这些内容：

- Python 项目结构
- 模块与包
- `__init__.py`
- 脚本运行方式
- `if __name__ == "__main__":`
- 如何把项目拆成多个文件