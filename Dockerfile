FROM python:3.10-alpine
RUN pip install --upgrade pip &&  pip install -r requirements.txt && pip install pyinstaller
CMD python main.py
