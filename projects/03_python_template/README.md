# python_template

这是一个可复用的 Python 项目模板。

## 项目结构

- src/：主代码目录
- tests/：测试目录
- .env.example：环境变量示例
- requirements.txt：依赖列表

## 功能

- 使用 venv 管理虚拟环境
- 使用 pip 安装依赖
- 使用 requirements.txt 管理依赖列表
- 使用 python-dotenv 管理环境变量
- 使用 pydantic 组织配置或数据结构

## 使用方法

### 创建虚拟环境
python3 -m venv .venv

### 激活环境
source .venv/bin/activate

### 安装依赖
pip install -r requirements.txt

### 4. 运行项目
python -m src.main
