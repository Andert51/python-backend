from flask import jsonify, request
from services.employee_service import EmployeeService

class EmployeeController:
    def __init__(self):
        self.service = EmployeeService() # el constructor sirve para inicializar variables y que no apunten a None
    
    def get_all(self):
        employees = self.service.get_all()
        return jsonify([employees.to_dict() for employees in employees])
    
    def get_by_id(self, id): #Pascal Case, Camel Case, Snake Case son formas de nombrar variables
        employee = self.service.get_by_id(id)
        return jsonify(employee.to_dict()) if employee else ('Employee not found', 404)
    
    def get_by_username(self, username): #Pascal Case, Camel Case, Snake Case son formas de nombrar variables
        employee = self.service.get_by_id(username)
        return jsonify(employee.to_dict()) if employee else ('Employee not found', 404)
    
    def create_employee(self):
        data = request.get_json()
        try:
            user_id = self.service.create_employee(data)
            return jsonify({'id': user_id}), 201
        except ValueError as e:
            return jsonify({'errors': str(e)}), 400
        
    def update_employee(self, id):
        data = request.get_json()
        self.service.update_employee(id, data)
        return jsonify({'message' : 'Employee updated successfully'}), 200
    
    def delete_employee(self, id):
        self.service.delete_employee(id)
        return jsonify({'message': 'Employee deleted successfully'}), 200