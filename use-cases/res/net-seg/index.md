#### Simulation

Before applying the policy all network connections to the mysql pod is permitted from other pods and the attacker can use ICMP for discovery

```sh
vagrant@master-node:—$ kubectl exec -it wordpress-fb448db97-46rrn -n wordpress-mysql -- /bin/bash 
root@wordpress-fb448db97-46rrn:/var/www/html# ping 10.0.0.10 
PING 10.0.0.10 (10.0.0.10): 56 data bytes 
64 bytes from 10.0.0.10: icmp_seq=0 tt1=64 time=0.078 ms
64 bytes from 10.0.0.10: icmp_seq=1 tt1=64 time=0.156 ms 
64 bytes from 10.0.0.10: icmp_seq=2 tt1=64 time=0.090 ms 
64 bytes from 10.0.0.10: icmp_seq=3 tt1=64 time=0.037 ms 
64 bytes from 10.0.0.10: icmp_seq=4 tt1=64 time=0.123 ms 
64 bytes from 10.0.0.10: icmp_seq=5 tt1=64 time=0.117 ms 
64 bytes from 10.0.0.10: icmp_seq=6 tt1=64 time=0.108 ms 
64 bytes from 10.0.0.10: icmp_seq=7 tt1=64 time=0.148 ms 
64 bytes from 10.0.0.10: icmp_seq=8 tt1=64 time=0.153 ms 
^C--- 10.0.0.10 ping statistics ---
9 packets transmitted, 9 packets received, 0% packet loss 
round-trip min/avg/max/stddev = 0.037/0.112/0.156/0.037 ms 
root@worderess-fb448db97-46rrn:/var/www/html# 
```

After applying the policy, all other connections than the one defined will be dropped

```sh
vagrant@master-node:—$ kubectl exec -it wordpress-fb448db97-42k66 -n wordpress-mysql -- /bin/bash 
root@wordpress-fb448db97-42k6S:/var/www/html# ping 10.0.0.10 
PING 10.0.0.10 (10.0.0.10): 56 data bytes 
92 bytes from 10.0.0.10: Destination Port Unreachable 
92 bytes from 10.0.0.10: Destination Port Unreachable 
92 bytes from 10.0.0.10: Destination Port Unreachable 
92 bytes from 10.0.0.10: Destination Port Unreachable 
92 bytes from 10.0.0.10: Destination Port Unreachable 
92 bytes from 10.0.0.10: Destination Port Unreachable 
^C--- 10.0.0.10 ping statistics ---
6 packets transmitted, 0 packets received, 100% packet loss 
root@wordpress-fb448db97-42k66:/var/www/html# 
root@wordpress-fb448db97-42k6S:/var/www/html# curl 10.0.0.10 
curl: (7) Failed to connect to 10.0.0.10 port 80: Connection refused 
root@wordpress-fb448db97-42k6S:/var/www/html# 
```