from Lecture3_control import fib

# =====测试函数====
def fib_test():
    assert fib(2) == 1 , 'The second Fibonacci number should be 1'
    assert fib(3) == 1 , 'The third Fibonacci number should be 1'
    assert fib(50) == 7778742049 , 'Error at the 50th Fibonacci number'
    print("ALL TESTS PASSED!")

# 执行测试
if __name__ == '__main__':
    fib_test()

# if __name__ == '__main__'   是一个python 惯例，意思是“只有当这个文件被直接运行时，才执行下面的代码”。这是防止测试代码在被意外导入时自动运行的好习惯