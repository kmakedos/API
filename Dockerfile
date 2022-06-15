FROM python:3.8-alpine
RUN apk --no-cache add curl
COPY api_emulator.py /
RUN chmod +x /api_emulator.py
ENTRYPOINT ["/api_emulator.py"]
