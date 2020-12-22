FROM python:3
RUN pip3 install flask
COPY instance1.py / 
EXPOSE 8080 8081
ENTRYPOINT ["python3", "instance1.py", "instance2.py"]
