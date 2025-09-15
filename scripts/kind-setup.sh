#!/bin/bash
kind create cluster --name devops-test --config <<EOF
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
containerdConfigPatches:
- |-
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localhost:5000"]
    endpoint = ["http://registry.devops-test.svc.cluster.local:5000"]
EOF
