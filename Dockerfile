FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

COPY poetry.lock pyproject.toml /./

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . .

RUN chmod a+x docker/*.sh

#WORKDIR .
#
#CMD uvicorn main:app --host 0.0.0.0 --port 8000


