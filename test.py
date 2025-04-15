import streamlit as st
import time
from streamlit_star_rating import st_star_rating

# 預設所有 chatbot 文字
default_texts = {
    "response": """## 大英博物館簡介
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
    "title": "## 大英博物館簡介",
    "intro": "大英博物館是位於倫敦的著名機構。它建立已久，有很多有趣的東西可以看。博物館很大，每年都有很多遊客。",
    "location": "## 位置和建築\n博物館位於倫敦一個美麗的地區，名叫布魯姆斯伯里。它有一個非常令人印象深刻的大庭院。",
    "collection": "## 收藏規模和意義\n大英博物館有很多東西，包括一些著名的東西。雖然沒有全部展出，但展出的內容非常有趣。",
    "visitors": "## 訪客數量\n每年都有很多人參觀大英博物館。2024年，遊客數量相當可觀，比前幾年增加。",
    "exhibitions": "## 近期值得關注的展覽\n博物館最近舉辦了一些不錯的展覽。它們總是在變化，所以總是會有一些新的東西可以看。",
    "ai_confidence": "🤖 AI自信水平：2/10",
    "ai_comment": "「Z」 AI：我認為我的資訊的可信度為 2 分（滿分 10 分）。",
    "instruction": "指引：請複製以下問題以獲取背景資訊：\n“討論大英博物館的歷史，包括其位置、藏品規模、遊客數量以及最近值得注意的展覽。”"

}

# 初始化 session_state
for key, value in default_texts.items():
    if key not in st.session_state:
        st.session_state[key] = value


def generate_response():
    # 直接用 session_state 裡的 response
    response = st.session_state["response"]
    for char in response:
        yield char
        if char in ['.', '!', '?', '\n']:
            time.sleep(0.01)
        else:
            time.sleep(0.002)


def main():
    st.title("老師可即時編輯 Chatbot 回應內容")

    # 讓老師即時修改 chatbot 回應
    st.session_state["response"] = st.text_area(
        "編輯 Chatbot 回應內容（支援Markdown）",
        st.session_state["response"],
        height=400
    )

    st.markdown("---")
    st.markdown("### Chatbot 回應預覽：")
    st.markdown(st.session_state["response"], unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 預覽：")
    # 頁面內容組合
    st.markdown(st.session_state["title"])
    st.markdown(st.session_state["intro"])
    st.markdown(st.session_state["location"])
    st.markdown(st.session_state["collection"])
    st.markdown(st.session_state["visitors"])
    st.markdown(st.session_state["exhibitions"])
    st.markdown("---")
    st.markdown(st.session_state["ai_confidence"])
    st.markdown(st.session_state["ai_comment"])
    st.markdown("---")
    st.markdown(st.session_state["instruction"])
    # 你原本的其他功能可以繼續寫在這下面
    # 例如 st.chat_message, st_star_rating 等
    # AI回應區塊
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # 使用按鈕觸發動畫效果
        if st.button("顯示動態回應"):
            response = ""
            response_area = response_placeholder.empty()
            # 逐字顯示效果
            for char in generate_response():
                response += char
                response_area.markdown(response, unsafe_allow_html=True)
        else:
            # 直接顯示完整回應
            response_placeholder.markdown(
                st.session_state["response"], unsafe_allow_html=True)

    # 用戶評分區域
    st.write("請對這個回應進行評分：")
    stars = st_star_rating("", maxValue=5, defaultValue=3, key="rating")
    st.write(f"你給了 {stars} 顆星")


if __name__ == "__main__":
    main()
