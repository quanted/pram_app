FROM puruckertom/uber_py27

COPY . /src/
WORKDIR /src
EXPOSE 8080
CMD ["python", "manage.py runserver 8080"]