from routes.employee_routes import init_employee_routes
from middleware.auth_middleware import require_auth
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'UCHALE_12345'

# Initialize routes
init_employee_routes(app)

#Definir el middleware
app.before_request(require_auth)

if __name__ == "__main__" :
    app.run(debug=True)