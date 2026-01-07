import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def llm_business_advisor(vendor_profile):
    """
    LLM business advisor
    - Enforced JSON schema
    - Always returns Python dict
    """

    prompt = f"""
You are a practical business mentor who understands real Indian market prices.

Think like a real shop owner.
Avoid unrealistically low prices.
Electronics and clothing should never be priced like snacks.

Business context:
{json.dumps(vendor_profile, indent=2)}

Return ONLY data that fits the required JSON schema.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "business_advice",
                "schema": {
                    "type": "object",
                    "properties": {
                        "recommended_products": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "product_name": {"type": "string"},
                                    "price_per_unit": {"type": "number"},
                                    "quantity": {"type": "number"},
                                    "reason_for_demand": {"type": "string"}
                                },
                                "required": [
                                    "product_name",
                                    "price_per_unit",
                                    "quantity",
                                    "reason_for_demand"
                                ]
                            }
                        },
                        "platform_recommendations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "platform_name": {"type": "string"},
                                    "why_cost_effective": {"type": "string"}
                                },
                                "required": ["platform_name", "why_cost_effective"]
                            }
                        },
                        "expansion_pitch": {"type": "string"},
                        "support_needs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "type": {"type": "string"},
                                    "description": {"type": "string"}
                                },
                                "required": ["type", "description"]
                            }
                        },
                        "collaboration_channels": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "channel_name": {"type": "string"},
                                    "why_suitable": {"type": "string"}
                                },
                                "required": ["channel_name", "why_suitable"]
                            }
                        }
                    },
                    "required": [
                        "recommended_products",
                        "platform_recommendations",
                        "expansion_pitch",
                        "support_needs",
                        "collaboration_channels"
                    ]
                }
            }
        }
    )

    # ✅ This is now GUARANTEED to be valid JSON
    return json.loads(response.choices[0].message.content)
