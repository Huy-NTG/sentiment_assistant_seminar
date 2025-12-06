from transformers import pipeline
from preprocess import normalize_text

MODEL_NAME = "wonrax/phobert-base-vietnamese-sentiment"

# Khởi tạo model một lần duy nhất (tối ưu tốc độ)
sentiment_model = pipeline(
    "sentiment-analysis",
    model=MODEL_NAME,
    tokenizer=MODEL_NAME
)

def load_sentiment_model():
    """Return model cho main.py"""
    return sentiment_model


def classify_text(model, text: str):
    """Xử lý tiền xử lý + gọi model + áp dụng threshold + xử lý lỗi"""

    # 1. Chuẩn hóa văn bản
    preprocessed = normalize_text(text)

    # 2. Bắt lỗi pipeline
    try:
        res = model(preprocessed)[0]
    except Exception as e:
        return {
            "text": text,
            "sentiment": "NEUTRAL",
            "score": 0,
            "error": str(e)
        }

    label = res.get("label")
    score = float(res.get("score", 0.0))  # HuggingFace pipeline trả 'score'

    # 3. Ngưỡng confidence theo yêu cầu đồ án
    if score < 0.5:
        mapped = "NEUTRAL"
    else:
        label_map = {
            "POS": "POSITIVE",
            "NEG": "NEGATIVE",
            "NEU": "NEUTRAL"
        }
        mapped = label_map.get(label, "NEUTRAL")

    # 4. Return dictionary đúng format yêu cầu
    return {
        "text": text,
        "sentiment": mapped,
        "score": score
    }
