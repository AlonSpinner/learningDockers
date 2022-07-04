FROM python:3

WORKDIR /usr/src/

COPY requirements.txt ./

COPY measurements.csv ./

COPY process_measurements.py ./

RUN pip install --no-cache-dir -r requirements.txt

RUN python ./process_measurements.py

CMD ["sleep", "infinity"]
