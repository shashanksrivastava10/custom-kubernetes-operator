import kubernetes as k8s
import os
k8s.config.load_incluster_config()
api = k8s.client.CustomObjectsApi()
group = "custom.app.local"
plural = "operations"
version = "v1"
items = api.list_cluster_custom_object(group=group, plural=plural, version=version)
ver = items["metadata"]["resourceVersion"]
print(items["metadata"])
kwargs = {}
kwargs["resource_version"] = ver
kwargs["watch"] = True
for event in k8s.watch.Watch().stream(api.list_cluster_custom_object, group, version, plural, **kwargs):
    os.system('python3 operator.py')
    f = open("logs.txt", "a")
    f.write("testing")
    f.close()
