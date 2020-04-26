#!/home/asrao2/my_venvs/py3.7/bin/python

from my_ipv4_functions import *

if __name__=='__main__':
    ip=str(input("Enter IP address: "))
    mask=cidr_to_common(int(input("Enter CIDR subnet mask [Ex: 28]: ")))
    if ipv4_address_validator(ip):
        ipv4_subnet_details(ip,mask)
    subnet_further=str(input("Do you want to subnet further?[y/n]: "))
    if subnet_further=='y':
        subnetting_mask=cidr_to_common(int(input("Enter CIDR mask to subnet to [Ex: 28]: ")))
        subnetting_funct(ip,mask,subnetting_mask)
    elif subnet_further=='n':
        print("Exiting App...")
    else:
        print("Invalid Input.. Please retry. Exiting App...")

