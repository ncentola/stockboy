# Stockboy
*Work In Progress*
Home inventory management system for your pantry & anything with a barcode

Currently a WIP monorepo - likely to be decomposed in the future

The idea is to have this running on a raspberry pi or similar cheap compute device. Barcode scanning will be done on the edge (rpi) and produce messages for the backend to consume. Eventually the backend consumers & services will most likely be deployed as Fargate services via AWS ECS
