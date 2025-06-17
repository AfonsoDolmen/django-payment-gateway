from dotenv import load_dotenv
from os import getenv
from mercadopago.sdk import SDK
import mercadopago


def save_payment_on_db(user, preference, Payment) -> None:
    """
    Salva as informações do pagamento no banco de dados
    """
    payment_id = preference.get('id', '')
    init_point = preference.get('sandbox_init_point', '')

    try:
        Payment.objects.create(
            payment_id=payment_id,
            init_point=init_point,
            user=user
        )
    except Exception as e:
        raise Exception(e)


def load_sdk() -> SDK:
    """
    Carrega o SDK
    """
    load_dotenv()  # Carrega variáveis de ambiente

    return mercadopago.SDK(getenv('API_PROD_TOKEN'))


def generate_link(user, orders, Payment) -> str:
    """
    Gera o link para compra
    """
    sdk = load_sdk()

    # Gera o array de pedidos
    items = [
        {
            "id": str(order.id),
            "title": order.ticket.name,
            "description": order.ticket.description,
            "quantity": order.quantity,
            "unit_price": float(order.ticket.price),
            "currency_id": "BRL",
        }
        for order in orders
    ]

    # Corpo da requisição
    request = {
        "items": items,
        "payer": {
            "email": user.email,
        },
        "back_urls": {
            "success": "http://127.0.0.1:8000/payments/success/",
            "pending": "http://127.0.0.1:8000/",
            "failure": "http://127.0.0.1:8000/",
        },
    }

    preference_response = sdk.preference().create(request)
    preference = preference_response['response']

    if preference.get('status', '') and preference['status'] != 201:
        raise Exception(f'Falha na requisição: {preference}')

    save_payment_on_db(user, preference, Payment)

    # Retorna o link de pagamento
    return preference['sandbox_init_point']
