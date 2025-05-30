from collections import deque
import datetime

catalogo_livros = {}
cadastro_usuarios = {}
registros_emprestimos = []
lista_espera = {}

def menu_principal():
    while True:
        print("=" * 47)
        print("📚 SISTEMA DE GERENCIAMENTO DE BIBLIOTECA 📚")
        print("=" * 47)
        print(" 1.  ➕  Adicionar Livro")
        print(" 2.  ➖  Remover Livro")
        print(" 3.  🔍  Buscar Livro")
        print(" 4.  📖  Catálogo de Livros")
        print(" 5.  👤  Adicionar Usuário")
        print(" 6.  📥  Emprestar Livro")
        print(" 7.  📤  Devolver Livro")
        print(" 8.  📚  Livros Emprestados")
        print(" 0.  🚪  Sair")
        print("=" * 47)
        opcao = input("🔸 Escolha uma opção: ")
        print("=" * 47)
        print("\n")

        match opcao:
            case '1':
                adicionar_livro()
            case '2':
                remover_livro()
            case '3':
                buscar_livro()
            case '4':
                exibir_catalogo()
            case '5':
                adicionar_usuario()
            case '6':
                realizar_emprestimo()
            case '7':
                registrar_devolucao()
            case '8':
                listar_emprestimos()
            case '0':
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.")
        if opcao != '0':
            input("\nPressione Enter para continuar...")

def adicionar_livro():
    print("=" * 47)
    print("➕📚 Adicionar Novo Livro")
    print("=" * 47)

    isbn_livro = input("ISBN do livro: ")
    if not isbn_livro.strip():
        print("ISBN não pode ser vazio.")
        return
    if isbn_livro in catalogo_livros:
        print(f"Erro: Livro com ISBN {isbn_livro} já existe.")
        return

    titulo_livro = input("Título do livro: ")
    if not titulo_livro.strip():
        print("Título não pode ser vazio.")
        return

    autor_livro = input("Autor do livro: ")
    if not autor_livro.strip():
        print("Autor não pode ser vazio.")
        return

    genero_livro = input("Gênero do livro: ")
    if not genero_livro.strip():
        print("Gênero não pode ser vazio.")
        return

    while True:
        try:
            num_copias = int(input("Número total de cópias: "))
            if num_copias > 0:
                break
            else:
                print("O número de cópias deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    catalogo_livros[isbn_livro] = {
        "titulo": titulo_livro,
        "autor": autor_livro,
        "genero": genero_livro,
        "copias_totais": num_copias,
        "copias_disponiveis": num_copias
    }
    print(f"Livro '{titulo_livro}' (ISBN: {isbn_livro}) adicionado com sucesso!")

def remover_livro():
    print("=" * 47)
    print("➖📚 Remover Livro do Catálogo")
    print("=" * 47)

    apagar_livro = input("Digite o ISBN do livro a ser removido: ")

    if not apagar_livro.strip():
        print("O ISBN não pode ser vazio.")
        return

    if apagar_livro not in catalogo_livros:
        print(f"Erro: Livro com ISBN '{apagar_livro}' não encontrado.")
        return

    emprestimo_status = False
    for emprestimo in registros_emprestimos:
        if emprestimo.get("isbn_livro") == apagar_livro and emprestimo.get("status") == "ativo":
            emprestimo_status = True
            break

    if emprestimo_status:
        print(f"Erro: O livro '{catalogo_livros[apagar_livro]['titulo']}' (ISBN: {apagar_livro}) está atualmente emprestado.")
        print("Ele não pode ser removido até que seja devolvido.")
        return

    livro_removido = catalogo_livros.pop(apagar_livro)

    if apagar_livro in lista_espera:
        lista_espera.pop(apagar_livro)
        print(f"Livro também removido da fila de espera.")

    print(f"Livro '{livro_removido['titulo']}' (ISBN: {apagar_livro}) removido com sucesso!")

