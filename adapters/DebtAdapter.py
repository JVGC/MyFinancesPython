from domain.entities import Date, Debt


class DebtAdapter():

    def __init__(self):
        pass

    def adapt(self, _id,
              description,
              part_value,
              total_parts,
              start_date,
              paid_parts):

        start_date = Date.create(start_date['year'], start_date['month']).ok()

        return Debt.create(_id,
                           description,
                           part_value,
                           total_parts,
                           start_date,
                           paid_parts).ok()
