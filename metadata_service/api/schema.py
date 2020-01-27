from flask_restful import fields

user_fields = {
    'email': fields.String,
    'first_name': fields.String,  # Optional
    'last_name': fields.String  # Optional
}

source_fields = {
    'source_type': fields.String,
    'source': fields.String
}

tag_fields = {
    'tag_type': fields.String,
    'tag_name': fields.String
}

field_fields = {
    'name': fields.String,
    'description': fields.String,
    'type': fields.String(attribute='field_type'),
}

schema_fields = {
    'schema_url': fields.String(attribute='schema_url'),
    'name': fields.String,
    'description': fields.String,
    'namespace': fields.String,
    'fields': fields.List(fields.Nested(field_fields)),
}