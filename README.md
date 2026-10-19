# KafkaRabbitmq2026
Comparative study of Apache Kafka and RabbitMQ for Distributed Systems.
Overview

This project presents a comparative functional study of Apache Kafka and RabbitMQ in the context of distributed systems and message-based communication.

Both technologies are deployed locally using Docker Compose and tested through Python producer and consumer applications. The experiments explore message delivery, multiple messages, consumer groups, partitions, message persistence, event replay, and recovery scenarios.

The goal is to understand the main differences between the two messaging systems through practical experiments rather than quantitative performance benchmarking.

Technologies

Apache Kafka — distributed event streaming platform.

RabbitMQ — message broker supporting queue-based messaging.

Python — implementation of producer and consumer applications.

Docker Compose — local deployment and management of the services.

LaTeX — preparation of the project report.

Project Structure

KafkaRabbitmq2026/
├── docker/        # Docker configuration
├── experiments/   # Experiment-related files and results
├── kafka/         # Kafka producer and consumer scripts
├── rabbitmq/      # RabbitMQ producer and consumer scripts
├── report/        # LaTeX report and figures
├── .gitignore
└── README.md

Requirements

Before running the experiments, make sure the following software is installed:

Docker

Docker Compose

Python 3

pip

The Python clients use the following libraries:

kafka-python for Apache Kafka

pika for RabbitMQ


The RabbitMQ management interface can be used to inspect queues, messages, consumers, and broker status. Kafka is inspected through command-line tools.

Experiments

The project includes experiments covering the following aspects:

RabbitMQ

Basic producer–consumer communication

Asynchronous message delivery

Multiple messages

Competing consumers

Durable queues and persistent messages

Message redelivery after consumer interruption

Apache Kafka

Basic producer–consumer communication

Multiple messages

Multiple consumers with a single partition

Multiple consumers with multiple partitions

Event persistence and consumer offsets

Event replay

Broker restart persistence

Consumer failure recovery

The experiments are intended to examine functional behavior and messaging mechanisms. They do not constitute a quantitative throughput or latency benchmark.


Report

The LaTeX report is located in the report/ directory. It describes the system architecture, experimental methodology, test results, and comparison between RabbitMQ and Apache Kafka.

Limitations

The experiments use a local Docker-based environment on a single physical machine. The project focuses on functional behavior and does not evaluate production-scale deployments or provide quantitative performance measurements.