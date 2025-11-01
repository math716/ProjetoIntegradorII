# 🏛️ Sistema de Cadastro de Pessoas em Situação de Rua  
**Secretaria de Assistência, Participação e Inclusão Social – Ribeirão Pires**

---

### 🔹 Introdução  
Este sistema foi desenvolvido para **realizar o cadastro de pessoas em situação de rua** que irão receber um **benefício social**.  
Ele coleta informações básicas — como **nome, CPF, RG e data de nascimento** — e também permite **anexar arquivos em PDF**, como documentos comprobatórios.

---

### 🔹 Estrutura geral  
O sistema foi desenvolvido em **Python**, utilizando o framework **FastAPI**, que permite criar aplicações web de forma simples, leve e rápida.  
Os dados são salvos em um **banco de dados SQLite**, e os arquivos enviados são armazenados em uma **pasta local** (`uploads/`).

---

### 🔹 Explicando o funcionamento  
Ao acessar a **página inicial**, o usuário encontra um **formulário de cadastro**.  
Quando o formulário é preenchido e enviado, o sistema:  
1. Grava as informações no banco de dados;  
2. Salva os arquivos PDF na pasta `uploads`;  
3. Redireciona o usuário para a **página de listagem**, onde é possível visualizar todos os cadastros e abrir os documentos anexados.

---

### 🔹 Parte técnica  
O código está dividido em três partes principais:

- **`database.py`** → Cria a conexão com o banco de dados SQLite.  
- **`models.py`** → Define a tabela `pessoas`, com os campos utilizados no cadastro.  
- **`main.py`** → Contém as rotas da aplicação (`/`, `/cadastro`, `/listagem`), o envio dos arquivos e a integração com o front-end.  

As páginas HTML ficam dentro da pasta **`templates/`**, utilizando o motor de templates **Jinja2**, responsável por exibir as informações de forma dinâmica.

---

### 🔹 Encerramento  
O objetivo deste projeto foi desenvolver um **sistema simples, funcional e de fácil demonstração**, com base em tecnologias modernas.  
O sistema pode ser facilmente **adaptado para outros tipos de cadastros**, bastando alterar os campos ou a estrutura do banco de dados.

---

## 🚀 Como executar o projeto

Siga os passos abaixo para configurar e rodar o sistema corretamente:

---

### 🐍 1. Instalar o Python

1. **Baixe o instalador do Python:**
   👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Durante a instalação**, marque a opção **"Add Python to PATH"** antes de continuar.

3. Após concluir, **feche e reabra o PowerShell** (ou o terminal que estiver usando).

4. Verifique se o Python foi instalado corretamente executando o comando:

   ```bash
   python --version
   ```

---

### ▶️ 2. Executar o sistema

1. Localize o arquivo **`start_projeto.bat`** na pasta do projeto.  
2. **Dê um duplo clique** sobre ele ou execute pelo PowerShell com:

   ```bash
   ./start_projeto.bat
   ```

Isso iniciará automaticamente o sistema com todas as configurações necessárias. 🎉

💡 **Dica:** Se o comando `python` não for reconhecido, reinicie o computador e tente novamente.

---

📘 **Tecnologias utilizadas**
- Python 3
- FastAPI
- SQLite
- Jinja2
- HTML5 / CSS3

---

👨‍💻 **Autor:** Matheus Euclides e Bernardo Goisman  
🏙️ **Projeto Integrador II – Secretaria de Assistência, Participação e Inclusão Social – Ribeirão Pires**


