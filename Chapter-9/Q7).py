
# with open("log.txt","r") as f:
#     content = f.readlines()
#     print(type(content))

# lineNo = 1
# for line in content:
#     if "python" in line:
#         print(type(line))
#         print(f"python is present in the log file on line number: {lineNo}")
#         break
#     lineNo+=1
# else:
#         print("No python is not present in the log file")


# needle = "python"
# with open("log.txt", "r", encoding="utf-8") as f:
#     for line_no, line in enumerate(f, 1):
#         if needle in line.lower():  # acceptable
#             print(f"Found at line {line_no}")
            
#     else:
#         print("Not found")



with open("log.txt", "r", encoding="utf-8") as f:
    found = False
    for line_no, line in enumerate(f, 1):
        if "python" in line.lower():
            print(f"Found at line {line_no}")
            found = True
    if not found:
        print("Not found")