🇻🇳 Vietnamese Sentiment Assistant

Ứng dụng phân loại cảm xúc tiếng Việt sử dụng Hugging Face Transformer (PhoBERT) và giao diện Streamlit.

📌 1. Giới thiệu

Dự án Vietnamese Sentiment Assistant được xây dựng nhằm phân tích cảm xúc trong câu tiếng Việt theo 3 nhãn:

POSITIVE – Tích cực

NEUTRAL – Trung tính

NEGATIVE – Tiêu cực

Hệ thống sử dụng mô hình:

wonrax/phobert-base-vietnamese-sentiment


kết hợp pipeline sentiment-analysis từ HuggingFace để xử lý nhanh và chính xác.

Ứng dụng được xây dựng bằng:

Python

Streamlit

HuggingFace Transformers

SQLite3

⚙️ 2. Kiến trúc hệ thống
📦 sentiment-assistant
 ┣ 📂 data/              → Lưu database SQLite
 ┣ 📜 main.py            → Giao diện Streamlit
 ┣ 📜 sentiment_model.py → Gọi Transformer + tiền xử lý & phân tích
 ┣ 📜 preprocess.py      → Hàm chuẩn hóa tiếng Việt
 ┣ 📜 database.py        → Lưu & đọc lịch sử phân loại
 ┣ 📜 styles.css         → Tùy chỉnh UI
 ┗ 📜 requirements.txt   → Danh sách thư viện

🚀 3. Hướng dẫn cài đặt
  1. Clone dự án
  git clone https://github.com/Huy-NTG/sentiment_assistant_seminar.git
  cd sentiment_assistant_seminar

  2. Tạo môi trường ảo
  python -m venv venv

  3. Kích hoạt môi trường ảo
  
  Windows
  
   venv\Scripts\activate
   
  MacOS / Linux
  
   source venv/bin/activate
  
  4. Cài đặt thư viện
  pip install -r requirements.txt

🏃‍♂️ 4. Chạy chương trình
streamlit run main.py

🧠 5. Cách sử dụng

Nhập câu tiếng Việt vào ô nội dung

Nhấn nút Phân loại cảm xúc

Xem kết quả:

POSITIVE

NEUTRAL

NEGATIVE

Hệ thống tự động lưu lịch sử vào SQLite

Khi chạy lại chương trình, lịch sử phân loại gần nhất sẽ được hiển thị

🗃️ 6. Lưu trữ cục bộ (SQLite)

Database được lưu tại:

/data/sentiments.db


Cấu trúc bảng:

Trường	Ý nghĩa
id	Khóa chính
text	Nội dung câu
sentiment	Nhãn cảm xúc
timestamp	Thời gian phân loại
✔️ 7. Mô hình NLP sử dụng

Ứng dụng dùng mô hình:

wonrax/phobert-base-vietnamese-sentiment


Thông qua pipeline:

pipeline("sentiment-analysis")


Bao gồm:

Tiền xử lý

Chuẩn hóa tiếng Việt

Mapping nhãn POS / NEG / NEU → POSITIVE / NEGATIVE / NEUTRAL

Áp dụng ngưỡng độ tin cậy (confidence score)

📈 8. Kết luận

Dự án đáp ứng đầy đủ yêu cầu:

Phân loại 3 nhãn cảm xúc

Xử lý tiếng Việt (kể cả câu thiếu dấu / viết tắt cơ bản)

Lưu trữ dữ liệu bằng SQLite

Giao diện trực quan dễ sử dụng

Độ chính xác cao nhờ mô hình PhoBERT

🌱 9. Hướng phát triển

Thêm REST API cho backend

Xây dựng dashboard thống kê cảm xúc

Nâng cấp lên mô hình mạnh hơn (phobert-large)

Hỗ trợ phân tích đoạn văn dài hoặc văn bản đa câu
