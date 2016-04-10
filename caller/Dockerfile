FROM hypriot/rpi-python:latest

WORKDIR /

ADD requirements.txt /
ADD caller.py /

#RUN pip install -r requirements.txt
RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org -r requirements.txt
EXPOSE 6000
