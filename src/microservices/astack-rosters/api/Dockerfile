FROM python:3.10.5

# Create Backend Directory in Container Files
WORKDIR /astack-rosters/
RUN mkdir /astack-rosters/main/

# Copy Requirements and Install Them in the Container Before Running it
COPY ./main/requirements.txt /astack-rosters/main/requirements.txt
RUN pip3 install -r /astack-rosters/main/requirements.txt

COPY ./main /astack-rosters/main/

RUN chmod +x /astack-rosters/main/wait-for-deps.sh

CMD ["uvicorn", "main.app:api", "--host", "0.0.0.0", "--reload", "--port", "8001"]
