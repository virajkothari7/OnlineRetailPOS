# base image  
FROM python:3.8   

# Set the working directory  
WORKDIR /OnlineRetailPOS

COPY . /OnlineRetailPOS/

# Set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Install all dependencies and perform migrations
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt --no-cache-dir

# Expose port 8000
EXPOSE 8000

RUN python manage.py collectstatic

# Please provide env varibales that are required to set up database configuration
# Command to run the migrations and start the server
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

# Don't forget to create a superuser from the terminal in Docker for accessing the app


# Required Variables:
# - SECRET_KEY_DEV: Pass in a secure key            (Default: 'django_dev_secret_key_online-retail-pos-1234')
# - NAME_OF_DATABASE: 'sqlite'/'postgres'/'mysql'   (Default: 'sqlite')

# Required if DB is other than sqlite from provided options
# - DB_USERNAME: 'DB_USER_NAME' 
# - DB_PASSWORD: 'DB_USER_PASS' 
# - DB_HOST: 'YOUR_DB_HOST' 
# - DB_PORT: 'YOUR_DB_HOST_PORT'

# STORE INFORMATION and PRINTER SETTING from .env.sample is Optional for running the app
# However, I will advise setting up if you plan to use it frequently


# Running the Dockerfile:
# - Make sure you provide required environment variables, either through passing .env file in docker run args or env variables itself
# - The Dockerfile will run on default configuration without any environment variables, and the database will be set to sqlite3
# - Update/Create .env file, change .env.sample to .env if you are providing an edited .env file 
# - Figure out mounting the sqlite file in Docker so that you don't lose your data when Docker stops 
# - Passing varibles example: docker run -e "VARIABLE1=value1" -e "VARIABLE2=value2" <image_name>
# - Passing .env file itself: docker run --env-file=/path/to/.env <image_name>


# Build the image and run Docker using these commands, for a custom Docker image compile:
# docker build -t docker-django-pos .
# docker run -i -t -p 8000:8000 docker-django-pos 

# Once built, create a superuser from the Django container terminal
