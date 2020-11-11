def ip_to_int32(ip4=type(str)):
    """This function converts the IP address to a 32 bit number then to a 10 number system"""
    listing = ip4.split(".")
    listing = [int(i) for i in listing]
    listing2 = list()
    for x in listing:
        binary=''
        while x:
            binary += str(x % 2)
            x //= 2
        binary2 = '0'*(8-len(binary))
        binary2 += binary[::-1]
        listing2.append(binary2)
        binary=''.join(listing2)

    return int(binary,2)


print(ip_to_int32("128.32.10.1 "))
print(ip_to_int32("0.0.0.0"))
print(ip_to_int32("128.114.17.104"))
