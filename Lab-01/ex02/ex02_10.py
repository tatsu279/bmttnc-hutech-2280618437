def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]


input_str = input("Nhập vào 1 chuỗi: ")
print("Chuỗi đảo ngược: ", dao_nguoc_chuoi(input_str))