import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_business_advisor(product_name, budget, ad_investment_choice):
    """
    Virtual Business Growth Manager
    Uses a resource-aware, realistic prompt for Indian vendors
    """

    prompt = f"""
You are an AI Assistant acting as a virtual business growth manager for non-technical vendors.

Your goal is to provide resource-aware, realistic, and actionable guidance that helps the vendor grow their business while respecting real-world constraints.

User Inputs:
- Product / Service Name: {product_name}
- Total Budget Available (INR): {budget}
- Is the user investing in advertisements: {ad_investment_choice}

Your response MUST include the following sections, clearly separated with headings:

1. Current Market Price of the Product in India
   - Provide an estimated market price range
   - Clearly state whether the product falls under budget, mid-range, or premium
   - Keep estimates realistic and conservative

2. Resource-Aware Budget Utilization
   Based on the given budget, clearly explain how the money should be divided into:
   - Procurement / wholesale cost
   - Human resources and operational support
   - Advertisement and promotion (ONLY if ad investment is selected)

3. Estimated Profit Based on the Investment
   - Expected selling price per unit
   - Approximate profit margin
   - Estimated total profit achievable with the given budget
   - Explain assumptions briefly and realistically

4. Best Platforms for Promotion (If Ads Are Selected)
   - Recommend platforms suitable for the product and budget
   - Explain why they are appropriate

5. Platforms to Avoid
   - Mention platforms that are not suitable
   - Explain reasons (cost, complexity, low ROI)

6. Fundraising, Collaboration, and Community Support Options
   - Suggest fundraising methods
   - Suggest collaboration opportunities
   - Explain how they help beyond advertising

Constraints:
- Assume Indian market conditions
- Focus on simplicity and clarity
- Avoid jargon
- Be conservative and realistic
- Do NOT include step-by-step action plans
- Focus on value creation and budget efficiency

Return the response in STRICT JSON using this schema:
{{
  "market_price_analysis": {{
    "price_range_inr": "",
    "category": "",
    "notes": ""
  }},
  "budget_utilization": {{
    "procurement": "",
    "operations": "",
    "advertising": ""
  }},
  "profit_estimation": {{
    "selling_price_per_unit": "",
    "profit_margin": "",
    "estimated_total_profit": "",
    "assumptions": ""
  }},
  "best_platforms": [],
  "platforms_to_avoid": [],
  "fundraising_and_collaboration": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)

