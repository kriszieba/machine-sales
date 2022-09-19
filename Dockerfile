FROM python:3.10.4

#ENV http_proxy http://proxy-chain.xxx.com:911/
#ENV https_proxy http://proxy-chain.xxx.com:912/

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
#ADD app.py .
ADD . /app
#COPY requirements.txt requirements.txt



# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt



# Run app.py when the container launches
CMD ["python", "app.py"]
