from domain.entities.Date import Date


class PayableMonth:
    def __init__(self,
                date: Date =  None,
                is_paid:bool = False) -> None:
    

        self._date = None
        self._is_paid = None

        self.date = date
        self.is_paid = is_paid

    @property
    def date(self):
        return self.date

    @date.setter
    def date(self, value):
        if value is None:
            raise Exception('Error: A Data não pode estar em branco')

        self._date = value

    @property
    def is_paid(self):
        return self.is_paid

    @is_paid.setter
    def is_paid(self, value):
        if value is None:
            raise Exception('Error: O atributo is_paid não pode estar em branco!')
        
        self._is_paid = value

    def pay(self):
        self.is_paid = True

    
    def to_dict(self):
        return {
            'date': self._date.to_dict(),
            'is_paid':self._is_paid
        }