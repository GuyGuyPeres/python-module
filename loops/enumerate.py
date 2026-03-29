# enumerate
# zip

# servers = ["web-01", "web-02", "web-03"]
# [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for server in enumerate(servers):
#     print(type(server))
#     print(server)
#     print(f"this is tuple {server}")
    

# servers = ["web-01", "web-02", "web-03"]
# # [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for index, server in enumerate(servers):
#     # print(type(server))
#     # print(server)
#     # print(server[0]) # index
#     # print(server[1]) # item
#     print(f"{index} Proccessing server {server}")

# names = ["Alice", "Bob", "Charlie"]
# for name in enumerate(names):
    # print(name)
    
# servers = ["app-01", "app-02", "app-03"]
# for server in enumerate(servers, start=1):
#     print(server)

# errors = ["disk full", "timeout", "connection lost"]
# for index, error in enumerate(errors):
#     if(index % 2 == 0):
#         print(error)

# ports = [22, 80, 443, 8080]
# for index, port in enumerate(ports, start=0):
#     if(index >= 1):
#         print(port)
        
# users = ["admin", "dev", "ops"]
# for index, user in enumerate(users):
#     print(f"user {index}: {user}")

# files = ["log1.txt", "log2.txt", "log3.txt"]
# for index, file in enumerate(files):
#     if(index == len(files) - 1):
#         print(file)
        
# regions = ["us-east-1", "eu-west-1", "ap-south-1"]
# for index, region in enumerate(regions):
#     if(index > 0):
#         print(region)

# tasks = ["backup", "cleanup", "monitoring"]
# for index, task in enumerate(tasks):
#     if(index % 2 != 0):
#         print(task)

# containers = ["c1", "c2", "c3", "c4"]
# for index, container in enumerate(containers):
#     print(container)
#     if(index == 2):
#         break