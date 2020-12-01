from random import choice

import string

string.ascii_lowercase # abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 0123456789
string.punctuation # <=>?@[\]^_`{|}~.

tamanho = 10
valores = string.ascii_letters + string.digits + string.punctuation
senha = ''
for i in range(tamanho):
  senha += choice(valores)

print(senha)