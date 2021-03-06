
spec = {
    'name' : "ODL demo",
    'external network name' : "exnet3",
    'keypair' : "X220",
    'controller' : "r720",
    'dns' : "10.30.65.200",
    'credentials' : { 'user' : "nic", 'password' : "nic", 'project' : "nic" },
    # 'credentials' : { 'user' : "admin", 'password' : "admin", 'project' : "admin" },
    # NOTE: network start/end range -
    #       a) must not include the gateway IP
    #       b) when assigning host IPs remember taht a DHCP server will be allocated from the range as well as the hosts
    #          Probably on the first or second available IP in the range....
    'Networks' : [
        { 'name' : "odldemo" , "start": "192.168.50.2", "end": "192.168.50.254", "subnet" :" 192.168.50.0/24", "gateway": "192.168.50.1" },
        { 'name' : "odldemo2" , "start": "192.168.111.2", "end": "192.168.111.254", "subnet" :" 192.168.111.0/24", "gateway": "192.168.111.1" },
        { 'name' : "odldemo3" , "start": "172.16.0.2", "end": "172.16.0.254", "subnet" :" 172.16.0.0/24", "gateway": "172.16.0.1" },
    ],
    # Hint: list explicity required external IPs first to avoid them being claimed by hosts that don't care...
    'Hosts' : [
        { 'name' : "devstack-control" , 'image' : "trusty64" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.20", "devstack-control"), ("odldemo2" , "192.168.111.10"), ("odldemo3" , "172.16.0.10") ] },
        { 'name' : "devstack-compute-1" , 'image' : "trusty64" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.21","devstack-compute-1"), ("odldemo2" , "192.168.111.11"), ("odldemo3" , "172.16.0.11") ] },
        # { 'name' : "devstack-compute-2" , 'image' : "trusty64" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.22") ] },
        # { 'name' : "devstack-compute-3" , 'image' : "trusty64" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.23") ] },
        { 'name' : "kilo-controller" , 'image' : "Centos7" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.60", "kilo-controller"), ("odldemo2" , "192.168.111.50"), ("odldemo3" , "172.16.0.50") ] }, 
        { 'name' : "kilo-compute-1" , 'image' : "Centos7" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.61", "kilo-compute-1"), ("odldemo2" , "192.168.111.51"), ("odldemo3" , "172.16.0.51") ] },
        { 'name' : "kilo-compute-2" , 'image' : "Centos7" , 'flavor':"m1.xlarge" , 'net' : [ ("odldemo" , "192.168.50.62", "kilo-compute-2"), ("odldemo2" , "192.168.111.52"), ("odldemo3" , "172.16.0.52") ] },
    ]
}
