FROM python:2
ADD config.ini /
ADD metrics.py /
RUN pip install kafka
CMD ["python", "./metrics.py"]