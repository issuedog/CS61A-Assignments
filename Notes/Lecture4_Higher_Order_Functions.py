# 我也不知道第一行要写什么......

# 高阶函数，可以理解为一般性的方法，概括性的方法，由此可以派生出各种具体方法。

# Example 1：计算图形面积
# 设边长为 r (圆的半径为 r)，那么可以导出各图形面积为：
# 正方形：r**2 ; 正六边形：3*sqrt(3)/2 * r**2; 圆：pi * r**2

# 那么与其一个个写各自的面积函数：

def area_square(r):
    assert r>0 , 'The length must be positive.'
    return r**2

from math import sqrt, pi
def area_hex(r):
    assert r>0 , 'The length must be positive.'
    return 3*sqrt(3)/2 * r**2

def area_hex(r):
    assert r>0 , 'The length must be positive.'
    return pi * r**2

# 更合理且规范的做法是提取它们的共同点并概括出一个“计算面积的公共部分”函数：

# “计算面积的公共部分”函数:
def area(r, const):
    assert r>0 , 'The length must be positive.'
    return r**2 * const

def area_square(r):
    return area(r, 1)

def area_hex(r):
    return area(r, 3*sqrt(3)/2)

def area_hex(r):
    return area(r, pi)

# 这就是高阶函数的一个体现，当然，如果有好好看书的的话，这也是 "DRY('don't repeat yourelf')" 的一个体现

# 当然，不只是数可以作为可变部分，某种运算过程也可以作为替换组件，以此带来更大的灵活性：

# Example 2 
# 几种不同数列的求和：

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

from operator import mul
def Ramanujan(k):
    return 8 / mul(4 * k - 3,4 * k - 1)

def summation(n ,term):
    """Returns the sum of different TERM
    
    >>> summation(5, identity)
    15
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

# 这里不同的数列项被打包成不同的项函数，在高阶函数 summation() 中用以替换 term() 

# Example 3
# 函数作为返回值

def make_adder(n):
    """Creates an adder funcion that adds N to any input number
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(3)(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# 通过函数 make_adder() ，我们制造了一个对输入加上 N 的一个函数，并将它作为返回值输出

# 由此，我们对函数和高阶函数有了更全面的认识：
# 1、函数是第一类值。这意味着它们可以被作为参数传递，可以作为返回值返回，就像其它值一样
# 2、高阶函数，或是将另一个函数作为参数，或是将函数作为返回值返回

#高阶函数有其意义：
# 1、表达了一般性的方法；
# 2、取消了重复性，契合DRY原则
# 3、将具体函数的工作重心分离出来，彰显其独有部分

# fin.