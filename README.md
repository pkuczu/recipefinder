# Recipe Finder
## Introduction

Recipe Finder is a web application designed to simplify meal planning for users. By entering the ingredients they have on hand, users can receive a list of links to recipes they can use with those ingredients. The application utilizes web scraping to collect recipe data from popular recipe websites, making it a valuable tool for those looking to optimize their meal preparation.

For more details, view the full project proposal [here](https://docs.google.com/document/d/1BANoQ4KpEchJ2zy73BZJRA3tW-l91exxKGCVacmxT1I/edit?usp=sharing).


# Developers
Team 47:
- **Patrick Kuczun**: React frontend and Flask server
- **Vivian Chen**: Database and connecting frontend to backend
- **Sarah Dowden**: Webscraping and Importing Information into Database
- **Aanya Singh Dhankhar**: Webscraping and updating Database

# Technical Architecture

<img width="655" alt="Screen Shot 2023-12-03 at 7 22 07 PM" src="https://github.com/CS222-UIUC-FA23/group-project-team47/assets/116613790/06835b43-ec07-4180-99df-78f526346197">


## Package Management

Packages used:

```
pip3 install requests
```
```
pip3 install flask_cors
```
```
pip3 install flask flask-sqlalchemy

```
```
pip3 install beautifulsoup4
```

```
pip3 install sqlite
```

```
npm install react-router-dom
```


Running the Flask server:
```
python3 server.py
```
Running the React application:

```
# make sure it is running on the same port as flask
npm run dev
```
  

