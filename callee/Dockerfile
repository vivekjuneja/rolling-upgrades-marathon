FROM hypriot/rpi-python:latest 
MAINTAINER vivekjuneja@gmail.com


WORKDIR /

ADD requirements.txt /
ADD callee.py /

#RUN pip install -r requirements.txt
RUN pip install --index-url=http://pypi.python.org/simple/ --trusted-host pypi.python.org -r requirements.txt
