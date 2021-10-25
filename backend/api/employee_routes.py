from flask import Blueprint
from flask import jsonify
from flask import request
from api.schemas import EmployeesSchema
from database.db import Employees
from database.db import db

employee_blueprint = Blueprint('employee', __name__)


@employee_blueprint.route('/users/<user_id>', methods=['GET'])
def get_employee(employee_id):
    session = db.session()
    employee = session.query(Employees).filter(Employees.id == employee_id)

    return jsonify(EmployeesSchema().dump(employee))


@employee_blueprint.route('/users/<user_id>', methods=['PATCH'])
def update_user(employee_id):
    session = db.session()
    query = session.query(Employees).filter(Employees.id == employee_id)

    content = request.get_json()
    if content is None:
        return 'Missing content', 400

    data = EmployeesSchema().load(content)
    query.update(data)
    session.commit()

    employee = query.first()
    return jsonify(EmployeesSchema().dump(employee))


@employee_blueprint.route('/users', methods=['POST'])
def create_user():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400

    session = db.session()
    employee = session.query(Employees).filter(Employees.rfc == content['rfc']).first()

    if employee is not None:
        return f'El empleado con el rfc: {content["rfc"]} ya existe', 409

    new_employee = Employees(
        id=content['id'],
        name=content['name'],
        last_name=content['last_name'],
        start_date=content['start_date'],
        birthday=content['birthday'],
        job_position=content['job_position'],
        pronouns=content['pronouns']
    )
    session.add(new_employee)

    session.commit()

    employee = session.query(Employees).filter(Employees.rfc == content['rfc']).first()
    return jsonify(EmployeesSchema().dump(employee))
