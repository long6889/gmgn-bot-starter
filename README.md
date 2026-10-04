# GMGN Bot Starter

Đây là repo khởi đầu để anh học và xây dựng bot auto trade crypto với GMGN.ai.

Mục tiêu:
- Cấu trúc dự án rõ ràng
- Có client API template để gọi GMGN.ai
- Có strategy skeleton để anh phát triển logic buying/selling
- Dễ mở rộng, dễ sửa theo API thực tế của GMGN

## Kiến trúc dự án

```text
gmgn-bot-starter/
├── README.md
├── .gitignore
├── requirements.txt
├── .env.example
├── gmgn_bot/
│   ├── __init__.py
│   ├── config.py
│   ├── client.py
│   ├── strategies.py
│   └── main.py
└── tests/
    └── __init__.py
```

## Cài đặt

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

## Cấu hình môi trường

Sửa `.env` theo nhà cung cấp API thật của anh:

```env
GMGN_BASE_URL=https://api.gmgn.ai
GMGN_API_KEY=your_api_key_here
GMGN_TIMEOUT=30
```

Lưu ý:
- Anh cần thay đúng endpoint và key thực tế của GMGN.ai
- Repo này là starter skeleton, không chắc chắn về API path thực tế của GMGN.ai ở từng thời điểm
- Nếu GMGN đổi schema endpoint, anh chỉ cần cập nhật trong `client.py`

## Chạy thử

```bash
python -m gmgn_bot.main
```

## Học theo tiến độ

1. Đọc `gmgn_bot/client.py` để hiểu cách gọi API
2. Đọc `gmgn_bot/strategies.py` để hiểu logic signal
3. Đọc `gmgn_bot/main.py` để biết cách chạy và test
4. Sau đó anh mở rộng:
   - lọc token
   - tính signal
   - risk management
   - order execution
   - logging
   - backtest

## Gợi ý phát triển tiếp

- Thêm `wallet.py` để quản lý ví
- Thêm `scanner.py` để quét token mới
- Thêm `risk.py` để giới hạn vị thế
- Thêm `backtest.py` để test lịch sử
- Thêm `database.py` để lưu dữ liệu

## Lưu ý quan trọng

- Không dùng tiền thật khi chưa test kỹ
- Luôn test trên môi trường demo / sandbox / dry-run trước
- Dùng logging đầy đủ để debug API và lệnh

Mình sẽ hỗ trợ tiếp để anh phát triển bot từ starter này. Nếu cần, mình có thể viết tiếp:
- module scanner token
- module signal strategy
- module order execution
- module risk management
- module backtest
- hoặc tạo repo tiếp theo theo hướng GMGN.ai thực tế
