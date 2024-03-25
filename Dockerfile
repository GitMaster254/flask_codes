FROM python

WORKDIR /flask_codes

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "__init__.py"]

EXPOSE 5000


