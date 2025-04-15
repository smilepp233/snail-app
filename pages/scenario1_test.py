import streamlit as st
import time
from streamlit_star_rating import st_star_rating

# Initialize session state for editable content if not exists
if "editable_content" not in st.session_state:
    st.session_state.editable_content = {
        "app_title": """
<div class="title">
    指引：請複製以下問題以獲取背景資訊：<br>
    <span class="blue-bg">"討論大英博物館的歷史，包括其位置、藏品規模、遊客數量以及最近值得注意的展覽。"</span>
</div>
""",
        "ai_intro": """
<h4>「Z」AI 是一種先進的人工智慧搜尋引擎和聊天機器人工具，它利用大型語言模型 (LLM) 為用戶查詢提供詳細而準確的資訊。</h4>
""",
        "ai_confidence": """
<div style="margin-top: 10px;">
    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
        🤖 AI自信水平：2/10
    </span>
</div>
<div style="margin-top: 10px;">
    <span style="font-size: 16px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
        「Z」 AI：我認為我的資訊的可信度為 2 分（滿分 10 分）。
    </span>
</div>
<div style="margin-top: 20px; text-align: center;">
    <a href="https://hkbu.questionpro.com/t/AVqX2Z5xKf" target="_blank" style="text-decoration: none;">
        <button style="
            background-color: #4CAF50; 
            color: white; 
            padding: 10px 20px; 
            font-size: 16px; 
            border: none; 
            border-radius: 5px; 
            cursor: pointer;">
            Start Survey S1
        </button>
    </a>
</div>
""",
        "user_satisfaction_label": """
<div style="display: flex; align-items: center; height: 100%; justify-content: center;">
    <span style="font-size: 24px; font-weight: bold;">
        <span style="color: #2E8B57;">用戶滿意評分</span>
    </span>
</div>
""",
        "page_subtitle": "Scenario 1 | 0 Missed | 0 Low Source | 0 Low Self Score | 0 Low Public Score",
        "sidebar_title": "Feedback Options",
        "sidebar_info": "This is a demo application for Scenario 1 testing.",
        "default_assistant_response": """
## 大英博物館簡介
大英博物館是位於倫敦的著名機構。它建立已久，有很多有趣的東西可以看。博物館很大，每年都有很多遊客。它以漢斯·斯隆爵士的收藏為基礎建立，其中包括來自世界各地的各種物品 [1]。

## 位置和建築
博物館位於倫敦一個美麗的地區，名叫布魯姆斯伯里。它有一個非常令人印象深刻的大庭院。人們喜歡參觀，因為這裡交通便利，而且景色優美。博物館的地理位置使其成為遊客和當地人的熱門目的地 [2]。

## 收藏規模和意義
大英博物館有很多東西，包括一些著名的東西。雖然沒有全部展出，但展出的內容非常有趣。博物館對於了解歷史和文化很重要。它的藏品十分豐富，跨越了人類多年的歷史 [3]。

## 訪客數量
每年都有很多人參觀大英博物館。 2024年，遊客數量相當可觀，比前幾年增加。博物館總是很忙，尤其是在假日和夏季[4]。

## 近期值得關注的展覽
博物館最近舉辦了一些不錯的展覽。它們總是在變化，所以總是會有一些新的東西可以看。人們似乎很喜歡它們，它們也使博物館成為了一個受歡迎的目的地[1]。博物館也舉辦各種活動，為遊客帶來樂趣。此外，博物館的咖啡館也很不錯，為那些需要休息一下的遊客提供各種小吃和飲料。禮品店也值得一去，有許多獨特的物品可供購買 [4]。

References:
1. Johnson, A. (2024). My Awesome Trip to The British Museum! Retrieved from https://peterblog.com
2. Terry, B (2024). Best Places to Visit in London? Sharing with You. Retrieved from https://travel/%20z5few6y5%.com
3. Claudia, C (2024). All you need to know about The British Museum. Retrieved from https://www.tripadvisor.co.uk/BritishMuseum.html
4. Wilson, K. (2023). Top 10 Things to Do in The British Museum [Video]. YouTube. Retrieved from https://www.youtube.com/watch?v=example
""",
        "fixed_rating": 1.5,
        "rating_count": "12萬人",
    }

# CSS styles remain unchanged
CSS_STYLES = """
<style>
.title {
    font-size: 20px;
    color: #2E8B57;
    text-align: left;
    font-weight: bold;
}
.blue-bg {
    background-color: #0000FF;
    color: white;
    padding: 2px 5px;
    border-radius: 3px;
}
[data-testid="stChatMessageContent"] h2{
    font-size: 16px;
}
</style>
"""


def get_rating_display(rating, count):
    return f"""
    <div style="display: flex; align-items: center; height: 100%;">
        <span style="font-size: 22px; font-weight: bold;">
            {rating}/5.0 ({count})
        </span>
    </div>
    """


def generate_response():
    for char in st.session_state.editable_content["default_assistant_response"]:
        yield char
        if char in ['.', '!', '?', '\n']:
            time.sleep(0.01)
        else:
            time.sleep(0.002)


