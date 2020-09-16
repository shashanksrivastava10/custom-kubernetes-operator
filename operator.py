from kubernetes import client, config, watch
from pprint import pprint
import kubernetes.client
def main():
    configuration = config.load_incluster_config()
    v1 = client.CoreV1Api()
    api_instance = kubernetes.client.AppsV1beta1Api(kubernetes.client.ApiClient(configuration))
    api = client.CustomObjectsApi()
    resource = api.get_namespaced_custom_object(
        group="custom.app.local",
        version="v1",
        name="application",
        namespace="default",
        plural="operations",
    )
    print("---------")
    namespace = "default"
    replicas = int(resource['spec']['replicas'])
    body = {"spec":{"replicas": replicas}}
    services = api_instance.list_namespaced_stateful_set(namespace)
    data = services.items[0].metadata.labels
    name = data['release']
    api_response = api_instance.patch_namespaced_stateful_set(name, namespace, body)
if __name__ == '__main__':
    main()
