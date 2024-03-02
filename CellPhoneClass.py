class CellPhone:

    def __init__(self, ma, mo, re): 
        self.__manufact = ma
        self.__model = mo
        self.__retail_price = re

    def set_manufact(self, ma):
        self.__manufact = ma
    
    def set_model(self, mo):
        self.__model = mo

    def set_retail_price(self, re):
        self.__retail_price = re

    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price