def xoa_phan_tu_tu_dict(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary

# Ví dụ sử dụng
tu_dien_mau = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_can_xoa = 'b'
result = xoa_phan_tu_tu_dict(tu_dien_mau, key_can_xoa)
if result:
    print(f"Phần tử đã được xoá từ Dictionary: {result}")
else:
    print(f"Không tìm thấy phần tử cần xoá trong Dictionary")