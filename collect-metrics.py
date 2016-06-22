import json
import requests
import socket
import time


def collect_metrics():
    return requests.get('http://localhost:9091/metrics').json()


def format_metric(host_name, metric_name, value, timestamp):
    return 'nodejsapp' + '.' + metric_name + '.' + host_name + ' ' + str(value) + ' ' + str(timestamp)


def process_metrics(raw_metrics):
    host_name = socket.gethostname()
    timestamp = int(time.time())
    all_metrics = []
    all_metrics.append(format_metric(host_name, 'request_count', raw_metrics['']['requests']['duration']['count'], timestamp))
    all_metrics.append(format_metric(host_name, 'request_time_min', raw_metrics['']['requests']['duration']['min'], timestamp))
    return all_metrics


def send_metrics(metrics):
    print(metrics)
    # sock = socket.socket()
    # sock.connect((CARBON_SERVER, CARBON_PORT))
    # sock.sendall('\n'.join(metrics) + '\n')


send_metrics(process_metrics(collect_metrics()))
