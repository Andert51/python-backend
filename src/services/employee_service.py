import bcrypt
from repositories.employee_repository import EmployeeRepository
from models.employee_model import Employee

class EmployeeService:
    def __init__(self):
        self.repository = EmployeeRepository()
        
    def get_all(self):
        return self.repository.get_all()
    
    def create_employee(self, data):
        if self.repository.get_by_username(data ['username']):
            raise ValueError ('Username already exists')
        
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed.decode('utf-8')
        
        employeeNew = Employee(**data)
        return self.repository.create_employee(employeeNew)
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    
    def get_by_username(self, username):
        return self.repository.get_by_username(username)
    
    def delete_employee(self, id):
        return self.repository.delete_employee(id)
    
    def update_employee(self, id, data):
        if 'password' in data:
            hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
            data['password'] = hashed.decode('utf-8')
        self.repository.update_employee(id, data)
        
        