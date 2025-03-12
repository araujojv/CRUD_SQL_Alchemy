# CRUD com SQLAlchemy

Este projeto demonstra como implementar operações CRUD (Criar, Ler, Atualizar e Deletar) utilizando a biblioteca SQLAlchemy em Python.

## Descrição

A aplicação exemplifica como interagir com um banco de dados relacional por meio do SQLAlchemy, um ORM (Object Relational Mapper) que facilita o mapeamento de classes Python para tabelas de banco de dados.

## Funcionalidades

- **Criação de registros**: Adiciona novos registros ao banco de dados.
- **Leitura de registros**: Recupera e exibe registros existentes.
- **Atualização de registros**: Modifica dados de registros existentes.
- **Exclusão de registros**: Remove registros do banco de dados.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **SQLAlchemy**: Biblioteca para mapeamento objeto-relacional.
- **SQLite**: Banco de dados relacional utilizado para armazenamento dos dados.

## Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/araujojv/CRUD_SQL_Alchemy.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd CRUD_SQL_Alchemy
   ```

3. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual**:

   - No Windows:
     
     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:
     
     ```bash
     source venv/bin/activate
     ```

5. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

## Como Utilizar

1. **Configure o banco de dados**:

   O projeto está configurado para utilizar um banco de dados SQLite. Caso deseje utilizar outro SGBD, ajuste a string de conexão no arquivo `app.py` conforme necessário.

2. **Execute a aplicação**:

   ```bash
   python main.py
   ```

3. **Interaja com a aplicação**:

   Utilize a interface de linha de comando ou outra interface implementada para realizar operações CRUD no banco de dados.

## Estrutura do Projeto

- `app.py`: Arquivo principal contendo a lógica da aplicação e as operações CRUD.
- `requirements.txt`: Lista de dependências necessárias para executar a aplicação.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

