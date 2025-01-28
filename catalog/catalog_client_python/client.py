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

import catalog_pb2
import catalog_pb2_grpc

def main():
    # Set up a connection to the server.
    with grpc.insecure_channel('localhost:50051') as channel:
        c = catalog_pb2_grpc.CatalogManagerStub(channel)

        # Test single item APIs
        print("--- Test single item APIs ---")

        # Get item without item name. Expect an error
        try:
            item_response = c.GetItem(catalog_pb2.ItemRequest())
            print("GetItem:", item_response)
        except grpc.RpcError as err:
            print("failed to get item:", err)

        # Set item 1
        item_response = c.SetItem(catalog_pb2.SetItemRequest(
            item=catalog_pb2.Item(
                name="Item 1",
                description="Item 1 description"
            )
        ))
        print("SetItem:", item_response)

        # Set item 2
        item_response = c.SetItem(catalog_pb2.SetItemRequest(
            item=catalog_pb2.Item(
                name="Item 2",
                description="Item 2 description"
            )
        ))
        print("SetItem:", item_response)

        # Get item again
        item_response = c.GetItem(catalog_pb2.ItemRequest(
            name="Item 1"
        ))
        print("GetItem:", item_response)

        # Update item 1
        item_response = c.SetItem(catalog_pb2.SetItemRequest(
            item=catalog_pb2.Item(
                name="Item 1",
                description="Updated Item 1 description"
            )
        ))
        print("SetItem:", item_response)

        # Get updated item 1
        item_response = c.GetItem(catalog_pb2.ItemRequest(
            name="Item 1"
        ))
        print("GetItem:", item_response)

        print()

        # Test multiple item APIs
        print("--- Test multiple items APIs ---")

        # Get items without item names. Expect an error
        try:
            items_response = c.GetItems(catalog_pb2.ItemsRequest())
            print("GetItems:", items_response)
        except grpc.RpcError as err:
            print("failed to get items:", err)

        # Set items
        items_response = c.SetItems(catalog_pb2.SetItemsRequest(
            items=[
                catalog_pb2.Item(
                    name="Item 3",
                    description="Item 3 description"
                ),
                catalog_pb2.Item(
                    name="Item 4",
                    description="Item 4 description"
                )
            ]
        ))
        print("SetItems:", items_response)

        # Get all items
        items_response = c.GetItems(catalog_pb2.ItemsRequest())
        print("GetItems:", items_response)

        # Get multiple specified items
        items_response = c.GetItems(catalog_pb2.ItemsRequest(
            names=["Item 1", "Item 3", "Item 4"]
        ))
        print("GetItems:", items_response)

        # Delete multiple items
        items_response = c.DeleteItems(catalog_pb2.ItemsRequest(
            names=["Item 1", "Item 4"]
        ))
        print("DeleteItems:", items_response)

        items_response = c.GetItems(catalog_pb2.ItemsRequest())
        print("GetItems:", items_response)

        # Delete all items
        items_response = c.DeleteItems(catalog_pb2.ItemsRequest())
        print("DeleteItems:", items_response)

        items_response = c.GetItems(catalog_pb2.ItemsRequest())
        print("GetItems:", items_response)

        # Test GetItemsAsStream
        # Set items
        items_response = c.SetItems(catalog_pb2.SetItemsRequest(
            items=[
                catalog_pb2.Item(
                    name="Item 5",
                    description="Item 5 description"
                ),
                catalog_pb2.Item(
                    name="Item 6",
                    description="Item 6 description"
                )
            ]
        ))
        print("SetItems:", items_response)

        print()

        # GetItemsAsStream
        print("--- Test get all items as stream with empty request ---")

        items_response = c.GetItemsAsStream(catalog_pb2.ItemsRequest())
        for item in items_response:
            print("GetItemsAsStream:", item)

        print()

        # GetItemsAsStream
        print("--- Test get items as stream with item names ---")
        print("Sending item names: Item 4, Item 5")
        items_response = c.GetItemsAsStream(catalog_pb2.ItemsRequest(
            names=["Item 4", "Item 5"]
        ))
        for item in items_response:
            print("GetItemsAsStream:", item)

        print()

        # GetItemsAsStreamInteractive
        print("--- Test get items as stream interactive ---")

        items_response = c.GetItemsAsStreamInteractive(generate_items_stream_request())
        for item in items_response:
            print("GetItemsAsStreamInteractive recieved response:", item)

        print()

def generate_items_stream_request():
    """
    Generates a stream of ItemRequests with names from "Item 0" to "Item 9".

    Yields:
        catalog_pb2.ItemRequest: An ItemRequest with the name of the item.
    """
    for i in range(10):
        item_name = "Item {}".format(i)
        print("Sending item name:", item_name)
        yield catalog_pb2.ItemRequest(
            name=item_name
        )

if __name__ == '__main__':
    main()