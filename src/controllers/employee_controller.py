from flask import jsonify, request
from services.employee_service import EmployeeService

class EmployeeController:
    @staticmethod
    def get_all():
        employees = EmployeeService.get_all()
        return jsonify(employees)
    
    @staticmethod
    def get_by_id(employee_id): #Pascal Case, Camel Case, Snake Case son formas de nombrar variables
        employee = EmployeeService.get_by_id(employee_id)
        return jsonify(employee)
    
    @staticmethod
    def create_employee():
        data = request.get_json()
        response = EmployeeService.create_employee(data)
        return jsonify(response)