FROM python:3.11
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    mutmut==2.4.0 \
    mypy \
    pylint \
    pytest \
    pytest-cov
