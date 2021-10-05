FROM python:3.7

WORKDIR /code

RUN pip install jupyterlab pandas pymongo

# Expose the API Port
EXPOSE 8080

# Run the server
CMD ["jupyter-lab", "--ip", "0.0.0.0", "--port", "8888", "--allow-root"]
