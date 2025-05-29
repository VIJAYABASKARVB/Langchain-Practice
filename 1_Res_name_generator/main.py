import streamlit as st
import langchain_helper

st.title("🍽️ Restaurant Name Generator")

cuisine = st.text_input("Enter a Cuisine")

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(f"## 🏷️ {response['restaurant_name'].strip()}")

    menu_items = response['menu_items'].strip().split(",")

    st.write("### 📋 Menu Items")

    # Display menu items in a single line
    formatted_menu = " | ".join([item.strip() for item in menu_items])
    st.write(formatted_menu)
