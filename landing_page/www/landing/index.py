import frappe

def get_context(context):
    # Ambil course
    context.courses = frappe.get_all(
        "LMS Course",
        fields=["name", "title", "image", "short_introduction"],
        order_by="creation desc",
        limit=5
    )

    # Ambil batch
    context.batches = frappe.get_all(
        "LMS Batch",
        fields=["name", "title", "start_date", "end_date", "description"],
        order_by="start_date desc",
        limit=5
    )
    return context

@frappe.whitelist()
def get_latest_batches(limit=5):
    return frappe.get_all(
        "LMS Batch",
        fields=["name", "title", "start_date", "description", "end_date"],
        order_by="start_date desc",
        limit=limit
    )