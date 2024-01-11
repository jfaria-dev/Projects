from enum import Enum, unique
from typing import Any
from django.db import models
from .TransactionEnums import StatusTransacao, Type, Interest

class AddressCustomer(models.Model):
    Street = models.CharField(max_length=255, null=True, blank=True)
    Number = models.CharField(max_length=15, null=True, blank=True)
    Complement = models.CharField(max_length=50, null=True, blank=True)
    ZipCode = models.CharField(max_length=9, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=2, null=True, blank=True)
    Country = models.CharField(max_length=35, null=True, blank=True)
    
    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':               
                result[k] = v          
        return result   
    
    class Meta:
        verbose_name = "Address"

class Customer(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Birthdate = models.CharField(max_length=10)
    Address = models.OneToOneField(AddressCustomer,related_name='address', on_delete=models.CASCADE, null=True, blank=True)
    DeliveryAddress = models.OneToOneField(AddressCustomer, related_name='delivery_address', on_delete=models.CASCADE, null=True, blank=True)
    Billing = models.OneToOneField(AddressCustomer, related_name='billing_address', on_delete=models.CASCADE, null=True, blank=True)

    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':               
                result[k] = v 
        if self.Address:
            result['Address'] = self.Address.to_dict()            
        return result


class CardOnFile(models.Model):    
    Usage = models.CharField(max_length=255, null=True)
    Reason = models.CharField(max_length=255, null=True)
    
    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':
                result[k] = v 
        return result   

class CreditCard(models.Model):
    CardNumber = models.CharField(max_length=19)
    Holder = models.CharField(max_length=25)
    ExpirationDate = models.CharField(max_length=7)
    SecurityCode = models.CharField(max_length=3)
    SaveCard = models.BooleanField()
    Brand = models.CharField(max_length=10)
    CardOnFile = models.OneToOneField(CardOnFile, on_delete=models.CASCADE)
    
    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':               
                result[k] = v 
        if self.CardOnFile:
            result['CardOnFile'] = self.CardOnFile.to_dict()            
        return result

class AirlineData(models.Model):
    TicketNumber = models.CharField(max_length=13, null=True, blank=True)
    
class Payment(models.Model):
    Currency = models.CharField(max_length=3)
    Country = models.CharField(max_length=5)
    ServiceTaxAmount = models.IntegerField() # Aplicável apenas para empresas aéreas. Montante do valor da autorização que deve ser destinado à taxa de serviço. Obs.: Esse valor não é adicionado ao valor da autorização.
    Installments = models.IntegerField() # PARCELAS
    Interest = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Interest]) # TIPO PARCELAMENTO (Loja 'ByMerchant' ou Cartão 'ByIssuer')
    Capture = models.BooleanField(default=True)
    Authenticate = models.BooleanField(default=False)
    Recurrent = models.BooleanField(default=True) # Indica se a transação é do tipo recorrente (“true”) ou não (“false”). O valor “true” não originará uma nova recorrência, apenas permitirá a realização de uma transação sem a necessidade de envio do CVV. Authenticate deve ser “false” quando Recurrent é “true”. Saiba mais sobre Recorrência.
    SoftDescriptor = models.CharField(max_length=13, default="123456789ABCD") # O complemento do nome da loja que aparecerá na fatura do cartão. Não permite caracteres especiais.
    IsCryptoCurrencyNegotiation = models.BooleanField(default=False)
    Type = models.CharField(max_length=13,choices=[(tag.name, tag.value) for tag in Type]) # Tipo do meio de pagamento.
    Amount = models.IntegerField() # Valor do pedido (ser enviado em centavos).
    CreditCard = models.OneToOneField(CreditCard, on_delete=models.CASCADE)
    
    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':               
                result[k] = v 
        if self.CreditCard:
            result['CreditCard'] = self.CreditCard.to_dict()            
        return result

class Transaction(models.Model):
    MerchantOrderId = models.CharField(max_length=50) # models.ForeignKey('Order', related_name='transaction', on_delete=models.DO_NOTHING)
    Customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    Payment = models.ForeignKey('Payment', on_delete=models.CASCADE)
    
    def to_dict(self):
        result = {}
        for k, v in vars(self).items():
            if v is not None and k != '_state':        
                result[k] = v 
        if self.Customer:
            result['Customer'] = self.Customer.to_dict()    
        if self.Payment:
            result['Payment'] = self.Payment.to_dict()              
        return result
    

################################################################

class ResponseIdentityType(Enum):
    CPF = "CPF"
    CNPJ = "CNPJ"

class ResponseCustomer(Customer, models.Model):
    Identity = models.CharField(max_length=14)
    IdentityType = models.CharField(max_length=4, choices=[(tag.name, tag.value) for tag in ResponseIdentityType])

    class Meta:
        verbose_name = "Customer"

class ResponseCreditCard(CreditCard, models.Model):
    PaymentAccountReference = models.CharField(max_length=29, help_text="Número de referência da conta de pagamento")

    class Meta:
        verbose_name = "CreditCard"
    
class ResponsePayment(Payment, models.Model):
    ResponseCreditCard = models.ForeignKey(ResponseCreditCard,verbose_name='CreditCard', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Payment"

class Links(models.Model):    
    Method = models.CharField(max_length=10, help_text="Método do link")
    Rel = models.CharField(max_length=10, help_text="Relacionamento do link")
    Href = models.URLField(help_text="URL do link")

class ResponseTransaction(models.Model):
    MerchantOrderId = models.CharField(max_length=50, help_text="Número da autorização, identico ao NSU.")
    Customer = models.OneToOneField(ResponseCustomer, on_delete=models.CASCADE)
    Payment = models.ForeignKey(ResponsePayment,on_delete=models.CASCADE)
    IsCryptoCurrencyNegotiation = models.BooleanField(help_text="Indica se a transação envolve negociação de criptomoedas")
    TryAutomaticCancellation = models.BooleanField(help_text="Tentar cancelamento automático em caso de erro durante a autorização")
    ProofOfSale = models.CharField(max_length=6, help_text="Número da autorização")
    Tid = models.CharField(max_length=20, help_text="ID da transação na adquirente")
    AuthorizationCode = models.CharField(max_length=6, help_text="Código de autorização")
    SoftDescriptor = models.CharField(max_length=13, help_text="Texto impresso na fatura bancária")
    PaymentId = models.UUIDField(help_text="Número de identificação do pagamento")
    Type = models.CharField(max_length=20, help_text="Tipo da transação")
    Amount = models.DecimalField(max_digits=15, decimal_places=2, help_text="Valor da transação")
    CaptureAmount = models.DecimalField(max_digits=15, decimal_places=2, help_text="Valor da transação")
    Country = models.CharField(max_length=3, help_text="País")
    AirlineData = models.ForeignKey(AirlineData,on_delete=models.CASCADE)
    ExtraDataCollection = []    
    Status = models.CharField(max_length=17,help_text="Status da transação", choices=[(tag.name, tag.value) for tag in StatusTransacao])
    ReturnCode = models.CharField(max_length=32, help_text="Código de retorno da adquirente")
    ReturnMessage = models.CharField(max_length=512, help_text="Mensagem de retorno da adquirente")
    MerchantAdviceCode = models.CharField(max_length=2, help_text="Código de orientação da bandeira")
    Links = models.ForeignKey(Links,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "ResponseSale"


