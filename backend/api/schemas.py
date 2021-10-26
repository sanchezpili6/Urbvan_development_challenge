from marshmallow import Schema
from marshmallow import fields
from marshmallow import validate


class EmployeesSchema(Schema):
    id = fields.Str(dump_only=True)
    rfc = fields.Str(validate=validate.Length(max=13))
    name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))
    start_date = fields.DateTime()
    birthday = fields.DateTime()
    job_position = fields.Str(validate=validate.Length(max=50))
    pronouns = fields.Str(validate=validate.Length(max=4))
