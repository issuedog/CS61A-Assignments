# 语句（statements）是 Python 程序的最小执行单元。
# 复合语句（compound statements）是由一个或多个语句组成的语句。复合语句包含一个或多个子语句。结构如下：
#               ____________________________________
# <header>:                             |clause     | statement
#     <statement>           | suite     |           |
#     <statement>           |           |           |
#     ...       ____________|___________|           |
# <separating header>:                              |
#     <statement>                                   |
#     <statement>                                   |
#     ...                                           |
# ...           ____________________________________|

# 第一个header决定了复合语句的类型，后续的header决定了子语句的类型。


# ————————————————————————————————————————————————————————————————————————————————————————

# 介绍一下条件语句
# 好吧其实不用介绍了，甩一个例子就好了：
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# —————————————————————————————————————————————————————————————————————————————————————————

# 介绍一下迭代语句
# 迭代语句用于重复执行一段代码，直到满足某个条件为止。Python 中主要有两种迭代语句：for 语句和 while 语句。
i , total = 1, 0
while i <= 10:
    total += i
    i += 1

# ————————————————————————————————————————————————————————————————————————————————————————

# 关于断言检验（assertion）
# 断言（assertion）常被用来检验函数的输出是否与预期相同，以斐波那契函数为例：
# 在较小的文件中，检验函数可被附在同一文件中：

# =====定义函数=====
def fib(n):
    """计算第n个斐波那契数"""
    pred, curr = 0,1
    k=2
    while k<n:
        pred, curr = curr, pred+curr
        k = k+1
    return curr

# =====定义测试函数=====
def fib_test():
    assert fib(2) == 1 , 'The second Fibonacci number should be 1'
    assert fib(3) == 1 , 'The third Fibonacci number should be 1'
    assert fib(50) == 7778742049 , 'Error at the 50th Fibonacci number'
    print("ALL TESTS PASSED!")

# =====执行测试函数======
# 当运行该文件时，测试函数会被调用
# 如果 assert 失败，程序会在该处跳出 AssertionError 并停止输出
fib_test()

# 当源码文件较大时，常把校验函数放在同一目录下的相邻文件中，这里我们新建了一个Lecture3_test.py文件，同样放在note目录下
# 注意由于Lecture3_control.py中已经写过一个测试函数，故会出现两次通过提示，无需在意即可

# ———————————————————————————————————————————————————————————————————————————————————————————

# doctest
# 相信你已经在作业里见过它了，就是函数下面"""docstring"""那种，第一行用来描述这个函数的作用，下面是一行空行，然后可以是详细描述或是样例交互输出，例如：

def sum_naturals(n):
    """Return the sum of the first n natural numbers
    
    n should be a positive integer
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k<=n:
        total, k = total + k, k + 1
    return total

# 关于testmod()测试整个文档和run_docstring_examples()测试单个函数的操作参照书
