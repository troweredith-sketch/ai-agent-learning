# Week 1 Day 2 - Linux / WSL 基础命令

---

## **今日主题**

- Linux / WSL 常用命令
- 相对路径与绝对路径
- 文件权限基础概念
- 环境变量基础概念
- 在 Git 仓库里提交 Day02 练习文件

---

## **1. 常用命令总结**

### **`pwd`**

显示当前所在目录。

### `ls`

查看当前目录下有哪些文件和文件夹。

```
ls
ls -l
ls -la
```

- `ls`：普通查看
- `ls -l`：查看详细信息
- `ls -la`：查看详细信息，并显示隐藏文件

隐藏文件通常以 `.` 开头，例如：

```
.git
.bashrc
.gitignore
```

---

### `cd`

切换目录。

```
cd notes
cd ..
cd ~
```

- `cd notes`：进入 `notes` 目录
- `cd ..`：回到上一级目录
- `cd ~`：回到家目录

---

### `mkdir`

创建目录。

```
mkdir test
mkdir -p linux-practice/day2
```

### `p` 的作用

- `p` 表示：

> 递归创建目录，并且目录已存在时不报错
> 

例如：

```
mkdir -p linux-practice/day2
```

意思是：

- 如果 `linux-practice` 不存在，就先创建它
- 再创建 `day2`
- 如果已经存在，也不会报错

可以把 `-p` 记成：

> parents，把父目录一起创建好
> 

---

### `rm`

删除文件或目录。

```
rm a.txt
rm -r notes
rm -rf temp
```

- `rm a.txt`：删除文件
- `rm -r notes`：删除目录
- `rm -rf temp`：强制递归删除目录

注意：

> `rm` 删除后通常不会进回收站，所以要非常小心，尤其是 `rm -rf`
> 

---

### `cp`

复制文件或目录。

```
cp a.txt b.txt
cp a.txt notes/
cp -r dir1 dir2
```

- `cp a.txt b.txt`：复制文件并改名
- `cp a.txt notes/`：复制到目录
- `cp -r dir1 dir2`：复制目录

---

### `mv`

移动文件，也可以重命名。

```
mv a.txt notes/
mv old.txt new.txt
```

- `mv a.txt notes/`：移动文件
- `mv old.txt new.txt`：重命名文件

理解重点：

> `mv` 既可以移动，也可以改名
> 

---

### `cat`

查看文件内容。

```
cat README.md
```

也可以配合重定向写入内容。

```
echo "hello linux" > a.txt
cat a.txt
```

---

## 2. 创建文件的方法

### 方法 1：创建空文件

```
touch a.txt
```

---

### 方法 2：创建文件并写入一行内容

```
echo "hello" > a.txt
```

`>` 表示覆盖写入。

---

### 方法 3：追加内容

```
echo "more content" >> a.txt
```

`>>` 表示追加。

---

### 方法 4：手动输入多行

```
cat > a.txt
```

输入内容后，按：

```
Ctrl + D
```

保存结束。

---

## 3. 相对路径与绝对路径

### 绝对路径

从根目录 `/` 开始写的完整路径。

例如：

```
/home/mr/ai-agent-learning/notes
```

特点：

> 不管当前在哪，都能准确找到这个位置
> 

---

### 相对路径

相对于当前目录的位置。

例如当前目录是：

```
/home/mr/ai-agent-learning
```

进入 `notes`：

```
cd notes
```

这里的 `notes` 就是相对路径。

---

### 常见符号

- `.`：当前目录
- `..`：上一级目录
- `~`：家目录

例如：

```
cd ..
cd ~
cat ./README.md
ls ..
```

---

## 4. 文件权限基础概念

用下面命令查看权限：

```
ls -l
```

可能会看到：

```
-rw-r--r-- 1 mr mr 120 Apr 8 10:00 README.md
```

最前面的：

```
-rw-r--r--
```

就是权限信息。

---

### 三类身份

- `u`：user，文件拥有者
- `g`：group，所属组
- `o`：others，其他人

---

### 三种权限

- `r`：read，读
- `w`：write，写
- `x`：execute，执行

---

### 例子理解

```
-rw-r--r--
```

表示：

- ：普通文件
- `rw-`：拥有者可读可写
- `r--`：组用户只读
- `r--`：其他人只读

如果开头是 `d`，说明它是目录，例如：

```
drwxr-xr-x
```

现阶段先记住：

> Linux 通过权限控制谁能读、写、执行文件
> 

---

## 5. 环境变量基础概念

环境变量可以理解为：

> shell 和系统运行时会使用的一些配置值
> 

---

### 常见环境变量

### `HOME`

家目录：

```
echo $HOME
```

---

### `USER`

当前用户名：

```
echo $USER
```

---

### `PWD`

当前目录：

