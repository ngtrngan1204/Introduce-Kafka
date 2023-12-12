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


## Tại sao chọn Kafka?
Kafka có một số ưu điểm mà khiến nó trở thành lựa chọn phổ biến:

**1. Tính Khả Dụng và Bền Bỉ:** 

**2. Phân Tán và Hiệu Suất Cao:**

**3. Hỗ Trợ Tính Toàn Vẹn Dữ Liệu:** 

**4. Phù Hợp với Dữ Liệu Thời Gian Thực:** 

**5. Cộng Đồng Mạnh Mẽ và Hỗ Trợ Mở Rộng:** 

Kafka không hoàn toàn thay thế Redis hoặc các hệ thống messaging khác.  afka thường được ưa chuộng trong các trường hợp lưu trữ và xử lý lưu lượng dữ liệu lớn, đặc biệt là trong việc xây dựng các hệ thống phân tán và thời gian thực. Kafka có thế mạnh là hiệu suất nhanh chóng và ổn định, cung cấp độ bền đáng tin cậy, có đăng kí/ xuất bản linh hoạt phù hợp với số lượng Consumer Group của người tiêu dùng. Cùng với sự sao chép mạnh mẽ, cung cấp cho các Producer sự đảm bảo tính nhất quán. Ngoài ra, Kafka hoạt động tốt với các hệ thống có luồng dữ liệu để xử lý và cho phép các hệ thống đó tổng hợp, chuyển đổi & tải vào các store khác.

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/3cb65fa0-b144-4166-87c3-22bdaa8106b5)

## Use Cases
* **Messaging:** Kafka works well as a replacement for a more traditional message broker. Message brokers are used for a variety of reasons (to decouple processing from data producers, to buffer unprocessed messages, etc). In comparison to most messaging systems Kafka has better throughput, built-in partitioning, replication, and fault-tolerance which makes it a good solution for large scale message processing applications.


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

* **Event sourcing:** Được sử dụng để thu thập và lưu trữ lịch sử các sự kiện, thường được ứng dụng trong:
  - Hệ thống quản lý cơ sở dữ liệu
  - Hệ thống quản lý ứng dụng
  - Hệ thống phân tích dữ liệu

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/0e5bed9e-38a0-4067-89f4-ff30e934ce5b)

* **Commit log:** Kafka có thể được sử dụng làm commit log cho các hệ thống phân tán đồng thời đảm bảo tính nhất quán của dữ liệu trong các hệ thống phân tán.

## Các properties của Consumer cần quan tâm

Các properties của consumer được sử dụng để cấu hình cách thức hoạt động của consumer.

- **group.id:** ID của nhóm consumer mà consumer thuộc về. Các consumer trong cùng một nhóm sẽ chia sẻ nhau công việc tiêu thụ dữ liệu.  

- **bootstrap.servers:** Danh sách các URL của brokers Kafka.  

- **key.deserializer:** Lớp giải mã được sử dụng để giải mã các khóa dữ liệu.  

- **value.deserializer:** Lớp giải mã được sử dụng để giải mã các giá trị dữ liệu.  

- **auto.offset.reset:** Cách thức mà consumer sẽ xử lý các offset dữ liệu. Có ba giá trị có thể được sử dụng:  
  - **earliest:** Consumer sẽ bắt đầu từ offset đầu tiên của topic.  
  - **latest:** Consumer sẽ bắt đầu từ offset mới nhất của topic.  
  - **none:** Consumer sẽ không xử lý các offset dữ liệu.  
- **max.poll.records:** Số lượng record tối đa mà consumer sẽ xử lý trong một lần poll.  
- **session.timeout.ms:** Khoảng thời gian tối đa mà consumer có thể không gửi yêu cầu nào đến brokers Kafka. Nếu consumer không gửi yêu cầu nào trong khoảng thời gian này, nó sẽ bị loại bỏ khỏi nhóm consumer.  

## Các properties của Producer cần quan tâm

Kafka Producer có một số thuộc tính quan trọng mà bạn cần quan tâm khi cấu hình Producer để tối ưu hóa hiệu suất và đảm bảo tính ổn định của hệ thống. 

- **bootstrap.servers**: Địa chỉ của Kafka broker hoặc danh sách các broker. Producer sẽ gửi dữ liệu tới các broker được liệt kê ở đây.

- **acks**: Quy định cách Producer xác nhận rằng một message đã được gửi thành công. Có các giá trị acks khác nhau như:

  - **0**: Producer không chờ xác nhận từ broker nào.
  - **1**: Producer chờ xác nhận từ broker leader.
  - **all**: Producer chờ xác nhận từ tất cả các replicas.
- **retries**: Số lần retry khi gửi message thất bại trước khi bỏ cuộc.

- **batch.size**: Kích thước tối đa của một batch trước khi gửi đi. Batching giúp tối ưu hóa hiệu suất bằng cách gửi nhiều message cùng một lúc.

- **linger.ms**: Thời gian tối đa mà Producer có thể chờ trước khi gửi một batch, ngay cả khi batch đã đầy.

- **compression.type**: Loại nén dữ liệu trước khi gửi (ví dụ: gzip, snappy). Nén có thể giảm băng thông và tăng tốc độ truyền dữ liệu.

- **max.in.flight.requests.per.connection**: Số lượng tối đa các request chưa được xác nhận mà Producer có thể gửi tới một broker mà không cần chờ xác nhận.

- **buffer.memory**: Bộ nhớ được cấp phát cho Producer để lưu trữ các message trước khi chúng được gửi đi.

- **max.request.size**: Kích thước tối đa cho một request gửi tới Kafka.

- **retry.backoff.ms**: Thời gian chờ giữa các lần retry.

- **request.timeout.ms**: Thời gian tối đa cho một request trước khi nó bị timeout.
