import requests
import json
from authenticate import login

def get_tunnel_statistics():
    session = login()

    baseurl = "https://sandboxsdwan.cisco.com:8443"
   #baseurl = "https://10.50.221.182:8443"

    params = {
        "deviceId": "4.4.4.60"
    }
    tunnel_endpoint = "/dataservice/device/tunnel/statistics"

    url = f"{baseurl}{tunnel_endpoint}"

    response_tunnel = session.get(url, params = params, verify=False)

    statistics = response_tunnel.json()['data']

    for statistic in statistics:
        print(f"{statistic['tunnel-protocol']}: from {statistic['source-ip']}:{statistic['source-port']} to {statistic['dest-ip']}:{statistic['dest-port']}")
        print(f"  => Rx: {statistic['rx_pkts']} / Tx: {statistic['tx_pkts']}")

if __name__ == "__main__":
   response = get_tunnel_statistics()
