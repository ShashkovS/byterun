from byterun.pyvm2 import VirtualMachine
import dis


codes = [
########################################
"""
print('hello world')
""",
########################################
"""
a = 1
b = 2
c = a + b""",
########################################
"""
'foo'.replace('o', '')
""",
########################################
"""
out = ""
for i in range(5):
    out = out + str(i)
print(out)
""",
########################################
"""
def foofunc():
    x = 1
    return x + 2
z = foofunc() + 3
print(z)
""",
########################################
"""
def foo(a, b, c):
    def boo():
        x = a
        y = b
        def zoo(z):
            return z + x + y + c
        return zoo
    return boo
print(foo(1, 2, 3)()(7))
""",
########################################
]

for code in codes:
    print('v'*150)
    print(code.strip())
    print('*'*50)
    vm = VirtualMachine()
    bytecode = compile(code, "<simple_example>", "exec", 0, 1)
    dis.dis(bytecode)
    print('*'*50)
    vm.run_code(bytecode)
    print('^'*150)
