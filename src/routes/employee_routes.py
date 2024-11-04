from flask import Blueprint
from controllers.employee_controller import EmployeeController
from middleware.auth_middleware import token_required

employee_controller = EmployeeController()

routes = Blueprint('routes', __name__)
routes.add_url_rule('/employees', 'get_all', employee_controller.get_all, methods=['GET'])              
routes.add_url_rule('/employees/<id>', 'get_by_id', employee_controller.get_by_id, methods=['GET'])    
routes.add_url_rule('/employees/user/<username>', 'get_by_username', token_required(employee_controller.get_by_username), methods=['GET']) 
routes.add_url_rule('/employees', 'create_employee', employee_controller.create_employee, methods=['POST'])       
routes.add_url_rule('/employees/<id>', 'update_employee', employee_controller.update_employee, methods=['PUT'])   
routes.add_url_rule('/employees/<id>', 'delete_employee', employee_controller.delete_employee, methods=['DELETE'])    

