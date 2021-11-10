from enum import Enum


class BankCode_(Enum):
    KBANK = "004"
    BBL = "002"
    SCB = "014"
    KTB = "006"
    KMA = "KMA"


class UrlType(Enum):
    KBANK = "MOBILE"
    BBL = "WEB"
    SCB = "WEB"
    KTB = "MOBILE"


class ApimBankPayment(Enum):
    BBL = "002"
    KBANK = "004"
    KTB = "006"
    SCB = "014"


class BankCode(Enum):
    # class Details:
    #     def __init__(self, url_type, bank_code, apim_bank_payment):
    #         self.url_type = url_type
    #         self.bank_code = bank_code
    #         self.apim_bank_payment = apim_bank_payment
    #
    # KBANK = Details(url_type="MOBILE", bank_code="004", apim_bank_payment="004")
    # BBL = Details(url_type="WEB", bank_code="002", apim_bank_payment="002")
    # SCB = Details(url_type="WEB", bank_code="014", apim_bank_payment="014")
    # KTB = Details(url_type="MOBILE", bank_code="006", apim_bank_payment="006")
    # KMA = Details(url_type=None, bank_code="KMA", apim_bank_payment=None)
    # def url_type(self):
    #     return self.value.url_type
    #
    # def bank_code(self):
    #     return self.value.bank_code
    #
    # def apim_bank_payment(self):
    #     return self.value.apim_bank_payment

    UrlType = Enum("UrlType", "MOBILE WEB")

    # url_type, apim bankcode, mpay bankcode
    KBANK = UrlType.MOBILE, "004", "100"
    BBL = UrlType.WEB, "002", "200"
    SCB = UrlType.WEB, "014", "201"
    KTB = UrlType.MOBILE, "006", "300"
    KMA = None, None, None

    def url_type(self):
        return self.value[0].name

    def apim_bank_code(self):
        return self.value[1]

    def mpay_bank_code(self):
        return self.value[2]


print(BankCode.KBANK.url_type())
print(BankCode.KBANK.apim_bank_code())
print(BankCode.KBANK.mpay_bank_code())


