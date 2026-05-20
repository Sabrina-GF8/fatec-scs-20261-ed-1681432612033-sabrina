'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul                                *                                *
* Autor: 1681432612033 - Sabrina Franca Costa             *
* Objetivo: Colocar em prática o conceito de árvores      *
* binárias em python                                      *
*                  Data: 11/05/2026                       *
*---------------------------------------------------------*
'''
    # AAnalisar arvore
    def analisar_arvore(self, valorBusca):
        if self.raiz is None:
            print("Árvore vazia")
            return

        print("===== DIAGNÓSTICO GERAL =====")

        print("Raiz: ", self.raiz.valor)

        print("Nós internos:", end=" ")
        self.imprimir_nos_internos()

        print("Nós externos (folhas):", end=" ")
        self.imprimir_folhas()

        print("Mostrando por níveis:")
        self.imprimir_niveis()

        print("\n===== DIAGNÓSTICO DO NÓ =====")

        def buscar(no):
            if no is None:
                return None

            if no.valor == valorBusca:
                return no

            elif valorBusca < no.valor:
                return buscar(no.esq)

            else:
                return buscar(no.dir)

        no = buscar(self.raiz)

        if no is None:
            print("Valor não encontrado")
            return

        print("Nó analisado:", no.valor)

        grau = 0

        if no.esq:
            grau += 1

        if no.dir:
            grau += 1

        print("Grau do nó:", grau)

        print("Ancestrais:", end=" ")
        self.imprimir_ancestrais(valorBusca)

        print("Descendentes:", end=" ")
        self.imprimir_descendentes(valorBusca)

        print("Altura do nó:", self.calcular_altura(no))

        print("Profundidade do nó:", self.calcular_profundidade(valorBusca))

    # Imprimir nos internos
    def imprimir_nos_internos(self):

        def interno(no):

            if no is None:
                return

            if no.esq is not None or no.dir is not None:
                print(no.valor, end=" ")

            interno(no.esq)
            interno(no.dir)

        interno(self.raiz)
        print()

    # Folhas
    def imprimir_folhas(self):

        def folhas(no):

            if no is None:
                return

            if no.esq is None and no.dir is None:
                print(no.valor, end=" ")
                return

            folhas(no.esq)
            folhas(no.dir)

        folhas(self.raiz)
        print()

    # Imprimir níveis
    def imprimir_niveis(self):

        def nivel(no, lvl):

            if no is None:
                return

            if lvl == 0:
                print(no.valor, end=" ")

            else:
                nivel(no.esq, lvl - 1)
                nivel(no.dir, lvl - 1)

        def altura(no):

            if no is None:
                return -1

            return 1 + max(
                altura(no.esq),
                altura(no.dir)
            )

        h = altura(self.raiz)

        for i in range(h + 1):
            print(f"Nível {i}: ", end="")
            nivel(self.raiz, i)
            print()

    # Calc altura
    def calcular_altura(self, no):

        if no is None:
            return -1

        return 1 + max(
            self.calcular_altura(no.esq),
            self.calcular_altura(no.dir)
        )

    # Calc profundidade
    def calcular_profundidade(self, valor):

        def profundidade(no, valor, nivel):

            if no is None:
                return -1

            if no.valor == valor:
                return nivel

            esq = profundidade(no.esq, valor, nivel + 1)

            if esq != -1:
                return esq

            return profundidade(no.dir, valor, nivel + 1)

        return profundidade(self.raiz, valor, 0)

    # Imprimir ancestrais
    def imprimir_ancestrais(self, valor):

        def ancestrais(no, valor):

            if no is None:
                return False

            if no.valor == valor:
                return True

            if ancestrais(no.esq, valor) or ancestrais(no.dir, valor):
                print(no.valor, end=" ")
                return True

            return False

        ancestrais(self.raiz, valor)
        print()

    # Imprimir descendentes
    def imprimir_descendentes(self, valor):

        def buscar(no, valor):

            if no is None:
                return None

            if no.valor == valor:
                return no

            if valor < no.valor:
                return buscar(no.esq, valor)

            return buscar(no.dir, valor)

        def imprimir(no):

            if no is None:
                return

            print(no.valor, end=" ")

            imprimir(no.esq)
            imprimir(no.dir)

        alvo = buscar(self.raiz, valor)

        if alvo:
            imprimir(alvo.esq)
            imprimir(alvo.dir)

        print()