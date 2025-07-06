From python:3.8
WORKDIR /app
COPY ./app /app
RUN pip install flask
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]