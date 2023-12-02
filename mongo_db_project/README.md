

## Como funciona ?

#### É uma aplicação de linha de comando onde é possível cadastrar turmas e alunos. Onde cada aluno possui sua pontuação e a turma correspondente. Ele conta com as funcionalidades de obter informações como: pontuação geral, turma com maior pontuação, ver alunos de cada turma, etc...


## Como executar o aplictivo ?


### 1 - Execute o ambiente venv e instale as dependências:

* #####  Navegue para apasta do projeto usando o terminal e execute o seguinte comando:  `python -m venv env``

* #### Após isso, instale as dependências utilizando o comando:  `pip install -r requirements.txt` *



### 2 - Defina a string de conexão do seu cluster

* #### Agora, é necessário definir a string de conexão do Cluster do MongoDB. Para isso, basta se registrar no [site do MongoDB](https://www.google.com) e criar um Cluster.

* #### No seu Cluster, clique em connect e copie a string de conexão. (Ela deve se parecer com isso: `mongodb+srv://SEU_USUÁRIO:SUA_SENHA@cluster0.jvuwfrt.mongodb.net/?retryWrites=true&w=majority`).  

 * #### Com a string de conexão em mãos, basta abrir o diretório do projeto e ir até  ``src/database/properties.py`* ``, que é onde colocaremos a string de conexão. 


### 3 - Tudo pronto

#### Após inserir a string e conexão corretamente, a aplicação estará pronta para ser executada.