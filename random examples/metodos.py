seq = "ASDLJFASKDJFKL"

print (seq)
print (seq.lower())
print (seq.upper())

seq = "   minha mae adora flores amarelas  "

print (seq)
print (seq.lower())
print (seq.upper())
print (seq.strip())
print (seq.split(" ")) # se eu não indicar o caractere de separação ele faz por espaço
print (seq.split("m")) # fez o split por letras m

busca = seq.find("mae") #procura a palavra e mostra a posição dela
print (busca)
print (seq[busca:]) #imprime o valor a partir da palavra encontrada

print (seq.replace("minha mae","meu pai"))