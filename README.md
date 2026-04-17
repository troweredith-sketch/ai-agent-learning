# ai-agent-learning

这是我的 AI Agent / Python 学习仓库，用来记录学习笔记、练手项目和每周复盘。

## 学习环境约定

- 默认在 WSL Ubuntu 环境中学习和开发
- Python 命令优先使用 `python3`
- Python 项目优先使用项目内 `.venv` 管理依赖
- 日常练习优先使用 Linux 路径和命令

## 仓库结构

- `notes/`：每天的学习笔记
- `projects/`：练手项目和脚本练习
- `weekly_review/`：每周复盘与阶段总结

## 当前学习进度

### Week 1

- Day 1：Git 基本概念、仓库与分支、WSL 基本目录和命令
- Day 2：Linux 常用命令、相对路径与绝对路径、文件权限、环境变量
- Day 3：Python 虚拟环境、`venv`、`pip`、`requirements.txt`
- Day 4：Python 项目目录结构、模块导入、`if __name__ == "__main__"`
- Day 5：Git 常见操作、commit 编写规范
- Day 6：Markdown 基础、学习笔记写法、项目 README 写法

### Week 2

- Day 1：函数设计、参数和返回值、类型标注、docstring 基础
- Day 2：异常处理、`try/except`、自定义错误提示、异常的抛出与捕获

## 项目索引

- `02_linux_practice`：Linux 基础命令与终端操作练习
- `03_python_template`：可复用的 Python 项目模板，练习基础项目结构
- `04_python_oop_notes`：面向对象基础概念整理笔记
- `05_Student_Management_System`：控制台学生管理系统，练习类设计和 CRUD
- `06_Refactoring_Exercise_Script_Shopping_List_Statistics`：购物清单统计脚本重构练习
- `07_Exception_Handling_CLI`：异常处理命令行脚本，练习输入校验与错误恢复

## 笔记索引

- [Week 1 Day 1 - Git 与 WSL 基础](notes/week1_day1_git_wsl.md)
- [Week 1 Day 2 - Linux 基础命令](notes/week1_day2_linux_basic.md)
- [Week 1 Day 3 - Python 虚拟环境](notes/week1_day3_python_env.md)
- [Week 1 Day 4 - Python 项目结构](notes/week1_day4_project_structure.md)
- [Week 1 Day 5 - Git 工作流](notes/week1_day5_git_workflow.md)
- [Week 2 Day 1 - 函数设计、类型标注、docstring 基础](notes/week2_day1_typing_function.md)
- [Week 2 Day 2 - 异常处理、try/except、自定义错误提示](notes/week2_day2_exception.md)

## 本周最新产出

- [Week 2 Day 2 学习笔记](notes/week2_day2_exception.md)：整理异常处理核心概念、常见异常类型和 `raise` / `except` 的职责分工
- [异常处理练习脚本](projects/07_Exception_Handling_CLI/exception_cli.py)：实现命令行输入、错误提示、重试逻辑与退出处理

## 运行示例

在仓库根目录可以直接运行今天的练习脚本：

```bash
python3 projects/07_Exception_Handling_CLI/exception_cli.py
```
