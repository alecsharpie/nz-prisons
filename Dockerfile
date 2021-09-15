FROM python:3.8.6-buster

COPY images /images
COPY application.py /application.py
COPY navigation.py /navigation.py
COPY requirements.txt /requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD web: sh setup.sh && python navigation.py && streamlit run application.py
