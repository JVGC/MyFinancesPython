class Debt:
    def __init__(self,
                id=None,
                description=None,
                part_value=None,
                total_parts=None,
                start_date=None,
                total_value=None,
                paid_parts=None,
                remaining_parts=None,
                remaining_value=None):

        self._id = None
        self._description = None
        self._part_value = None
        self._total_parts = None
        self._total_value = None
        self._paid_parts =  None
        self._remaining_parts = None
        self._remaining_value = None
        self._start_date = None
        
        self.id = id
        self.description = description
        self.part_value = part_value
        self.total_parts = total_parts
        self.total_value = total_value
        self.paid_parts =  paid_parts
        self.remaining_parts = remaining_parts
        self.remaining_value = remaining_value
        self.start_date = start_date

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, value):
        if value is None:
            raise Exception('Error: O ID não pode estar em branco!')

        self._id = value



    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        if value is None:
            raise Exception('Error: A descrição não pode estar em branco!')

        self._description = value

    @property
    def part_value(self):
        return self.part_value

    @part_value.setter
    def part_value(self, value):
        if value is None:
            raise Exception('Error: O valor da Parcela não pode estar em branco')

        self._part_value = value
    
    @property
    def total_parts(self):
        return self.total_parts

    @total_parts.setter
    def total_parts(self, value):
        if value is None:
            raise Exception('Error: O total de parcelar não pode estar em branco')

        self._total_parts = value

    @property
    def total_value(self):
        return self.total_value

    @total_value.setter
    def total_value(self, value):
        if value is None:
            raise Exception('Error: O valor total não pode estar em branco')

        self._total_value = value

    @property
    def paid_parts(self):
        return self.paid_parts

    @paid_parts.setter
    def paid_parts(self, value):
        if value is None:
            raise Exception('Error: O numero de parcelas pagas não pode estar em branco')

        self._paid_parts = value

    @property
    def remaining_parts(self):
        return self.remaining_parts

    @remaining_parts.setter
    def remaining_parts(self, value):
        if value is None:
            raise Exception('Error: As parcelas restantes não podem estar em branco')

        self._remaining_parts = value

    @property
    def remaining_value(self):
        return self.remaining_value

    @remaining_value.setter
    def remaining_value(self, value):
        if value is None:
            raise Exception('Error: O valor restante não pode estar em branco!')

        self._remaining_value = value

    @property
    def start_date(self):
        return self.start_date

    @start_date.setter
    def start_date(self, value):
        if value is None:
            raise Exception('Error: A data inicial não pode estar em branco!')

        self._start_date = value

    
    def is_paid(self):
        return self._remaining_parts == 0