def ipv4_address_validator(addr):
    '''
    Regex to validate an ipv4 address.
    Checks if each octet is in range 0-255.
    Returns True/False
    '''
    import re
    pattern=re.compile(r'^([1]?\d?\d|2[0-4]\d|25[0-5])\.([1]?\d?\d|2[0-4]\d|25[0-5])\.([1]?\d?\d|2[0-4]\d|25[0-5])\.([1]?\d?\d|2[0-4]\d|25[0-5])$')
    if pattern.fullmatch(str(addr).strip().strip('\n')): return True
    else:
        print("Invalid IP address entered!")
        return False

def cidr_to_common(cidr_mask):
    '''Function that returns a common mask (Ex: 255.255.255.0)
       for a given input CIDR mask (Ex: 24)'''
    cidrtocommon={1:'128.0.0.0',2:'192.0.0.0',3:'224.0.0.0',4:'240.0.0.0',5:'248.0.0.0',6:'252.0.0.0',7:'254.0.0.0',8:'255.0.0.0',
9:'255.128.0.0',10:'255.192.0.0',11:'255.224.0.0',12:'255.240.0.0',13:'255.248.0.0',14:'255.252.0.0',15:'255.254.0.0',16:'255.255.0.0',
17:'255.255.128.0',18:'255.255.192.0',19:'255.255.224.0',20:'255.255.240.0',21:'255.255.248.0',22:'255.255.252.0',23:'255.255.254.0',24:'255.255.255.0',
25:'255.255.255.128',26:'255.255.255.192',27:'255.255.255.224',28:'255.255.255.240',29:'255.255.255.248',30:'255.255.255.252',31:'255.255.255.254',32:'255.255.255.255'}
    if int(cidr_mask)>=0 and int(cidr_mask)<=32:
        return cidrtocommon[int(cidr_mask)]
    else:
        raise ValueError("Incorrect CIDR mask entered")

def common_to_cidr(common_mask):
    '''Function that returns a CIDR mask (Ex: 24)
        for a given input common mask (Ex: 255.255.255.0)'''
    commontocidr={'128.0.0.0':1,'192.0.0.0':2,'224.0.0.0':3,'240.0.0.0':4,'248.0.0.0':5,'252.0.0.0':6,'254.0.0.0':7,'255.0.0.0':8,
'255.128.0.0':9,'255.192.0.0':10,'255.224.0.0':11,'255.240.0.0':12,'255.248.0.0':13,'255.252.0.0':14,'255.254.0.0':15,'255.255.0.0':16,
'255.255.128.0':17,'255.255.192.0':18,'255.255.224.0':19,'255.255.240.0':20,'255.255.248.0':21,'255.255.252.0':22,'255.255.254.0':23,'255.255.255.0':24,
'255.255.255.128':25,'255.255.255.192':26,'255.255.255.224':27,'255.255.255.240':28,'255.255.255.248':29,'255.255.255.252':30,'255.255.255.254':31,'255.255.255.255':32}
    return commontocidr[common_mask]

def ipv4_mask_validator(mask):
    '''
    Regex to validate an ipv4 subnet mask.
    Checks if each octet is has one of the values (255,254,252,248,240,224,192,128)
    Also checks if the value in next octet is less than previous
    Returns True/False
    '''
    valid_masks=('255','254','252','248','240','224','192','128','0')
    mask_split=mask.strip().strip('\n').split('.')
    count=0
    for i in range(4):
        if i==0 and (mask_split[i] in valid_masks):
            count+=1
            continue
        elif mask_split[i] in valid_masks and mask_split[i]<=mask_split[i-1]:
            count+=1
    if count==4: return True
    else:
        print("Invalid mask entered!")
        return False

def ipv4_subnet_details(addr,mask):
    """
    Function that prints the subnet related details- Network, Broadcast, Host IP range and number of host addresses
    :param addr: IP address
    :param mask: subnet mask
    :return: None. Prints Subnet details
    """
    network_address=[]
    broadcast_address=[]
    num_ips=1   #to keep track of total no of ips in this subnet by multiplying (wcmask per octet+1) in the loop
    wildcard_mask={'255':'0','254':'1','252':'3','248':'7','240':'15','224':'31','192':'63','128':'127','0':'255'}
    for _octet,_mask in zip(addr.split('.'),mask.split('.')): # iterate over octet values and mask values simultaneously
        network_address.append(str(int(_octet) & int(_mask))) # bitwise AND of the octet value and the mask--> gives the network ip
        broadcast_address.append(str(int(_octet)|int(wildcard_mask[_mask]))) # bitwise OR of octet value and wc_mask--> gives the broadcast address
        num_ips*=(int(wildcard_mask[_mask])+1) # multiplies num hosts per octet
    host_address_low=network_address[:3]+[str(int(network_address[3])+1)] # add 1 to last octet of network address to get the first usable host ip
    host_address_high=broadcast_address[:3]+[str(int(broadcast_address[3])-1)] # subtract 1 from the last octet of the broadcast address to get the last usable host ip
    host_ips=num_ips-2 # subtract 2 that is network and bc address
    print(f"Network Address: {'.'.join(network_address)}")
    print(f"Broadcast Address: {'.'.join(broadcast_address)}")
    print(f"Host Address range: {'.'.join(host_address_low)} to {'.'.join(host_address_high)}")
    print(f"Total no. of usable host addresses: {host_ips}")
    return network_address

def subnetting_funct(addr,mask,subnetting_mask):
    wildcard_mask = {'255': '0', '254': '1', '252': '3', '248': '7', '240': '15', '224': '31', '192': '63',
                     '128': '127', '0': '255'}
    if common_to_cidr(subnetting_mask)<common_to_cidr(mask) or common_to_cidr(subnetting_mask)>32:
        print("Invalid Subnetting mask...Please Retry.. Exiting App..")
        return
    else:
        total_sub_networks=2**(common_to_cidr(subnetting_mask)-common_to_cidr(mask))
        print(f"Total subnets: {total_sub_networks}")

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



