# INTEGRANTES - GRUPO 2 
ANTHONY GABRIEL PIOVAN DOS SANTOS - RA1987602 <br>
LEONARDO NUNES NAVAS - RA2010317 <br>
WENDELL PEREIRA RIBEIRO - RA2004501 <br>


#  Sistema de Gerenciamento de Biblioteca CLI em Python
Sistema de gerenciamento de biblioteca feito em Python com um Command Line Interface (CLI). Ele permite gerenciar livros, usuários e empréstimos de maneira fácil, rápida e prática


# Pré-requisitos


Para executar este código, você precisará ter:
* **Python 3.10 ou superior instalado.** 


# Como Executar o Código
Siga os passos abaixo para executar o sistema de gerenciamento de biblioteca:


1.  **Salve o Código:**
    *  Baixe o arquivo com uma extensão `.py`, por exemplo, `biblioteca_cli.py`.


2.  **Abra um Terminal (ou Prompt de Comando):**
    * No Windows: Procure por "cmd" ou "PowerShell".
    * No macOS: Procure por "Terminal".
    * No Linux: Geralmente Ctrl+Alt+T ou procure por "Terminal" no menu de aplicativos.


3.  **Navegue até o Diretório do Arquivo:**
    * Use o comando `cd` (change directory) para navegar até a pasta onde você salvou o arquivo `biblioteca_cli.py`.
    * Por exemplo, se você salvou em uma pasta chamada `ProjetosPython` na sua Área de Trabalho:
        ```
        cd Desktop/ProjetosPython
        ```
        ou
        ```
        cd "Área de Trabalho/ProjetosPython"
        ```
        (use aspas se o caminho tiver espaços).


4.  **Execute o Script Python:**
    * Uma vez no diretório correto, digite o seguinte comando e pressione Enter:
        ```
        python biblioteca_cli.py
        ```
# Como Usar o Sistema
Após executar o script, você verá o menu principal do sistema no seu terminal:


# Estrutura de dados
# 1. Importações 📦
* from collections import deque
* import datetime
#2. Estruturas de Dados Globais 💾
* catalogo_livros = {}
* cadastro_usuarios = {}
* registros_emprestimos = []
* lista_espera = {}
#3. Função Principal de Interação (menu_principal) 🖥️
Loop while True para manter o menu ativo:
* Exibe o cabeçalho e as opções do menu principal (1-8 e 0 para Sair).
* Solicita a opcao ao usuário.
* Bloco match opcao: para direcionar a ação:
```
       print(" 1.  ➕  Adicionar Livro")
        print(" 2.  ➖  Remover Livro")
        print(" 3.  🔍  Buscar Livro")
        print(" 4.  📖  Catálogo de Livros")
        print(" 5.  👤  Adicionar Usuário")
        print(" 6.  📥  Emprestar Livro")
        print(" 7.  📤  Devolver Livro")
        print(" 8.  📚  Livros Emprestados")
```
   * case '0': imprime mensagem de saída e executa break para sair do loop.
   * case _: imprime mensagem de opção inválida.
   * Condicional if opcao != '0': para pausar antes de mostrar o menu novamente.


# 4. Definições das Funções de Funcionalidade 🛠️
   * função adicionar_livro():
   * função remover_livro():
   * função buscar_livro():
   * função exibir_catalogo():
   * função adicionar_usuario():
   * função realizar_emprestimo():
   * função registrar_devolucao():
   * função listar_emprestimos():
# 5. Bloco de Execução Principal ▶️
   * if __name__ == "__main__":

      * menu_principal() (chama a função principal para iniciar o programa).


