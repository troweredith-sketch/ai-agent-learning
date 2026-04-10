# Python 面向对象笔记

## 一、面向对象简介

### 1. 什么是面向对象

面向对象编程，英文叫 **OOP（Object-Oriented Programming）**。

它的核心想法是：

**把现实世界中的事物，抽象成“对象”，再让对象之间配合完成任务。**

比如在程序里可以有：

- 人 `Person`
- 狗 `Dog`
- 银行卡 `BankAccount`
- 学生 `Student`

这些“对象”通常都有两类东西：

- **属性**：这个对象有什么数据
- **行为**：这个对象能做什么事

例如：

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} 在叫")
```

这里：

- `name` 是属性
- `bark()` 是行为

---

### 2. 为什么要学面向对象

因为当程序越来越大时，单纯写一堆函数会越来越乱。

面向对象的好处主要是：

- 把数据和方法组织在一起
- 代码更接近现实建模
- 更容易复用和扩展
- 更适合多人协作和大型项目

---

### 3. 面向对象的几个核心概念

你学 Python 面向对象，最重要的是这几个：

- **类（class）**
- **对象 / 实例（object / instance）**
- **封装**
- **继承**
- **多态**
- **抽象**

这几个概念后面会一个个讲。

---

## 二、类和对象

### 1. 类是什么

类可以理解成：

**模板、图纸、规范**

比如：

```python
class Dog:
    pass
```

这里 `Dog` 只是“狗这个类别”的定义，还不是某一只具体的狗。

---

### 2. 对象是什么

对象，也叫实例，就是：

**按照类这个模板创建出来的具体东西**

```python
d1 = Dog()
d2 = Dog()
```

这里：

- `Dog` 是类
- `d1`、`d2` 是对象

可以理解成：

- 类 = 图纸
- 对象 = 按图纸造出来的实物

---

### 3. 类和对象的关系

可以这样记：

- 类是抽象的
- 对象是具体的
- 一个类可以创建很多个对象

例如：

```python
class Person:
    pass

p1 = Person()
p2 = Person()
```

`Person` 是类，`p1` 和 `p2` 是两个具体的人对象。

---

## 三、定义类的格式

Python 中常见的类定义格式有这些。

### 1. 最基础写法

```python
class Person:
    pass
```

这是最推荐的新式写法。

---

### 2. 带空括号写法

```python
class Person():
    pass
```

在 Python 3 中，这和上面通常没有本质区别。现在更常见的是不写空括号。

---

### 3. 继承写法

```python
class Student(Person):
    pass
```

表示 `Student` 继承了 `Person`。

---

### 4. 多继承写法

```python
class Child(Father, Mother):
    pass
```

表示一个类同时继承多个父类。

---

### 5. 推荐记法

平时最常见的是这两种：

```python
class 类名:
    ...
```

```python
class 子类(父类):
    ...
```

---

## 四、创建对象与访问类中行为

### 1. 创建对象

创建对象就是“调用类”。

```python
class Person:
    pass

p = Person()
```

这里：

- `Person` 是类
- `Person()` 是创建对象
- `p` 是对象变量

---

### 2. 定义对象属性和方法

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"你好，我是{self.name}")
```

---

### 3. 访问对象属性

```python
p = Person("小明")
print(p.name)
```

---

### 4. 调用对象方法

```python
p.say_hi()
```

---

### 5. 类.方法() 和 实例.方法() 的区别

先看普通实例方法：

```python
class Person:
    def say_hi(self):
        print("你好")
```

实例调用：

```python
p = Person()
p.say_hi()
```

这是最常见的。

类调用：

```python
Person.say_hi(p)
```

这也可以，但需要你手动传入对象 `p`。

所以对于普通实例方法：

- `实例.方法()`：Python 自动传入实例给 `self`
- `类.方法(实例)`：你自己手动传实例

---

## 五、self 关键字

### 1. self 是什么

`self` 表示：

**当前对象自己**

例如：

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"你好，我是{self.name}")
```

这里：

- `self.name` 表示当前对象自己的名字
- `self` 不是关键字，只是约定俗成的写法，但几乎所有人都这么写

---

### 2. 为什么方法里要写 self

因为实例方法调用时，Python 会把调用该方法的对象自动传进去。

```python
p.say_hi()
```

大致可以理解成：

```python
Person.say_hi(p)
```

所以方法定义时，第一个参数就用 `self` 接住这个对象。

---

### 3. 什么时候要写 self

当这个方法要访问对象自己的属性或其他实例方法时，就要写 `self`。

例如：

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name)
```

