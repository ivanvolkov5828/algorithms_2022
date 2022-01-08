from hashlib import pbkdf2_hmac
from binascii import hexlify

dct_url = dict()

def check_url(url):
    if url in dct_url.keys():
        print(f"Данная страница уже есть. Вот ее хэш: {dct_url[url]}")
    else:
        obj = pbkdf2_hmac(hash_name = 'sha512',
                          password = url.encode(),
                          salt = b'123456',
                          iterations = 1000
                          )
        param = hexlify(obj)
        dct_url[url] = param

n = int(input("Введите количество: "))
for i in range(n):
    url_f = input("Введите url: ")
    check_url(url_f)

print(dct_url)

