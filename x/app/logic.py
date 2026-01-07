def budget_strategy(budget):
    if budget <= 2000:
        return "Avoid paid ads. Focus on organic promotion."
    elif budget <= 5000:
        return "Run ads only during festivals or special offers."
    else:
        return "Use limited paid ads with organic growth."


def platform_strategy(profile):
    actions = []

    if profile.customer_flow == "walk-in":
        actions.append("Use WhatsApp broadcast for daily offers")

    if profile.online_presence == "instagram":
        actions.append("Post 3 Instagram reels per week")
    elif profile.online_presence == "none":
        actions.append("Create a basic Instagram account")

    return actions


def automation_decision(profile):
    if profile.staff_count <= 1:
        return "Manual posting is sufficient. Avoid automation tools."
    return "Use simple scheduling tools to save time."


def get_candidate_products(business_type):
    catalog = {
        "tea shop": [
            {"name": "Samosa", "price": 15},
            {"name": "Biscuits", "price": 10},
            {"name": "Puffs", "price": 25}
        ],
        "kirana": [
            {"name": "Rice (1kg)", "price": 55},
            {"name": "Cooking Oil (1L)", "price": 160},
            {"name": "Snacks", "price": 20}
        ],
        "clothing": [
            {"name": "T-Shirts", "price": 300},
            {"name": "Leggings", "price": 250}
        ]
    }
    return catalog.get(business_type, [])


def final_advice(profile):
    candidates = get_candidate_products(profile.business_type)

    affordable = [
        p for p in candidates if p["price"] <= profile.monthly_budget
    ]

    return {
        "business_type": profile.business_type,
        "monthly_budget": profile.monthly_budget,
        "candidate_products": affordable,
        "budget_advice": budget_strategy(profile.monthly_budget),
        "platform_actions": platform_strategy(profile),
        "automation_advice": automation_decision(profile)
    }
