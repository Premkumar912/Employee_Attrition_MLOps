FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY Dockerfile compose.yaml ./

RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir --retries 10 --timeout 120 -r requirements.txt

COPY src/ ./src/
COPY orchestration/ ./orchestration/
COPY WA_Fn-UseC_-HR-Employee-Attrition.csv .

CMD ["python", "src/train.py"]
