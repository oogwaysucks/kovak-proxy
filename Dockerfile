FROM debian:12

RUN apt update && apt install -y python3-pip python3-venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install mitmproxy

WORKDIR /app
COPY catch.py .

EXPOSE 8080

CMD ["mitmweb", "-s", "/app/catch.py", "--listen-host", "0.0.0.0", "--listen-port", "8080", "--set", "web_host=0.0.0.0", "--set", "web_port=8081"]
