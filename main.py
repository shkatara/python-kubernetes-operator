#I need to create a configmap each time a new pod is created. 
from kubernetes import client, config, watch

kubeconfig = open("kubeconfig","r")
config.load_kube_config(config_file=kubeconfig)

CoreV1Api = client.CoreV1Api()
podInfo = CoreV1Api.list_namespaced_pod(namespace="default")
for pod in podInfo.items:
    print(pod.spec.volumes)