# Principais recursos
# O sistema CLI tem as seguintes funcionalidades:
# Adicionar novos livros ao catálogo;
A primeira função apresentada no sistema, que é adicionar um livro ao catálogo, permite ao usuário inserir os dados de um novo livro, com ISBN, título, autor, gênero e o número de cópias. O sistema verifica se o ISBN fornecido já existe no catálogo para evitar duplicidade e também verifica se os inputs obrigatórios do usuário não foram deixados em branco. Também, é feita uma validação para garantir que o número de cópias inserido seja um valor positivo. Se as informações passarem por todas as verificações, o livro é armazenado na estrutura de dados catalogo_livros, juntamente com o registro das cópias totais.
# Remover livros existentes do catálogo.
Para a remoção de um livro do catálogo, o sistema solicita ao usuário o ISBN do livro que se deseja excluir. Em seguida, é verificado se um livro com o ISBN existe. é realizada também uma verificação em  registros_emprestimos , que visa impedir a remoção do livro, caso ele esteja atualmente emprestado e com status "ativo". Se o livro puder ser removido e não estiver com ninguem, ele é efetivamente retirado do catalogo_livros e, caso conste em alguma lista_espera, sua entrada também é eliminada dessa fila.
# Buscar livros por título, autor, gênero ou ISBN.
A opção de buscar um livro no catálogo oferece ao usuário diferentes maneiras de encontrar um livro, apresentando um sub-menu com while, para que se escolha o critério de busca, que pode ser Título, Autor, Gênero ou ISBN. Quando a busca é realizada por Título, Autor ou Gênero, o sistema solicita ao usuário o input e efetua uma verificação do termo, exibindo todos os que satisfazem a condição. Se a busca for por ISBN, o sistema solicita o número e realiza uma busca exata no catálogo. Se o input não corresponder aos dados registrados, o sistema informa ao usuário que não foi possível localizar.
# Exibir o catálogo completo de livros.
Na exibição do catálogo de todos os livros, o usuário pode visualizar todos os livros que estão presentes no catalogo_livros. Para cada livro, são exibidos o ISBN, título, autor, gênero, juntamente com o número de cópias disponíveis em relação ao número total de cópias. O sistema também mostra se há usuários na lista_espera para algum dos livros listados, oferecendo uma visão geral do acervo. Caso a biblioteca não possua nenhum livro cadastrado, uma mensagem indicando que ela está vazia é apresentada e o usuário retornará ao menu inicial.
# Adicionar novos usuários ao sistema.
Dentro do sistema é possível adicionar novos usuários, permitindo a inclusão dos mesmo dentro do gerenciador da biblioteca. Para registro, solicita um CPF, que é utilizado como identificador único do usuário, além do seu nome e endereço de email. O sistema realiza verificações para garantir que o CPF informado ainda não esteja cadastrado, evitando duplicidade de usuários, e também valida se os inputs obrigatórios de CPF, nome e email foram devidamente preenchidos. Após a validação bem-sucedida, os dados do novo usuário são armazenados no dicionário cadastro_usuarios.
# Realizar o empréstimo de livros para usuários cadastrados.
Na realização de um empréstimo de um livro, o sistema solicita o ISBN do livro que se deseja emprestar e o CPF do usuário que está fazendo o empréstimo. De início, são feitas duas verificações, a primeira para confirmar a existência do livro no catálogo, e a segunda do usuário no cadastro. Além disso, é checado antes se há cópias disponíveis do livro para empréstimo. Se todas as condições forem aprovadas, o número de cópias disponíveis do livro é reduzido. Um registro do empréstimo é adicionado à lista registros_emprestimos, contendo o ISBN, o CPF do usuário, a data do empréstimo, a data de devolução prevista (10 dias a partir da data atual) e o status "ativo". Caso o livro não esteja disponível no momento, o sistema oferece ao usuário a opção de entrar na lista_espera para aquele ISBN, e se o usuário aceitar e ainda não estiver na fila, ele é adicionado à estrutura deque correspondente.
# Registrar a devolução de livros.
A funcionalidade de registrar a devolução de um livro gerencia o retorno de um livro emprestado ao catalogo. O sistema solicita o input ao usuário do ISBN do livro devolvido e o CPF do usuário que o está devolvendo. Com esses dados, ele procura na lista registros_emprestimos por um empréstimo com status ativo que corresponde aos dados fornecidos. Se algum empréstimo ativo for encontrado com informações compatíveis, o número de cópias disponíveis do livro é alterado no catalogo_livros, e o status daquele registro de empréstimo é alterado para "devolvido", podendo ser emprestado novamente. Caso tenha usuários na lista_espera para o livro que acabou de ser devolvido, o sistema notifica o próximo usuário da fila sobre a disponibilidade do livro e o remove da espera. Se nenhum empréstimo ativo compatível for localizado, uma mensagem informativa é exibida e o usuário retorna ao menu de início
# Listar todos os livros que estão atualmente emprestados.
Para exibir uma relação dos livros que estão emprestados, o sistema exibe uma lista formatada de todos os empréstimos que constam com status "ativo" na lista registros_emprestimos. Para cada empréstimo que tem seu status ativo, é exibido o ISBN do livro, seu título, o CPF do usuário que o emprestou, o nome desse usuário e a data prevista que deve ser realizada a devolução. Se não houver nenhum livro emprestado ativamente no momento, o sistema informa essa situação ao usuário e retorna ao menu de início.
#Justificativa da estrutura
# 1. Importações 📦
```
from collections import deque
import datetime
```
      * from collections import deque: Esta linha importa a estrutura de dados deque da biblioteca collections do Python. foi escolhida e selecionada para a lista_espera porque permite realizar operações de adição (append) e remoção (popleft). Isso a torna ideal para implementar uma fila (FIFO - First-In, First-Out), que é o esperado para uma lista de espera de livros, onde o primeiro usuário a entrar na fila é o primeiro a ser atendido.
      *       * import datetime: Este módulo é essencial para manipular datas, Dentro do contexto da biblioteca, ele é usado para registrar a data em que um livro é emprestado (realizar_emprestimo) e assim calcular a data de devolução prevista.

