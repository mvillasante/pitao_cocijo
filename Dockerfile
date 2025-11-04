FROM python:3.13
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    flake8 \
    mutmut \
    mypy \
    pandas-stubs \
    matplotlib-stubs \
    pylint \
    pytest \
    pytest-cov
