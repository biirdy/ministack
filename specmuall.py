
spec = {
    'name' : "Mu's template #2",
    'default network name' : "demo-net3",
    'external network name' : "ext-net3",
    'keypair' : "dell4",
    'Networks' : [
        { 'name' : "lan201" , "start": "192.168.1.201", "end": "192.168.1.202", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 201, "physical_network": "vlannet" },
        { 'name' : "lan202" , "start": "192.168.1.202", "end": "192.168.1.203", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 202, "physical_network": "vlannet" },
        { 'name' : "lan203" , "start": "192.168.1.203", "end": "192.168.1.204", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 203, "physical_network": "vlannet" },
        { 'name' : "lan204" , "start": "192.168.1.204", "end": "192.168.1.205", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 204, "physical_network": "vlannet" },
        { 'name' : "lan205" , "start": "192.168.1.205", "end": "192.168.1.206", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 205, "physical_network": "vlannet" },
        { 'name' : "lan206" , "start": "192.168.1.206", "end": "192.168.1.207", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 206, "physical_network": "vlannet" },
        { 'name' : "lan207" , "start": "192.168.1.207", "end": "192.168.1.208", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 207, "physical_network": "vlannet" },
        { 'name' : "lan208" , "start": "192.168.1.208", "end": "192.168.1.209", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 208, "physical_network": "vlannet" },
        { 'name' : "lan209" , "start": "192.168.1.209", "end": "192.168.1.210", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 209, "physical_network": "vlannet" },
        { 'name' : "lan210" , "start": "192.168.1.210", "end": "192.168.1.211", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 210, "physical_network": "vlannet" },
        { 'name' : "lan211" , "start": "192.168.1.211", "end": "192.168.1.212", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 211, "physical_network": "vlannet" },
        { 'name' : "lan212" , "start": "192.168.1.212", "end": "192.168.1.213", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 212, "physical_network": "vlannet" },
        { 'name' : "lan213" , "start": "192.168.1.213", "end": "192.168.1.214", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 213, "physical_network": "vlannet" },
        { 'name' : "lan214" , "start": "192.168.1.214", "end": "192.168.1.215", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 214, "physical_network": "vlannet" },
        { 'name' : "lan215" , "start": "192.168.1.215", "end": "192.168.1.216", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 215, "physical_network": "vlannet" },
        { 'name' : "lan216" , "start": "192.168.1.216", "end": "192.168.1.217", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 216, "physical_network": "vlannet" },
        { 'name' : "lan217" , "start": "192.168.1.217", "end": "192.168.1.218", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 217, "physical_network": "vlannet" },
        { 'name' : "lan218" , "start": "192.168.1.218", "end": "192.168.1.219", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 218, "physical_network": "vlannet" },
        { 'name' : "lan219" , "start": "192.168.1.219", "end": "192.168.1.220", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 219, "physical_network": "vlannet" },
        { 'name' : "lan220" , "start": "192.168.1.220", "end": "192.168.1.221", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 220, "physical_network": "vlannet" },
        { 'name' : "lan221" , "start": "192.168.1.221", "end": "192.168.1.222", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 221, "physical_network": "vlannet" },
        { 'name' : "lan222" , "start": "192.168.1.222", "end": "192.168.1.223", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 222, "physical_network": "vlannet" },
        { 'name' : "lan223" , "start": "192.168.1.223", "end": "192.168.1.224", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 223, "physical_network": "vlannet" },
        { 'name' : "lan224" , "start": "192.168.1.224", "end": "192.168.1.225", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 224, "physical_network": "vlannet" },
        { 'name' : "lan225" , "start": "192.168.1.225", "end": "192.168.1.226", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 225, "physical_network": "vlannet" },
        { 'name' : "lan226" , "start": "192.168.1.226", "end": "192.168.1.227", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 226, "physical_network": "vlannet" },
        { 'name' : "lan227" , "start": "192.168.1.227", "end": "192.168.1.228", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 227, "physical_network": "vlannet" },
        { 'name' : "lan228" , "start": "192.168.1.228", "end": "192.168.1.229", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 228, "physical_network": "vlannet" },
        { 'name' : "lan229" , "start": "192.168.1.229", "end": "192.168.1.230", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 229, "physical_network": "vlannet" },
        { 'name' : "lan230" , "start": "192.168.1.230", "end": "192.168.1.231", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 230, "physical_network": "vlannet" },
        { 'name' : "lan231" , "start": "192.168.1.231", "end": "192.168.1.232", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 231, "physical_network": "vlannet" },
        { 'name' : "lan232" , "start": "192.168.1.232", "end": "192.168.1.233", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 232, "physical_network": "vlannet" },
        { 'name' : "lan233" , "start": "192.168.1.233", "end": "192.168.1.234", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 233, "physical_network": "vlannet" },
        { 'name' : "lan234" , "start": "192.168.1.234", "end": "192.168.1.235", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 234, "physical_network": "vlannet" },
        { 'name' : "lan235" , "start": "192.168.1.235", "end": "192.168.1.236", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 235, "physical_network": "vlannet" },
        { 'name' : "lan236" , "start": "192.168.1.236", "end": "192.168.1.237", "subnet" :" 192.168.1.0/24", "gateway": "192.168.1.1", "vlan": 236, "physical_network": "vlannet" },
    ],
    'Hosts' : [
        { 'name' : "h201" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan201" , "192.168.1.201") ] },
        { 'name' : "h202" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan202" , "192.168.1.202") ] },
        { 'name' : "h203" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan203" , "192.168.1.203") ] },
        { 'name' : "h204" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan204" , "192.168.1.204") ] },
        { 'name' : "h205" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan205" , "192.168.1.205") ] },
        { 'name' : "h206" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan206" , "192.168.1.206") ] },
        { 'name' : "h207" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan207" , "192.168.1.207") ] },
        { 'name' : "h208" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan208" , "192.168.1.208") ] },
        { 'name' : "h209" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan209" , "192.168.1.209") ] },
        { 'name' : "h210" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan210" , "192.168.1.210") ] },
        { 'name' : "h211" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan211" , "192.168.1.211") ] },
        { 'name' : "h212" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan212" , "192.168.1.212") ] },
        { 'name' : "h213" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan213" , "192.168.1.213") ] },
        { 'name' : "h214" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan214" , "192.168.1.214") ] },
        { 'name' : "h215" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan215" , "192.168.1.215") ] },
        { 'name' : "h216" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan216" , "192.168.1.216") ] },
        { 'name' : "h217" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan217" , "192.168.1.217") ] },
        { 'name' : "h218" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan218" , "192.168.1.218") ] },
        { 'name' : "h219" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan219" , "192.168.1.219") ] },
        { 'name' : "h220" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan220" , "192.168.1.220") ] },
        { 'name' : "h221" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan221" , "192.168.1.221") ] },
        { 'name' : "h222" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan222" , "192.168.1.222") ] },
        { 'name' : "h223" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan223" , "192.168.1.223") ] },
        { 'name' : "h224" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan224" , "192.168.1.224") ] },
        { 'name' : "h225" , 'image' : "qtest-template" , 'flavor':"m1.small" , 'net' : [ ("lan225" , "192.168.1.225") ] },
    ]
}
