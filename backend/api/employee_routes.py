from flask import Blueprint
from flask import jsonify
from flask import request
from database.db import employees
from database.db import notes
import json

employee_blueprint = Blueprint('employee', __name__)


@employee_blueprint.route('/employee', methods=['GET'])
def get_employees():
    employees_array = []
    for employee in employees:
        employees_array.append(employees[employee])
    return jsonify(employees_array)


@employee_blueprint.route('/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = employees.get(employee_id, {'employee': 'employee not found'})
    return jsonify({'data': employee})


@employee_blueprint.route('/employee/update', methods=['GET'])
def update_user():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400

    employees[content['id']] = content
    return 'Usuario actualizado'


@employee_blueprint.route('/employee/delete/<employee_id>', methods=['GET'])
def delete_user(employee_id):
    employees.pop(employee_id)
    return 'Usuario borrado'


@employee_blueprint.route('/employee/add', methods=['POST'])
def create_employee():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400
    print(content)
    employee = employees.get(content['id'])

    if employee is not None:
        return f'El empleado con el rfc: {content["rfc"]} ya existe', 409

    employees[content['id']] = content

    return jsonify(employees)


@employee_blueprint.route('/notes/add', methods=['GET'])
def create_note():
    content = request.get_json()
    if content is None:
        return 'Missing content', 400
    print(notes)

    notes[content['id']] = notes.get(content['id'], []) + [content]
    print(notes)
    return 'excelente'


@employee_blueprint.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)


@employee_blueprint.route('/notes/<employee_id>', methods=['GET'])
def get_note(employee_id):
    note = notes.get(employee_id, {'note': 'no notes'})
    return jsonify({'data': note})
