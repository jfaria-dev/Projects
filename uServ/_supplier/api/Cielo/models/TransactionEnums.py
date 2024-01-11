from enum import Enum, unique

@unique
class StatusTransacao(Enum):
    NOT_FINISHED = 0
    AUTHORIZED = 1
    PAYMENT_CONFIRMED = 2
    DENIED = 3
    VOIDED = 10
    REFUNDED = 11
    PENDING = 12
    ABORTED = 13
    SCHEDULED = 20    

@unique
class Interest(Enum):
    Loja = "ByMerchant"
    Cartao = "ByIssuer"

@unique
class Type(Enum):
    CartaoCredito = "CreditCard"
    
    
class BinStatus:
    AUTHORIZED = '00'
    BRAND_NOT_SUPPORTED = '01'
    CARD_NOT_SUPPORTED = '02'
    AFFILIATION = '73'

    STATUS_CHOICES = [
        (AUTHORIZED, "Análise autorizada"),
        (BRAND_NOT_SUPPORTED, "Bandeira não suportada"),
        (CARD_NOT_SUPPORTED, "Cartão não suportado na consulta de bin"),
        (AFFILIATION, "Afiliação bloqueada")
    ]

    @classmethod
    def get_description(cls, status_code):
        for code, description in cls.STATUS_CHOICES:
            if code == status_code:
                return description
        return None