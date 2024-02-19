FROM python:3.7
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 wsgi:app
RUN pip install --no-cache-dir spacy
RUN python -m spacy download en_core_web_sm
CMD ["bash", "-c", "python app.py & streamlit run streamlit_app.py"]