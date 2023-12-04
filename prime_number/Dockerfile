FROM base_image

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}


# Install the specified packages
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY prime_number_check_lambda.py ${LAMBDA_TASK_ROOT}

CMD [ "prime_number_check_lambda.lambda_handler" ]