# Kafka - Cơ bản về Hệ thống Truyền Tin
## Giới thiệu về Kafka
Kafka là một hệ thống truyền tin (messaging system) mã nguồn mở được thiết kế để xử lý và truyền tin nhắn (messages) một cách linh hoạt, hiệu quả và bền bỉ. Nó được xây dựng để xử lý lưu lượng dữ liệu lớn và duy trì tính đáng tin cậy cao.

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/70ac7ea7-f603-4481-b616-05cec1f86680)


## Các Khái Niệm Cơ Bản
### **1. Topic**
Là một phân loại hoặc danh mục cho các tin nhắn. Mỗi tin nhắn được sản xuất (published) và tiêu thụ (consumed) trong Kafka đều thuộc về một topic cụ thể.
### **2. Partition**
Partition là một phần của một topic trong Kafka. Các partition cho phép dữ liệu được chia nhỏ, phân tán trên nhiều máy chủ (brokers) để tăng khả năng mở rộng và hiệu suất.
### **3. Producer**
Producer là thành phần gửi dữ liệu (messages) tới Kafka topic. Nó chịu trách nhiệm sản xuất dữ liệu và gửi nó tới các topic cụ thể trong Kafka.
### **4. Consumer**
Là thành phần nhận và xử lý dữ liệu từ Kafka topic. Consumer đọc các tin nhắn từ các topic và thực hiện các hành động như lưu trữ, xử lý hoặc truyền dữ liệu đó ra ngoài.
### **5. Ứng Dụng**
Các ứng dụng có thể là producers (gửi dữ liệu) hoặc consumers (nhận và xử lý dữ liệu) trong hệ thống Kafka.

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

## Mô hình dùng Kafka
* **Messaging:** Như đã biết, Kafka được sử dụng để truyền thông tin giữa các ứng dụng. Các ứng dụng thường dùng Kafka như:  

  - Hệ thống phân phối thời gian thực  
  - Hệ thống nhắn tin  
  - Hệ thống cảnh báo

* **Stream processing:** Là hệ thống có thế mạnh thu thập và xử lý lượng dữ liệu lớn trong thời gian thực nên thường được sử dụng vào:  
  - Hệ thống phân tích dữ liệu
  - Hệ thống phát hiện lỗi
  - Hệ thống phản hồi nhanh

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/8a2b94b9-93ab-4465-a202-b30d70e67bf8)

* **Data integration:** Kafka còn có thể được sử dụng để tích hợp dữ liệu từ các nguồn khác nhau như:
  - Hệ thống thu thập dữ liệu
  - Hệ thống báo cáo
  - Hệ thống phân tích dữ liệu

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/b154c997-dc2b-4888-aea2-f7aa644bd91c)

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
