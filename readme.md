# Online Retail POS System (Django)

Welcome to the Online Retail POS (Point of Sale) System project built on Django. This system allows you to run a retail store, manage inventory, and process sales, all within a web-based interface. You can also run it locally and access it from different devices on the same network using the system's IP address.

## Table of Contents
- [Online Retail POS System (Django)](#online-retail-pos-system-django)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Downloading Project](#downloading-project)
        - [Option 1 (Git Clone)](#option-1-git-clone)
        - [Option 2 (Zip Downlaod)](#option-2-zip-downlaod)
    - [Configuration](#configuration)
        - [conf.env configuration](#confenv-configuration)
        - [Database configuration](#database-configuration)
    - [Intial Setup](#intial-setup)
    - [Usage](#usage)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [License](#license)

## Getting Started

- ### Prerequisites
  
  Before you begin, ensure you have the following prerequisites installed:
  - Python 3.x
  - Django
  - SQLite (for local development)
  - Any web browser for accessing the application 


- ### Downloading Project

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


- ### Configuration

  - #### .env configuration
    - Create a .env file in the project's root directory to store your configuration variables. See .env.sample file for required variables.

  - #### Database configuration 
    - Change Databse configuration in settings/dev.py according to your database requirement, I would suggest to use some cloud database so that you data is stored regardless where project is running and can have multiple POS setup
  
    - Currently there is optional setting configured for PythonAnyWhere Database, hence they require connecting through ssh. Your database host might require different way to connect. Look into settings/developement.py for further.
  
    - You can also just use SQLite, comment other databse configuration and uncomment sqlite configuration in django settings/devlopement.py Databases. It will map if already present otherwise will create new one.


- ### Intial Setup

  **Correctly setup conf.env file, as well as configure Database correctly in settings. Make sure all tweaks are done according to your setup.**

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
  - Creating your main user, to access admin panel and create more users, if running in docker, use docker shell once docker setup is done.
    ```
    python manage.py createsuperuser
    ```
      - Superuser can create staff and users, hence you want to have one superuser. Also, you wont be able to access admin page for first time without it.
  
      - Staff status for people who you will want to have access to admin panel, you might have to tweak their permission on admin panel. This users will be able to add new products and create department and all.
  
      - User status for people who will just use pos for sales transaction and are not required to manuplate inventory data.


- ### Usage

  This app can be run on any device where django or docker(may require some configuration) can be run. You will need a server/local machine to run the project
  
  - To start the Django development server, run the following command:
  
        python manage.py runserver 0.0.0.0:8000
        # To stop the server, you can typically use Ctrl+C in the terminal where the server is running.
  
  - You can now access the POS system in your web browser by navigating:
  
    - If same machine where django is running
    
        http://127.0.0.1:8000 
    - Same network where django is running, devices with VPN will screw this functionality
    
        http://djangoserver_ip_addrs:8000


- ### Other
  - Reciept Functionality
    This only works on the machine where the project is running, since it requires port connection to printer.
    - Make sure you have receipt printer connected to django server machine.
    - If your tablet can connect to pos printer than configure this project print_recipt method on tranasaction.views accordingly
    
  - Customer Screen
    You need to do a dual monitor setup on the machine where you will accesing POS system, 
    Example: 
    - If accesing POS from Tablet with django server running on rasp-pi or a server, you will connect second monitor to Tablet for this functionality
    - If accesing POS from Window touch tablet/pc with django runnnig locally on same machine, connect second display here for this funcitonality
    

## Features

- Manage inventory and products
- Process sales transactions
- ESPPOS Receipt generation(Only Works if Printer is Connceted to Server or Your device has ESCPOS drivers and can print using those mini printers)
- Multi-device access on the same network using IP address
- Can set-up as live web app, however will have to configure accodingly. Some funcitonality may not work on prod web app.
- Run locally on touch screen device for best functionality
- Can have set up as-display images on customer facing screen, manage images4display folder in base dir of project.

## Screenshots

## License

This project is licensed under the MIT License
