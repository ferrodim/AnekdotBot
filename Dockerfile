FROM ubuntu:18.10
RUN mkdir /code
WORKDIR /code
RUN apt update && apt install -y \
  python3-pip \
  pkg-config
RUN pip3 install pyTelegramBotAPI feedparser python-telegram-bot
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
CMD ["bash", "start.sh"]