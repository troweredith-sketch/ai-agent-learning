# DEVLOG

## 2026-04-10

### 本次目标
初始化学生管理系统项目，搭建基础目录结构，准备进入类设计阶段。

### 已完成
- 创建 `src/`、`tests/`、`docs/` 目录
- 初始化 `.gitignore`
- 创建 `README.md`
- 创建 `DESIGN.md`、`DEVLOG.md`、`TESTLOG.md`、`CHANGELOG.md`

### 当前想法
- 使用 Python 面向对象实现控制台版学生管理系统
- 先设计 `Student` 和 `StudentManager`
- 先做最小可运行版本，再逐步扩展

### 下一步
- 完成任务一：明确类职责和整体设计


## 2026-04-10

### 本次目标
完成 Student 类第一版设计与实现。

### 已完成
- 新增 Student 类
- 定义 student_id、name、age、gender、score 五个属性
- 使用 `__str__` 作为学生对象的展示方式
- 明确 Student 只表示单个学生，不负责管理学生列表

### 设计想法
- 第一版先完成“创建对象”和“展示对象”
- 不在 Student 中处理学号重复问题
- 不在当前阶段加入复杂输入校验

### 遇到的问题
- 一开始在 `show_info()` 和 `__str__()` 之间犹豫
- 最终选择 `__str__()`，因为直接 `print(对象)` 更自然

### 下一步
- 开始设计 StudentManager 的内部结构