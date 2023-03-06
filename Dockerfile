FROM public.ecr.aws/lambda/python:3.9-arm64

COPY main.py ${LAMBDA_TASK_ROOT}

RUN pip install twilio

CMD ["main.lambda_handler"]