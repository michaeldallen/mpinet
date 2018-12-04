#BOF

FROM ubuntu:xenial


ENV \
        DEBIAN_FRONTEND noninteractive


RUN \
        apt-get update && apt-get --assume-yes dist-upgrade


RUN \
        apt-get update && apt-get --assume-yes install \
                apt-utils \
                curl \
                eject \
                file \
                hdparm \
                pv \
                python \
                python-pip \
                rsync \
                sudo \
                udev \
                unzip \
                usbutils \
		jq \
                util-linux \
                \
                cowsay

RUN apt-get --assume-yes install openssh-client

RUN \
        pip install --upgrade pip


RUN \
        pip install ansible==2.5


WORKDIR \
        /opt


COPY \
        fs/ \
        /

#EOF
