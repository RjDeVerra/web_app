import re
from typing import Dict, Any
from create_db import db

def validate_field(field_name: str, field_value: str) -> str:
    if re.match(r"\d{2}.\d{2}.\d{4}", field_value):
        return "date"
    elif re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", field_value):
        return "phone"
    elif re.match(r"[^@]+@[^@]+\.[^@]+", field_value):
        return "email"
    else:
        return "text"

def find_matching_template(form_data: Dict[str, Any]) -> Dict[str, str]:
    templates = db.all()
    for template in templates:
        template_name = template["name"]
        template_fields = {k: v for k, v in template.items() if k != "name"}

        match = True
        for field_name, field_type in template_fields.items():
            if field_name not in form_data or validate_field(field_name, form_data[field_name]) != field_type:
                match = False
                break
        
        if match:
            return {"form_name": template_name}
    
    result = {}
    for field_name, field_value in form_data.items():
        result[field_name] = validate_field(field_name, field_value)
    return result