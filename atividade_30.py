# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return f"Aprovado com média {media:.2f}"
    else:
        return f"Reprovado com média {media:.2f}"
nota1 = 8
nota2 = 7.5
nota3 = 6.8

resultado = calcular_media(nota1, nota2, nota3)
print(resultado)

    