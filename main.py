import streamlit as st
from sentiment_model import load_sentiment_model, classify_text
from database import init_db, save_result, get_history, clear_history
from preprocess import normalize_text

st.set_page_config(page_title="Vietnamese Sentiment Assistant", layout="centered")

# Load CSS file
with open("styles.css", "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Titles
st.title("Hệ thống phân loại cảm xúc tiếng Việt")
st.write("Nhập một câu tiếng Việt và hệ thống sẽ phân tích cảm xúc theo **PhoBERT**.")

# Init DB
init_db()
# ❗ Only clear on first load, NOT on rerun
if "history_cleared" not in st.session_state:
    clear_history()
    st.session_state["history_cleared"] = True

@st.cache_resource
def get_model():
    return load_sentiment_model()

model = get_model()

# User input
text = st.text_area("📝 Nhập câu tiếng Việt:", placeholder="Ví dụ: Hôm nay tôi rất vui!")

# Button
if st.button("🚀 Phân loại cảm xúc"):
    if len(text.strip()) < 5:
        st.warning("⚠️ Câu quá ngắn, vui lòng nhập câu dài hơn.")
    else:
        with st.spinner("⏳ Đang phân tích..."):
            processed = normalize_text(text)
            result = classify_text(model, processed)

            color_class = result["sentiment"].lower()

            st.markdown(
                f"""
                <div class="result-box {color_class}">
                    👉 Kết quả: <b>{result['sentiment']}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            save_result(result["text"], result["sentiment"])

# History
st.markdown('<div class="section-title">📜 Lịch sử phân loại gần đây</div>', unsafe_allow_html=True)

history = get_history()
for row in history:
    sentiment = row[2]
    st.markdown(
        f"""
        <div class="history-item">
            <b>{row[3]}</b> - [{sentiment}]<br>
            {row[1]}
        </div>
        """,
        unsafe_allow_html=True
    )

