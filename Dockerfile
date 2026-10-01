CMD ["sh", "-c", "mitmdump -s /app/catch.py --listen-host 0.0.0.0 --listen-port ${PORT:-5000}"]
