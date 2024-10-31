from repositories.employee_repository import EmployeeRepository
from utils.encryption_util import encrypt_password
from utils.token_util import generate_token
import time

class EmployeeService:
    @staticmethod
    def get_all():
        return EmployeeRepository.get_all()
    
    @staticmethod
    def create_employee(data):
        if EmployeeRepository.get_by_username(data ['username']):
            return {'message': 'Username already exists'}
        data['password'] = encrypt_password(data['password'])
        EmployeeRepository.create_employee(data)
        token = generate_token(data['username'])
        return {
            'message': 'Employee created successfully',
            'token': token
        }
    