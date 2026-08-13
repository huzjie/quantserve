# ---- build web console ----
FROM node:20-alpine AS web
WORKDIR /app/web
COPY web/package.json web/package-lock.json* ./
RUN npm install
COPY web/ ./
RUN npm run build

# ---- runtime ----
FROM python:3.11-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
RUN pip install --no-cache-dir -e .

# serve built web assets
COPY --from=web /app/web/dist ./web/dist

EXPOSE 8000

CMD ["uvicorn", "quantserve.api.app:get_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
