FROM python:3
WORKDIR /usr/src/app
COPY operator.py ./
COPY watcher.py ./
COPY logs.txt ./
RUN pip install kubernetes
RUN pip install pprint
CMD [ "python", "./watcher.py" ]
