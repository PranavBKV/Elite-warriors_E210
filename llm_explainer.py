def generate_mentor_response(vendor, plan):
    """
    vendor : VendorInput object
    plan   : dict output from generate_business_guidance()

    returns: str (mentor-style explanation)
    """

    lines = []

    # Opening summary
    lines.append(
        f"Based on your ₹{vendor.monthly_budget} monthly budget "
        f"and {vendor.staff_count} staff member(s), "
        "here is a realistic growth plan:"
    )

    # Constraints explanation
    if plan.get("constraints_identified"):
        lines.append("\nImportant considerations:")
        for c in plan["constraints_identified"]:
            lines.append(f"- {c}")

    # Action steps
    lines.append("\nWhat you should do next:")
    for action in plan.get("recommended_actions", []):
        lines.append(f"- {action}")

    # Automation vs human effort
    if plan.get("automation_used"):
        lines.append("\nTasks I can help automate:")
        for a in plan["automation_used"]:
            lines.append(f"- {a}")

    if plan.get("human_effort_required"):
        lines.append("\nTasks best handled manually:")
        for h in plan["human_effort_required"]:
            lines.append(f"- {h}")

    # Closing mentor advice
    lines.append(
        "\nThis approach avoids unnecessary spending and focuses "
        "on what will work best for your current situation. "
        "Once your budget or staff increases, better options will open up."
    )

    return "\n".join(lines)
