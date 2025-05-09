import streamlit as st
import glob
import os
import frontmatter
from streamlit_star_rating import st_star_rating

# ---- 1. 掃描 content/*.md, 讀出 metadata 與 content ----
CONTENT_DIR = "content"
md_paths = sorted(glob.glob(os.path.join(CONTENT_DIR, "scenario_*.md")))

pages = []
for path in md_paths:
    post = frontmatter.load(path)
    pages.append({
        "title": post.get("title", os.path.basename(path)),
        "star": post.get("star", None),
        "confidence": post.get("confidence", None),
        "content": post.content
    })

# ---- 2. 側邊欄：自動列出所有 scenario ----
titles = [p["title"] for p in pages]
sel = st.sidebar.selectbox("選擇 Scenario 頁面", titles)
page = pages[titles.index(sel)]

# ---- （可選）老師上傳入口，無需改程式即可新增 scenario_x.md ----
if st.sidebar.checkbox("📄 老師：上傳新 Scenario"):
    up = st.sidebar.file_uploader("上傳 scenario_x.md", type=["md"])
    if up:
        save_to = os.path.join(CONTENT_DIR, up.name)
        with open(save_to, "wb") as f:
            f.write(up.getbuffer())
        st.sidebar.success(f"已儲存 {up.name}，請從選單重新選取")
        st.rerun()

# ---- 3. 顯示星等 & 信心水準 ----
if page["star"] is not None:
    st_star_rating("", maxValue=5, size=24,
                   defaultValue=page["star"], read_only=True)
if page["confidence"] is not None:
    st.markdown(f"**AI 自信水平：** {page['confidence']}/10")

# ---- 4. 把 Markdown 內容拆段，並用 Chat-style 顯示 ----
paras = [p.strip() for p in page["content"].split("\n\n") if p.strip()]
for para in paras:
    with st.chat_message("assistant"):
        st.markdown(para, unsafe_allow_html=True)

# ---- 5. （可選）學生可在 Chat 底下互動提問 ----
if q := st.chat_input("有關本 Scenario 的問題？"):
    with st.chat_message("user"):
        st.write(q)
    with st.chat_message("assistant"):
        st.markdown("謝謝提問，目前功能開發中～")
