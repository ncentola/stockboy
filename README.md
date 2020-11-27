# Stockboy

Home inventory management system for your pantry & anything with a barcode

I often forget what I have in my home pantry and end up buying more diced tomatoes when I already have 17 cans at home.

This is a simple system that allows me to check what I have in stock from anywhere

## Architecture

![Architecture](/stockboy.png)

The idea is to have this running on a raspberry pi or similar cheap compute device. Barcode scanning will be done on the edge (rpi) and produce messages for the backend to consume. Eventually the backend consumers & services will most likely be deployed as Fargate services via AWS ECS

### Scanner Service
Runs on RPi with a USB barcode scanner. The service translates data from the USB barcode scanner into UPC codes and passes to the message queue. RPi will have an in/out toggle for adding and removing from stock

### Queue
Basic RabbitMQ where a single "scan" goes into a fanout exchange which can then be consumed by the UPC Lookup & Transaction services

### UPC Lookup
Checks if we have the UPC in our system, if not reaches out to a UPC API, retrieves product info, and puts it into the database

### Transaction Service
Consumes messages produced by the scanner and passes them to the API

### API
Simple routes to interact with the DB

### Frontend
Currently a simple Plotly Dash data table which some search & sort functionality

### Database
Simple Postgres db, schemas managed by Flyway
