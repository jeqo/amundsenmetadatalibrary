from flask_restful import fields

user_fields = {
    'email': fields.String,
    'first_name': fields.String,  # Optional
    'last_name': fields.String  # Optional
}

topic_consumer_fields = {
    'application_url': fields.String(attribute='application_url'),
    'name': fields.String,
    'id': fields.String,
    'description': fields.String  # Optional
}

topic_producer_fields = {
    'application_url': fields.String(attribute='application_url'),
    'name': fields.String,
    'id': fields.String,
    'description': fields.String  # Optional
}

source_fields = {
    'source_type': fields.String,
    'source': fields.String
}

tag_fields = {
    'tag_type': fields.String,
    'tag_name': fields.String
}

message_fields = {
    'schema_url': fields.String(attribute='schema_url'),
    'name': fields.String,
    'description': fields.String,
}

field_fields = {
    'name': fields.String,
    'description': fields.String,
    'type': fields.String(attribute='field_type'),
}

topic_fields = {
    'broker': fields.String,
    'cluster': fields.String,
    'topic_name': fields.String(attribute='name'),
    'topic_description': fields.String(attribute='description'), #Optional
    'tags': fields.List(fields.Nested(tag_fields)),  # Can be an empty list
    'badges': fields.List(fields.Nested(tag_fields)),  # Can be an empty list
    # Can be an empty list
    'topic_consumers': fields.List(fields.Nested(topic_consumer_fields)),
    # Can be an empty list
    'owners': fields.List(fields.Nested(user_fields)),
    # Can be an empty list
    'headers': fields.List(fields.Nested(field_fields)),
    # Can be an empty list
    'records': fields.List(fields.Nested(record_fields)),
    # Can be an empty list
    'topic_producers': fields.List(fields.Nested(topic_producer_fields)) #fields.Nested(table_writer_fields),
    'last_updated_timestamp': fields.Integer,  # Optional
    'source': fields.Nested(source_fields),  # Optional
    'is_queue': fields.Boolean  # Optional
}