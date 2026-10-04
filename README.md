# GMGN Bot Starter

Đây là repo khởi đầu để anh học và xây dựng bot auto trade crypto với GMGN.ai.

Mục tiêu:
- Cấu trúc dự án rõ ràng
- Có client API template để gọi GMGN.ai
- Có strategy skeleton để anh phát triển logic buying/selling
- Có scanner + risk manager để anh học cách lọc token và quản lý rủi ro
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
│   ├── scanner.py
│   ├── risk.py
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

## Mô tả từng file chính

### `gmgn_bot/config.py`
- Đọc biến môi trường
- Tạo `settings` object dùng chung cho toàn dự án

### `gmgn_bot/client.py`
- Wrapper gọi API
- Có các method mẫu: `ping()`, `get_market()`, `get_wallet_balance()`, `place_order()`
- Anh sẽ cập nhật theo API thật của GMGN.ai

### `gmgn_bot/scanner.py`
- Filter token bằng volume / trend
- Chọn token tốt nhất cho signal

### `gmgn_bot/risk.py`
- Giới hạn vị thế theo balance
- Chặn trade nếu vượt mức rủi ro
- Dùng cho việc kiểm soát drawdown / stop loss

### `gmgn_bot/strategies.py`
- Strategy mẫu với logic `buy / sell / hold`
- Cần anh thay bằng logic thực tế dựa trên market data, RSI, volume, trend, hoặc whale activity

### `gmgn_bot/main.py`
- Điểm khởi chạy bot
- Gồm scanner + risk check + strategy demo

## Học theo tiến độ

1. Đọc `gmgn_bot/client.py` để hiểu cách gọi API
2. Đọc `gmgn_bot/scanner.py` để hiểu cách lọc token
3. Đọc `gmgn_bot/risk.py` để hiểu cách kiểm soát rủi ro
4. Đọc `gmgn_bot/strategies.py` để hiểu logic signal
5. Đọc `gmgn_bot/main.py` để biết cách chạy và test

## Gợi ý phát triển tiếp

- Thêm `wallet.py` để quản lý ví
- Thêm `monitor.py` để quét token mới theo thời gian thực
- Thêm `backtest.py` để test lịch sử
- Thêm `database.py` để lưu dữ liệu
- Thêm `alerts.py` để gửi thông báo khi signal xuất hiện

## Lưu ý quan trọng

- Không dùng tiền thật khi chưa test kỹ
- Luôn test trên môi trường demo / sandbox / dry-run trước
- Dùng logging đầy đủ để debug API và lệnh

Mình sẽ hỗ trợ tiếp để anh phát triển bot từ starter này.
