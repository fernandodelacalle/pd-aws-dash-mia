FROM python:3.8

# set the working directory in the container
WORKDIR /code
# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install -r requirements.txt

# Expose the API Port
EXPOSE 8080
# Run the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]