# 🎟️ Django Ticket Store

Sistema web para gestão de ingressos e pagamentos via Mercado Pago. Os usuários podem visualizar eventos, adquirir ingressos, gerar pedidos (Orders) e realizar pagamentos de forma segura e integrada.

---

## 🚀 Funcionalidades

- ✅ Listagem de ingressos disponíveis
- ✅ Visualização de detalhes de cada ingresso
- ✅ Criação de pedidos vinculados ao usuário
- ✅ Geração de link para pagamentos via Mercado Pago
- ✅ Cancelamento de pedidos pendentes

---

## 🧠 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- SQLite3 (padrão - substituível por PostgreSQL)
- Mercado Pago SDK
- HTML5 + CSS3 (Django templates)
- Bootstrap

---

## ⚙️ Instalação e Execução

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do Mercado Pago

# 5. Execute as migrações
python manage.py migrate

# 6. (Opcional) Crie um superusuário
python manage.py createsuperuser

# 7. Inicie o servidor de desenvolvimento
python manage.py runserver
