FROM python:3.10.5

# Create Backend Directory in Container Files
WORKDIR /ymbl-site-query
RUN mkdir /ymbl-site-query/main

# Copy Requirements and Install Them in the Container Before Running it
COPY ./main/requirements.txt /ymbl-site-query/main/requirements.txt
RUN pip3 install -r /ymbl-site-query/main/requirements.txt

COPY ./main /ymbl-site-query/main/

RUN chmod +x /ymbl-site-query/main/wait-for-deps.sh

CMD ["uvicorn", "main.app:api", "--host", "0.0.0.0", "--reload", "--port", "8100"]

