#!/bin/sh
NAME_YAML="/demo_prod.yaml"
CONTROL_DEL="delete"
CONTROL_DEP="deploy"
#read PATH_YAML
read TARGET
read IMAGE
read VERSION
export image=$IMAGE
export tag=$VERSION
PATH_YAML=$(dirname $0)$NAME_YAML
if [ "$TARGET" = "$CONTROL_DEL" ]
then
	envsubst '$image:$tag' < $PATH_YAML
	kubectl delete -f -
else
	envsubst '$image:$tag' < $PATH_YAML
	kubectl create -f -
fi
exit 0
