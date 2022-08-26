class Tab:

    #class level attribute
    menu = {
        'wine': 5,
        'beer': 3,
        'soft_drink': 2,
        'chicken': 10,
        'veggie': 12,
        'salmon': 15,
        'desert': 6
    }

    # init function
    def __init__(self):
        self.total = 0
        self.items = []

    # instance method
    def add(self, item):
        self.items.append(item)
        self.total = self.total + self.menu[item]

    # instance method
    def print_bill(self, tax, service):
        tax = (tax / 100) * self.total
        service = (service / 100) * self.total
        total = self.total + tax + service

        for item in self.items:
            print(f'{item:20} ${self.menu[item]}')

        print(f'{"Total":20} ${total:.2f}')