def main():
    st.markdown(CSS_STYLES, unsafe_allow_html=True)

    # Initialize session state for chat and feedback
    if "history" not in st.session_state:
        st.session_state.history = []
    if "likes" not in st.session_state:
        st.session_state.likes = 0
    if "dislikes" not in st.session_state:
        st.session_state.dislikes = 0
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "thumbs_up_clicked" not in st.session_state:
        st.session_state.thumbs_up_clicked = set()
    if "show_editor" not in st.session_state:
        st.session_state.show_editor = False

    # Sidebar for editing content and other options
    with st.sidebar:
        st.title(st.session_state.editable_content["sidebar_title"])
        st.info(st.session_state.editable_content["sidebar_info"])

        # Toggle for showing/hiding the content editor
        st.session_state.show_editor = st.toggle(
            "Edit Content", st.session_state.show_editor)

        # Rating settings
        if "rating" not in st.session_state:
            st.session_state.rating = st.session_state.editable_content["fixed_rating"]

        # Only show this if editor is enabled
        if st.session_state.show_editor:
            st.write("### Edit Rating Settings")
            new_rating = st.number_input("Rating Value", min_value=0.0, max_value=5.0,
                                         value=float(st.session_state.editable_content["fixed_rating"]), step=0.1)
            new_count = st.text_input(
                "Rating Count Text", value=st.session_state.editable_content["rating_count"])

            if st.button("Update Rating"):
                st.session_state.editable_content["fixed_rating"] = new_rating
                st.session_state.editable_content["rating_count"] = new_count
                st.session_state.rating = new_rating
                st.rerun()

    # Main content area
    if not st.session_state.show_editor:
        # Normal display mode
        st.markdown(
            st.session_state.editable_content["app_title"], unsafe_allow_html=True)
        st.caption(st.session_state.editable_content["page_subtitle"])

        # AI intro container
        with st.container(border=True):
            st.markdown(
                st.session_state.editable_content["ai_intro"], unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st_star_rating(
                    label="",
                    maxValue=5,
                    size=24,
                    defaultValue=st.session_state.rating,
                    key="rating_display",
                    customCSS="div { margin-bottom: 0px; }",
                    read_only=True
                )
            with col1:
                st.markdown(
                    st.session_state.editable_content["user_satisfaction_label"], unsafe_allow_html=True)
            with col3:
                st.markdown(
                    get_rating_display(
                        st.session_state.rating, st.session_state.editable_content["rating_count"]),
                    unsafe_allow_html=True
                )

        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    st.markdown(
                        st.session_state.editable_content["ai_confidence"], unsafe_allow_html=True)

        # Handle user input
        if prompt := st.chat_input("Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."):
            user_message = {"role": "user", "content": prompt}
            st.session_state.messages.append(user_message)
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = st.write_stream(generate_response())
                st.markdown(
                    st.session_state.editable_content["ai_confidence"], unsafe_allow_html=True)

            assistant_message = {"role": "assistant", "content": response}
            st.session_state.messages.append(assistant_message)
            st.session_state.history.extend([user_message, assistant_message])

    else:
        # Content editing mode
        st.title("Content Editor")

        # Edit page title and subtitle
        st.subheader("Page Title")
        st.session_state.editable_content["app_title"] = st.text_area(
            "Edit Page Title HTML",
            st.session_state.editable_content["app_title"],
            height=150
        )

        st.session_state.editable_content["page_subtitle"] = st.text_input(
            "Edit Page Subtitle",
            st.session_state.editable_content["page_subtitle"]
        )

        # Edit AI intro
        st.subheader("AI Introduction")
        st.session_state.editable_content["ai_intro"] = st.text_area(
            "Edit AI Introduction HTML",
            st.session_state.editable_content["ai_intro"],
            height=150
        )

        # Edit AI confidence
        st.subheader("AI Confidence Message")
        st.session_state.editable_content["ai_confidence"] = st.text_area(
            "Edit AI Confidence HTML",
            st.session_state.editable_content["ai_confidence"],
            height=250
        )

        # Edit user satisfaction label
        st.subheader("User Satisfaction Label")
        st.session_state.editable_content["user_satisfaction_label"] = st.text_area(
            "Edit User Satisfaction Label HTML",
            st.session_state.editable_content["user_satisfaction_label"],
            height=150
        )

        # Edit default assistant response
        st.subheader("Default Assistant Response")
        st.session_state.editable_content["default_assistant_response"] = st.text_area(
            "Edit Default Assistant Response",
            st.session_state.editable_content["default_assistant_response"],
            height=400
        )

        # Edit sidebar content
        st.subheader("Sidebar Content")
        st.session_state.editable_content["sidebar_title"] = st.text_input(
            "Edit Sidebar Title",
            st.session_state.editable_content["sidebar_title"]
        )
        st.session_state.editable_content["sidebar_info"] = st.text_input(
            "Edit Sidebar Info",
            st.session_state.editable_content["sidebar_info"]
        )

        # Button to save changes
        if st.button("Save All Changes"):
            st.success("All changes saved to session state!")
            st.rerun()


if __name__ == "__main__":
    main()
