from datetime import datetime
import streamlit as st
from google import genai
from google.genai import types

# ======================================
# API KEY
# ======================================

api_key = st.secrets["API"]
client = genai.Client(api_key=api_key)

# ======================================
# SYSTEM INSTRUCTION
# ======================================

SYSTEM_INSTRUCTION = """
You are Capital Buddy, a friendly Personal Finance Assistant.

Your responsibilities:
- Explain budgeting.
- Explain saving money.
- Explain personal finance concepts.
- Explain loans and EMI.
- Provide beginner-friendly guidance.

Rules:
- Keep answers simple.
- Use easy language.
- Do NOT recommend stocks.
- Do NOT recommend cryptocurrencies.
- Do NOT provide investment advice.
- Do NOT promise profits.
- Focus only on financial education.
- Use examples whenever possible.
"""

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Capital Buddy",
    page_icon="💰",
    layout="wide",
)

# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

[data-testid="stChatMessage"] {
border-radius:15px;
padding:10px;
margin-bottom:10px;
}

[data-testid="stChatMessage"]:has([data-testid=="chatAvatarIcon-assistant"]) {
background-color:#E0F2FE;
}

[data-testid="stChatMessage"]::has([data-testid="chatAvatarIcon-user"]) {
background-color:#F0F9FF;
}

</style>
""", unsafe_allow_html=True)



# ======================================
# HEADER
# ======================================

st.markdown("""
<h1 style='text-align:center;color:#0EA5E9;'>
💰 Capital Buddy
</h1>

<h4 style='text-align:center;color:#0369A1;'>
Your AI Personal Finance Assistant
</h4>
""", unsafe_allow_html=True)

current_time = datetime.now().strftime("%d %b %Y | %I:%M %p")
st.markdown(
    f"""
    <div style='text-align:center;
                padding:8px;
                color:#0369A1;
                font-weight:bold;'>
        📅 {current_time}
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📈 Budgeting")

with col2:
    st.info("💰 Savings")

with col3:
    st.info("🏦 Loans")

with col4:
    st.info("📚 Finance Learning")

# ======================================
# METRICS
# ======================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Finance Topics", "100+")

with col2:
    st.metric("💡Budget Tips", "50+")

with col3:
    st.metric("🤖 Available", "24/7")


# ======================================
# MARKET SNAPSHOT
# ======================================

st.subheader("📈 Market Snapshot")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("NIFTY 50\n\n25,420 (+0.85%)")

with col2:
    st.success("SENSEX\n\n83,100 (+0.82%)")

with col3:
    st.success("BANK NIFTY\n\n55,420 (+1.05%)")


st.markdown("""
<div style="
background:#DBEAFE;
padding:15px;
border-radius:15px;
margin-top:10px;
margin-bottom:20px;">
<h3 style="color:#1E40AF;">💳 Money Tip of the Day</h3>
<p style="color:black;">
Save at least 20% of your income before planning non-essential expenses.
</p>
</div>
""", unsafe_allow_html=True)

from datetime import datetime

now = datetime.now()

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"📅 Date: {now.strftime('%d-%m-%Y')}")

with col2:
    st.info(f"🕒 Time: {now.strftime('%I:%M %p')}")

with col3:
    st.info(f"📆 Day: {now.strftime('%A')}")


st.subheader("📊 Financial Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Savings Rate", "20%")

with col2:
    st.metric("📈 Inflation", "5.2%")

with col3:
    st.metric("🏦 Repo Rate", "6.50%")

with col4:
    st.metric("💵 USD/INR", "83.20")

# ======================================
# WELCOME CARD
# ======================================

st.subheader("🧮 Quick EMI Calculator")

loan = st.number_input("Loan Amount ₹", 1000, 10000000, 100000)

rate = st.number_input("Annual Interest Rate (%)", 1.0, 30.0, 8.5)

years = st.number_input("Loan Tenure (Years)", 1, 30, 5)

