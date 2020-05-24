FROM python:3

WORKDIR /usr/src/vulnerable

COPY requirements.txt                           .
COPY app.py                                     .

COPY server/main.py                             server/
COPY server/vuln/*                              server/vuln/
COPY server/templates/*                         server/templates/

COPY server/static/favicon.png                  server/static/
COPY server/static/css/*                        server/static/css/
COPY server/static/js/*                         server/static/js/

COPY server/database/utils/*                    server/database/utils/
COPY server/database/creds/*                    server/database/creds/
COPY server/database/wordlists/*                server/database/wordlists/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
