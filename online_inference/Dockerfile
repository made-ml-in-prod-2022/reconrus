FROM python:3.9-slim
COPY . /online_inference
WORKDIR /online_inference
RUN pip install -r requirements.txt

ENV MODEL_URL https://made-yastrebov-2022.s3.eu-central-1.amazonaws.com/model.pkl
ENV TOKENIZER_URL https://made-yastrebov-2022.s3.eu-central-1.amazonaws.com/transformer.pkl

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
