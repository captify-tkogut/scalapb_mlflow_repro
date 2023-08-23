#! /bin/bash

python -m grpc_tools.protoc -Iprotos/v0.5.0 --python_out=pkg_050 protos/v0.5.0/scalapb.proto
python -m grpc_tools.protoc -Iprotos/v0.8.2 --python_out=pkg_082 protos/v0.8.2/scalapb.proto