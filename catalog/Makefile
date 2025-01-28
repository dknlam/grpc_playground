build_proto_golang:
	protoc --go_out=. --go_opt=paths=source_relative \
		--go-grpc_out=. --go-grpc_opt=paths=source_relative \
		catalog_proto/catalog.proto

build_proto_python:
	python3 -m grpc_tools.protoc \
		-I catalog_proto \
		--python_out=catalog_proto \
		--grpc_python_out=catalog_proto \
		catalog_proto/catalog.proto

build_proto_all: build_proto_golang build_proto_python