
nome = input("nome do aluno: ")
nota1 = int(input("primeira nota"))
nota2 = int(input("segunda nota"))
nota3 = int(input("terceira nota"))
media = (nota1+nota2+nota3)/3
print(nome)
if(media<=5):print('Reprovado')
elif(media>=7):print("Aprovado")
else:print("Recuperação")