#2. Estruturas de Dados Globais 💾
```
catalogo_livros = {}
cadastro_usuarios = {}
registros_emprestimos = []
lista_espera = {}
```
 Essas estruturas são definidas globalmente para que possam ser acessadas e modificadas por todas as funções do sistema. 
catalogo_livros = {}: Um dicionário que é usado para o catálogo, oferecendo acesso rápido aos detalhes de um livro, usando o ISBN como chave única. Isso é eficiente para adicionar, remover e buscar informações específicas de um livro. Para cada ISBN, os detalhes do livro (como título e autor) são guardados em um dicionário separado. Isso ajuda a manter os dados organizados.
cadastro_usuarios = {}: Dicionário parecido com o de catálogo de livros, só que agora aplicado para os usuários, usando um identificador único, o CPF como chave. Isso 
registros_emprestimos = []: Uma lista que é usada para armazenar os registros de empréstimos. Cada empréstimo é um evento que pode ser adicionado sequencialmente. Cada item na lista é um dicionário contendo os detalhes de um empréstimo (ISBN do livro, ID do usuário, datas, status). A adição de novos empréstimos é simples (append).
lista_espera = {}: Um dicionário que é usado para mapear um ISBN (chave) para uma fila de usuários (deque), que estão esperando por aquele livro. Isso permite que cada livro tenha sua própria fila de espera independente. O deque é usado como valor para garantir a ordem FIFO e a eficiência das operações de enfileirar e desenfileirar usuários.

#3. Função Principal de Interação (menu_principal 🖥️
Esta função serve como o ponto central de controle da interface com o usuário (CLI).
      * Loop while True: Garantindo que o menu seja exibido continuamente, permitindo que o usuário realize múltiplas operações sem que o programa termine após cada ação.
      * Exibição do Menu: Apresenta de forma clara as funcionalidades disponíveis, guiando o usuário.
      * Solicitação da opcao: Captura a escolha do usuário.
      * Bloco match opcao:: Estrutura de controle que direciona a execução para a função com base na opcao do usuário. É uma forma simples de lidar com múltiplas escolhas, substituindo, if-elif-else.
      * Pausa para continuar: Melhora a usabilidade, permitindo que o usuário leia a saída de uma operação antes que o menu seja reexibido.


# 4. Definições das Funções de Funcionalidade 🛠️
Função adicionar_livro():
      * Para que serve o catalogo_livros (dicionário) aqui? Usamos o catalogo_livros como um grande arquivo de fichas, onde cada livro tem sua "ficha" identificada pelo ISBN. Quando você adiciona um livro, é como criar uma nova ficha nesse arquivo. O dicionário é eficiente para esse tipo de operação por que é muito rápido verificar se um ISBN já foi cadastrado antes de adicionar um novo.
