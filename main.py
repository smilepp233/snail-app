import streamlit as st
import os
import importlib

# Hide all scenario pages from sidebar
st.set_page_config(page_title="Snail Sleep Assignment",
                   page_icon="🐌", layout="wide")

# Run this once to create the .streamlit/config.toml with the right settings
if not os.path.exists(".streamlit/config.toml"):
    os.makedirs(".streamlit", exist_ok=True)
    with open(".streamlit/config.toml", "w") as f:
        f.write("""
[browser]
gatherUsageStats = false

[server]
runOnSave = true

[theme]
primaryColor = "#2E8B57"
        
[ui]
hideSidebarNav = true
        """)

# Your existing app code


def main():
    # Custom CSS for a professional academic look
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #2E8B57;
            text-align: center;
            font-weight: bold;
        }
        .warning {
            color: #FF4500;
            font-weight: bold;
            text-align: center;
        }
        .content {
            font-size: 18px;
            line-height: 1.6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and intro
    st.markdown('<div class="title">Snail Sleep: A Critical Assignment 🐌</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="warning">Worth 50% of the Course Grade</div>',
                unsafe_allow_html=True)
    st.markdown("---")

    # Add custom sidebar with organized navigation
    with st.sidebar:
        st.title("Navigation")

        st.subheader("Case Selection")
        for i in range(1, 17):
            if st.button(f"Case {i}", key=f"case_btn_{i}"):
                # Link to the corresponding case file
                st.switch_page(f"pages/case{i}.py")

    # Description and purpose
    st.markdown("""
    <div class="content">
        <h2>Assignment Overview</h2>
        <p>This project explores the fascinating topic of snail sleep, leveraging AI tools to create an informative and engaging study. As a major assessment contributing 50% to the final grade, this assignment requires a deep dive into the biology, behavior, and ecological significance of how snails rest.</p>
    </div>
    """, unsafe_allow_html=True)

    # Display cases in a grid
    st.subheader("Select a Case:")
    cols = st.columns(4)
    for i in range(1, 17):
        col_idx = (i - 1) % 4
        with cols[col_idx]:
            if st.button(f"Case #{i}", key=f"grid_case_{i}"):
                st.switch_page(f"pages/case{i}.py")


if __name__ == "__main__":
    main()
