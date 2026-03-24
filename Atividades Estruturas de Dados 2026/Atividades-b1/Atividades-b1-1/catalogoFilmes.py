''' 
*---------------------------------------------------------* 
*              Fatec São Caetano do Sul                   * 
*                   Atividade B1-1                        * 
*    Autor: Sabrina Franca Costa                          * 
*    Objetivo: Criar um catálogo em que filmes possam     *
*     ser adicionados, buscados, listados e removidos.    * 
*                 data: 24/02/2026                        * 
*---------------------------------------------------------* 
'''

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("Filme já adicionado")
    else:
        catalogo[id_filme] = {
            "titulo": titulo,
            "diretor": diretor
        }
        print("Filme adicionado com sucesso")

def buscar_filme(id_filme):
    buscar = catalogo.get(id_filme)

    if buscar:
        print(f"Filme encontrado: {buscar}")
    else:
        print("Filme não cadastrado")

def remover_filme(id_filme):
    if id_filme in catalogo:
        catalogo.pop(id_filme)
        print("Filme removido.")
    else:
        print("Filme não encontrado")

def listar_todos():
    if not catalogo:
        print("O catálogo está vazio")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_filme, dados in catalogo.items():
            print(f"ID: {id_filme} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")

# ------------------------------------------------------------------------------------------------ #

adicionar_filme(1, "Matrix", "Lilly Wachowski")
adicionar_filme(2, "Titanic", "James Cameron")

listar_todos()

buscar_filme(1)

remover_filme(2)

listar_todos()