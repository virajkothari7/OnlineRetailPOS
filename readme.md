<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>

<h1 align="center"> Online Retail POS System (Django) </h1>

<p align="center">
	<img src="https://img.shields.io/github/license/virajkothari7/OnlineRetailPOS?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/virajkothari7/OnlineRetailPOS?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/virajkothari7/OnlineRetailPOS?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/virajkothari7/OnlineRetailPOS?style=default&color=0080ff" alt="repo-language-count">
<p>
<br>

The Online Retail POS System is a web-based application developed with Django, designed to manage retail operations efficiently by handling inventory, sales, and hardware integrations. You can run it locally and access it from different devices on the same network using the system's IP address.

<br>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Getting Started](#getting-started)
    - [Downloading Project](#downloading-project)
    - [Configuration](#configuration)
    - [Intial Setup](#intial-setup)
    - [Usage](#usage)
    - [Other](#other)
- [Docker](#docker)
    - [Docker Package](#docker-package)
    - [Docker Compose (Locally)](#docker-compose-locally)
- [Screenshots](#screenshots)
- [Features](#features)
- [License ](#license-)


<br>

## Getting Started
  Before you begin, ensure you have the following prerequisites installed:
  - **Python 3.x**
  - **Docker(Optional)**
  - **Database**


  #### Downloading Project

  - ##### Option 1 (Git Clone)
    Clone this repository to your local machine, 
    ```bash
    git clone https://github.com/virajkothari7/OnlineRetailPOS.git
    cd path_to_dir/online-retail-pos
    pip install -r requirements.txt
    ```

  - ##### Option 2 (Zip Downlaod)
    If you prefer, you can also download the project as a ZIP file and extract it to your desired location.
    ```
    cd path_to_dir/online-retail-pos
    pip install -r requirements.txt
    ```


  #### Configuration

  - #### .env configuration
    - Create a .env file in the project's root directory to store your configuration variables. See .env.sample file for required variables.

  - #### Database configuration 
    - Change Databse configuration in settings/dev.py according to your database requirement, I would suggest to use some cloud database so that you data is stored regardless where project is running and can have multiple POS setup.
  
    - There is optional setting commented out for Cloud Database with SSH tunneling. Your database host might require different way to connect. Look into settings/developement.py for further.
  
    - SQLite file is configured for default, change it in django settings/devlopement.py *Databases* if using another database setup. You can change between databses from postgres, mysql and sqlite through passing env varibales.


  #### Intial Setup
  ***Correctly setup .env file, as well as configure Database correctly. Make sure all tweaks are done according to you.***

  - Go to the project folder
    ```
    cd path_to_dir/online-retail-pos
    ```
  - Install required python libraries, if not already done.
    ```
    pip install -r requirements.txt
    ```
  - Intial Database setup
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
  - **Creating Superuser for access to platform**
    <br>
    Creating your main user, to access admin panel and create more users, if running in docker, use docker shell once docker setup is done.
    ```
    python manage.py createsuperuser
    ```
      - Superuser can create staff and users, hence you want to have one superuser. Also, you won't be able to access admin page for first time without it.
      - Staff status for users who you want to provide access to admin panel, you might have to tweak their permission on admin panel. This users will be able to add new products and create department and all.
      - User status for those who will just use POS for sales transaction and are not required to manuplate inventory data.


  #### Usage
  This app can be run on any device where django or docker(may require some configuration) can be run. You will need a server/local machine to run the project
  <br>

  - To start the Django development server, run the below command. To stop the server, you can typically use Ctrl+C in the terminal  where the server is running.
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
  - You can now access the POS system in your web browser by navigating:
    - If same machine where django is running
      `http://127.0.0.1:8000` 
    - Same network where django is running, this functionality may not work as expected 
      `http://djangoserver_ip_addrs:8000`


  #### Other
  - **Reciept Functionality**   
    This only works on the machine where the project is running, since it requires port connection to printer.
    - Make sure you have receipt printer connected to django server machine.
    - If your tablet can connect to POS printer than configure this project print_reciept method on tranasaction.views accordingly
    <br>
  - **Customer Screen**   
    You need to do a dual monitor setup on the machine where you will accesing POS system, 
    Example: 
    - If accesing POS from Tablet with django server running on rasp-pi or a server, you will connect second monitor to Tablet for this functionality
    - If accesing POS from Window touch tablet/pc with django runnnig locally on same machine, connect second display here for this funcitonality
    <br>
  - **Folder: images4display**   
    In customer display there is slideshow of images, which can be used to put promotion/prices. Project uses directory images4display to slideshow phots from that directory, all photos in directory will be used. Only add photos in directory otherwise it will run into erro. More [info](/images4display/readme.md)


<br>

## Docker

  #### Docker Package

  Docker package is provided for the [repository](https://github.com/virajkothari7/OnlineRetailPOS/pkgs/container/onlineretailpos) to be pulled directly in docker. You can just pass in .env file with required varibles in the docker image, it should run as expected. Read dockerfile for better undertanding. Make sure you have docker installed for respective setup.

  - Pull docker image
      ```
      docker pull ghcr.io/virajkothari7/onlineretailpos:latest
      ```
  - Run docker image
      ```
      docker run ghcr.io/virajkothari7/onlineretailpos:latest
      ```
    It will run without passing any varibles with default values, however, it will best if you provide secret_key and database configuration thorugh either passing varible or .env file in command line, read further in dockerfile. 
    - Passing varibles example: docker run -e "VARIABLE1=value1" -e "VARIABLE2=value2" <image_name>
    - Passing .env file itself: docker run --env-file=/path/to/.env <image_name>
    - **<image_name>** refers to docker image name you have, for example form above, it will be **`ghcr.io/virajkothari7/onlineretailpos:latest`**

  #### Docker Compose (Locally)

  If you want to run docker setup with docker postgres associated with the app. You can download the repo and just run docker compose up from the folder. 

  - Make sure to update DBUSER, DBPASS and SECRET_KEY_DEV in docker compose file
  - Go to project directory
  - Building image
    ```
      docker compose build
    ```
  - Running docker
    ```
    docker compose up
    ```
    If you run into error just cancel and run 'docker compose up' again.
  
  Also if you want to customize the project and still use docker, you can make changes to the code and build the docker image with that code using docker compose.


<br>

## Screenshots
<table>
  <tr>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_21.png /></td>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_4.png /></td>
  </tr>
  <tr>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_6.png /></td>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_7.png /></td>
  </tr>
  <tr>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_2.png /></td>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_1.png /></td>
  </tr>
  <tr>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_16.png /></td>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_15.png /></td>
  </tr>
  <tr>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_17.png /></td>
    <td><img src=https://github.com/virajkothari7/OnlineRetailPOS/blob/main/screenshots/Screenshot_20.png /></td>
  </tr>
</table>

<br>

## Features

- Manage inventory and products
- Process sales transactions
- ESPPOS Receipt generation(Only Works if Printer is Connceted to Server or Your device has ESCPOS drivers and can print using those mini printers)
- Multi-device access on the same network using IP address
- Can set-up as live web app, however will have to configure accodingly. Some funcitonality may not work on prod web app.
- Run locally on touch screen device for best functionality
- Can have set up as-display images on customer facing screen, manage images4display folder in base dir of project.


<br>

## License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
This project is licensed under MIT License. For more details, refer to the License file.




