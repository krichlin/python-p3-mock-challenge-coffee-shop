import ipdb

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name') and isinstance(new_name, str) and len(new_name) >= 3:
            self._name = new_name
    
    def orders(self):
        ipdb.set_trace()
        return [order for order in Order.all if order.coffee == self]
        print('hello')
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

    def __repr__(self):
        return f'<Coffee name={self.name}>'

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name

    def orders(self):
        return [order for order in Order.all if order.customer == self]
        

    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass

    def __repr__(self):
        return f'<Customer name={self.name}>'
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.add_new_order(self)

    @classmethod
    def add_new_order(cls, new_order):
        cls.all.append(new_order)


    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if isinstance(new_price, float) and 1.0 <= new_price <= 10.0 and not hasattr(self,'_price'):
            self._price = new_price

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self,new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee

    def __repr__(self):
        return f'<Order customer={self.customer.name} coffee={self.coffee.name} price={self.price}>'

