# Week 1 Day 1 - Git 和 WSL 基础

## 1. Git 是什么

Git 是一个**版本控制工具**，用来管理代码历史。

它能做的事：

- 记录每次代码修改
- 查看历史版本
- 回退错误修改
- 使用分支进行独立开发

一句话理解：

> Git 负责管理本地代码版本。
> 

---

## 2. GitHub 是什么

GitHub 是一个**托管 Git 仓库的平台**。

它的作用：

- 把本地仓库放到云端
- 备份代码
- 多人协作
- 展示项目

一句话理解：

> GitHub 是远程仓库平台，Git 是本地版本管理工具。
> 

---

## 3. Git 常见核心概念

### 仓库 repository

一个被 Git 管理的项目目录就是仓库。

如果目录里有 `.git/`，那它就是一个 Git 仓库。

---

### commit

一次 commit 就是一次“版本快照”。

可以理解为：

> 在某个时间点，把当前项目状态正式存档。
> 

---

### branch

分支是一条独立开发线。

常见分支：

- `main`：主分支
- `feature/xxx`：功能开发分支

---

### push / pull

### `git push`

把本地提交上传到 GitHub

### `git pull`

把 GitHub 上的最新代码拉到本地

一句话记忆：

- `commit`：提交到本地历史
- `push`：推到远程
- `pull`：从远程拉下来

---

## 4. Git 的三个区域

### 工作区 Working Directory

当前你看到并修改的文件目录。

### 暂存区 Staging Area

准备提交的区域。

先用 `git add` 把修改加入暂存区。

### 本地仓库 Repository

正式保存提交历史的地方。

用 `git commit` 创建版本记录。

---

## 5. Git 的基本工作流

日常最基础流程：

```
git status
git add .
git commit-m"提交说明"
git push
```

完整理解：

1. 修改文件
2. `git status` 查看状态
3. `git add` 加入暂存区
4. `git commit` 提交到本地仓库
5. `git push` 推送到 GitHub

---

## 6. WSL 是什么

WSL 是 Windows Subsystem for Linux，意思是：

> 在 Windows 里使用 Linux 环境
> 

它适合写代码、跑命令行、学习 Linux 和 Git。

---

## 7. WSL 常用命令

### 查看当前目录

```
pwd
```

### 查看当前目录下文件

```
ls
```

### 查看完整列表（含隐藏文件）

```
ls-la
```

### 切换目录

```
cd ~
cd ai-agent-learning
cd ..
```

### 创建目录

```
mkdir notes
mkdir-p notes projects weekly_review
```

### 创建空文件

```
touch README.md
```

### 查看文件内容

```
cat README.md
```

### 清屏

```
clear
```

---

## 8. Git 初始化与基础配置

### 查看 Git 版本

```
git--version
```

### 配置用户名和邮箱

```
git config--global user.name"你的名字"
git config--global user.email"你的邮箱"
```

### 查看全局配置

```
git config--global--list
```

### 设置默认分支名为 main

```
git config--global init.defaultBranch main
```

---

## 9. 创建本地仓库

### 初始化仓库

```
git init
```

### 查看状态

```
git status
```

### 创建 README

```
echo"# 我的项目" > README.md
```

### 加入暂存区

```
git add README.md
```

### 提交

```
git commit-m"第一次提交"
```

### 查看历史

```
git log--oneline
```

---

## 10. GitHub SSH 配置

为了用 SSH 连接 GitHub，需要先生成密钥。

### 生成 SSH 密钥

```
ssh-keygen-t ed25519-C"你的GitHub邮箱"
```

出现：

```
Enter filein which to save the key (/home/用户名/.ssh/id_ed25519):
```

这里直接按 **回车**，使用默认路径即可。

---

### 启动 ssh-agent

```
eval"$(ssh-agent -s)"
```

### 添加私钥

```
ssh-add ~/.ssh/id_ed25519
```

### 查看公钥

```
cat ~/.ssh/id_ed25519.pub
```

把输出内容复制到 GitHub：

- Settings
- SSH and GPG keys
- New SSH key

### 测试连接

```
ssh-Tgit@github.com
```

第一次如果提示确认连接，输入：

```
yes
```

---

## 11. clone GitHub 仓库到 WSL

