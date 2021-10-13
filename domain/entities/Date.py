class Date:
    def __init__(self,
                year:int=None,
                month:str=None,
                day:int=None):
        

        self.AVAIABLE_MONTHS = {
            '1':'JAN', 
            '2':'FEV', 
            '3':'MAR',
            '4':'APR',
            '5':'MAY',
            '6':'JUN',
            '7':'JUL',
            '8':'AUG',
            '9':'SEP',
            '10':'OCT',
            '11':'NOV',
            '12':'DEC',
        }
        
        self._year = None
        self._month = None
        self._day = None

        self.year = year
        self.month = month
        self.day = day

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
        if value not in self.AVAIABLE_MONTHS.keys():
            raise Exception('Error: Mês Inválido!')

        self._month = value

    @property
    def day(self):
        return self.day

    @day.setter
    def day(self, value):

        self._day = value

    def get_next_month(self):
        
        next_month = ((int(self._month))%12)+1
        next_year =  self._year +1 if next_month <= int(self._month) else self._year

        return {
            'month':str(next_month),
            'year': next_year
        }

    def to_dict(self):
        return {
            "day": self._day,
            "month": self.AVAIABLE_MONTHS.get(self._month),
            "year": self._year
        }
