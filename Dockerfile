FROM continuumio/miniconda3:4.10.3

RUN apt-get update --allow-releaseinfo-change -y
RUN apt-get upgrade --fix-missing -y
RUN apt-get install -y --fix-missing --no-install-recommends \
    python3-pip software-properties-common build-essential \
    cmake sqlite3 gfortran python-dev && \
    pip install -U pip

WORKDIR /src/pram_app
COPY . /src/pram_app

RUN conda create --name pyenv python=3.9
RUN conda config --add channels conda-forge
RUN conda run -n pyenv --no-capture-output pip install -r /src/pram_app/requirements.txt
RUN conda install -n pyenv uwsgi

ENV PATH "/src:/src/pram_app":${PATH}
ENV PYTHONPATH "/src:/src/pram_app":${PYTHONPATH}
ENV DJANGO_SETTINGS_MODULE "settings"
EXPOSE 8080

COPY uwsgi.ini /etc/uwsgi/

RUN chmod 755 /src/pram_app/start_django.sh
CMD ["conda", "run", "-n", "pyenv", "--no-capture-output", "sh", "/src/pram_app/start_django.sh"]