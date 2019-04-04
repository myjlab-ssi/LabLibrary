FROM ubuntu:16.04

# Install.
RUN \
  apt-get update && \
  apt-get install -y  build-essential libbz2-dev libdb-dev \
  libreadline-dev libffi-dev libgdbm-dev liblzma-dev \
  libncursesw5-dev libsqlite3-dev libssl-dev \
  zlib1g-dev uuid-dev tk-dev \
  python3 python3-dev wget curl unzip apt-utils && \
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
  python3 get-pip.py && \
  pip install --upgrade pip && \
  pip install selenium scrapy scrapy-splash&& \
  apt-get install -y libfontconfig && \
  mkdir -p /home/root/src && cd $_ && \
  wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && \
  unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ && \
  apt-get install -y libappindicator1 fonts-liberation libasound2 libnspr4 libnss3 libxss1 lsb-release xdg-utils && \
  touch /etc/default/google-chrome && \
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg -i google-chrome-stable_current_amd64.deb && \
  apt-get install -y fonts-migmix

RUN apt-get install -y sudo

# add sudo user
RUN groupadd -g 1000 developer && \
    useradd  -g      developer -G sudo -m -s /bin/bash rotelstift && \
    echo 'rotelstift:password' | chpasswd

RUN echo 'Defaults visiblepw'                >> /etc/sudoers
RUN echo 'rotelstift ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Set japanese
RUN apt-get install -y language-pack-ja-base language-pack-ja
RUN locale-gen ja_JP.UTF-8

# Set environment variables.
ENV LANG ja_JP.UTF-8
ENV PYTHONIOENCODIND utf_8

USER rotelstift

WORKDIR /crawler

ENTRYPOINT [ "scrapy" ]
CMD ["shell"]