```
echo $PWD
```

---

### `PATH`

命令查找路径：

```
echo $PATH
```

例如输出：

```
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

意思是：

> 当你输入 `git`、`python`、`ls` 这些命令时，系统会去这些目录里找对应程序
> 

一句话记忆：

> `PATH` 决定系统去哪里找命令
> 

---

## 6. Day02 Linux 练习流程

### 创建练习目录

```
cd ~
mkdir -p linux-practice/day2
cd linux-practice/day2
```

---

### 创建目录

```
mkdir notes temp
```

---

### 创建文件

```
echo "Linux command practice" > intro.txt
echo "Today I learned ls cd pwd mkdir rm cp mv cat" > notes/day2.txt
```

---

### 查看内容

```
cat intro.txt
cat notes/day2.txt
```

---

### 复制文件

```
cp intro.txt intro_backup.txt
```

---

### 移动文件

```
mv intro_backup.txt temp/
```

---

### 重命名文件

```
mv intro.txt readme.txt
```

---

### 复制目录

```
cp -r notes notes_copy
```

---

### 删除文件和目录

```
rm readme.txt
rm -r notes_copy
rm -r temp
```

---

## 7. 20 分钟练习目标

今天练习的重点不是“看懂”，而是“不查教程自己敲”。

建议反复练以下操作：

- 创建目录
- 创建文件
- 查看目录
- 复制文件
- 移动文件
- 重命名文件
- 删除文件
- 删除目录
- 使用相对路径
- 使用绝对路径

---

## 8. Git 相关补充：如何提交 Day02 练习文件

在 Git 里，不是“提交文件夹”，而是：

> 提交文件夹里的文件变化
> 

---

### 查看当前状态

```
git status
```

---

### 一个一个添加并提交

例如分别提交不同文件：

```
git add README.md
git commit -m "docs: update README"

git add .gitignore
git commit -m "chore: add .gitignore"

git add notes/week1_day2_linux_basic.md
git commit -m "docs: add week1 day2 linux basic notes"
```

重点理解：

- `git add`：把内容放进暂存区
- `git commit`：把暂存区内容正式提交

所以：

> 想一个一个提交，就每次只 `git add` 你想提交的文件
> 

---

### 提交整个 Day02 目录

```
git add projects/day02-linux-practice
git commit -m "feat: add day02 linux practice"
```

这表示：

> 把 `projects/day02-linux-practice` 目录下的文件变化加入暂存区并提交
> 

---

### `git add projects/day02-linux-practice` 和 `git add projects` 的区别

### 1）更精确的写法

```
git add projects/day02-linux-practice
```

只会加入这个目录下面的改动。

---

### 2）更大的范围

```
git add projects
```

会把整个 `projects/` 目录下的改动都加入暂存区。

---

### 什么时候两者看起来一样

如果当前 `projects/` 下面只有一个子目录：

```
projects/
└── day02-linux-practice/
```

那它们当前效果可能一样。

但从习惯上说，更推荐：

```
git add projects/day02-linux-practice
```

因为范围更明确。

---

### 为什么第一次不能直接 `git push`

第一次推送时，Git 往往还不知道当前分支要推到哪里，所以通常要先执行：

```
git push -u origin main
```

以后建立好追踪关系后，就可以直接：

```
git push
```

---

## 9. 今日最常用命令速查表

### 目录与路径

```
pwd
ls
ls -la
cd notes
cd ..
cd ~
```

### 创建

```
mkdir test
mkdir -p a/b/c
touch a.txt
```

### 文件内容

```
cat a.txt
echo "hello" > a.txt
echo "world" >> a.txt
```

### 复制

```
cp a.txt b.txt
cp a.txt notes/
cp -r dir1 dir2
```

### 移动 / 重命名

```
mv a.txt notes/
mv old.txt new.txt
```

### 删除

```
rm a.txt
rm -r notes
rm -rf temp
```

### 环境变量

```
echo $HOME
echo $USER
echo $PWD
echo $PATH
```

### Git

```
git status
git add 文件名
git add 目录名
git commit -m "message"
git push
```

---

## 10. 今日最重要的理解

1. `pwd` 用来确认自己当前在哪
2. `ls` 用来看当前目录里有什么
3. `mv` 既能移动文件，也能给文件改名
4. `mkdir -p` 会连父目录一起创建
5. 相对路径是相对于当前目录，绝对路径是完整路径
6. `PATH` 决定系统去哪里找命令
7. `rm -rf` 很危险，删除前要确认路径
8. Git 想分开提交时，要每次只 `git add` 需要的文件
9. `git add projects/day02-linux-practice` 比 `git add projects` 更精确

---

## 11. 明日可继续学习的内容

建议下一步学习：

- `grep`
- `find`
- `chmod`
- `nano`
- Git branch / merge