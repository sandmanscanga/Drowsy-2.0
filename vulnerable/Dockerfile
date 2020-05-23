FROM python:3

WORKDIR /usr/src/vulnerable

COPY requirements.txt               .

COPY app/app.py                     app/
COPY app/templates/index.html       app/templates/

COPY app/database/db_prep.py        app/database/
COPY app/database/db_creds.py       app/database/
COPY app/database/creds/root.json   app/database/creds/
COPY app/database/creds/user.json   app/database/creds/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/app.py"]
