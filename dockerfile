FROM python:3.14.7
WORKDIR /app
COPY . .
CMD ["python", "menu_system.py"]