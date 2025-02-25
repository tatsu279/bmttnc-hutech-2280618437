def tao_tuple_tu_list(List):
    return tuple(List)

input_list = input("Nhập các phần tử của list, cách nhau bởi dấu phẩy: ")
number_list = list(map(int,input_list.split(',')))

# Chuyển đổi list thành tuple
output_tuple = tuple(number_list)

print("List được tạo từ bàn phím là:", number_list)
print("Tuple được tạo từ list là:", output_tuple)