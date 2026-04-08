# Week 1 Day 2 - Linux / WSL 基础命令

## 今天学了什么

### 常用命令
- `ls`：查看目录内容
- `cd`：切换目录
- `pwd`：显示当前路径
- `mkdir`：创建目录
- `rm`：删除文件或目录
- `cp`：复制文件或目录
- `mv`：移动文件或重命名
- `cat`：查看文件内容

### 路径
- 绝对路径：从 `/` 开始的完整路径
- 相对路径：相对于当前目录的路径
- `.` 表示当前目录
- `..` 表示上一级目录
- `~` 表示家目录

### 文件权限
- `r`：读
- `w`：写
- `x`：执行
- `ls -l` 可以查看权限信息

### 环境变量
- `HOME`：家目录
- `USER`：用户名
- `PWD`：当前路径
- `PATH`：命令查找路径

## 今天做了什么

- 在 WSL 中手动创建目录和文件
- 练习了复制、移动、重命名、删除
- 理解了相对路径和绝对路径
- 初步认识了权限和环境变量

## 练习命令

```bash
pwd
ls
ls -la
mkdir notes
echo "hello" > a.txt
cp a.txt b.txt
mv b.txt notes/
cat notes/b.txt
rm a.txt
rm -r notes

## Linux 命令速查表

### 目录与路径
```bash
pwd              # 显示当前目录
ls               # 查看当前目录内容
ls -la           # 查看详细内容（含隐藏文件）
cd notes         # 进入 notes 目录
cd ..            # 返回上一级目录
cd ~             # 回到家目录