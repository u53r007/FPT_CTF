### TITLE
>Database Attack Analyzing
### DESCRIPTION
> During the operation of the enterprise's IT system, the SOC team suspected that a database server was attacked. You (tier 2 personnel) are assigned to analyze a file (db_attack_capture.pcap) that has previously recorded network traffic. Let's try to analyze and answer the following question: At the 19th line in the pcap file, what is the content of a query that the attacker has entered?

>  Flag format: FUSec{*query}

> Example: query: 1’ or 1=1 => FUSec{1’ or 1=1}
### CATEGORY
>Forensic
### SCORE
>100
### HINT
>None
### DIFFICULTY
>Easy
### FLAG
>FUSec{1' or 1=1 union select database(), user()#}
### SOLVED
Đầu tiên phân tích file pcap. Ta thấy file này ghi lại các cuộc trò chuyện TCP nhưng sử dụng __HTTP__ nên không mã hoá đường truyền vì thế có thể dùng HTTP stream đọc được nội dung. Tìm đến dòng thứ 19 và ngay lập tức có thể thấy được cái query cần tìm.

![image](https://github.com/user-attachments/assets/bface3f4-2f81-4bee-98d0-80bfd7b52165)

![image](https://github.com/user-attachments/assets/93ae48c5-9aff-4dfd-9577-e9e3685a0d33)

#### END!!
