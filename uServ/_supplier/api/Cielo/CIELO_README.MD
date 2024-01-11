# RETORNA A BANDEIRA DO CARTAO
# GET
CARD_BIN = "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/cardBin/" + '[06 DIGITOS DO CARTAO]'

# RETORNO
# {
#   "Status": "00",
#   "Provider": "VISA",
#   "CardType": "Multiplo",
#   "ForeignCard": true,
#   "CorporateCard": false,
#   "Issuer": "Bradesco",
#   "IssuerCode": "237",
#   "Prepaid": false
# }

################################
# ZERO AUTH - VALIDA O CARTAO PARA COMPRA
ZEROAUTH = "https://apiquerysandbox.cieloecommerce.cielo.com.br//1/zeroauth"

################################
# REQ COMPRA
# DADOS:
# {
#   "MerchantOrderId": "2014111701", - ORIGATORIO (NUMERO DO PEDIDO)
#   "Customer": {
#     "Name": "Comprador crédito completo",
#     "Email": "compradorteste@teste.com",
#     "Birthdate": "1991-01-02",
#     "Address": {
#       "Street": "Rua Teste",
#       "Number": "123",
#       "Complement": "AP 123",
#       "ZipCode": "12345987",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BRA"
#     },
#     "DeliveryAddress": {
#       "Street": "Rua Teste",
#       "Number": "123",
#       "Complement": "AP 123",
#       "ZipCode": "12345987",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BRA"
#     },
#     "Billing": {
#       "Street": "Rua Neturno",
#       "Number": "12345",
#       "Complement": "Sala 123",
#       "Neighborhood": "Centro",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BR",
#       "ZipCode": "20080123"
#     }
#   },
#   "Payment": {
#     "Currency": "BRL",
#     "Country": "BRA",
#     "ServiceTaxAmount": 0,
#     "Installments": 1, - ORIGATORIO (PARCELAS)
#     "Interest": "ByMerchant",
#     "Capture": true,
#     "Authenticate": "false",
#     "Recurrent": "false", - OBRIGATORIO (PARA A RECORRENCIA ANUAL DEVE SER SETADO TRUE)
#     "SoftDescriptor": "123456789ABCD",
#     "InitiatedTransactionIndicator": {
#       "Category": Categoria do indicador de início da transação. Válido apenas para bandeira Mastercard. Valores possíveis: 
#                                       - “C1”: transação inciada pelo portador do cartão; 
#                                       - “M1”: transação recorrente ou parcelada iniciada pela loja;
#                                       - “M2”: transação iniciada pela loja.# 
#       }
#     "CreditCard": {
#       "CardNumber": "1234123412341231", - ORIGATORIO
#       "Holder": "Teste Holder",
#       "ExpirationDate": "12/2030", - ORIGATORIO
#       "SecurityCode": "123",
#       "SaveCard": "false",
#       "Brand": "Visa", - ORIGATORIO (ATRAVES DO CARD_BIN ACIMA)
#       "CardOnFile": {
#         "Usage": "Used", - ORIGATORIO (Indica o propósito de armazenamento de cartões, caso o campo “Usage” for “Used”.)                                         
#         "Reason": "Unscheduled" - OBRIGATORIO ("Recurring" - Compra recorrente programada (ex. assinaturas). Se for transação recorrente, 
#                                         usar Payment.Recurrent = true (recorrência própria) ou Recurrent.Payment = true (recorrência programada).)
#       }
#     },  
#     "IsCryptoCurrencyNegotiation": true,
#     "Type": "CreditCard", - ORIGATORIO (TIPO DE PAGAMENTO)
#     "Amount": 15700, - ORIGATORIO (VALOR)
#     "AirlineData": {
#       "TicketNumber": "AR988983"
#     }
#   }
# }