if st.button("Calculate EMI"):
    monthly_rate = rate / 12 / 100
    months = years * 12

    emi = (
        loan
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

    st.success(f"Estimated EMI: ₹{emi:,.2f}")

st.markdown("""
<div style="
padding:20px;
border-radius:15px;
background: linear-gradient(135deg, #E0F2FE, #BAE6FD);
border:1px solid #7DD3FC;
margin-bottom:20px;
color:#0F172A;">
<h3>👋 Welcome to Capital Buddy</h3>

<p>Your smart companion for:</p>

✅ Budgeting <br>
✅ Savings <br>
✅ Loans & EMI <br>
✅ Personal Finance <br>
✅ Financial Planning

</div>
""", unsafe_allow_html=True)



# ======================================
# WELCOME CARD
# ======================================

finance_tips = [
    "Save at least 20% of your income.",
    "Track daily expenses.",
    "Build an emergency fund.",
    "Avoid unnecessary debt.",
    "Review your budget monthly."
]

import random

st.info(
    "💡 Today's Finance Tip:\n\n"
    + random.choice(finance_tips)
)

st.markdown(...)

# ======================================
# DAILY EXPENSE TRACKER
# ======================================

st.subheader("💵 Daily Expense Tracker")

expense = st.number_input(
    "Today's Expense (₹)",
    min_value=0
)

if st.button("Add Expense"):
    st.session_state.setdefault("expenses", [])
    st.session_state.expenses.append(expense)

if "expenses" in st.session_state:
    st.write("Total Expenses")
    st.success(f"₹{sum(st.session_state.expenses):,.0f}")

# ======================================
# SPENDING BREAKDOWN
# ======================================

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Category": ["Food", "Transport", "Shopping", "Bills"],
    "Amount": [3000, 2000, 4000, 2500]
})

st.subheader("📊 Spending Breakdown")

colors = ["#38BDF8", "#22C55E", "#F59E0B", "#EF4444"]

fig, ax = plt.subplots(figsize=(2, 2))

ax.pie(
    data["Amount"],
    labels=data["Category"],
    autopct="%1.1f%%",
    startangle=50,
    colors=colors,
    textprops={
        "fontsize": 6,
        "fontweight": "bold"
    }
)

ax.set_title(
    "Monthly Expense Distribution",
    fontsize=6,
    fontweight="bold"
)

st.pyplot(
    fig,
    use_container_width=False
)

    
# ======================================
# SIDEBAR
# ======================================

with st.sidebar:



# ======================================
# SIDEBAR
# ======================================

    st.sidebar.success("🟢 AI Online")
        with st.sidebar:

        st.title("💰 Capital Buddy")

    st.metric(
    "💬 Total Messages",
    len(st.session_state.get("messages", []))
)

    st.info(
        "Learn budgeting, savings, EMI, loans and personal finance."
    )

    st.divider()

    st.subheader("Sample Questions")

    st.write("💡 What is budgeting?")
    st.write("💡 What is EMI?")
    st.write("💡 What is compound interest?")
    st.write("💡 How can I save money?")
    st.write("💡 What is an emergency fund?")
    st.write("💡 Explain the 50-30-20 rule")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ======================================
# CHAT HISTORY
# ======================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:

    with st.chat_message("assistant", avatar="💰"):

        st.markdown("""
### 👋 Welcome to Capital Buddy

I can help you learn about:

✅ Budgeting

✅ Savings

✅ EMI

✅ Loans

✅ Personal Finance

Ask me anything!
""")    

for message in st.session_state.messages:

    avatar = "🧑" if message["role"] == "user" else "💰"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

st.subheader("🔥 Popular Questions")

questions = [
    "What is budgeting?",
    "How can I save ₹5000 every month?",
    "What is EMI?",
    "What is an emergency fund?",
    "Explain compound interest",
    "What is the 50-30-20 rule?"
]

cols = st.columns(3)

for i, question in enumerate(questions):
    with cols[i % 3]:
        if st.button(question):
            st.session_state.quick_question = question
            st.rerun()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Budgeting"):
        st.session_state.quick_question = "What is budgeting?"

with col2:
    if st.button("🏦 EMI"):
        st.session_state.quick_question = "What is EMI?"

with col3:
    if st.button("💰 Savings"):
        st.session_state.quick_question = "How can I save money?"


st.subheader("⚡ Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("💰 Savings")

with col2:
    st.button("🏦 EMI")

with col3:
    st.button("📊 Budget")

with col4:
    st.button("📈 Stocks")

# ======================================
# CHAT INPUT
# ======================================

prompt = st.session_state.get("quick_question")

if not prompt:
    prompt = st.chat_input(
        "Ask Capital Buddy about budgeting, savings, EMI or finance..."
    )

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    st.session_state.quick_question = None

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="💰"):

        try:

            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION,
                    temperature=0.5,
                ),
            )

            answer = response.text

        except Exception as e:
            answer = f"Error: {str(e)}"

        st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