---

### 4. 什么时候不用 self

主要有两种：

- 类方法用 `cls`
- 静态方法不用 `self` 也不用 `cls`

后面会详细讲。

---

## 六、对象属性和类属性

### 1. 对象属性

对象属性一般定义在 `__init__` 中，使用 `self.xxx`。

```python
class Person:
    def __init__(self, name):
        self.name = name
```

每个对象有自己独立的一份：

```python
p1 = Person("小明")
p2 = Person("小红")

print(p1.name)  # 小明
print(p2.name)  # 小红
```

---

### 2. 类属性

类属性定义在类中、方法外。

```python
class Person:
    country = "中国"

    def __init__(self, name):
        self.name = name
```

类属性是整个类共享的：

```python
p1 = Person("小明")
p2 = Person("小红")

print(p1.country)
print(p2.country)
print(Person.country)
```

---

### 3. 二者区别

对象属性：

- 属于具体对象
- 每个对象一份
- 一般用 `self.xxx`

类属性：

- 属于类本身
- 所有对象默认共享
- 一般写在类体中

---

### 4. 一个常见陷阱

看这段：

```python
class Person:
    country = "中国"

    def __init__(self, name):
        self.name = name
```

然后：

```python
p1 = Person("小明")
p2 = Person("小红")

p1.country = "英国"
```

这不是修改类属性，而是给 `p1` 新增了一个同名对象属性。

此时：

```python
print(p1.country)      # 英国
print(p2.country)      # 中国
print(Person.country)  # 中国
```

---

### 5. 可变类属性要小心

例如：

```python
class A:
    items = []
```

所有对象会共用这一个列表。

```python
a1 = A()
a2 = A()

a1.items.append(1)
print(a2.items)  # [1]
```

如果你想让每个对象有自己的列表，应该写到 `__init__` 中：

```python
class A:
    def __init__(self):
        self.items = []
```

## 七、构造方法与对象初始化

### 1. `__init__` 是什么

`__init__` 是最常见的魔法方法之一，叫构造初始化方法。

当对象创建后，它会自动执行。

```python
class Person:
    def __init__(self, name):
        self.name = name
```

```python
p = Person("小明")
```

这里 `__init__` 会自动执行。

---

### 2. 默认参数

可以给参数设置默认值：

```python
class Person:
    def __init__(self, name="匿名", age=18):
        self.name = name
        self.age = age
```

使用：

```python
p1 = Person("小明", 20)
p2 = Person()
p3 = Person("小红")
```

---

### 3. 一个必传，一个默认

例如：

```python
class Student:
    def __init__(self, name, score=60):
        self.name = name
        self.score = score
```

这里：

- `name` 必传
- `score` 可传可不传

---

### 4. 可变对象默认参数要小心

不要这样写：

```python
class A:
    def __init__(self, items=[]):
        self.items = items
```

更安全的是：

```python
class A:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items
```

---

## 八、封装

### 1. 什么是封装

封装就是：

**把数据和操作这些数据的方法，放到一个类中，并尽量限制外部直接乱改内部细节。**

例如银行卡：

- 有余额
- 能存钱
- 能取钱
- 能查余额

外部最好不要直接修改余额，而应该通过类提供的方法来操作。

---

### 2. 封装的基本例子

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, money):
        if money > 0:
            self._balance += money

    def withdraw(self, money):
        if 0 < money <= self._balance:
            self._balance -= money

    def get_balance(self):
        return self._balance
```

---

### 3. Python 中的“公开 / 受保护 / 私有”

Python 没有像 Java 那样严格的访问权限控制，但有约定。

### 公开属性

```python
self.name
```

表示公开，外部可以正常访问。

### 单下划线属性

```python
self._balance
```

表示“内部属性，外部尽量别直接碰”。

### 双下划线属性

```python
self.__balance
```

表示更强的内部属性，Python 会进行名字改写。

---

### 4. `@property` 实现更好的封装

很多时候，我们希望：

- 外面看起来像普通属性
- 内部却能做校验逻辑

例如：

```python
class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能小于 0")
        self._age = value
