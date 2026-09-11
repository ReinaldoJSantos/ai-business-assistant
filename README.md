# 🤖 AI Business Assistant

Backend de um assistente inteligente para negócios, desenvolvido com **Python e FastAPI**, com foco em arquitetura organizada, APIs REST, persistência de dados, testes automatizados e futura integração com recursos de Inteligência Artificial e automação de processos.

O projeto está sendo desenvolvido de forma incremental, aplicando boas práticas de desenvolvimento de software e evoluindo a arquitetura conforme novas funcionalidades são adicionadas.

---

## 🎯 Objetivo

O **AI Business Assistant** tem como objetivo fornecer uma base backend para um assistente capaz de apoiar empresas na automação e gerenciamento de processos, podendo futuramente integrar:

* Inteligência Artificial;
* atendimento automatizado;
* gerenciamento de usuários;
* APIs externas;
* automações de processos;
* gerenciamento de dados;
* integrações com serviços de terceiros.

Neste momento, o projeto está concentrado na construção da **base arquitetural e do módulo de usuários**.

---

## 🛠️ Tecnologias

### Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* Pydantic
* Pydantic Settings

### Banco de dados

* PostgreSQL 16
* Alembic

### Testes

* Pytest
* FastAPI TestClient
* unittest.mock

  * `Mock`
  * `MagicMock`
  * `patch`

### Infraestrutura

* Docker
* Docker Compose

### Controle de versão

* Git
* GitHub

---

## 🏗️ Arquitetura

O projeto utiliza uma separação por responsabilidades, buscando manter as diferentes camadas independentes.

```text
                    ┌───────────────────┐
                    │      Cliente      │
                    │ Web / Frontend /  │
                    │      API Client   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │       API         │
                    │     FastAPI       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │      Service      │
                    │  Regras de negócio│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Repository     │
                    │ Acesso aos dados  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    PostgreSQL     │
                    └───────────────────┘
```

### Responsabilidades

**API**

Responsável pela exposição dos endpoints HTTP, validação das requisições e respostas da aplicação.

**Service**

Responsável pelas regras de negócio.

**Repository**

Responsável pela comunicação com o banco de dados.

**Models**

Representam as entidades persistidas no banco.

**Schemas**

Responsáveis pela validação e estrutura dos dados de entrada e saída da API.

---

## 📁 Estrutura do projeto

```text
ai-business-assistant/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── users.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── base_class.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── user.py
│   │
│   ├── repositories/
│   │   └── user.py
│   │
│   ├── schemas/
│   │   └── user.py
│   │
│   ├── services/
│   │   └── user.py
│   │
│   ├── utils/
│   │   └── security.py
│   │
│   └── main.py
│
├── alembic/
│   ├── versions/
│   └── env.py
│
├── tests/
│   ├── unit/
│   │   ├── test_security.py
│   │   └── test_user_service.py
│   │
│   ├── integration/
│   │   ├── test_users_api.py
│   │   └── test_user_repository.py
│   │
│   └── conftest.py
│
├── .env
├── alembic.ini
├── docker-compose.yml
├── requirements.txt
└── README.md
```

> A estrutura poderá evoluir conforme novos módulos e funcionalidades forem adicionados.

---

## 👤 Módulo de Usuários

O primeiro módulo implementado é o gerenciamento de usuários.

### Atualmente implementado

* Criação de usuário;
* validação dos dados de entrada;
* hash da senha;
* verificação de e-mail duplicado;
* persistência no PostgreSQL;
* retorno padronizado da API;
* tratamento de conflito de e-mail.

### Endpoint atual

```http
POST /api/v1/users
```

### Exemplo de requisição

```json
{
  "name": "Reinaldo",
  "email": "reinaldo@example.com",
  "password": "12345678"
}
```

### Resposta

```http
201 Created
```

Exemplo:

```json
{
  "id": "12345678-1234-1234-1234-123456789012",
  "name": "Reinaldo",
  "email": "reinaldo@example.com",
  "is_active": true,
  "created_at": "2026-01-01T10:00:00Z",
  "updated_at": "2026-01-01T10:00:00Z"
}
```

### E-mail já cadastrado

Quando o e-mail já existe:

```http
409 Conflict
```

Resposta:

```json
{
  "detail": "Email already registered"
}
```

---

## 🔐 Segurança

As senhas não são armazenadas diretamente no banco.

Durante a criação do usuário:

```text
Senha informada
      │
      ▼
  hash_password()
      │
      ▼
Password Hash
      │
      ▼
 PostgreSQL
```

O projeto também possui testes específicos para os mecanismos de segurança implementados.

A autenticação baseada em JWT será adicionada em uma etapa futura.

---

## 🧪 Testes

O projeto utiliza **Pytest** para testes automatizados.

Atualmente existem testes separados em:

