import os
from typing import List

from grpc_tools import protoc

# Run hell proto
proto_paths: List[str] = [
    "./../protos/hello.proto",
    "./../protos/match_service.proto",
]

existed_proto_names: List[str] = []
proto_gen_path: str = "./codegen_protos"

for _f in os.listdir(proto_gen_path):
    file_path: str = os.path.join(proto_gen_path, _f)
    if os.path.isfile(file_path) and _f.endswith("_pb2.py"):
        existed_proto_names.append(f"{_f[:-7]}.proto")

print(f"Existed Proto name: {existed_proto_names}")

needed_gen_proto_paths: List[str] = [
    _n for _n in proto_paths if os.path.basename(_n) not in existed_proto_names
]
# Force update last proto
if proto_paths[-1] not in needed_gen_proto_paths:
    needed_gen_proto_paths.append(proto_paths[-1])

print(f"Needed proto paths: {needed_gen_proto_paths}")

for proto_path in needed_gen_proto_paths:
    if os.path.isfile(proto_path):
        print(f"Generating code from file: {proto_path}")
        protoc.main(
            (
                "",
                "-I../protos",
                "--python_out=./codegen_protos",
                "--grpc_python_out=./codegen_protos",
                proto_path,
            )
        )
    else:
        print(f"Can't generate code from file: {proto_path}")
