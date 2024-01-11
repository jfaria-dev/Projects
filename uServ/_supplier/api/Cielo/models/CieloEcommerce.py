import json
import requests
from .TransactionCancel import RequestCancelTransaction, ResponseCancelTransaction
from .TransactionSale import Transaction, ResponseTransaction

class CieloEcommerce:
    BASE_URL = "https://apisandbox.cieloecommerce.cielo.com.br"
    BASE_BINCARD_URL = "https://apiquerysandbox.cieloecommerce.cielo.com.br"
    MERCHANT_ID = "4adb101d-76e4-44d5-99e5-9d78ef76f929"
    MERCHANT_KEY = "SPFMLARZJBGIGVMNTEPDBAECOPCPWFOLTSCKKNNS"    
    
    def __init__(self):
        self.auth_headers = {
            "Content-Type": "application/json",
            "MerchantId": self.MERCHANT_ID,
            "MerchantKey": self.MERCHANT_KEY
            }
    # GET CARD_BIN - Pega dados do cartão
    def query_card(self, cardnumber):
        print(cardnumber)
        response = requests.get(f"{self.BASE_BINCARD_URL}/1/cardBin/{cardnumber}", headers=self.auth_headers)
        # print(response.json())
        return response.json()
    
    # POST - Envia transaçao credito
    def create_sale_creditcard(self, transaction):  
        if not transaction is None:
            # print(self.BASE_URL)
            print(transaction)
            response = requests.post(f"{self.BASE_URL}/1/sales/", json=transaction, headers=self.auth_headers)
            # print(response.json())
            return response
        return None

    # POST - Envia transaçao debito
    # def create_sale_debitcard(self, request):        
    #     response = requests.post(f"{self.BASE_URL}/1/sales/", json=request, headers=self.auth_headers)
    #     return response.json()

    # GET - Consulta Transaçao por PaymentId
    def query_sale(self, payment_id):        
        response = requests.get(f"{self.url}/1/sales/{payment_id}", headers=self.headers)
        return response.json()
    
    # PUT - Envia transaçao de cancelamento pelo id do pagamento fornecido pela Cielo
    def cancel_total_payment_byPaymentId(self, req_t_cancel : RequestCancelTransaction):   
        self.auth_headers['RequestId'] = req_t_cancel.request_id
        response = requests.put(f"{self.BASE_URL}/1/sales/{req_t_cancel.payment_id}/void?amount={req_t_cancel.amount}", headers=self.auth_headers)
        return response.json()
    
    # PUT - Envia transaçao de cancelamento por numero do pedido
    def cancel_total_payment_byOrderId(self, req_t_cancel : RequestCancelTransaction):   
        self.auth_headers['RequestId'] = req_t_cancel.request_id
        response = requests.put(f"{self.BASE_URL}/1/sales/OrderId/{req_t_cancel.order_id}/void?amount={req_t_cancel.amount}", headers=self.auth_headers)
        return response.json()
    
    def custom_serializer(obj):
        if isinstance(obj, (Transaction)):
            sale_json = json.dumps(obj.__dict__, indent=2)
            return sale_json        
        return None