## 今天学了什么

今天主要学习了 Git 最常见的一组日常操作：

- `git status`
- `git add`
- `git commit`
- `git log`
- `git branch`
- `git checkout`

还学习了：

- commit 信息怎么写更清楚
- 如何新建分支并在分支里修改代码
- 如何把分支 merge 回主分支
- 如何查看 commit 历史
- 合并后的分支要不要删除，以及怎么删除

---

## 一、今天最核心的理解

今天学的不是单个命令，而是一套最常见的 Git 工作流：

**查看状态 → 修改文件 → add → commit → 新建分支 → 在分支开发 → merge 回 main → 查看历史**

一句话理解：

> Git 不只是“保存代码”，而是在管理你的开发过程。
> 

---

## 二、常用命令总结

### 1. `git status`

作用：

> 查看当前仓库状态
> 

它可以告诉你：

- 当前在哪个分支
- 有没有修改过的文件
- 哪些文件已经暂存
- 哪些文件还没暂存
- 有没有新文件
- 有没有被删除的文件

这是最常用的命令。

现阶段最重要的习惯是：

> 一旦不确定当前状态，先敲 `git status`
> 

---

### 2. `git add`

作用：

> 把改动加入暂存区，准备提交
> 

例如：

```
git add README.md
```

表示只暂存 `README.md`

```
git add .
```

表示把当前目录下的改动都加入暂存区

```
git add -A
```

表示把新增、修改、删除全部加入暂存区

重要理解：

> `git add` 不是提交，它只是“把这次要提交的内容挑出来”
> 

---

### 3. `git commit`

作用：

> 把暂存区内容正式记录到本地历史中
> 

例如：

```
git commit -m "docs: update README"
```

commit 可以理解成：

> 给当前代码状态拍一张快照，并写一句说明
> 

---

### 4. `git log`

作用：

> 查看提交历史
> 

常用命令：

```
git log
git log --oneline
git log --oneline -5
```

推荐现阶段优先使用：

```
git log --oneline
```

因为更简洁，更适合快速看历史。

---

### 5. `git branch`

作用：

> 查看、创建、管理分支
> 

查看当前分支：

```
git branch
```

创建分支：

```
git branch feature/day5-readme-update
```

---

### 6. `git checkout`

作用：

> 切换分支，或者创建并切换到新分支
> 

切换到已有分支：

```
git checkout main
```

创建并切换到新分支：

```
git checkout -b feature/day5-readme-update
```

这条命令同时做了两件事：

1. 创建新分支
2. 切换到这个新分支

---

## 三、什么是分支

分支可以理解成：

> 一条独立的开发线
> 

例如：

- `main`：主分支
- `feature/day5-readme-update`：专门用于修改 README 的功能分支

这样做的好处是：

- 可以先在分支里改，不影响主分支
- 改好了再 merge 回主分支
- 更安全，也更接近真实开发方式

一句话理解：

> 分支就是一个安全的开发试验区。
> 

---

## 四、什么是 merge

`git merge` 的作用是：

> 把另一个分支上的改动合并到当前分支
> 

例如：

```
git checkout main
git merge feature/day5-readme-update
```

意思是：

> 把 `feature/day5-readme-update` 这个分支上的改动合并到 `main`
> 

如果没有冲突，Git 会自动合并成功。

---

## 五、commit 信息怎么写

commit 信息不能总写成：

```
update
fix
修改
test
```

因为这种写法太模糊，过几天自己都看不懂。

更好的写法是：

> 写清楚“做了什么”
> 

例如：

```
docs: update README for day5 workflow practice
feat: add project structure
fix: correct import path
chore: update gitignore
```

---

## 六、常见 commit 前缀

### `docs:`

文档相关修改

例如：

```
docs: update week1 day5 git workflow notes
```

### `feat:`

新增功能

例如：

```
feat: add day5 practice branch workflow
```

### `fix:`

修复问题

例如：

```
fix: correct README typo
```

### `chore:`

杂项、维护类修改

例如：

```
chore: remove unused file
```

---

## 七、今天练习的标准工作流

今天的练习流程是：

### 1）先查看状态

```
git status
```

### 2）查看当前分支

```
git branch
```

### 3）创建并切换到新分支

```
git checkout -b feature/day5-readme-update
```

### 4）修改 README

### 5）查看状态

```
git status
```

### 6）暂存 README

```
git add README.md
```

### 7）提交修改

```
git commit -m "docs: update README for day5 workflow practice"
```

### 8）查看历史

```
git log --oneline
```

