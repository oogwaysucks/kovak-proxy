FROM debian:12

RUN apt update && apt install -y python3-pip
RUN pip3 install mitmproxy --break-system-packages

WORKDIR /app
COPY start.sh .
RUN chmod +x start.sh

EXPOSE 8080

CMD ["./start.sh"]