```

这样外部使用时：

```python
p = Person(18)
print(p.age)
p.age = 20
```

看起来像操作属性，但背后其实执行了方法逻辑。

---

### 5. 封装的好处

封装的主要作用：

- 保护数据
- 统一操作方式
- 隐藏内部实现细节
- 后续更容易维护

---

## 九、继承

### 1. 什么是继承

继承就是：

**子类获得父类的属性和方法**

例如：

```python
class Person:
    def eat(self):
        print("吃东西")

class Student(Person):
    pass
```

这里 `Student` 继承了 `Person`，所以 `Student` 的对象也能调用 `eat()`。

---

### 2. 单继承

```python
class Animal:
    def eat(self):
        print("吃东西")

class Dog(Animal):
    def bark(self):
        print("汪")
```

`Dog` 同时拥有：

- 自己的 `bark()`
- 从 `Animal` 继承来的 `eat()`

---

### 3. 多层继承

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass
```

`C` 继承 `B`，`B` 继承 `A`，所以 `C` 也间接拥有 `A` 的内容。

---

### 4. 多继承

```python
class Father:
    def money(self):
        print("有财富")

class Mother:
    def love(self):
        print("有爱")

class Child(Father, Mother):
    pass
```

`Child` 同时继承两个父类。

---

### 5. 方法查找顺序

调用方法时，Python 会按一定顺序查找，这个顺序叫 **MRO**（方法解析顺序）。

例如：

```python
class A:
    def hello(self):
        print("A")

class B(A):
    pass

class C(B):
    pass
```

调用：

```python
c = C()
c.hello()
```

查找顺序大致是：

- 先找 `C`
- 再找 `B`
- 再找 `A`

---

## 十、super()

### 1. super() 是什么

`super()` 常用于子类中调用父类的方法。

最常见的是调用父类的 `__init__`：

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
```

这里：

```python
super().__init__(name)
```

表示：先执行父类的初始化逻辑。

---

### 2. 为什么要用 super()

因为子类往往只负责自己的新增部分，父类负责公共部分。

上例中：

- `Person` 负责 `name`
- `Student` 负责 `grade`

---

### 3. super() 在多继承中的意义

在多继承中，`super()` 不是简单地“去直接父类”，而是沿着 MRO 往后找下一个类。

这也是为什么多继承场景下更推荐用 `super()`，而不是手写父类名。

---

## 十一、多态

### 1. 什么是多态

多态就是：

**同样的调用方式，对不同对象会产生不同的行为。**

例如：

```python
class Dog:
    def speak(self):
        print("汪汪")

class Cat:
    def speak(self):
        print("喵喵")
```

```python
d = Dog()
c = Cat()

d.speak()
c.speak()
```

都是 `.speak()`，但输出不同，这就是多态。

---

### 2. 继承中的多态

```python
class Animal:
    def speak(self):
        print("动物发出声音")

class Dog(Animal):
    def speak(self):
        print("汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵")
```

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

这里统一调用 `animal.speak()`，但每个对象表现不同。

---

### 3. Python 中的鸭子类型

Python 中很多时候不强依赖继承，只要对象有相应的方法，就能使用。

```python
class Dog:
    def speak(self):
        print("汪汪")

class Person:
    def speak(self):
        print("你好")
```

```python
def make_sound(obj):
    obj.speak()
```

这里传 `Dog()` 也行，传 `Person()` 也行。

这体现了 Python 风格的多态。

---

### 4. 多态的好处

多态的价值主要体现在：

- 统一接口
- 少写 `if/else`
- 扩展方便
- 代码更通用

---

## 十二、魔法方法

### 1. 什么是魔法方法

魔法方法就是前后都有双下划线的方法，例如：

```python
__init__
__str__
__len__
__call__
```

它们也叫：

- 特殊方法
- dunder 方法

---

### 2. 魔法方法的作用

魔法方法的作用是：

**让你的对象支持 Python 的内置语法和行为。**

例如：

- `print(obj)` 会找 `__str__`
- `len(obj)` 会找 `__len__`
- `obj1 + obj2` 会找 `__add__`
- `obj[i]` 会找 `__getitem__`

---

### 3. 常见魔法方法

### `__init__`

初始化对象。

```python
class Person:
    def __init__(self, name):
        self.name = name
```

---

### `__str__`

定义 `print(obj)` 时显示的内容。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person({self.name})"
```

---

### `__repr__`

定义更偏调试用的显示形式。

```python
def __repr__(self):
    return f"Person('{self.name}')"
```

---

### `__len__`

定义 `len(obj)`。

