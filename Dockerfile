FROM python:3.9

RUN mkdir -p /app
WORKDIR /app

# Copy files
COPY ./requirements.txt ./
COPY ./setup.py ./

# Copy folders
ADD ./src ./src

# Install packages
RUN pip install -U pip && pip install -r requirements.txt

# Run flask app
EXPOSE 5000
ENV FLASK_APP="src/main.py" FLASK_DEBUG=1 FLASK_ENV=docker
CMD ["flask", "run", "-h", "0.0.0.0"]
