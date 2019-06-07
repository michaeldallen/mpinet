#BOF

FROM ubuntu:xenial


ENV \
        DEBIAN_FRONTEND noninteractive


RUN \
        apt-get update && apt-get --assume-yes dist-upgrade


RUN \
        apt-get update && apt-get --assume-yes install \
                \
                apt-utils \
                bsdmainutils\
                curl \
                eject \
                file \
                hdparm \
                iputils-ping \
                iputils-ping \
                jq \
                libffi-dev \
                libssl-dev \
                openssh-client \
                pv \
                python \
                python-pip \
                rsync \
                sudo \
                udev \
                unzip \
                usbutils \
                util-linux \
                vim \
                \
                cowsay

RUN apt-get --assume-yes install 

RUN \
        pip install --upgrade pip


RUN \
        pip install ansible==2.5


WORKDIR \
        /opt/mpinet


COPY \
        fs/ \
        /

#EOF