```python
class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
```

---

### `__eq__`

定义 `==`。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
```

---

### `__call__`

让对象像函数一样调用。

```python
class Adder:
    def __call__(self, x, y):
        return x + y

a = Adder()
print(a(3, 4))
```

---

### `__getitem__`

定义下标访问 `obj[i]`。

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]
```

---

### 4. 魔法方法的学习建议

新手先掌握这些最够用：

- `__init__`
- `__str__`
- `__repr__`
- `__len__`
- `__eq__`
- `__getitem__`

记忆方式不要死背定义，而要按“触发场景”记：

- `print(obj)` → `__str__`
- `len(obj)` → `__len__`
- `obj[i]` → `__getitem__`
- `obj1 == obj2` → `__eq__`

---

## 十三、抽象类与抽象方法

### 1. 为什么需要抽象类

有些类只用来规定规范，不适合直接创建对象。

例如“动物”这个概念，所有动物都应该会 `speak()`，但父类层面不好统一实现。

---

### 2. 抽象类

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

这里：

- `Animal` 是抽象类
- 它不能直接实例化

---

### 3. 抽象方法

抽象方法表示：

**这个方法子类必须实现。**

```python
@abstractmethod
def speak(self):
    pass
```

---

### 4. 为什么要加 `@abstractmethod`

不加时：

```python
class Animal:
    def speak(self):
        pass
```

这只是普通空方法，子类不实现也不会报错。

加了之后：

- 子类如果不实现，就不能实例化
- 可以强制所有子类遵守接口规范

---

### 5. 抽象类和普通父类的区别

普通父类：

- 可以直接实例化
- 可以有普通方法

抽象类：

- 不能直接实例化
- 更像“定规范的模板”

---

### 6. 抽象类里也可以有普通方法

例如：

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def eat(self):
        print("吃东西")

    @abstractmethod
    def speak(self):
        pass
```

这里 `eat()` 是普通方法，`speak()` 是抽象方法。

## 十四、与面向对象有关的修饰器

### 1. 什么是修饰器语法

你看到的：

```python
@classmethod
@staticmethod
@property
```

本质上都是“把下面定义的函数加工一下”。

例如：

```python
@staticmethod
def add(x, y):
    return x + y
```

大致等价于：

```python
def add(x, y):
    return x + y

add = staticmethod(add)
```

---

### 2. 实例方法、类方法、静态方法

### 实例方法

最普通的方法，不需要修饰器。

```python
class Person:
    def say_hi(self):
        print("你好")
```

特点：

- 第一个参数是 `self`
- 操作对象自己的数据

---

### 类方法 `@classmethod`

```python
class Student:
    total = 0

    @classmethod
    def get_total(cls):
        return cls.total
```

特点：

- 第一个参数是 `cls`
- 操作类属性
- 常用于工厂方法、类级逻辑

---

### 静态方法 `@staticmethod`

```python
class MathTool:
    @staticmethod
    def add(x, y):
        return x + y
```

特点：

- 没有 `self`
- 没有 `cls`
- 只是放在类里的普通函数

---

### 3. `@property`

```python
class Person:
    @property
    def age(self):
        return self._age
```

作用：

**把一个方法变成“像属性一样访问”。**

原本要写：

```python
obj.get_age()
```

现在可以写成：

```python
obj.age
```

---

### 4. `@xxx.setter`

```python
class Person:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能小于 0")
        self._age = value
```

作用：

**给 property 配套定义赋值逻辑。**

外部写：

```python
p.age = 20
```

实际上会进入 setter。

---

### 5. `@xxx.deleter`

给 property 定义删除逻辑。

```python
@age.deleter
def age(self):
    del self._age
```

---

### 6. `@abstractmethod`

用于抽象方法。

```python
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def f(self):
        pass
