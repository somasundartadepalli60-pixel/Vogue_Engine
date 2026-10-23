FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.lock
EXPOSE 8000
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "8000"]
