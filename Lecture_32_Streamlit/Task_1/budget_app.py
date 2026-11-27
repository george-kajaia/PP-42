import streamlit as st

def add_expense():
    expense = {
        "category": st.session_state.category,
        "name": st.session_state.expense_name,
        "amount": st.session_state.expense_amount
    }

    st.session_state.expenses.append(expense)

    # Clear input boxes
    st.session_state.expense_name = ""
    st.session_state.expense_amount = 0.0

def add_space(height=30):
    st.markdown(
        f'<div style="height: {height}px;"></div>',
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="IT Step",
    page_icon="_"
)

st.title("პირადი ბიუჯეტის ტრეკერი")
st.caption("დღიური ხარჯების მთვლელი")

add_space(50)

category_col, expense_name_col, expense_amount_col, submit_button_col = st.columns(4, vertical_alignment="bottom")

with category_col:
    st.selectbox("აირჩიეთ კატეგორია", ["საკვები", "ტრანსპორტი", "სხვა"], key="category")

with expense_name_col:
    st.text_input("ხარჯი", key="expense_name")

with expense_amount_col:
    st.number_input("თანხა", value=0.0, key="expense_amount")

with submit_button_col:
    st.button("დამატება", on_click=add_expense)

if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

st.dataframe(st.session_state.expenses)

total_expenses = sum(expense["amount"] for expense in st.session_state.expenses)

add_space(50)

st.metric(
    label="მთლიანი დანახარჯი",
    value=f"{total_expenses:.2f} ₾"
)