```

---

### 7. 一个对比总结

面向对象里最常见的修饰器有：

- `@classmethod`
- `@staticmethod`
- `@property`
- `@xxx.setter`
- `@xxx.deleter`
- `@abstractmethod`

---

## 十五、类方法和静态方法再总结一次

这是容易混的地方，单独再收一遍。

### 1. 实例方法

```python
def func(self):
```

- 给对象用
- 用对象自己的数据

---

### 2. 类方法

```python
@classmethod
def func(cls):
```

- 给类用
- 用类自己的数据
- 常见用途：工厂方法、操作类属性

---

### 3. 静态方法

```python
@staticmethod
def func(...):
```

- 不依赖对象
- 不依赖类
- 只是逻辑上属于这个类

---

### 4. 判断口诀

可以直接背：

- **用对象** → 实例方法
- **用类** → 类方法
- **都不用** → 静态方法

---

## 十六、对象的引用、赋值与拷贝

这部分虽然不完全属于 OOP 概念，但和对象理解关系非常大。

### 1. Python 变量更像“引用”

```python
a = [1, 2, 3]
b = a
```

这不是复制，而是：

- `a` 指向列表对象
- `b` 也指向同一个列表对象

---

### 2. 赋值不是复制

```python
b = a
```

只是在共享同一个对象。

---

### 3. 浅拷贝

```python
b = a.copy()
```

只复制外层。

---

### 4. 深拷贝

```python
import copy

b = copy.deepcopy(a)
```

会递归复制整个对象结构。

---

### 5. 这对面向对象有什么帮助

因为你在处理对象时，经常会碰到：

- 两个变量是否指向同一个对象
- 修改一个对象会不会影响另一个变量
- 方法接收对象后到底是在改谁

理解“引用”和“拷贝”后，这些就不会乱。

---

## 十七、面向对象的常见学习误区

### 1. 把类当成函数用

类不是普通函数，它是对象模板。

---

### 2. 以为 `self` 是关键字

不是关键字，只是约定俗成的名字，但几乎必须按这个习惯写。

---

### 3. 分不清对象属性和类属性

记住：

- `self.xxx` 一般是对象属性
- 类体里的 `xxx = ...` 一般是类属性

---

### 4. 以为赋值就是复制

不是，很多时候只是多一个引用。

---

### 5. 滥用继承

继承很强大，但不是所有场景都必须用。

很多时候组合也比复杂继承更清晰。

---

### 6. 一开始就硬背所有魔法方法

不要。先学常用的，按触发场景记。

---

## 十八、推荐的学习顺序

建议按这个顺序学最稳：

1. 类和对象
2. `__init__`
3. `self`
4. 对象属性和类属性
5. 实例方法
6. 封装
7. 继承
8. `super()`
9. 多态
10. 类方法、静态方法、property
11. 魔法方法
12. 抽象类

---

## 十九、一个综合示例

下面这个例子把前面很多知识点串起来。

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    total = 0

    def __init__(self, name):
        self.name = name
        Animal.total += 1

    @classmethod
    def get_total(cls):
        return cls.total

    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("名字不能为空")
        self._name = value

    @abstractmethod
    def speak(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

class Dog(Animal):
    def speak(self):
        print("汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵")

d = Dog("旺财")
c = Cat("小黑")

print(d)  # __str__
print(c)

d.speak()  # 多态
c.speak()

print(Animal.get_total())           # 类方法
print(Animal.is_valid_name("Tom"))  # 静态方法
```

这个例子包含了：

- 抽象类
- 抽象方法
- 继承
- 多态
- 类属性
- 类方法
- 静态方法
- property
- 魔法方法 `__str__`

---

## 二十、最后的总总结

你可以用下面这组话把整套面向对象收住：

### 1. 类和对象

- 类是模板
- 对象是实例

### 2. 属性和方法

- 属性表示对象的数据
- 方法表示对象的行为

### 3. 封装

- 把数据和方法包在类里
- 控制外部访问方式

### 4. 继承

- 子类获得父类能力
- 用于复用和扩展

### 5. 多态

- 同样的调用方式
- 不同对象有不同表现

### 6. 抽象

- 抽象类定规范
- 抽象方法要求子类必须实现

### 7. 修饰器

- `@classmethod`：类方法
- `@staticmethod`：静态方法
- `@property`：把方法伪装成属性
- `@abstractmethod`：抽象方法

### 8. 魔法方法

- 让对象支持 Python 内置语法
- 常见有 `__init__`、`__str__`、`__len__` 等

---

## 二十一、适合新手的复习口诀

可以直接记这版：

- **类是图纸，对象是实物**
- **self 是当前对象**
- **对象属性各有各的，类属性大家共享**
- **封装是把数据和方法包起来**
- **继承是子类拿到父类的能力**
- **多态是同样调用，不同对象不同表现**
- **抽象类定规矩，子类来实现**
- **类方法用 cls，静态方法啥都不用**
- **property 让方法看起来像属性**
- **魔法方法是 Python 自动调用的特殊方法**