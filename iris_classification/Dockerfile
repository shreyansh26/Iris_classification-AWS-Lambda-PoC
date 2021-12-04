FROM amazon/aws-lambda-python

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

COPY ./ ./

# Run test cases and this saves the transformer model in the container
RUN pip install pytest --no-cache-dir && pytest tests -s -vv

RUN chmod -R 0777 ./models

CMD [ "main.lambda_handler"]