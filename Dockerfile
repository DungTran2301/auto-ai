
FROM ubuntu


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y python3-pip


# RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/
RUN pip install -r requirements.txt

# RUN pip install pypiwin32
# RUN pip install --upgrade pip && pip install -r requirements.txt
# RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/


RUN pip install django

EXPOSE 8000


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]