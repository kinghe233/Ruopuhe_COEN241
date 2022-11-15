Task 1: Defining custom topologies

Questions

1. What is the output of “nodes” and “net”
Nodes:
	available nodes are:
	c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7
net:
	h1 h1-eth0:s3-eth2
	h2 h2-eth0:s3-eth3
	h3 h3-eth0:s4-eth2
	h4 h4-eth0:s4-eth3
	h5 h5-eth0:s6-eth2
	h6 h6-eth0:s6-eth3
	h7 h7-eth0:s7-eth2
	h8 h8-eth0:s7-eth3
	s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
	s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
	s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
	s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
	s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
	s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
	s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
	c0

2. What is the output of “h7 ifconfig”
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
		inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
		inet6 fe80::5f7:9c9c:fe2f:53ef  prefixlen 64  scopeid 0x20<link>
		ether 8e:9c:4b:20:dc:b5  txqueuelen 1000  (Ethernet)
		RX packets 72  bytes 5476 (5.4 KB)
		RX errors 0  dropped 0  overruns 0  frame 0
		TX packets 12  bytes 936 (936.0 B)
		TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

	lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
		inet 127.0.0.1  netmask 255.0.0.0
		inet6 ::1  prefixlen 128  scopeid 0x10<host>
		loop  txqueuelen 1000  (Local Loopback)
		RX packets 0  bytes 0 (0.0 B)
		RX errors 0  dropped 0  overruns 0  frame 0
		TX packets 0  bytes 0 (0.0 B)
		TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


Task 2: Analyze the “of_tutorial’ controller

Questions
1. Draw the function call graph of this controller. For example, once a packet comes to thecontroller, which function is the first to be called, which one is the second, and so forth?
Here is the function call graph of this controller:
Launch Function() -> start_switch(event) -> class tutorial constructor() -> handle_packetln() -> ack_like_hub() -> resend_packet()

2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long does it take (on average) to ping for each case?
The average time of h1 ping h2 = 7.212ms
The average time of h1 ping h8 = 27.605ms

b. What is the minimum and maximum ping you have observed?
h1 ping h2:
	min: 1.42ms
	max: 17.457ms
h1 ping h8:
	min: 7.546ms
	max: 54.756ms

c. What is the difference, and why?
H1 ping h8 takes much more time than h1 ping h2, because the packets between h1 and h8 have to travel through multiple switches than h1 and h2.

3. Run “iperf h1 h2” and “iperf h1 h8”
a. What is “iperf” used for?
Test the TCP bandwidth between two hosts

b. What is the throughput for each case?
h1-> h2: 
Results: [‘7.58 Mbits/sec’,’8.14 Mbits/sec’]
h1-> h8: 
Results: [‘3.54 Mbits/sec’,’3.84 Mbits/sec’]

c. What is the difference and explain the reasons for the difference.
The throughput between h1 and h2 is much higher than between h1 and h8, because h1 is only connected with h2 by switch s3, but h1 to h8 needs more switches than h1 to h2.

4. Which of the switches observe traffic? Please describe your way for observing 
Because of act_like_hub() sending packets to all the switches in the network, the all switches observe traffic. In order to observe the traffic, we can add a log print statement in the method of handle_packetln() to keep track of each packets.

Task 3: MAC Learning Controller
Questions
1. Describe how the above code works, such as how the "MAC to Port" map is established. You could use a ‘ping’ example to describe the establishment process (e.g., h1 ping h2).
	Because all the switches have own dictionaries which map the MAC address to its corresponding port number. So, if a switch receives a packet, it will check if the packet source address is present in its own dictionary and destination address of packet is present in the HashMap. Then, the switch will resend the packet to the destination address if it is, else will resend the packet to all ports.

2. Have h1 ping h2, and h1 ping h8 for 100 times (e.g., h1 ping -c100 p2).
a. How long did it take (on average) to ping for each case?
The average time of h1 ping h2 = 4.241 ms
The average time of h1 ping h8 = 11.237 ms

b. What is the minimum and maximum ping you have observed?
h1 ping h2:
	min: 1.573 ms
	max: 5.741 ms
h1 ping h8:
	min: 6.782 ms
	max: 38.563 ms

c. Any difference from Task 2 and why do you think there is a change if there is?
The difference is that pings in task 2 cost less time, because with the mac_to_port dictionary, switches have MAC address so that packets can be send directly to destination address. 

3. Q.3 Run “iperf h1 h2” and “iperf h1 h8”.
a. What is the throughput for each case?
Iperf h1 h2:
	Results: [’51.2 Mbits/sec’, ’53.4 Mbits/sec’]
Iperf h1 h8:
	Results: [’11.3 Mbits/sec’, ’13.2 Mbits/sec’]

b. What is the difference from Task 2 and why do you think there is a change if there is?
The throughput for h1-h2 and h1-h8 is much higher than that in task 2. I think this is because of the help of mac_to_port dictionary, switches can send packets directly to destination address so that congestion can be reduced greatly.
