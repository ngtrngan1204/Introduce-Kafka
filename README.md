# Kafka - Cơ bản về Hệ thống Truyền Tin
## Giới thiệu về Kafka
Kafka là một hệ thống truyền tin (messaging system) mã nguồn mở được thiết kế để xử lý và truyền tin nhắn (messages) một cách linh hoạt, hiệu quả và bền bỉ. Nó được xây dựng để xử lý lưu lượng dữ liệu lớn và duy trì tính đáng tin cậy cao.

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/70ac7ea7-f603-4481-b616-05cec1f86680)


## Các Khái Niệm Cơ Bản
### **1. Topic**
**Khái niệm:** Topic trong Kafka là một phân loại hoặc danh mục cho các tin nhắn.  
**Vai trò:** Mỗi tin nhắn được sản xuất (published) và tiêu thụ (consumed) trong Kafka đều thuộc về một topic cụ thể.
### **2. Partition**
**Khái niệm:** Partition là một phần của một topic trong Kafka.  
**Vai trò:** Các partition cho phép dữ liệu được chia nhỏ, phân tán trên nhiều máy chủ (brokers) để tăng khả năng mở rộng và hiệu suất.
### **3. Producer**
**Khái niệm:** Producer là thành phần gửi dữ liệu (messages) tới Kafka topic.  
**Vai trò:** Nó chịu trách nhiệm sản xuất dữ liệu và gửi nó tới các topic cụ thể trong Kafka.
### **4. Consumer**
**Khái niệm:** Consumer là thành phần nhận và xử lý dữ liệu từ Kafka topic.  
**Vai trò:** Consumer đọc các tin nhắn từ các topic và thực hiện các hành động như lưu trữ, xử lý hoặc truyền dữ liệu đó ra ngoài.
### **5. Ứng Dụng**
**Khái niệm:** Các ứng dụng (applications) sử dụng Kafka để gửi và nhận dữ liệu.  
**Vai trò:** Các ứng dụng có thể là producers (gửi dữ liệu) hoặc consumers (nhận và xử lý dữ liệu) trong hệ thống Kafka.

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/2f3667e5-230b-4b99-9f64-040eedc82327)


## Tại sao chọn Kafka?
Kafka có một số ưu điểm mà khiến nó trở thành lựa chọn phổ biến:

**1. Tính Khả Dụng và Bền Bỉ:** Kafka được thiết kế để xử lý lưu lượng dữ liệu lớn và có khả năng mở rộng cao mà vẫn duy trì tính đáng tin cậy.

**2. Phân Tán và Hiệu Suất Cao:** Các partition trong Kafka cho phép dữ liệu được phân tán trên nhiều máy chủ, tăng hiệu suất và khả năng mở rộng của hệ thống.

**3. Hỗ Trợ Tính Toàn Vẹn Dữ Liệu:** Kafka đảm bảo việc lưu trữ và xử lý dữ liệu một cách an toàn và toàn vẹn.

**4. Phù Hợp với Dữ Liệu Thời Gian Thực:** Kafka có khả năng xử lý dữ liệu thời gian thực, phù hợp cho các ứng dụng yêu cầu độ trễ thấp.

**5. Cộng Đồng Mạnh Mẽ và Hỗ Trợ Mở Rộng:** Kafka được sử dụng rộng rãi và có một cộng đồng lớn hỗ trợ việc phát triển và mở rộng tính năng.

Kafka không hoàn toàn thay thế Redis hoặc các hệ thống messaging khác. Sự lựa chọn phụ thuộc vào nhu cầu cụ thể của dự án, với Kafka thường được ưa chuộng trong các trường hợp lưu trữ và xử lý lưu lượng dữ liệu lớn, đặc biệt là trong việc xây dựng hệ thống phân tán và thời gian thực. Kafka có hiệu suất nhanh chóng và ổn định, cung cấp độ bền đáng tin cậy, có đăng kí/ xuất bản linh hoạt phù hợp với số lượng Consumer Group của người tiêu dùng. Có sự sao chép mạnh mẽ, cung cấp cho các Producer sự đảm bảo tính nhất quán. Ngoài ra, Kafka hoạt động tốt với các hệ thống có luồng dữ liệu để xử lý và cho phép các hệ thống đó tổng hợp, chuyển đổi & tải vào các store khác.

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/3cb65fa0-b144-4166-87c3-22bdaa8106b5)

## Mô hình dùng Kafka
* **Messaging:** Kafka có thể được sử dụng để truyền thông tin giữa các ứng dụng. Điều này có thể được sử dụng cho các ứng dụng như:  

  - Hệ thống phân phối thời gian thực  
  - Hệ thống nhắn tin  
  - Hệ thống cảnh báo

