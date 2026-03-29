this_list = ["python3", "pip", "requests", "boto3", "pip"]

required_packages = set(this_list)
print(required_packages)
print(f"Is request required? true/fals- {"requests" in required_packages}")
print(f"is ansible required? true/false- {"ansible" in required_packages}")
required_packages.add("paramiko")
print(required_packages)
required_packages.discard("pip")
print(required_packages)

installed_packages = {"docker", "python3", "pip"}

missing_packages = required_packages - installed_packages
extra_packages = installed_packages - required_packages
common_packages = required_packages & installed_packages

 
