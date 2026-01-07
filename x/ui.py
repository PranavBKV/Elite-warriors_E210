import streamlit as st
from app.logic import llm_business_advisor

st.set_page_config(page_title="AI Business Growth Manager", layout="centered")

st.title("🧠 AI Business Growth Manager")
st.caption("Practical guidance for small business owners (India-focused)")

# ===================== INPUT SECTION =====================

product_name = st.text_input(
    "Product / Service Name",
    placeholder="Example: Tea, Saree, Bluetooth Speaker, Snacks"
)

budget = st.number_input(
    "Total Monthly Budget (₹)",
    min_value=500,
    step=500
)

ad_investment_choice = st.radio(
    "Are you planning to invest in advertisements?",
    ["Yes", "No"]
)

# ===================== ACTION =====================

if st.button("📊 Get Business Guidance"):

    if not product_name:
        st.warning("Please enter a product or service name.")
    else:
        with st.spinner("Analyzing your business realistically..."):
            result = llm_business_advisor(
                product_name=product_name,
                budget=budget,
                ad_investment_choice=ad_investment_choice
            )

        # ===================== OUTPUT SECTIONS =====================

        st.subheader("📈 Current Market Price (India)")
        market = result.get("market_price_analysis", {})
        st.write(f"**Price Range:** {market.get('price_range_inr', '')}")
        st.write(f"**Category:** {market.get('category', '')}")
        st.write(market.get("notes", ""))

        st.subheader("💰 Resource-Aware Budget Utilization")
        budget_use = result.get("budget_utilization", {})
        st.write(f"**Procurement:** {budget_use.get('procurement', '')}")
        st.write(f"**Operations:** {budget_use.get('operations', '')}")
        st.write(f"**Advertising:** {budget_use.get('advertising', '')}")

        st.subheader("📊 Estimated Profit")
        profit = result.get("profit_estimation", {})
        st.write(f"**Selling Price / Unit:** {profit.get('selling_price_per_unit', '')}")
        st.write(f"**Profit Margin:** {profit.get('profit_margin', '')}")
        st.write(f"**Estimated Total Profit:** {profit.get('estimated_total_profit', '')}")
        st.write(profit.get("assumptions", ""))

        st.subheader("📣 Best Platforms for Promotion")
        for platform in result.get("best_platforms", []):
            st.write(f"• {platform}")

        st.subheader("🚫 Platforms to Avoid")
        for platform in result.get("platforms_to_avoid", []):
            st.write(f"• {platform}")

        st.subheader("🤝 Fundraising & Collaboration Options")
        for option in result.get("fundraising_and_collaboration", []):
            st.write(f"• {option}")