* **Stream processing:** Kafka có thể được sử dụng để xử lý dữ liệu theo thời gian thực. Điều này có thể được sử dụng cho các ứng dụng như:
  - Hệ thống phân tích dữ liệu
  - Hệ thống phát hiện lỗi
  - Hệ thống phản hồi nhanh

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/8a2b94b9-93ab-4465-a202-b30d70e67bf8)

* **Data integration:** Kafka có thể được sử dụng để tích hợp dữ liệu từ các nguồn khác nhau. Điều này có thể được sử dụng cho các ứng dụng như:
  - Hệ thống thu thập dữ liệu
  - Hệ thống báo cáo
  - Hệ thống phân tích dữ liệu

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/b154c997-dc2b-4888-aea2-f7aa644bd91c)

* **Event sourcing:** Kafka có thể được sử dụng để lưu trữ lịch sử các sự kiện. Điều này có thể được sử dụng cho các ứng dụng như:
  - Hệ thống quản lý cơ sở dữ liệu
  - Hệ thống quản lý ứng dụng
  - Hệ thống phân tích dữ liệu

![image](https://github.com/ngtrngan1204/Introduce-Kafka/assets/109300791/0e5bed9e-38a0-4067-89f4-ff30e934ce5b)

* **Commit log:** Kafka có thể được sử dụng làm commit log cho các hệ thống phân tán. Điều này có thể được sử dụng để đảm bảo tính nhất quán của dữ liệu trong các hệ thống phân tán.

## Các properties của consumer

Các properties của consumer được sử dụng để cấu hình cách thức hoạt động của consumer. Một số properties quan trọng bao gồm:

**group.id:** Đây là ID của nhóm consumer mà consumer thuộc về. Các consumer trong cùng một nhóm sẽ chia sẻ nhau công việc tiêu thụ dữ liệu.  
**bootstrap.servers:** Đây là danh sách các URL của brokers Kafka.  
**key.deserializer:** Đây là lớp giải mã được sử dụng để giải mã các khóa dữ liệu.  
**value.deserializer:** Đây là lớp giải mã được sử dụng để giải mã các giá trị dữ liệu.  
**auto.offset.reset:** Đây là cách thức mà consumer sẽ xử lý các offset dữ liệu. Có ba giá trị có thể được sử dụng:  
**earliest:** Consumer sẽ bắt đầu từ offset đầu tiên của topic.  
**latest:** Consumer sẽ bắt đầu từ offset mới nhất của topic.  
**none:** Consumer sẽ không xử lý các offset dữ liệu.  
**max.poll.records:** Đây là số lượng record tối đa mà consumer sẽ xử lý trong một lần poll.  
**session.timeout.ms:** Đây là khoảng thời gian tối đa mà consumer có thể không gửi yêu cầu nào đến brokers Kafka. Nếu consumer không gửi yêu cầu nào trong khoảng thời gian này, nó sẽ bị loại bỏ khỏi nhóm consumer.  

## Các thông số cần quan tâm
Khi sử dụng Kafka consumer, cần quan tâm đến các thông số sau:

* **Throughput:** Throughput là số lượng record mà consumer có thể tiêu thụ trong một đơn vị thời gian. Thông số này phụ thuộc vào nhiều yếu tố, bao gồm:

  - Số lượng brokers Kafka
  - Số lượng consumer
  - Kích thước record
  - Tốc độ xử lý của consumer

* **Latency:** Latency là khoảng thời gian giữa lúc consumer nhận được record và lúc consumer xử lý xong record. Thông số này phụ thuộc vào nhiều yếu tố, bao gồm:

  - Khoảng cách giữa consumer và brokers Kafka
  - Số lượng brokers Kafka
  - Kích thước record
  - Tốc độ xử lý của consumer

* **Reliability:** Reliability là khả năng của consumer để xử lý tất cả các record mà nó nhận được. Thông số này phụ thuộc vào nhiều yếu tố, bao gồm:

  - Số lượng brokers Kafka
  - Số lượng consumer
  - Khả năng chịu lỗi của brokers Kafka
  - Khả năng chịu lỗi của consumer

* **Scalability:** Scalability là khả năng của consumer để đáp ứng với sự gia tăng về khối lượng dữ liệu. Thông số này phụ thuộc vào nhiều yếu tố, bao gồm:

  - Khả năng mở rộng của brokers Kafka
  - Khả năng mở rộng của consumer

* **Cost:** Cost là chi phí để vận hành Kafka consumer. Thông số này phụ thuộc vào nhiều yếu tố, bao gồm:

  - Số lượng brokers Kafka
  - Số lượng consumer
  - Khả năng xử lý của brokers Kafka
  - Khả năng xử lý của consumer
