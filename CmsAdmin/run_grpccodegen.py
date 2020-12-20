from grpc_tools import protoc

protoc.main(
    (
        "",
        "-I../protos",
        "--python_out=./codegen_protos",
        "--grpc_python_out=./codegen_protos",
        "./../protos/hello.proto",
    )
)
