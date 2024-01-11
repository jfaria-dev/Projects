LINKS TESTES:
Envio de transação: https://apisandbox.cieloecommerce.cielo.com.br
Consulta transação: https://apiquerysandbox.cieloecommerce.cielo.com.br/

O cartão de teste 4024.0071.5376.3191, por exemplo, irá simular o status autorizado.

LINKS PRODUÇÃO:
Envio de transação: https://api.cieloecommerce.cielo.com.br/
Consulta transação: https://apiquery.cieloecommerce.cielo.com.br/

CONSULTAS:
GET CARD_BIN - Pega dados do cartão
# /1/cardBin/ + [06 DIGITOS DO CARTAO]

GET - Consulta Transaçao por MerchantId
# /1/sales?merchantOrderId={merchantOrderId}

GET - Consulta Transaçao por PaymentId
# /1/sales/{PaymentId}

GET - Consulta Transaçao por TId (Numero de identificação do pagamento na adquirente.)
# /1/sales/acquirerTid/{TID}

GET - Consulta Transaçao por Recorrência
# /1/RecurrentPayment/{RecurrentPaymentId}


----------------[]----------------
TRANSAÇAO:
POST - Envia transaçao
# /1/Sales/ + [body]



