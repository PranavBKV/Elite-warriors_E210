def analyze_constraints(profile):
    constraints = []

    if profile.monthly_budget <= 2000:
        constraints.append("low_budget")

    if profile.staff_count <= 1:
        constraints.append("low_staff")

    if profile.customer_flow == "walk-in":
        constraints.append("local_customers")

    if profile.online_presence == "none":
        constraints.append("no_online_base")

    return constraints


def budget_strategy(budget):
    if budget <= 2000:
        return "Do not run daily ads. Focus on organic promotion."
    elif budget <= 5000:
        return "Run ads only during festivals or special offers."
    else:
        return "Use limited paid ads along with organic growth."


def platform_strategy(profile, constraints):
    actions = []

    if "local_customers" in constraints:
        actions.append("Use WhatsApp broadcast for daily offers")

    if profile.online_presence == "instagram":
        actions.append("Post 3 Instagram reels per week")

    if profile.online_presence == "none":
        actions.append("Create a basic Instagram account")

    return actions


def automation_decision(constraints):
    if "low_staff" in constraints:
        return "Avoid automation tools. Manual posting is sufficient."
    else:
        return "Use simple scheduling tools to save time."


def generate_instagram_content(business_type):
    captions = {
        "kirana": "Fresh daily essentials 🛒 Visit our store today!",
        "tea shop": "Hot tea & snacks ☕ Perfect evening break!",
        "clothing": "New arrivals 👕 Style within your budget!"
    }

    hashtags = ["#ShopLocal", "#SupportSmallBusiness", "#LocalStore"]

    return captions.get(business_type, "Visit our store today!"), hashtags


def final_advice(profile):
    constraints = analyze_constraints(profile)

    caption, hashtags = generate_instagram_content(profile.business_type)

    return {
        "budget_advice": budget_strategy(profile.monthly_budget),
        "platform_actions": platform_strategy(profile, constraints),
        "automation_advice": automation_decision(constraints),
        "instagram_caption": caption,
        "hashtags": hashtags
    }
