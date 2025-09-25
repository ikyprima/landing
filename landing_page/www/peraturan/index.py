import frappe

def get_context(context):
    context.courses = frappe.get_all(
        "LMS Course",
        fields=["name", "title", "image", "short_introduction"],
        limit=5
    )
    return context
