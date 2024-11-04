import firebase_admin
from firebase_admin import credentials, firestore
from config.firebase_config import Initialize_firebase
from models.employee_model import Employee
class EmployeeRepository:
    def __init__(self):
        self.db = Initialize_firebase()
        self.collection = self.db.collection('employees_python')
    
    def get_all(self):
        employees = [Employee.from_dict(doc.to_dict())
        for doc in self.collection.stream()]
        return employees
    
    def create_employee(self, employee_new):
        doc = self.collection.document()
        doc.set(employee_new.to_dict())
        return doc.id
        
    def get_by_username(self, username):
        docs = self.collection.where("username", "==", username).stream()
        for doc in docs:
            return Employee.from_dict(doc.to_dict())
        return None
    
    def get_by_id(self, id):
        doc = self.collection.document(id).get()
        return Employee.from_dict(doc.to_dict()) if doc.exists else None
    
    def update_employee(self, id, data):
        self.collection.document(id).update(data)
        
    def delete_employee(self, id):
        self.collection.document(id).delete()
        
    