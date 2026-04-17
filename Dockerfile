# Stage 1: Build
FROM python3.12-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final Stage
FROM python3.12-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY ./app ./app
COPY main.py .

ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000

CMD ["python", "main.py"]
