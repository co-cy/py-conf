from config import FuncArgConfig


def print_arg(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)
    print()


print_arg(**FuncArgConfig())

print_arg(**FuncArgConfig(arg_1="123"))

print_arg(**FuncArgConfig("first", "second"))

FuncArgConfig.__new_arg_1__()
print_arg(**FuncArgConfig())

print("Simple dict:", FuncArgConfig())