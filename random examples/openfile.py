arquivo = open ("arquivo.txt")

textocompleto = arquivo.read()
print (textocompleto)


linhas = arquivo.readlines()
for linha in linhas:
    print (linha)
