Telegram Notification


Run Python file finance_alert.py
command  =

$token = Read-Host "Telegram bot token" -AsSecureString
$env:TELEGRAM_BOT_TOKEN = [System.Net.NetworkCredential]::new("", $token).Password
$env:TELEGRAM_CHAT_ID = Read-Host "Telegram chat ID"
python .\finance_alert.py