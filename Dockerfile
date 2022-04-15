FROM python:3.8

RUN useradd -ms /bin/bash toto
USER toto

WORKDIR /app
COPY . /app
 
RUN pip install -r requirements.txt

#EXPOSE 8080 
CMD ["python","app.py"]
