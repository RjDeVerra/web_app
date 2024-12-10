from tinydb import TinyDB

db = TinyDB('forms_db.json')

form_templates = [
    {"name": "MyForm", "user_name": "text", "order_date": "date", "lead_email": "email"},
    {"name": "Order Form", "order_date": "date", "user_phone": "phone", "lead_email": "email"},
]

for template in form_templates:
    db.insert(template)