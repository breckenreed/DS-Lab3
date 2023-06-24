FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY logging_service_alt.py /app/logging_service_alt.py
RUN pip install flask hazelcast-python-client
EXPOSE 8001
CMD ["python", "-u", "logging_service_alt.py"]
