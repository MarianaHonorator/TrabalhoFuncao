n = 1
A = 'A.M'
P = 'P.M'

while n != 0:
    hora_add = 0
    min_passados = 0


    def conversao(hora, conversao):

        if hora <= 12:
            conversao = hora
            return conversao

        if hora > 24:
            conversao = hora - 24
            return conversao

        if hora > 11:
            conversao = (hora + 12) - 24
            return conversao


    def resultado(resultado):

        resultado = (f"Conversão: \033[7m{conversao(hora, conversao) + hora_add}:{min} {periodo}\033[m")
        return resultado


    hora = int(input("Digite a hora: "))

    if hora < 0:
        break

    min = int(input("Digite o minuto: "))

    if min < 0:
        print("Valor Inválido,Digite novamente!")
        continue



    if min >= 60:

        hora_add = int(min / 60)
        min_passados = min - (60 * hora_add)
        min = min_passados

    if hora <= 11:
        periodo = A

    else:
        periodo = P


    if hora == 0:
        hora_add = 12




    print(resultado(resultado))






