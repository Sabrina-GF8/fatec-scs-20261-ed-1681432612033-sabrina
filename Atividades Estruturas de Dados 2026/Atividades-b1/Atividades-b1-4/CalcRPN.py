def eh_numero(valor):
    """Verifica se o valor pode ser convertido para número"""
    try:
        float(valor)
        return True
    except ValueError:
        return False


def calculadora_rpn(expressao, mostrar_passos=False):
    pilha = []
    pilha_expr = []  # Pilha para a expressão algébrica

    # separar elementos
    elementos = expressao.split()

    for elemento in elementos:

        # se for número - empilhar
        if eh_numero(elemento):
            pilha.append(float(elemento))
            pilha_expr.append(elemento)

        # se for operador - calcular
        elif elemento in ['+', '-', '*', '/']:

            # 🔥 NOVO: verificar se há elementos suficientes
            if len(pilha) < 2:
                raise ValueError("Erro: elementos insuficientes na pilha")

            # remover topo da pilha (valor)
            x = pilha.pop()
            y = pilha.pop()

            # remover topo da pilha (expressão)
            x_expr = pilha_expr.pop()
            y_expr = pilha_expr.pop()

            # aplicar operação (Y (operador) X)
            if elemento == '+':
                resultado = y + x
            elif elemento == '-':
                resultado = y - x
            elif elemento == '*':
                resultado = y * x
            elif elemento == '/':
                if x == 0:
                    raise ZeroDivisionError("Erro: divisão por zero")
                resultado = y / x

            # montar expressão algébrica
            nova_expr = f"({y_expr} {elemento} {x_expr})"

            # empilhar resultado
            pilha.append(resultado)
            pilha_expr.append(nova_expr)

        else:
            raise ValueError(f"Operador inválido: {elemento}")

        # mostrar estado da pilha
        if mostrar_passos:
            print(f"Após '{elemento}':")
            print("  Pilha valores:", pilha)
            print("  Pilha expr:   ", pilha_expr)
            print()

    # 🔥 NOVO: validação final mais clara
    if len(pilha) != 1:
        raise ValueError("Erro: expressão inválida (valores ou operadores incorretos)")

    return pilha[0], pilha_expr[0]


print("--- Calculadora Polonesa Inversa (RPN) ---")
print("Exemplo: 5 5 + 2 *")
print("Digite 'sair' para encerrar.\n")

while True:
    expressao = input("Digite a expressão: ")

    if expressao.lower() == "sair":
        print("Encerrando")
        break

    try:
        resultado, expr = calculadora_rpn(expressao, mostrar_passos=True)
        print(f"Resultado final: {resultado}")
        print(f"Notação algébrica: {expr}\n")

    except Exception as erro:
        print(f"{erro}\n")