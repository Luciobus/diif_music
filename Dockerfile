FROM ubuntu:20.04

RUN apt-get update && apt-get install --yes --no-install-recommends \
    python3.9 \
    python3-pip

RUN pip3 install \
    python-dotenv \
    pytelegrambotapi \
    spotipy \
    requests

COPY main.py /main.py

ENTRYPOINT ["python3", "/main.py"]
