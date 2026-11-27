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


def clear_expenses():
    st.session_state.expenses.clear()


def add_space(height=30):
    st.markdown(
        f'<div style="height: {height}px;"></div>',
        unsafe_allow_html=True
    )


st.set_page_config(
    page_title="IT Step",
    page_icon="_",
    initial_sidebar_state="expanded"
)

if "expenses" not in st.session_state:
    st.session_state["expenses"] = []


# Sidebar

with st.sidebar:

    st.header("ხარჯის დამატება")

    st.selectbox(
        "აირჩიეთ კატეგორია",
        ["საკვები", "ტრანსპორტი", "სხვა"],
        key="category"
    )

    st.text_input(
        "ხარჯი",
        key="expense_name"
    )

    st.number_input(
        "თანხა",
        value=0.0,
        key="expense_amount"
    )

    st.button(
        "დამატება",
        on_click=add_expense
    )


# Main area

st.title("პირადი ბიუჯეტის ტრეკერი")
st.caption("დღიური ხარჯების მთვლელი")

add_space(50)


# Category filter

filter_col, empty_col = st.columns([1, 3])

with filter_col:
    filter_category = st.selectbox(
        "კატეგორიით ფილტრი",
        ["ყველა", "საკვები", "ტრანსპორტი", "სხვა"],
        key="filter_category"
    )


# Filter expenses

if filter_category == "ყველა":
    filtered_expenses = st.session_state.expenses
else:
    filtered_expenses = [
        expense
        for expense in st.session_state.expenses
        if expense["category"] == filter_category
    ]


# Dataframe and Clear button

dataframe_col, clear_button_col = st.columns(
    [5, 1],
    vertical_alignment="top"
)

with dataframe_col:
    st.dataframe(filtered_expenses)

with clear_button_col:
    st.button("გასუფთავება", on_click=clear_expenses)


# Total expenses

total_expenses = sum(
    expense["amount"]
    for expense in st.session_state.expenses
)

add_space(50)

st.metric(
    label="მთლიანი დანახარჯი",
    value=f"{total_expenses:.2f} ₾"
)