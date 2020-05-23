FROM python:3

WORKDIR /usr/src/vulnerable

COPY requirements.txt                       .

COPY temporary/app.py                       temporary/
COPY temporary/templates/index.html         temporary/templates/

COPY temporary/database/db_prep.py          temporary/database/
COPY temporary/database/db_creds.py         temporary/database/
COPY temporary/database/creds/root.json     temporary/database/creds/
COPY temporary/database/creds/user.json     temporary/database/creds/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "temporary/app.py"]
