
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee-manager.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

# creating model tables structure
class Employee(db.Model):
    __tablename__ = 'employees_table'
    id = db.Column(db.Integer(), primary_key=True)
    emp_name = db.Column(db.String(255), nullable=False)
    dl = db.relationship('Manager', backref='employee', uselist=False)

class Manager(db.Model):
    __tablename__ = 'manager_table'
    manager_name = db.Column(db.String(255), nullable=False)
    employee_id = db.Column(db.Integer(), db.ForeignKey('employees_table.id'), primary_key=True)  # Foreign key

# creating model tables
db.create_all()

# URI for displaying the employee-manager relationship
@app.route('/',methods=['GET'])
def show_all():
    if request.method == 'GET':
		# querying the data from employee and manager tables using join
        data = (db.session.query(Employee.id,Employee.emp_name,Manager.manager_name).join(Manager)).all()
        result = []
		
		#Required format output
        for row in data:
            r={}
            r["emp_id"]=row[0]
            r["emp_name"]=row[1]
            r["manager_name"]=row[2]
            result.append(r)
			
		# return jsonified result
        return jsonify(result)

# Run the flask app
if __name__ == '__main__':
    app.run(debug = True)