# Kafka 
## Introduction

Kafka combines three key capabilities so you can implement your use cases for event streaming end-to-end with a single battle-tested solution:

  - **To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems.**
  - **To store streams of events durably and reliably for as long as you want.**
  - **To process streams of events as they occur or retrospectively.**

And all this functionality is provided in a distributed, highly scalable, elastic, fault-tolerant, and secure manner.

   ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/70ac7ea7-f603-4481-b616-05cec1f86680)


## How it works and basic concepts
Kafka is a distributed system consisting of servers and clients communicating via a high-performance TCP network protocol. 
**Servers**: Kafka is run as a cluster of one or more servers that can span multiple data centres or cloud regions. Some of these servers form the storage layer, called the brokers. Other servers run Kafka Connect to continuously import and export data as event streams to integrate Kafka with your existing systems such as relational databases as well as other Kafka clusters. To let you implement mission-critical use cases, a Kafka cluster is highly scalable and fault-tolerant.

**Clients**: They allow you to write distributed applications and microservices that read, write, and process streams of events in parallel, at scale, and in a fault-tolerant manner even in the case of network problems or machine failures.

An **event** records also called record or message. When you read or write data to Kafka, you do this in the form of events.

**Producers** are those client applications that publish (write) events to Kafka, and **consumers** are those that subscribe to (read and process) these events. In Kafka, producers and consumers are fully decoupled and agnostic of each other, which is a key design element to achieve high scalability

Events are organized and durably stored in **topics**. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder. Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. 

Topics are **partitioned**, meaning a topic is spread over several "buckets" located on different Kafka brokers. This distributed placement of your data is very important for scalability because it allows client applications to both read and write the data from/to many brokers at the same time. When a new event is published to a topic, it is actually appended to one of the topic's partitions. Events with the same event key (e.g., a customer or vehicle ID) are written to the same partition, and Kafka guarantees that any consumer of a given topic-partition will always read that partition's events in exactly the same order as they were written.

  ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/2f3667e5-230b-4b99-9f64-040eedc82327)


## Benefits of using Kafka

- **Real-Time Data Processing**: Kafka is designed for real-time data processing and streaming, allowing respond quickly to emerging events. This is useful for monitoring, analysis, and immediate response to changing situations.

- **High Consistency and Reliability**: Keeps data consistent through backup and message replication across brokers. This ensures data is not lost and is always available for consuming applications.

- **Easy Scalability**: Easily scalable by adding brokers to the cluster. This allows increased data processing capacity without changing the entire system structure.

- **Diverse Data**: Kafka not only supports regular data but is also capable of processing diverse data such as logs, application status, events related to financial transactions, and many other types of data.

- **Large Volume Ability**: Through the use of partitioning, it is capable of handling large amounts of data efficiently. This makes it suitable for situations that need to process billions of events per day.

- **Flexible integration**: Kafka has the ability to integrate with many other technologies and applications, can use different programming languages ​​to write producer and consumer applications, and Kafka also supports different transport protocols.

- **Long-Term Data Storage**: In addition to real-time data processing, it is also capable of long-term data storage. This allows storage and retrieval of event data in the future for analysis and auditing.

- **Log System**: Kafka acts as a log system, allowing storage and search of event information over time, useful for debugging, data analysis, and monitoring system activity.

    ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/3cb65fa0-b144-4166-87c3-22bdaa8106b5)


## Use Cases
* **Messaging:** Kafka works well as a replacement for a more traditional message broker. Message brokers are used for a variety of reasons (to decouple processing from data producers, to buffer unprocessed messages, etc). In comparison to most messaging systems Kafka has better throughput, built-in partitioning, replication, and fault-tolerance which makes it a good solution for large scale message processing applications.
  - At PayPal, Kafka is used for first-party tracking, application health metrics streaming and aggregation, database synchronization, application log aggregation, batch processing, risk detection and management, and analytics and compliance, with each of these use-cases processing over 100 billion messages per day. Kafka fleet consists of over 1,500 brokers that host over 20,000 topics and close to 2,000 Mirror Maker nodes which are used to mirror the data among the clusters, offering 99.99% availability for our Kafka clusters.
  - PayPal infrastructure is spread across multiple geographically distributed data centres and security zones. The Kafka clusters are deployed across these zones, based on data classification and business requirements. MirrorMaker is used to mirror the data across the data centers, which helps with disaster recovery and to achieve inter-security zone communication.
  
    ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/bc619b23-8743-42f4-b00b-fd469b09fee4)

