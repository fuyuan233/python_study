# Writer :fuyuan360
# Email  :fuyuan360@qq.com
def print_binary_numbers(n, current=""):
    if len(current) == n:
        print(current)
        return
    print_binary_numbers(n, current + "0")
    print_binary_numbers(n, current + "1")
print_binary_numbers(int(input("请输入一个数：")))