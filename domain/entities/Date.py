class Date:
    def __init__(self,
                year=None,
                month=None,
                day=None):
        

        self._year = None
        self._month = None
        self._day = None

        self.year = year
        self.month = month
        self.day = day

        self.AVAIABLE_MONTHS = ['JAN', 'FEV', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, value):
        if value is None:
            raise Exception('Error: O ano não pode estar em branco')

        self._year = value

    @property
    def month(self):
        return self.month

    @month.setter
    def month(self, value):
        if value is None:
            raise Exception('Error: O mês não pode estar em branco!')
        
        if value not in self.AVAIABLE_MONTHS:
            raise Exception('Error: Mês Inválido!')

        self._month = value

    @property
    def day(self):
        return self.day

    @day.setter
    def day(self, value):

        self._day = value
