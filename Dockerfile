FROM amancevice/pandas:latest

RUN pip install mesa

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN mkdir /usr/local/models

COPY *.py /usr/local/models/

CMD ["python", "/usr/local/models/VisualizeEconomy.py"]