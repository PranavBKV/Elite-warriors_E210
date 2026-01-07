def decide_effort_split(vendor):
    automation = []
    human_effort = []

    if vendor.staff_count <= 1:
        automation.extend([
            "Caption generation",
            "Hashtag suggestions"
        ])
    else:
        human_effort.append("Manual posting")

    human_effort.extend([
        "Customer interaction",
        "Content recording"
    ])

    return automation, human_effort
