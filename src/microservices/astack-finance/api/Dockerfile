FROM python:3.10.5

# Create Backend Directory in Container Files
WORKDIR /astack-finance
# Create main directory because we don't want to copy the tests over in this image
RUN mkdir /astack-finance/main

# Copy Requirements and Install Them in the Container Before Running it
COPY ./main/requirements.txt /astack-finance/main/requirements.txt
RUN pip3 install -r /astack-finance/main/requirements.txt

COPY ./main /astack-finance/main

RUN chmod +x /astack-finance/main/wait-for-deps.sh

CMD ["uvicorn", "main.app:api", "--host", "0.0.0.0", "--reload", "--port", "8000"]

