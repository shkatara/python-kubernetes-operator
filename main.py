#I need to create a configmap each time a new pod is created. 
from kubernetes import client, config, watch

kubeconfig = open("kubeconfig","r")
watch = watch.Watch()
config.load_kube_config(config_file=kubeconfig)
CoreV1Api = client.CoreV1Api()
podInfo = CoreV1Api.list_namespaced_pod(namespace="default")
#print(type([podInfo]))
#for pod in podInfo.items:
#    print(pod)

def createConfigmap(pod_name: str):
    cmap = client.V1ConfigMap()
    cmap.data = {}
    cmap.metadata = client.V1ObjectMeta(name=f'pod-{pod_name}')
    cmap.data["Pod_Name"] = pod_name
    CoreV1Api.create_namespaced_config_map(namespace="default", body=cmap)

#Capture Events of pod creation in default namespace. 
for event in watch.stream(func=CoreV1Api.list_namespaced_pod,namespace="default"):
    if event['type'] == "ADDED":
        pod_name = event['object'].metadata.name
        print(f'Pod with name {pod_name} Added')
        createConfigmap(pod_name)
    if event['type'] == "DELETED":
        pod_name = event['object'].metadata.name
        print(f'Pod with name {pod_name} Deleted')