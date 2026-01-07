import streamlit as st
from llm_helper import llm_business_advisor
from openai_ads import generate_ad_content

st.set_page_config(page_title="AI Business Growth Advisor")

st.title("🧠 AI Business Growth Advisor")
st.caption("Product, pricing & ad creation using AI")

# ===================== INPUTS =====================

business_type = st.selectbox(
    "Business Type",
    ["tea shop", "dress shop", "kirana", "electronics"],
    key="business_type"
)

monthly_budget = st.number_input(
    "Monthly Budget (₹)",
    min_value=500,
    step=500,
    key="monthly_budget"
)

inventory_type = st.selectbox(
    "Inventory Type",
    ["fast moving", "slow moving", "seasonal"],
    key="inventory_type"
)

staff_count = st.number_input(
    "Staff Count",
    min_value=1,
    step=1,
    key="staff_count"
)

customer_flow = st.selectbox(
    "Customer Flow",
    ["walk-in", "mixed", "online"],
    key="customer_flow"
)

online_presence = st.selectbox(
    "Online Presence",
    ["instagram", "whatsapp", "none"],
    key="online_presence"
)

# ===================== ACTION =====================

if st.button("🚀 Get AI Advice", key="get_ai_advice"):

    vendor_profile = {
        "business_type": business_type,
        "monthly_budget": monthly_budget,
        "inventory_type": inventory_type,
        "staff_count": staff_count,
        "customer_flow": customer_flow,
        "online_presence": online_presence
    }

    with st.spinner("Analyzing your business..."):
        result = llm_business_advisor(vendor_profile)

    # ===================== PRODUCTS =====================

    st.subheader("🛒 Product Recommendations")

    for idx, product in enumerate(result.get("recommended_products", []), start=1):
        st.markdown(f"### Option {idx}: {product.get('product_name', 'N/A')}")
        st.write(f"**Price per unit:** ₹{product.get('price_per_unit', 0)}")
        st.write(f"**Quantity:** {product.get('quantity', 0)}")
        st.write(f"**Why it sells:** {product.get('reason_for_demand', '')}")

    # ===================== PLATFORMS =====================

    st.subheader("📣 Cost-Effective Marketing Platforms")

    for platform in result.get("platform_recommendations", []):
        st.write(
            f"**{platform.get('platform_name', '')}** – "
            f"{platform.get('why_cost_effective', '')}"
        )

    # ===================== ADS =====================

    st.divider()
    st.subheader("🎨 AI-Generated Ads")

    if result.get("recommended_products"):
        top_product = result["recommended_products"][0]

        with st.spinner("Creating ad content..."):
            ads = generate_ad_content(vendor_profile, top_product)

        st.markdown("### 📸 Instagram Reel Caption")
        st.write(ads.get("instagram_reel_caption", ""))

        st.markdown("### 🖼️ Instagram Post Caption")
        st.write(ads.get("instagram_post_caption", ""))

        st.markdown("### 📲 WhatsApp Broadcast Message")
        st.write(ads.get("whatsapp_message", ""))

        st.markdown("### 🎯 Call To Action")
        st.write(ads.get("call_to_action", ""))

        st.markdown("### 🔖 Hashtags")
        st.write(" ".join(ads.get("hashtags", [])))
