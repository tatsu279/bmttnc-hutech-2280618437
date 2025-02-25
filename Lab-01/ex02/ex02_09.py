def kiem_tra_so_nt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
number = int(input("Nhập vào 1 số: "))
if kiem_tra_so_nt(number):
    print(f"{number} là số nguyên tố.")
else:
    print(f"{number} không phải là số nguyên tố.")