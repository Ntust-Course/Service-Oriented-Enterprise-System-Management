# Deployment

## Steps

Create name space

```shell
kubectl create -f ./namespace.yml
```

Create service

```shell
kubectl create -f ./service.yml
```

Create deployment

```shell
kubectl create -f ./deployment.yml
```

## Observe

```shell
kubectl get <kind>
```

Example

```shell
 $ kubectl get namespace
NAME               STATUS   AGE
default            Active   21m
docker             Active   20m
kube-node-lease    Active   21m
kube-public        Active   21m
kube-system        Active   21m
soa-registry   Active   7m52s
```

## Check status

```shell
kubectl get deployment -n soa
```

```shell
kubectl get -n soa
```
