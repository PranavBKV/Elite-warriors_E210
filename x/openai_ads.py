import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ad_content(vendor_profile, top_product):
    """
    OpenAI-based ad content generator
    TEXT ONLY (Instagram + WhatsApp)
    """

    prompt = f"""
You are a creative social media marketer for small local Indian businesses.

Business details:
{json.dumps(vendor_profile, indent=2)}

Featured product:
{json.dumps(top_product, indent=2)}

Create SHORT, SIMPLE promotional content.

Generate:
1. Instagram Reel caption
2. Instagram Post caption
3. WhatsApp broadcast message
4. Call-to-action
5. 5 hashtags

Tone:
- Friendly
- Local
- Honest
- No exaggeration

Return STRICT JSON ONLY in this format:
{{
  "instagram_reel_caption": "",
  "instagram_post_caption": "",
  "whatsapp_message": "",
  "call_to_action": "",
  "hashtags": []
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
