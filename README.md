# IPv4 subnet calculator

This python3 script takes an IPv4 address and a subnet mask as input and prints the following info about the subnet:
* Network Address
* Broadcast Address
* Host Address range
* Total number of usable host addresses

The script then prompts the user if it is required to subnet the input network further. If yes, the user can input the mask to be subnetted to. The script returns the number of subnets possible for the given mask.

###Example
Below is an example of the inputs and outputs on the console:
```commandline
Enter IP address: 192.168.1.1
Enter CIDR subnet mask [Ex: 28]: 24
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Host Address range: 192.168.1.1 to 192.168.1.254
Total no. of usable host addresses: 254
Do you want to subnet further?[y/n]: y
Enter CIDR mask to subnet to [Ex: 28]: 25
Total subnets: 2
```
###Author
* Ashish Rao - <ash.floydian@gmail.com>

###License
This project is licensed under the MIT License - see the LICENSE.md file for details