例如仓库名为 `ai-agent-learning`：

```
git clonegit@github.com:你的用户名/ai-agent-learning.git
cd ai-agent-learning
```

---

## 12. 创建学习仓库结构

```
mkdir-p notes projects weekly_review
touch README.md
touch notes/week1_day1_git_wsl.md
```

目录结构：

```
ai-agent-learning/
├── README.md
├── notes/
│   └── week1_day1_git_wsl.md
├── projects/
└── weekly_review/
```

---

## 13. 第一次 push 的关键命令

### `git branch -M main`

意思：

> 把当前分支强制重命名为 `main`
> 

常见原因：

- 本地默认分支可能叫 `master`
- GitHub 现在通常默认主分支叫 `main`
- 所以要统一名字

---

### `git push -u origin main`

意思：

> 把本地 `main` 分支推送到远程仓库 `origin`，并建立追踪关系
> 

拆开理解：

- `push`：推送
- `origin`：远程仓库名
- `main`：本地分支名
- `u`：建立上游关系

建立关系后，以后可以直接用：

```
git push
```

---

## 14. 为什么第一次不能直接 `git push`

因为第一次时，Git 往往还不知道：

- 你要推到哪个远程仓库
- 你要推到哪个远程分支

所以第一次通常要写完整：

```
git push-u origin main
```

这样 Git 才会记住：

> 本地 `main` 对应远程 `origin/main`
> 

以后再推送就可以直接：

```
git push
```

---

## 15. 常见报错与理解

### 报错：`src refspec main does not match any`

意思通常是：

- 本地没有 `main` 分支
- 或者还没有任何 commit

解决思路：

```
git add .
git commit-m"first commit"
git branch-M main
git push-u origin main
```

---

## 16. `.gitignore` 是什么

`.gitignore` 用来忽略不该提交的文件，比如：

- `__pycache__/`
- `.venv/`
- `.pyc`
- `.env`

示例：

```
__pycache__/
.venv/
*.pyc
.env
```

---

## 17. EOF 写文件的用法

### 覆盖写入文件

```
cat > README.md<<'EOF'
这里写内容
EOF
```

### 追加内容

```
cat >> README.md<<'EOF'
这里是追加内容
EOF
```

---

### 如果 EOF 里写错了怎么办

### 情况 1：还没结束 EOF

可以按：

```
Ctrl+ C
```

取消当前输入，然后重新写。

### 情况 2：已经写完并保存

可以用编辑器修改，例如：

```
nano notes/week1_day1_git_wsl.md
```

保存方法：

- `Ctrl + O` 保存
- 回车确认
- `Ctrl + X` 退出

---

## 18. 最常用 Git 命令总结

```
git--version
git config--global--list
git init
git status
git add README.md
git add .
git commit-m"message"
git log--oneline
gitdiff
git branch
git switch-c dev
git push
git pull
```

---

## 19. 今天完成的学习任务

### 学了什么

- Git 是什么
- GitHub 是什么
- 仓库、commit、branch、push/pull 的概念
- WSL 常用命令

### 做了什么

- 配置 Git 用户名和邮箱
- 创建 GitHub 仓库 `ai-agent-learning`
- 在 WSL 里 clone 下来
- 新建：
    - `notes/`
    - `projects/`
    - `weekly_review/`
- 创建 `README.md`
- 创建 `notes/week1_day1_git_wsl.md`
- 完成第一次 commit 和 push

---

## 20. 我现在的理解

- Git 是本地版本管理工具
- GitHub 是远程代码仓库平台
- commit 是一次本地存档
- push 是上传到 GitHub
- pull 是从 GitHub 下载更新
- branch 是独立开发线
- WSL 是 Windows 里的 Linux 环境

---

## 21. 下一步建议学习内容

下一阶段建议继续学习：

1. `branch` 分支创建与切换
2. `merge` 合并分支
3. 解决冲突 conflict
4. Pull Request 基础
5. 在 GitHub 上进行协作流程

---

## 22. 今日最重要的记忆版

### Git 工作流

```
git status
git add .
git commit-m"说明"
git push
```

### WSL 常用命令

```
pwd
ls
cd
mkdir-p
touch
cat
```

### 第一次推送

```
git add .
git commit-m"first commit"
git branch-M main
git push-u origin main
```