### 9）切回主分支

```
git checkout main
```

### 10）合并分支

```
git merge feature/day5-readme-update
```

### 11）再次查看历史

```
git log --oneline
```

---

## 八、至少 3 次 commit 可以怎么安排

今天的练习要求至少 3 次 commit，比较合理的拆法是：

### Commit 1

修改 README

```
docs: update README for day5 workflow practice
```

### Commit 2

新增今天的学习笔记

```
docs: add week1 day5 git workflow notes
```

### Commit 3

再补一次 README 或别的小修改

```
docs: refine README git workflow section
```

这样每次 commit 的内容都比较清晰。

---

## 九、如果不小心 `git add -A` 了怎么办

如果你把全部改动都 add 进暂存区了，但还没 commit，可以撤回暂存：

```
git restore --staged .
```

或者：

```
git reset
```

作用都是：

> 取消暂存，但不会删除你的实际修改内容
> 

---

## 十、如果项目里有删除的文件，Git 要怎么处理

分两种情况。

### 情况 1：你就是想把删除提交进去

这时可以：

```
git add -A
git commit -m "remove unused files"
```

因为 `git add -A` 会把新增、修改、删除一起加入暂存区。

---

### 情况 2：你删错了，不想删

这时可以恢复文件：

```
git restore 文件名
```

例如：

```
git restore README.md
```

---

## 十一、合并后的分支要不要删除

不是必须删，但通常建议删除已经合并完成、以后不会再继续开发的分支。

原因：

- 分支列表更干净
- 不容易混乱
- 更符合完整 Git 工作流习惯

---

## 十二、怎么删除分支

### 删除本地分支

先切回主分支：

```
git checkout main
```

然后删除本地分支：

```
git branch -d feature/day5-readme-update
```

这里的 `-d` 表示安全删除。

如果 Git 发现这个分支没合并，通常会阻止你删掉。

---

### 强制删除本地分支

如果你非常确定这个分支不要了，可以：

```
git branch -D feature/day5-readme-update
```

这里的 `-D` 表示强制删除，要小心使用。

---

## 十三、为什么本地删了分支，GitHub 上还在

因为：

- 本地分支和远程分支是分开的
- 删除本地分支，不会自动删除 GitHub 上的远程分支

所以你本地删完后，GitHub 上可能还保留着这个分支。

---

## 十四、怎么删除 GitHub 上的远程分支

执行：

```
git push origin --delete feature/day5-readme-update
```

意思是：

> 删除远程仓库 `origin` 上的这个分支
> 

---

## 十五、如果远程删了，本地还显示旧的远程分支怎么办

刷新远程分支缓存：

```
git fetch -p
```

或者：

```
git remote prune origin
```

作用是：

> 清理本地记录里已经不存在的远程分支信息
> 

---

## 十六、查看分支的常用命令

查看本地分支：

```
git branch
```

查看远程分支：

```
git branch -r
```

查看所有分支：

```
git branch -a
```

---

## 十七、今天最重要的理解

1. `git status` 是最常用的状态查看命令
2. `git add` 是暂存，不是提交
3. `git commit` 才是正式记录历史
4. 分支是独立开发线
5. `git checkout -b xxx` 表示创建并切换到新分支
6. `git merge` 是把分支上的修改合并回来
7. `git log --oneline` 很适合快速查看历史
8. commit 信息要尽量写清楚“做了什么”
9. 已经合并完成的分支通常建议删除
10. 删除本地分支不会自动删除 GitHub 上的远程分支

---

## 十八、今天的最简工作流总结

```
git status
git checkout -b feature/day5-readme-update
git add README.md
git commit -m "docs: update README for day5 workflow practice"
git checkout main
git merge feature/day5-readme-update
git log --oneline
```

如果练习结束后想清理分支：

```
git branch -d feature/day5-readme-update
git push origin --delete feature/day5-readme-update
git fetch -p
```

---

## 十九、今天下课前应该能回答的问题

1. `git status` 是干什么的？
2. `git add` 和 `git commit` 的区别是什么？
3. 分支是什么？
4. `git checkout -b xxx` 做了什么？
5. `git merge` 是干什么的？
6. commit 信息为什么不能总写 `update`？
7. 本地删分支后，为什么 GitHub 上还在？
8. 删除远程分支的命令是什么？

---

## 二十、一句话总结 Day 5

> Day 5 学的是 Git 最基础也最重要的工作流：在分支中开发、提交、合并，并通过清晰的 commit 历史管理自己的代码变化。
>