FROM python:3.8
WORKDIR /app
COPY . /app
EXPOSE 8501
RUN pip3 install -r requirements.txt
CMD streamlit run app.py