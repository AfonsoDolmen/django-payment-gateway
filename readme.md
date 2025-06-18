# 🎟️ Django Ticket Store

Sistema web para gestão de ingressos e pagamentos via Mercado Pago. Os usuários podem visualizar eventos, adquirir ingressos, gerar pedidos (Orders) e realizar pagamentos de forma segura e integrada.

---

## 🚀 Funcionalidades

- ✅ Sistema de autenticação com validação de e-mail e senha
- ✅ Listagem de ingressos disponíveis
- ✅ Visualização de detalhes de cada ingresso
- ✅ Criação de pedidos vinculados ao usuário
- ✅ Cancelamento de pedidos pendentes
- ✅ Geração de link para pagamentos via Mercado Pago

---

## 🧠 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- PostgreSQL
- AWS EC2 para Deploy
- Mercado Pago SDK
- HTML5 + CSS3 (Django templates)
- Bootstrap

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute as migrações
```bash
python manage.py migrate

# 6. (Opcional) Crie um superusuário
python manage.py createsuperuser

# 7. Inicie o servidor de desenvolvimento
python manage.py runserver
```
