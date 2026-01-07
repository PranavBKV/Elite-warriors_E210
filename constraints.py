def detect_constraints(vendor):
    constraints = []

    if vendor.monthly_budget < 3000:
        constraints.append(
            "You can’t run daily ads with a budget below ₹3,000/month"
        )

    if vendor.staff_count <= 1:
        constraints.append(
            "Limited staff — automation is preferred"
        )

    if not vendor.online_presence:
        constraints.append(
            "No online presence — focus on WhatsApp before ads"
        )

    return constraints
