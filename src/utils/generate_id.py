import uuid
def generate_id():
        generate_id = str(uuid.uuid4()).replace('-','')

        if len(generate_id) < 10:
            generate_id += uuid.uuid4().hex[:10-len(generate_id)]

        return generate_id[:10]