def buscar_livro():
    print("=" * 47)
    print("🔍📚 Buscar Livro no Catálogo")
    print("=" * 47)

    while True:
        print("\nComo você gostaria de buscar o livro?")
        print("  1. Por Título")
        print("  2. Por Autor")
        print("  3. Por Gênero")
        print("  4. Por ISBN")
        print("  0. Voltar ao Menu Principal")
        print("-" * 47)

        criterio_busca = input("Escolha o critério de busca: ")
        print("-" * 47)

        match criterio_busca:
            case '1':
                termo_pesquisa = input("Digite o título a buscar: ")
                if not termo_pesquisa.strip():
                    print("O campo 'Título' não pode ser vazio.")
                else:
                    busca_resultados = False
                    print(f"\n--- Buscando livros por TÍTULO contendo: '{termo_pesquisa}' ---")
                    for isbn, dados_livro in catalogo_livros.items():
                        if termo_pesquisa.lower() in dados_livro.get("titulo", "").lower():
                            if not busca_resultados:
                                print("--- Resultados Encontrados ---")
                                busca_resultados = True
                            print(f"  ISBN: {isbn}")
                            print(f"  Título: {dados_livro.get('titulo', 'N/D')}")
                            print(f"  Autor: {dados_livro.get('autor', 'N/D')}")
                            print(f"  Gênero: {dados_livro.get('genero', 'N/D')}")
                            print(f"  Cópias Totais: {dados_livro.get('copias_totais', 'N/D')}")
                            print(f"  Cópias Disponíveis: {dados_livro.get('copias_disponiveis', 'N/D')}")
                            print("-" * 30)
                    if not busca_resultados:
                        print(f"Nenhum livro encontrado com o título contendo '{termo_pesquisa}'.")

            case '2':
                termo_pesquisa = input("Digite o autor a buscar: ")
                if not termo_pesquisa.strip():
                    print("O campo 'Autor' não pode ser vazio.")
                else:
                    busca_resultados = False
                    print(f"\n--- Buscando livros por AUTOR contendo: '{termo_pesquisa}' ---")
                    for isbn, dados_livro in catalogo_livros.items():
                        if termo_pesquisa.lower() in dados_livro.get("autor", "").lower():
                            if not busca_resultados:
                                print("--- Resultados Encontrados ---")
                                busca_resultados = True
                            print(f"  ISBN: {isbn}")
                            print(f"  Título: {dados_livro.get('titulo', 'N/D')}")
                            print(f"  Autor: {dados_livro.get('autor', 'N/D')}")
                            print(f"  Gênero: {dados_livro.get('genero', 'N/D')}")
                            print(f"  Cópias Totais: {dados_livro.get('copias_totais', 'N/D')}")
                            print(f"  Cópias Disponíveis: {dados_livro.get('copias_disponiveis', 'N/D')}")
                            print("-" * 30)
                    if not busca_resultados:
                        print(f"Nenhum livro encontrado do autor contendo '{termo_pesquisa}'.")

            case '3':
                termo_pesquisa = input("Digite o gênero a buscar: ")
                if not termo_pesquisa.strip():
                    print("O campo 'Gênero' não pode ser vazio.")
                else:
                    busca_resultados = False
                    print(f"\n--- Buscando livros por GÊNERO contendo: '{termo_pesquisa}' ---")
                    for isbn, dados_livro in catalogo_livros.items():
                        if termo_pesquisa.lower() in dados_livro.get("genero", "").lower():
                            if not busca_resultados:
                                print("--- Resultados Encontrados ---")
                                busca_resultados = True
                            print(f"  ISBN: {isbn}")
                            print(f"  Título: {dados_livro.get('titulo', 'N/D')}")
                            print(f"  Autor: {dados_livro.get('autor', 'N/D')}")
                            print(f"  Gênero: {dados_livro.get('genero', 'N/D')}")
                            print(f"  Cópias Totais: {dados_livro.get('copias_totais', 'N/D')}")
                            print(f"  Cópias Disponíveis: {dados_livro.get('copias_disponiveis', 'N/D')}")
                            print("-" * 30)
                    if not busca_resultados:
                        print(f"Nenhum livro encontrado do gênero contendo '{termo_pesquisa}'.")

            case '4':
                termo_pesquisa = input("Digite o ISBN a buscar: ")
                if not termo_pesquisa.strip():
                    print("O campo 'ISBN' não pode ser vazio.")
                else:
                    busca_resultados = False
                    print(f"\n--- Buscando livro por ISBN: '{termo_pesquisa}' ---")
                    if termo_pesquisa in catalogo_livros:
                        dados_livro = catalogo_livros[termo_pesquisa]
                        print("--- Resultado Encontrado ---")
                        busca_resultados = True
                        print(f"  ISBN: {termo_pesquisa}")
                        print(f"  Título: {dados_livro.get('titulo', 'N/D')}")
                        print(f"  Autor: {dados_livro.get('autor', 'N/D')}")
                        print(f"  Gênero: {dados_livro.get('genero', 'N/D')}")
                        print(f"  Cópias Totais: {dados_livro.get('copias_totais', 'N/D')}")
                        print(f"  Cópias Disponíveis: {dados_livro.get('copias_disponiveis', 'N/D')}")
                        print("-" * 30)
                    if not busca_resultados:
                        print(f"Nenhum livro encontrado com o ISBN '{termo_pesquisa}'.")

            case '0':
                print("Retornando ao menu principal...")
                return

            case _:
                print("Opção de critério inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

def exibir_catalogo():
    print("=" * 47)
    print("📖  Catálogo de Livros Completo")
    print("=" * 47)
    if not catalogo_livros:
        print("A biblioteca está vazia. Nenhum livro para listar.")
        return

    print(f"{'ISBN':<20} | {'Título':<30} | {'Autor':<25} | {'Gênero':<15} | {'Disp/Total':<10}")
    print("-" * 112)

    for isbn, dados_livro in catalogo_livros.items():
        titulo = dados_livro.get('titulo', 'N/D')
        autor = dados_livro.get('autor', 'N/D')
        genero = dados_livro.get('genero', 'N/D')
        copias_disp = dados_livro.get('copias_disponiveis', 0)
        copias_total = dados_livro.get('copias_totais', 0)
        print(f"{isbn:<20} | {titulo:<30} | {autor:<25} | {genero:<15} | {f'{copias_disp}/{copias_total}':<10}")

        if isbn in lista_espera and lista_espera[isbn]:
            print(f"{'':<20} | {'Fila de espera:':<30} {list(lista_espera[isbn])}")
    print("-" * 112)
def adicionar_usuario():
    print("=" * 47)
    print("👤  Adicionar Novo Usuário")
    print("=" * 47)

    cpf_usuario = input("Digite o CPF do usuário, (ex: 12345678900): ")
    if not cpf_usuario:
        print("CPF do usuário não pode ser vazio.")
        return
    if cpf_usuario in cadastro_usuarios:
        print(f"Erro: Usuário com um CPF que já existe: '{cpf_usuario}'")
        return

    nome_usuario = input("Nome do usuário: ")
    if not nome_usuario:
        print("Nome do usuário não pode ser vazio.")
        return
    email_usuario = input("Email do usuário: ")
    if not email_usuario:
        print("Email não pode estar vazio.")
        return

    cadastro_usuarios[cpf_usuario] = {
        "nome": nome_usuario,
        "email": email_usuario
    }
    print(f"Usuário: {nome_usuario}' portador do CPF: {cpf_usuario} e do Email: {email_usuario} adicionado ao cadastro com sucesso!")

def realizar_emprestimo():
    print("=" * 47)
    print("📥  Realizar Empréstimo de Livro")
    print("=" * 47)

    isbn_emprestimo = input("ISBN do livro a ser emprestado: ")
    if not isbn_emprestimo:
        print("ISBN não pode ser vazio.")
        return
    if isbn_emprestimo not in catalogo_livros:
        print(f"Erro: Livro com ISBN '{isbn_emprestimo}' não encontrado.")
        return

    cpf_emprestimo = input("CPF do usuário que está pegando o livro: ")
    if not cpf_emprestimo:
        print("CPF do usuário não pode ser vazio.")
        return
    if cpf_emprestimo not in cadastro_usuarios:
        print(f"Erro: Usuário com CPF '{cpf_emprestimo}' não encontrado. Cadastre o usuário primeiro.")
        return

    livro_solicitado = catalogo_livros[isbn_emprestimo]

    if livro_solicitado.get("copias_disponiveis", 0) > 0:
        livro_solicitado["copias_disponiveis"] -= 1

        data_limite_devolucao = datetime.date.today() + datetime.timedelta(10)

        registro_emprestimo = {
            "isbn_livro": isbn_emprestimo,
            "cpf_usuario": cpf_emprestimo,
            "data_emprestimo": datetime.date.today().isoformat(),
            "data_devolucao_prevista": data_limite_devolucao.isoformat(),
            "status": "ativo"
        }
        registros_emprestimos.append(registro_emprestimo)

        print(f"Livro '{livro_solicitado['titulo']}' emprestado para '{cadastro_usuarios[cpf_emprestimo]['nome']}'.")
        print(f"Devolver até: {data_limite_devolucao.isoformat()}.")
    else:
        print(f"Livro '{livro_solicitado['titulo']}' não está disponível (0 cópias disponíveis).")
        resposta_fila = input("Deseja entrar na fila de espera para este livro (s/n)? ")
        if resposta_fila == 's':
            if isbn_emprestimo not in lista_espera:
                lista_espera[isbn_emprestimo] = deque()

            if cpf_emprestimo not in lista_espera[isbn_emprestimo]:
                lista_espera[isbn_emprestimo].append(cpf_emprestimo)
                print(
                    f"Usuário '{cadastro_usuarios[cpf_emprestimo]['nome']}' adicionado à fila de espera para '{livro_solicitado['titulo']}'.")
            else:
                print(f"Usuário '{cadastro_usuarios[cpf_emprestimo]['nome']}' já está na fila de espera para este livro.")

def registrar_devolucao():
    print("=" * 47)
    print("📤  Registrar Devolução de Livro")
    print("=" * 47)

    isbn_devolucao = input("ISBN do livro a ser devolvido: ")
    if not isbn_devolucao:
        print("ISBN do livro não pode ser vazio.")
        return

    cpf_devolucao = input("CPF do usuário que está devolvendo: ")
    if not cpf_devolucao:
        print("CPF do usuário não pode ser vazio.")
        return

    busca_emprestimo = None
    i_emprestimo = -1

    for i, registro in enumerate(registros_emprestimos):
        if registro.get("isbn_livro") == isbn_devolucao and registro.get("cpf_usuario") == cpf_devolucao and registro.get("status") == "ativo":
            busca_emprestimo = registro
            i_emprestimo = i
            break

    if busca_emprestimo:
        isbn_devolvido = busca_emprestimo["isbn_livro"]
        cpf_devolvendo = busca_emprestimo["cpf_usuario"]

        if isbn_devolvido in catalogo_livros:
            catalogo_livros[isbn_devolvido]["copias_disponiveis"] += 1
        else:
            print(
                f"Atenção: O livro com ISBN {isbn_devolvido} não foi encontrado no catálogo (pode ter sido removido).")

        registros_emprestimos[i_emprestimo]["status"] = "devolvido"

        nome_livro = catalogo_livros.get(isbn_devolvido, {}).get('titulo', f"ISBN: {isbn_devolvido}")
        nome_usuario = cadastro_usuarios.get(cpf_devolvendo, {}).get('nome', f"CPF Usuário: {cpf_devolvendo}")

        print(f"Livro '{nome_livro}' devolvido com sucesso por '{nome_usuario}'.")

        if isbn_devolvido in catalogo_livros and isbn_devolvido in lista_espera and lista_espera[isbn_devolvido]:
            cpf_proximo = lista_espera[isbn_devolvido].popleft()
            nome_proximo = cadastro_usuarios.get(cpf_proximo, {}).get('nome', cpf_proximo)
            livro_disponivel = catalogo_livros[isbn_devolvido].get('titulo', isbn_devolvido)

            print(f"Notificação: Livro '{livro_disponivel}' agora disponível. "
                  f"Usuário '{nome_proximo}' é o próximo na fila.")

            if not lista_espera[isbn_devolvido]:
                del lista_espera[isbn_devolvido]
    else:
        print(f"Nenhum empréstimo ATIVO encontrado para o livro ISBN '{isbn_devolucao}' pelo usuário ID '{cpf_devolucao}'.")


def listar_emprestimos():
    print("=" * 47)
    print("📚  Livros Emprestados Atualmente (Ativos)")
    print("=" * 47)

    emprestimo_ativo = False

    print(f"{'ISBN Livro':<20} | {'Título':<30} | {'Usuário (CPF)':<20} | {'Nome Usuário':<25} | {'Devolução Até':<15}")
    print("-" * 115)

    for registro_emprestimo in registros_emprestimos:
        if registro_emprestimo.get("status") == "ativo":
            emprestimo_ativo = True

            isbn = registro_emprestimo.get("isbn_livro", "N/D")

            cpf_emprestimo = registro_emprestimo.get("cpf_usuario", "N/D")

            livro_devolucao = catalogo_livros.get(isbn, {}).get("titulo", "Título Desconhecido")
            nome_devolucao = cadastro_usuarios.get(cpf_emprestimo, {}).get("nome", "Nome Desconhecido")

            data_devolucao = registro_emprestimo.get("data_devolucao_prevista", "N/D")

            print(
                f"{isbn:<20} | {livro_devolucao:<30} | {cpf_emprestimo:<20} | {nome_devolucao:<25} | {data_devolucao:<15}")

    if not emprestimo_ativo:
        print("Nenhum livro emprestado ativamente no momento.")
    else:
        print("-" * 115)

if __name__ == "__main__":
    menu_principal()