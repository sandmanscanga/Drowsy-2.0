FROM python:3

WORKDIR /usr/src/vulnerable

COPY requirements.txt               .
COPY temporary/app.py               temporary/
COPY temporary/templates/index.html temporary/templates/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "temporary/app.py"]
