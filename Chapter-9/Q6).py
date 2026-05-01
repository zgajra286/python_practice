# 6.	Write a program to mine a log file and find out whether it contains ‘python’. 

with open("log.txt","r") as f:
    content = f.read().strip()
    
    if "python" in content:
        print("python is present in the log file")
    else:
        print("python is not present in the log file")
