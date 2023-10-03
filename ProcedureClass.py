class Procedure:
    def __init__(self, name, pro_date, practitioner, charges, ID):
        self.__name = name
        self.__pro_date = pro_date
        self.__practitioner = practitioner
        self.__charges = charges
        self.__ID = ID

    def get_name(self):
        return self.__name

    def get_pro_date(self):
        return self.__pro_date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    def get_ID(self):
        return self.__ID