# RESPOSTA
# {
#   "MerchantOrderId": "2014111706",
#   "Customer": {
#     "Name": "Comprador crédito completo",
#     "Identity": "11225468954",
#     "IdentityType": "CPF",
#     "Email": "compradorteste@teste.com",
#     "Birthdate": "1991-01-02",
#     "Address": {
#       "Street": "Rua Teste",
#       "Number": "123",
#       "Complement": "AP 123",
#       "ZipCode": "12345987",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BRA"
#     },
#     "DeliveryAddress": {
#       "Street": "Rua Teste",
#       "Number": "123",
#       "Complement": "AP 123",
#       "ZipCode": "12345987",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BRA"
#     },
#     "Billing": {
#       "Street": "Rua Neturno",
#       "Number": "12345",
#       "Complement": "Sala 123",
#       "Neighborhood": "Centro",
#       "City": "Rio de Janeiro",
#       "State": "RJ",
#       "Country": "BR",
#       "ZipCode": "20080123"
#     }
#   },
#   "Payment": {
#     "ServiceTaxAmount": 0,
#     "Installments": 1,
#     "Interest": "ByMerchant",
#     "Capture": true,
#     "Authenticate": false,
#     "CreditCard": {
#       "CardNumber": "455187******0183",
#       "Holder": "Teste Holder",
#       "ExpirationDate": "12/2030",
#       "SaveCard": false,
#       "Brand": "Visa",
#       "PaymentAccountReference": "92745135160550440006111072222",
#       "CardOnFile": {
#         "Usage": "Used",
#         "Reason": "Unscheduled"
#       }
#     },    
#     "IsCryptoCurrencyNegotiation": true,
#     "TryAutomaticCancellation": true,
#     "ProofOfSale": "674532",
#     "Tid": "0305020554239",
#     "AuthorizationCode": "123456",
#     "SoftDescriptor": "123456789ABCD",
#     "PaymentId": "24bc8366-fc31-4d6c-8555-17049a836a07",
#     "Type": "CreditCard",
#     "Amount": 15700,
#     "CapturedAmount": 15700,
#     "Country": "BRA",
#     "AirlineData": {
#       "TicketNumber": "AR988983"
#     },
#     "ExtraDataCollection": [],
#     "Status": 2,
#     "ReturnCode": "6",
#     "ReturnMessage": "Operation Successful",
#     "MerchantAdviceCode": "1",
#     "Links": [
#       {
#         "Method": "GET",
#         "Rel": "self",
#         "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}"
#       },
#       {
#         "Method": "PUT",
#         "Rel": "void",
#         "Href": "https://apisandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}/void"
#       }
#     ]
#   }
# }

################################################################
# REQUISIÇAO COMPRA RECORRENTE PROPRIA
URL="https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/"
# DADOS:
# {
#   "MerchantOrderId": "2014113245231706", - OBRIGATÓRIO
#   "Customer": {
#     "Name": "Comprador rec propria" - OBRIGATÓRIO
#   },
#   "Payment": {
#     "Type": "CreditCard", - OBRIGATÓRIO
#     "Amount": 1500, - OBRIGATÓRIO
#     "Installments": 1, - OBRIGATÓRIO
#     "SoftDescriptor": "123456789ABCD",
#     "Recurrent": true, - OBRIGATÓRIO
#     "CreditCard": {
#       "CardNumber": "1234123412341231", - OBRIGATÓRIO
#       "Holder": "Teste Holder", - OBRIGATÓRIO
#       "ExpirationDate": "12/2030", - OBRIGATÓRIO
#       "SecurityCode": "262", - OBRIGATÓRIO
#       "SaveCard": "false",
#       "Brand": "Visa" - OBRIGATÓRIO
#     }
#   }
# }
# RESPOSTA
# {
#     "MerchantOrderId": "2014113245231706",
#     "Customer": {
#         "Name": "Comprador rec propria"
#     },
#     "Payment": {
#         "ServiceTaxAmount": 0,
#         "Installments": 1,
#         "Interest": "ByMerchant",
#         "Capture": false,
#         "Authenticate": false,
#         "Recurrent": true,
#         "CreditCard": {
#             "CardNumber": "123412******1231",
#             "Holder": "Teste Holder",
#             "ExpirationDate": "12/2030",
#             "SaveCard": false,
#             "Brand": "Visa"
#         },
#         "ProofOfSale": "3827556",
#         "Tid": "0504043827555",
#         "AuthorizationCode": "149867",
#         "SoftDescriptor":"123456789ABCD",
#         "PaymentId": "737a8d9a-88fe-4f74-931f-acf81149f4a0",
#         "Type": "CreditCard",
#         "Amount": 1500,
#         "Currency": "BRL",
#         "Country": "BRA",
#         "Provider": "Simulado",
#         "ExtraDataCollection": [],
#         "Status": 1,
#         "ReturnCode": "4",
#         "ReturnMessage": "Operation Successful",
#         "Link": {
#                 "Method": "GET",
#                 "Rel": "recurrentPayment",
#                 "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/RecurrentPayment/{RecurrentPaymentId}"
#             },
#             "AuthorizeNow": true
#         },
#         "Links": [
#             {
#                 "Method": "GET",
#                 "Rel": "self",
#                 "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}"
#             },
#             {
#                 "Method": "PUT",
#                 "Rel": "capture",
#                 "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}/capture"
#             },
#             {
#                 "Method": "PUT",
#                 "Rel": "void",
#                 "Href": "https://apiquerysandbox.cieloecommerce.cielo.com.br/1/sales/{PaymentId}/void"
#             }
#         ]
#     }
# }

