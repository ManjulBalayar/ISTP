import re
from django.core.exceptions import ValidationError
from django.db.models import QuerySet

def sanitize_json_key(key):
    """
    Sanitize JSON keys to prevent SQL injection when used with values() or values_list()
    methods with JSONField.
    """
    # Only allow alphanumeric characters, underscores, and hyphens
    if not re.match(r'^[a-zA-Z0-9_-]+$', str(key)):
        raise ValidationError(f"Invalid JSON key format: {key}")
    return key

def safe_values(queryset, *fields, **expressions):
    """Safe wrapper for QuerySet.values() to prevent SQL injection with JSONField."""
    sanitized_fields = [sanitize_json_key(field) for field in fields]
    sanitized_expressions = {sanitize_json_key(k): v for k, v in expressions.items()}
    return queryset.values(*sanitized_fields, **sanitized_expressions)

def safe_values_list(queryset, *fields, flat=False, named=False):
    """Safe wrapper for QuerySet.values_list() to prevent SQL injection with JSONField."""
    sanitized_fields = [sanitize_json_key(field) for field in fields]
    return queryset.values_list(*sanitized_fields, flat=flat, named=named) 