
from marshmallow import Schema, fields

class EmployeeSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    phone_number = fields.String(required=True)

class CompanySchema(Schema):
    name = fields.String(required=True)
    salary = fields.Float(required=True)
    manager_id = fields.Integer(required=True)
    department_id = fields.Integer(required=True)

