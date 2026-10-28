#!/usr/bin/env python3

__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import ipaddress
from netaddr import IPNetwork, IPAddress

def check_ip_address(ipaddr):
    ip = ipaddress.ip_address(ipaddr)
    ip_attributes = []

    if ip.is_private:
        ip_attributes.append("IP Address is Private")
    else:
        ip_attributes.append("IP Address is Public")

    if ip.is_multicast:
        ip_attributes.append("IP Address is Multicast")
    elif ip.is_loopback:
        ip_attributes.append("IP Address is Loopback")
    elif ip.is_unspecified:
        ip_attributes.append("IP Address is Unspecified")
    elif ip.is_link_local:
        ip_attributes.append("IP Address is Link-local")
    else:
        ip_attributes.append("IP Address is Unicast")

    return "\n".join(ip_attributes)

def operate_on_ip_network(ipnet):
    net_attributes = []
    net = IPNetwork(ipnet)

    net_attributes.append(
        f"Network IP Address is {net.network} "
        f"and Network Mask is {net.netmask}"
    )

    net_attributes.append(f"The Broadcast is {net.broadcast}")
    net_attributes.append(f"IP Version is {net.version}")
    net_attributes.append(
        f"Information known about this network is {net.info}"
    )
    net_attributes.append(f"The IPv6 representation is {net.ipv6()}")
    net_attributes.append(f"The Network size is {net.size}")

    net_attributes.append(
        "Generating a list of IP addresses inside the subnet:"
    )

    for ip in net:
        net_attributes.append(f"\t{ip}")

    return "\n".join(net_attributes)


def main():
    try:
        ipaddr = input("Please Enter the IP Address: ")
        print(check_ip_address(ipaddr))

        ipnet = input("\nPlease Enter the IP Network (CIDR i.e 10.10.10.10/24): ")
        print(operate_on_ip_network(ipnet))

    except (ValueError, TypeError) as error:
        print(f"Invalid IP address or network: {error}")


if __name__ == "__main__":
    main()
