import firebase_admin
from firebase_admin import credentials, firestore
from models.employee_model import Employee

cred = credentials.Certificate("RUTA")
firebase_admin.initialize_app(cred)
db = firestore.client()
collection = 'employee_python'

class EmployeeRepository:
    @staticmethod
    def get_all():
        employees = db.collection(collection)
        return [doc.to_dict() for doc in employees.stream()]
    
    @staticmethod
    def create_employee(data):
        db.collection(collection).add(data)
        
    @staticmethod
    def get_by_username(self, username):
        docs = db.collection(collection).where("username", "==", username).stream()
        
        for doc in docs:
            return Employee.from_dict(doc.to_dict())
        return None