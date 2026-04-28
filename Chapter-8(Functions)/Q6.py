# 6. Write a python function which converts inches to cms.
inches = int(input("Enter inches which will be converted to cms = "))
def inches_to_cms(inches):
    cms = 2.54 *inches
    return(cms)

print(inches_to_cms(inches))