* **Website Activity Tracking**: The original use case for Kafka was to be able to rebuild a user activity tracking pipeline as a set of real-time publish-subscribe feeds. This means site activity (page views, searches, or other actions users may take) is published to central topics with one topic per activity type. These feeds are available for subscription for a range of use cases including real-time processing, real-time monitoring, and loading into Hadoop or offline data warehousing systems for offline processing and reporting.

  - Apache Kafka is a core part of infrastructure at LinkedIn. It was originally developed in-house as a stream processing platform and was subsequently open-sourced, with a large external adoption rate today. Kafka is used extensively throughout software stack, powering use cases like activity tracking, message exchanges, metric gathering, and more. LinkedIn maintains over 100 Kafka clusters with more than 4,000 brokers, which serve more than 100,000 topics and 7 million partitions. The total number of messages handled by LinkedIn’s Kafka deployments recently surpassed 7 trillion per day.
  - The streaming ecosystem built around Apache Kafka is a key part of our technology stack at LinkedIn. The ecosystem includes the following components:

      - Kafka clusters, consisting of brokers 
      - Application with Kafka client
      - REST proxy for serving non-Java client
      - Schema registry for maintaining Avro schemas
      - Brooklin for mirroring among clusters
      - Cruise Control for Apache Kafka for cluster maintenance and self-healing
      - Pipeline completeness audit and a usage monitor called “Bean Counter”

        ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/dfb42baf-7c16-426c-a4b3-8a3c703d01f3)


* **Stream processing:** Many users of Kafka process data in processing pipelines consisting of multiple stages, where raw input data is consumed from Kafka topics and then aggregated, enriched, or otherwise transformed into new topics for further consumption or follow-up processing.
  - Netflix embraces Apache Kafka® as the de-facto standard for its eventing, messaging, and stream processing needs. Kafka acts as a bridge for all point-to-point and Netflix Studio wide communications. It provides with the high durability and linearly scalable, multi-tenant architecture required for operating systems at Netflix. In-house Kafka as a service offering provides fault tolerance, observability, multi-region deployments, and self-service. This makes it easier for entire ecosystem of microservices to easily produce and consume meaningful events and unleash the power of asynchronous communication.
  - A typical message exchange within Netflix Studio ecosystem looks like this:

    ![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/c405d72d-49d3-4551-87e4-8c1dc5ed1838)


* **Log Aggregation**: Many people use Kafka as a replacement for a log aggregation solution. Log aggregation typically collects physical log files off servers and puts them in a central place (a file server or HDFS perhaps) for processing. Kafka abstracts away the details of files and gives a cleaner abstraction of log or event data as a stream of messages. This allows for lower-latency processing and easier support for multiple data sources and distributed data consumption

* **Commit Log**: Kafka can serve as a kind of external commit-log for a distributed system. The log helps replicate data between nodes and acts as a re-syncing mechanism for failed nodes to restore their data.

## Important properties of Kafka Consumer

  - **bootstrap.servers**: A list of host/port pairs used to establish the initial connection to the Kafka cluster. The consumer needs to discover the cluster and start consuming messages.

  - **group.id**: Specifies the consumer group the consumer belongs to. Consumers in the same group collaborate to consume messages from a topic.
  
  - **key.deserializer**: Defines the class responsible for deserializing the message keys from bytes to their actual data type.
  
  - **value.deserializer**: Similar to the key deserializer, this class handles deserialization of message values.
  
  - **fetch.min.bytes**: Specifies the minimum amount of data the consumer expects in a fetch request. It influences the efficiency of data transfer.
  
  - **fetch.max.bytes**: Sets the maximum number of bytes the consumer retrieves per partition in a fetch request.
  
  - **enable.auto.commit**: Controls whether the consumer automatically commits offsets after consuming messages. Disabling it allows for manual commit control.
  
  - **auto.offset.reset**: Determines how the consumer handles the initial offset when starting for the first time or after a rebalance.
  
  - **isolation.level**: Defines the level of data isolation between consumers in the same group, ensuring consistent data processing.
  
  - **max.poll.records**: Limits the number of records returned in each poll call, influencing processing efficiency and resource consumption.
  
  - **session.timeout.ms**: Defines the inactivity period after which the consumer is considered disconnected from the group and triggers a rebalance.
  
  - **heartbeat.interval.ms**: Specifies the interval at which the consumer sends heartbeats to the group coordinator, indicating its active status.