### Testes unitários

Validam componentes de forma isolada, utilizando mocks quando necessário.

Exemplos:

* criação de usuário;
* tentativa de cadastro com e-mail existente;
* hash de senha;
* verificação de senha;
* senha incorreta.

### Testes de integração

Validam a interação entre componentes reais da aplicação.

Exemplos:

* criação de usuário através da API;
* validação de requisições HTTP;
* acesso ao `UserRepository`;
* comunicação com PostgreSQL.

### Executar todos os testes

```bash
python -m pytest -v
```

Resultado atual:

```text
9 passed
```

---

## 🧩 Mock e Patch

Durante os testes unitários, o projeto utiliza recursos do módulo `unittest.mock`.

### MagicMock

Utilizado para criar objetos controláveis durante os testes.

Exemplo:

```python
db = MagicMock()
```

### patch

Utilizado para substituir temporariamente uma implementação real.

Exemplo:

```python
with patch("app.services.user.UserRepository") as mock_repository:
    ...
```

Isso permite testar uma regra de negócio sem depender diretamente do banco de dados.

A utilização de mocks é feita de forma consciente, mantendo testes de integração para validar o comportamento real entre as camadas.

---

## 🐘 Banco de dados

O projeto utiliza:

```text
PostgreSQL 16
```

O banco é executado através do Docker.

Banco principal utilizado durante o desenvolvimento:

```text
aibusiness
```

As alterações estruturais do banco são controladas pelo **Alembic**.

### Verificar a versão atual das migrations

```bash
python -m alembic current
```

### Verificar a última migration

```bash
python -m alembic heads
```

### Executar migrations

```bash
python -m alembic upgrade head
```

---

## 🐳 Docker

O PostgreSQL é executado através do Docker Compose.

### Iniciar os serviços

```bash
docker compose up -d
```

### Verificar containers

```bash
docker ps
```

### Parar os serviços

```bash
docker compose down
```

---

## ▶️ Executando o projeto

Clone o repositório:

```bash
git clone <repository-url>
```

Entre no diretório:

```bash
cd ai-business-assistant
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente no arquivo `.env`.

Exemplo:

```env
APP_NAME=AI Business Assistant

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/aibusiness

TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ai_business_test
```

Inicie o PostgreSQL:

```bash
docker compose up -d
```

Execute as migrations:

```bash
python -m alembic upgrade head
```

Inicie a aplicação:

```bash
uvicorn app.main:app --reload
```

A API estará disponível localmente.

A documentação interativa do FastAPI poderá ser acessada através de:

```text
/docs
```

---

## 🌱 Desenvolvimento

O desenvolvimento do projeto segue uma abordagem incremental:

```text
Funcionalidade
      ↓
Implementação
      ↓
Teste unitário
      ↓
Teste de integração
      ↓
Revisão
      ↓
Git commit
      ↓
Git push
```

Cada funcionalidade deve ser implementada e testada antes da evolução para a próxima etapa.

---

## 🗺️ Roadmap

### 👤 Usuários

* [x] Criar usuário
* [x] Validar dados de entrada
* [x] Hash de senha
* [x] Verificar e-mail duplicado
* [x] Retornar `409 Conflict`
* [x] Repository de usuários
* [ ] Buscar usuário por ID
* [ ] Listar usuários
* [ ] Atualizar usuário
* [ ] Desativar/remover usuário

### 🔐 Autenticação

* [ ] Login
* [ ] JWT
* [ ] Access Token
* [ ] Refresh Token
* [ ] Proteção de endpoints
* [ ] Controle de permissões

### 🤖 Inteligência Artificial

* [ ] Integração com LLM
* [ ] Gerenciamento de conversas
* [ ] Contexto de conversação
* [ ] Assistente baseado em IA
* [ ] Integração com ferramentas externas

### 🔄 Automação

* [ ] Integração com APIs externas
* [ ] Webhooks
* [ ] Processamento assíncrono
* [ ] Filas de mensagens
* [ ] Integração com ferramentas de automação

### 🚀 DevOps

* [ ] CI
* [ ] CD
* [ ] Pipeline automatizado
* [ ] Dockerização completa
* [ ] Deploy em cloud
* [ ] Monitoramento

---

## 📌 Status atual

**Em desenvolvimento 🚧**

O projeto atualmente possui uma base funcional de backend com:

* FastAPI;
* PostgreSQL;
* SQLAlchemy;
* Alembic;
* Docker;
* arquitetura em camadas;
* módulo de usuários;
* segurança de senha;
* testes unitários;
* testes de integração.

A próxima evolução planejada é a implementação da consulta de usuários por ID.

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido como estudo prático de desenvolvimento backend, arquitetura de software, testes automatizados, APIs REST, banco de dados, DevOps e integração com Inteligência Artificial.
