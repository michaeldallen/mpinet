#BOF

FROM ubuntu:xenial


ENV \
        DEBIAN_FRONTEND noninteractive


RUN \
        apt-get update && apt-get --assume-yes dist-upgrade


RUN \
        apt-get update && apt-get --assume-yes install \
            apt-utils


RUN \
        apt-get update && apt-get --assume-yes install \
                curl \
                eject \
                file \
                hdparm \
                pv \
                rsync \
                sudo \
                udev \
                unzip \
                usbutils \
                util-linux \
	        \
	        cowsay


WORKDIR \
        /opt


COPY mpinet.host_device_map.v4 \
    /opt

#EOF
