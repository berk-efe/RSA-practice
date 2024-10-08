from main import encrypt_data, decrypt_data

e = encrypt_data("ABC", (8447, 8633)) # 65, 66, 67
print(e)

d = decrypt_data(e, (16895, 8633))
print(d)