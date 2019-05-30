from byterun.pyvm2 import VirtualMachine
import dis
import types


def print_dis_code(bytecode):
    """Disassemble `code` and all the code it refers to."""
    for const in bytecode.co_consts:
        if isinstance(const, types.CodeType):
            print_dis_code(const)

    print("-"*20)
    dis.dis(bytecode)
    print("-"*20)


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
]

for code in codes:
    print('*'*150)
    print(code.strip())
    print('*'*50)
    vm = VirtualMachine()
    bytecode = compile(code, "<simple_example>", "exec", 0, 1)
    print_dis_code(bytecode)
    print('v'*50)
    vm.run_code(bytecode)
    print('^'*150)
