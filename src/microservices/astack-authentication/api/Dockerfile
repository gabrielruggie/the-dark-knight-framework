FROM python:3.10.5

# Create Backend Directory in Container Files
WORKDIR /astack-authentication
RUN mkdir /astack-authentication/main

# Copy Requirements and Install Them in the Container Before Running it
COPY ./main/requirements.txt /astack-authentication/main/requirements.txt
RUN pip3 install -r /astack-authentication/main/requirements.txt

COPY ./main /astack-authentication/main

RUN chmod +x /astack-authentication/main/wait-for-deps.sh

CMD ["uvicorn", "main.app:api", "--host", "0.0.0.0", "--reload", "--port", "8002"]

