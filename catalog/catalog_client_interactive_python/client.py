import grpc

import sys
import os

# Add the folder to the system path
# Construct the relative path
relative_path = os.path.join('..', 'catalog_proto')
absolute_path = os.path.abspath(relative_path)

# Add the absolute path to sys.path
if absolute_path not in sys.path:
    sys.path.append(absolute_path)

import grpc
import catalog_pb2
import catalog_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = catalog_pb2_grpc.CatalogManagerStub(channel)

    while True:
        print("Options:")
        print("1. Add item")
        print("2. Delete item")
        print("3. Add multiple items")
        print("4. Delete multiple items")
        print("5. Get item description")
        print("6. Get multiple items descriptions")
        print("7. Get items as a stream")
        print("8. Get items descriptions interactively")
        print("9. List all items")
        print("10. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            item = catalog_pb2.Item(name=name, description=description)
            request = catalog_pb2.SetItemRequest(item=item)
            try:
                response = stub.SetItem(request)
                print(f"Item added: {response.item}")
            except grpc.RpcError as e:
                print(f"Error adding item: {e.details()}")

        elif choice == '2':
            name = input("Enter item name to delete: ")
            request = catalog_pb2.ItemRequest(name=name)
            try:
                response = stub.DeleteItem(request)
                print(f"Item deleted: {name}")
            except grpc.RpcError as e:
                print(f"Error deleting item: {e.details()}")

        elif choice == '3':
            items = []
            while True:
                name = input("Enter item name (or 'done' to finish): ")
                if name == 'done':
                    break
                description = input("Enter item description: ")
                items.append(catalog_pb2.Item(name=name, description=description))
            request = catalog_pb2.SetItemsRequest(items=items)
            try:
                response = stub.SetItems(request)
                print("Items added successfully.")
            except grpc.RpcError as e:
                print(f"Error adding items: {e.details()}")

        elif choice == '4':
            names = input("Enter item names to delete (comma separated): ").split(',')
            request = catalog_pb2.ItemsRequest(names=names)
            try:
                response = stub.DeleteItems(request)
                print("Items deleted successfully.")
            except grpc.RpcError as e:
                print(f"Error deleting items: {e.details()}")

        elif choice == '5':
            name = input("Enter item name: ")
            request = catalog_pb2.ItemRequest(name=name)
            try:
                response = stub.GetItem(request)
                print(f"Item description: {response.item.description}")
            except grpc.RpcError as e:
                print(f"Error getting item description: {e.details()}")

        elif choice == '6':
            names = input("Enter item names (comma separated): ").split(',')
            request = catalog_pb2.ItemsRequest(names=names)
            try:
                response = stub.GetItems(request)
                for item in response.items:
                    print(f"Item: {item.name}, Description: {item.description}")
            except grpc.RpcError as e:
                print(f"Error getting items descriptions: {e.details()}")

        elif choice == '7':
            names = input("Enter item names (comma separated): ").split(',')
            request = catalog_pb2.ItemsRequest(names=names)
            try:
                responses = stub.GetItemsAsStream(request)
                for response in responses:
                    print(f"Item: {response.item.name}, Description: {response.item.description}")
            except grpc.RpcError as e:
                print(f"Error getting items as a stream: {e.details()}")

        elif choice == '8':
            def request_iterator():
                while True:
                    name = input("Enter item name (or 'done' to finish): ")
                    if name == 'done':
                        break
                    yield catalog_pb2.ItemRequest(name=name)

            try:
                responses = stub.GetItemsAsStreamInteractive(request_iterator())
                for response in responses:
                    print(f"Item: {response.item.name}, Description: {response.item.description}")
            except grpc.RpcError as e:
                print(f"Error getting items descriptions interactively: {e.details()}")

        elif choice == '9':
            try:
                request = catalog_pb2.ItemsRequest(names=[])
                response = stub.GetItems(request)
                for item in response.items:
                    print(f"Item: {item.name}, Description: {item.description}")
            except grpc.RpcError as e:
                print(f"Error listing items: {e.details()}")

        elif choice == '10':
            print("Quitting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    run()