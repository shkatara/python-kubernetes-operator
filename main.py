#I need to create a configmap each time a new pod is created. 
from kubernetes import client, config, watch

kubeconfig = open("kubeconfig","r")
watch = watch.Watch()
config.load_kube_config(config_file=kubeconfig)
CoreV1Api = client.CoreV1Api()
#podInfo = CoreV1Api.list_namespaced_pod(namespace="default")

#for pod in podInfo.items:
#    print(pod.spec.volumes)

#Capture Events of pod creation in default namespace. 
for event in watch.stream(CoreV1Api.list_pod_for_all_namespaces):
    if event['type'] == "ADDED":
        pod_name = event['object'].metadata.name
        print(f'Pod with name {pod_name} Added')
    if event['type'] == "DELETED":
        pod_name = event['object'].metadata.name
        print(f'Pod with name {pod_name} Deleted')