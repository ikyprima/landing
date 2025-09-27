import frappe

def get_context(context):
    # Ambil course
    context.courses = frappe.get_all(
        "LMS Course",
        fields=["name", "title", "image", "short_introduction"],
        order_by="creation desc",
        limit=4
    )

    # Ambil batch
    context.batches = frappe.get_all(
        "LMS Batch",
        fields=["name", "title", "start_date", "end_date", "description"],
        order_by="start_date desc",
        limit=5
    )

    user = frappe.session.user
    # Default guest
    context.user_fullname = None
    context.user_image = None
    context.username = None

    if user and user != "Guest":
        # Ambil data user langsung dari DocType
        user_doc = frappe.get_doc("User", user)

        context.username = user_doc.username
        context.user_fullname = user_doc.full_name or user_doc.first_name or user
        context.user_image = user_doc.user_image or "/assets/frappe/images/default-avatar.png"
    
    return context

@frappe.whitelist()
def get_latest_batches(limit=5):
    return frappe.get_all(
        "LMS Batch",
        fields=["name", "title", "start_date", "description", "end_date"],
        order_by="start_date desc",
        limit=limit
    )