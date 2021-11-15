class InvalidMonth:
    def __init__(self, avaiable_months) -> None:

        self.message = 'Invalid Month'
        self.entity = 'Month'
        self.reason = f"Month should be in: {avaiable_months}"