## Important properties of Kafka Producer

  - **bootstrap.servers**: Defines a list of host/port pairs used to establish the initial connection to the Kafka cluster. This facilitates cluster discovery and message sending by the producer.

  - **acks**: Specifies the level of acknowledgment required from the Kafka brokers before considering a message sent successfully. Possible values include:
    - **0**: Fire-and-forget; no acknowledgment is requested.
  
    - **1**: Wait for acknowledgment from the leader of the partition.
    
    - **all**: Wait for acknowledgment from all replicas of the partition.
  - **key.serializer**: Defines the class responsible for serializing message keys from their actual data type to bytes.
  
  - **value.serializer**: Similar to the key.serializer, this property defines the class used to serialize message values.

  - **retries**: Sets the number of times the producer retries sending a message in case of failure.
  
  - **enable.idempotence**: Enables idempotent message delivery, ensuring that each message is delivered exactly once, even in case of retries or network issues.
  
  - **batch.size**: Configures the size of the batch used for sending messages. Larger batches can improve throughput but increase latency.
  
  - **linger.ms**: Defines the maximum amount of time the producer waits for more messages to be added to the batch before sending it.
  
  - **buffer.memory**: Sets the maximum amount of memory the producer can use for buffering messages before sending them.
  
  - **max.in.flight.requests.per.connection**: Limits the number of outstanding requests the producer can have per connection.

## Sample
  - **Docker compose**: environment
    - **Zookeeper**: `ALLOW_ANONYMOUS_LOGIN: 'yes' # Allow anonymous login to ZooKeeper`
    - **Kafka**:
        ```
        KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181   # Kafka will use to connect to ZooKeeper
        ALLOW_PLAINTEXT_LISTENER: 'yes'   # Allow plain text listener connections
        KAFKA_LISTENERS: INTERNAL://:9090,EXTERNAL://:9092   # Defining two listeners - INTERNAL and EXTERNAL - on ports 9090 and 9092
        KAFKA_ADVERTISED_LISTENERS: INTERNAL://:9090,EXTERNAL://:9092   # Addresses are advertised to ZooKeeper for clients to connect
        KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT   # Maps the listener names  to security protocols
        KAFKA_INTER_BROKER_LISTENER_NAME: INTERNAL   # The listener used for communication between brokers
        BOOTSTRAP_SERVERS: kafka:9092   # Defines the initial brokers as a comma-separated list for Kafka clients to connect
    - **Kowl**:
        `KAFKA_BROKERS: "kafka:9092"   # Kafka broker address that Kowl will use to connect and interact with Kafka
    - Set the ip address to host Kafka:
      ```
      nano /etc/hosts
      # Write to the file:
      1.52.246.121 Kafka # Public ip
    - Run the command to create topic:
      ```
      docker exec -it KAFKA  kafka-topics.sh --create --topic testing --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1  
## Example usage

  - **Consumer**:  initializes a Kafka consumer with specified configurations, subscribes to a given topic, and continuously polls for messages. When a message is received, it's checked for successful reception and any potential errors. If the message is error-free, it decodes the data, extracts the key, and attempts to store this data into Redis. If successful, it prints a success message; otherwise, it logs the error.
  - **Producer**: a FastAPI application serving as an API for handling CPU information. It consists of two endpoints:
    - **POST Endpoint (/cpu-info/<id_counter>)**:

      - Receives CPU information data in JSON format via POST requests.
      - Validates the received JSON data, ensuring it contains specific required fields of integer type.
      - Sends the validated data to a Kafka topic using a Kafka producer.
      - Responds with the posted data in JSON format or appropriate error messages if the data is invalid.
  
    - **GET Endpoint (/cpu-info/<m_id>)**:

      - Retrieves CPU information data from Redis based on the provided <m_id>.
      - If the data exists in Redis associated with the given <m_id>, it responds with the data in JSON format.
      - If the data is not found, it returns a "Data not found" error message with a status code 404.
  - **Instruction document**: http://ngan.cpe-lab.com:5050/docs
