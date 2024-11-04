# Deben tener un setter y getter para cada atributo de la clase, en el modelo mostrara como se guardara en la base de datos
# Se usa un constructor porque es la forma en la que se crean los objetos en python
class Employee:
    def __init__(self, id=None, name='', patsurn='', matsurn='', address='', phone='', city='', state='', username='', password='', role=''):
        self.name = name
        self.patsurn = patsurn
        self.matsurn = matsurn
        self.address = address
        self.phone = phone
        self.city = city
        self.state = state
        self.username = username
        self.password = password
        self.role = role
        
    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Employee(**data)