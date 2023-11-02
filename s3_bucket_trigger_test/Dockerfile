FROM public.ecr.aws/lambda/python:3.11-arm64

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}


# Install the specified packages
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY s3_bucket_trigger_function.py ${LAMBDA_TASK_ROOT}

CMD [ "s3_bucket_trigger_function.lambda_handler" ]