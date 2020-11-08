FROM python:3
RUN pip3 install flask \
    && python3 -m pip install requests 
COPY balance.py /
EXPOSE 8082
ENTRYPOINT ["python3", "balance.py"]
