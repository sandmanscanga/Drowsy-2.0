FROM python:3

WORKDIR /usr/src/vulnerable

COPY requirements.txt                           .

COPY app/app.py                                 app/
COPY app/templates/*                            app/templates/

COPY app/static/favicon.png                     app/static/
COPY app/static/css/*                           app/static/css/
COPY app/static/js/*                            app/static/js/

COPY app/database/db_*.py                       app/database/
COPY app/database/creds/*                       app/database/creds/
COPY app/database/wordlists/*                   app/database/wordlists/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/app.py"]