Função remover_livro():
      * Como as estruturas ajudam a remover um livro?
      * O catalogo_livros (dicionário) é usado como nosso índice principal; achar e tirar a "ficha" de um livro usando o ISBN.
      * A registros_emprestimos (lista) guarda o histórico de todas as vezes que livros foram emprestados. Precisamos olhar essa lista, item por item (cada item é um dicionário com dados do empréstimo), para ter certeza que o livro que queremos remover não está atualmente com alguém.
      * A lista_espera (dicionário) guarda as filas de pessoas esperando por cada livro. Se o livro é removido do catálogo, sua fila de espera correspondente também precisa ser eliminada para não manter pessoas esperando por algo que não existe mais.
Função buscar_livro():
      * Como o catalogo_livros (dicionário) é usado na busca? Para encontrar um livro, a função olha todas as "fichas" (detalhes de cada livro) dentro do catalogo_livros. Se você escolhe buscar pelo ISBN, o sistema pode, em alguns casos, ir direto na "ficha" correta se o ISBN for exato. Para outros critérios como título, autor ou gênero, a função compara o que você digitou com os detalhes escritos em cada "ficha" para ver se combinam.
Função exibir_catalogo():
      * Como as estruturas mostram o catálogo?
      * Para mostrar todos os livros, a função pega cada "ficha" (ISBN e seus detalhes) do catalogo_livros e exibe as informações de forma organizada.
      * Ela também consulta a lista_espera (dicionário) para cada livro listado, para verificar e mostrar se tem gente esperando por ele.
Função adicionar_usuario():
      * Para que serve o cadastro_usuarios (dicionário) aqui? Esta estrutura funciona de forma parecida com o catalogo_livros, mas para pessoas. O cadastro_usuarios guarda uma "ficha" para cada usuário, identificada pelo CPF. Usar um dicionário torna fácil e rápido adicionar novos usuários e verificar se um CPF já existe no sistema antes de cadastrar.
Função realizar_emprestimo():
      * Quais estruturas são usadas e por quê?
      * Quando um livro é emprestado, primeiro olhamos sua "ficha" no catalogo_livros para ver se ele existe e se tem cópias disponíveis, e então atualizamos essa ficha (diminuindo uma cópia disponível).
      * Verificamos também no cadastro_usuarios se a pessoa que quer pegar o livro está registrada.
      * Os detalhes importantes desse empréstimo (qual livro, quem pegou, quando pegou, quando devolver e o status "ativo") são guardados como um novo item (um dicionário) na lista registros_emprestimos. Uma lista é usada para manter esses registros de empréstimo.
      * Se o livro não estiver disponível, usamos a lista_espera (um dicionário onde cada livro pode ter sua própria fila). O CPF do usuário é adicionado ao final da fila daquele livro, que é um deque (uma lista especial otimizada para funcionar bem como fila).
Função registrar_devolucao():
      * Como as estruturas ajudam na devolução?
      * Quando um livro é devolvido, procuramos na lista registros_emprestimos para encontrar qual foi o empréstimo ativo daquele livro para aquela pessoa.
      * Uma vez encontrado, marcamos esse empréstimo como "devolvido" dentro da lista.
      * Depois, atualizamos a "ficha" do livro no catalogo_livros, aumentando o número de cópias disponíveis.
      * Se tinha gente na lista_espera (um dicionário que usa deque para as filas) por aquele livro, avisamos o primeiro da fila que o livro chegou e o removemos da espera.
Função listar_emprestimos():
      * Como os empréstimos são listados? Para mostrar os livros que estão atualmente com alguém, a função olha a lista registros_emprestimos, item por item.
      * Para cada empréstimo que ainda está "ativo", ela pega os detalhes do livro consultando o catalogo_livros (usando o ISBN do empréstimo).
      * E pega os dados do usuário consultando o cadastro_usuarios (usando o CPF do empréstimo).
      * Assim, consegue mostrar tudo direitinho: qual livro, com quem está e até quando deve ser devolvido.


# 5. Bloco de Execução Principal ▶️
```
if __name__ == "__main__":
    menu_principal()
```
O bloco if __name__ == "__main__", garante que a função menu_principal() (que inicia o programa) seja chamada apenas quando o script é executado diretamente (e não quando é importado como um módulo por outro script). Isso organiza o ponto de entrada do programa.
