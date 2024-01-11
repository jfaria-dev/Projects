from django.db import models
from .TransactionEnums import StatusTransacao

class RequestCancelTransaction(models.Model):    
    request_id = models.CharField(max_length=36, null=True, blank=True) # ID da requisição feita ao Cielo. Este campo é opcional, pois nem todas as requisições gerarão um pagamento.
    payment_id = models.CharField(max_length=36) # ID do pagamento na plataforma Cielo
    order_id = models.CharField(max_length=36, null=True, blank=True) # ID do pedido na loja
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True) # Valor do pagamento. Este campo aceita valores decimais com duas casas decimais.

class ResponseCancelTransaction(models.Model):
    Status = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in StatusTransacao]) # Status da Transação.
    ProofOfSale = models.CharField(max_length=6) # Número da autorização, identico ao NSU.
    Tid = models.CharField(max_length=20) # Id da transação na adquirente.
    AuthorizationCode = models.CharField(max_length=6) # Código de autorização.
    ReturnCode = models.CharField(max_length=32) # Código de retorno da adquirente.
    ReturnMessage = models.TextField(max_length=512) # Mensagem de retorno da adquirente.
    
    
