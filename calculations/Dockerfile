FROM python:3.6

COPY ./ /calculations
WORKDIR /calculations

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "manage.py"]