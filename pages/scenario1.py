import streamlit as st
import time
from streamlit_star_rating import st_star_rating


st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] h2{
        font-size: 16px;
    }
   
    ### Custom CSS for the chat message container
    </style>
    """, unsafe_allow_html=True
)


def generate_response():
    """
    Function to generate the assistant's response with a typing effect.
    Args:
        prompt (str): The user's input prompt.
    Returns:
        str: The assistant's response.
    """

    response = (
        "## 大英博物館簡介\n"
        "大英博物館是位於倫敦的著名機構。它建立已久，有很多有趣的東西可以看。博物館很大，每年都有很多遊客。它以漢斯·斯隆爵士的收藏為基礎建立，其中包括來自世界各地的各種物品 [1]。\n\n"
        "## 位置和建築\n"
        "博物館位於倫敦一個美麗的地區，名叫布魯姆斯伯里。它有一個非常令人印象深刻的大庭院。人們喜歡參觀，因為這裡交通便利，而且景色優美。博物館的地理位置使其成為遊客和當地人的熱門目的地 [2]。\n\n"
        "## 收藏規模和意義\n"
        "大英博物館有很多東西，包括一些著名的東西。雖然沒有全部展出，但展出的內容非常有趣。博物館對於了解歷史和文化很重要。它的藏品十分豐富，跨越了人類多年的歷史 [3]。\n\n"
        "## 訪客數量\n"
        "每年都有很多人參觀大英博物館。 2024年，遊客數量相當可觀，比前幾年增加。博物館總是很忙，尤其是在假日和夏季[4]。\n\n"
        "## 近期值得關注的展覽\n"
        "博物館最近舉辦了一些不錯的展覽。它們總是在變化，所以總是會有一些新的東西可以看。人們似乎很喜歡它們，它們也使博物館成為了一個受歡迎的目的地[1]。博物館也舉辦各種活動，為遊客帶來樂趣。此外，博物館的咖啡館也很不錯，為那些需要休息一下的遊客提供各種小吃和飲料。禮品店也值得一去，有許多獨特的物品可供購買 [4]。\n\n"
        "References:\n"
        "1. Anonymous. (2008). My Trip to The British Museum! Retrieved from https://n&tab=TT&sl=en&tl=zh-TW&op.com\n"
        "2. Terry, B (2004). Sharing My Trip to London with You. Retrieved from https://en&tl=zh-TW&text=make%20the%20below%\n"
        "3. Anonymous. (2006). Visiting UK Museums. Retrieved from https://%20uk%203%3A%0A%0A.html\n"
        "4. Wilson, K. (n.d). Experiences in The British Museum. Retrieved from https://?q=21899&tip=sid&clean=0\n\n"
    )
    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            # Slightly longer pause after sentences and line breaks
            time.sleep(0.01)
        else:
            time.sleep(0.002)  # Faster typing for regular characters


def save_feedback(index):
    st.session_state.history[index][
        "feedback"] = st.session_state[f"feedback_{index}"]


def main():

    st.markdown("""
        <style>
        .title {
            font-size: 20px;  /* Bigger title */
            color: #2E8B57;
            text-align: left;
            font-weight: bold;
        }
        .blue-bg {
            background-color: #0000FF;  /* Blue background */
            color: white;  /* White text for contrast */
            padding: 2px 5px;  /* Small padding for better appearance */
            border-radius: 3px;  /* Slight rounding */
        }
      
        </style>
        """,
                unsafe_allow_html=True
                )
    st.markdown(
        """
            <div class="title">
                指引：請複製以下問題以獲取背景資訊：
                </br>
                <span class="blue-bg" style="visibility=hidden;">
                “討論大英博物館的歷史，包括其位置、藏品規模、遊客數量以及最近值得注意的展覽。”</span>
            </div>
            """,
        unsafe_allow_html=True
    )

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

   # Initialize rating default value (but don't store in session_state yet)
    fixed_rating = 1.5
    rating_count = "12萬人"

    if "rating" not in st.session_state:
        st.session_state.rating = fixed_rating

    with st.container(border=True):
        st.markdown(
            """
            <h4>「Z」AI 是一種先進的人工智慧搜尋引擎和聊天機器人工具，它利用大型語言模型 (LLM) 為用戶查詢提供詳細而準確的資訊。</h4>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st_star_rating(
                label="",
                maxValue=5,
                size=24,
                defaultValue=fixed_rating,
                key="rating",
                customCSS="div { margin-bottom: 0px; }",
                read_only=True
            )

        with col1:
            st.markdown(
                """
                <div style="display: flex; align-items: center; height: 100%; justify-content: center;">
                    <span style="font-size: 24px; font-weight: bold;">
                        <span style="color: #2E8B57;">用戶滿意評分</span>
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col3:
            st.markdown(
                f"""
                <div style="display: flex; align-items: center; height: 100%;">
                    <span style="font-size: 22px; font-weight: bold;">
                        {fixed_rating}/5.0 ({rating_count})
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # Initialize feedback keys if they don't exist
    for i in range(len(st.session_state.history)):
        key = f"feedback_{i}"
        if key not in st.session_state:
            st.session_state[key] = None

    # Display chat history
    for i, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Add feedback buttons for assistant messages

    # Handle new user input
    if prompt := st.chat_input("Discuss the history of the British Museum, including its location, collection size, visitor numbers, and notable recent exhibitions."):
        # Add user message to chat history
        user_message = {"role": "user", "content": prompt}
        st.session_state.history.append(user_message)
        st.session_state.messages.append(user_message)
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response with typing effect

        # Create a unique but consistent key for this message
        message_id = len(st.session_state.messages) - 1

        with st.chat_message("assistant"):
            response = st.write_stream(generate_response())
            st.markdown(
                """
                <div style="margin-top: 10px;">
                    <span style="font-size: 24px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
                        🤖 AI自信水平：2/10
                    </span>
                </div>
                <div style="margin-top: 10px;">
                    <span style="font-size: 24px; font-weight: bold; color: #2E8B57; border: 1px solid #2E8B57; padding: 5px; border-radius: 5px;">
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
                unsafe_allow_html=True
            )
        assistant_message = {"role": "assistant",
                             "content": response}
        st.session_state.history.append(assistant_message)
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
