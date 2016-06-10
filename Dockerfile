FROM ubuntu:16.04
RUN export DEBIAN_FRONTEND=noninteractive \
	&& apt-get update -y && apt-get upgrade -y \
	&& apt-get install -y python3 python3-pip python3-setuptools python3-psycopg2 \
	&& apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.5-dev tk8.5-dev python-tk \
	&& BUILD_DEPS='build-essential python3-dev' \
	&& apt-get install -y --no-install-recommends ${BUILD_DEPS} \
	&& pip3 install --no-cache-dir \
		circus==0.13.0 \
		Pillow==3.2.0 \
	&& apt-get autoremove -y ${BUILD_DEPS} \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt
