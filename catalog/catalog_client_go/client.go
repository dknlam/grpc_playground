package main

import (
	"context"
	"errors"
	"fmt"
	"io"

	"log"
	"time"

	pb "github.com/dknlam/grpc_playground/catalog/catalog_proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

// main is the entry point of the program.
//
// It sets up a connection to the server, performs various tests on the catalog
// manager API, and logs the results.
//
// No parameters.
// No return types.
func main() {

	// Set up a connection to the server.
	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("failed to connect to Golang Catalog Server: %v", err)
	}
	defer conn.Close()
	c := pb.NewCatalogManagerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	// Test single item APIs
	log.Printf("--- Test single item APIs ---")

	// Get item wihout item name. Expect an error
	itemResponse, err := c.GetItem(ctx, &pb.ItemRequest{})
	if err != nil {
		log.Printf("failed to get item: %v", err)
	} else {
		log.Printf("GetItem: %v", itemResponse)
	}

	// Set item 1
	itemResponse, err = c.SetItem(ctx, &pb.SetItemRequest{
		Item: &pb.Item{
			Name: "Item 1",
			Description: "Item 1 description",
		},
	})

	if err != nil {
		log.Printf("failed to set item: %v", err)
	} else {
		log.Printf("SetItem: %v", itemResponse)
	}

	// Set item 2
	itemResponse, err = c.SetItem(ctx, &pb.SetItemRequest{
		Item: &pb.Item{
			Name: "Item 2",
			Description: "Item 2 description",
		},
	})

	if err != nil {
		log.Printf("failed to set item: %v", err)
	} else {
		log.Printf("SetItem: %v", itemResponse)
	}

	// Get item again
	itemResponse, err = c.GetItem(ctx, &pb.ItemRequest{
		Name: "Item 1",
	})

	if err != nil {
		log.Printf("failed to get item: %v", err)
	} else {
		log.Printf("GetItem: %v", itemResponse)
	}

	// Update item 1
	itemResponse, err = c.SetItem(ctx, &pb.SetItemRequest{
		Item: &pb.Item{
			Name: "Item 1",
			Description: "Updated Item 1 description",
		},
	})

	if err != nil {
		log.Printf("failed to set item: %v", err)
	} else {
		log.Printf("SetItem: %v", itemResponse)
	}

	// Get updated item 1
	itemResponse, err = c.GetItem(ctx, &pb.ItemRequest{
		Name: "Item 1",
	})

	if err != nil {
		log.Printf("failed to get item: %v", err)
	} else {
		log.Printf("GetItem: %v", itemResponse)
	}

	log.Println()

	// Test multiple item APIs
	log.Printf("--- Test multiple items APIs ---")

	// Get items without item names. Expect an error
	itemsResponse, err := c.GetItems(ctx, &pb.ItemsRequest{})
	if err != nil {
		log.Printf("failed to get items: %v", err)
	}

	log.Printf("GetItems: %v", itemsResponse)

	// Set items
	itemsResponse, err = c.SetItems(ctx, &pb.SetItemsRequest{
		Items: []*pb.Item{
			{
				Name: "Item 3",
				Description: "Item 3 description",
			},
			{
				Name: "Item 4",
				Description: "Item 4 description",
			},
		},
	})

	if err != nil {
		log.Printf("failed to set items: %v", err)
	}

	log.Printf("SetItems: %v", itemsResponse)

	// Get all items
	log.Printf("Get all items")

	itemsResponse, err = c.GetItems(ctx, &pb.ItemsRequest{
		Names: nil,
	})

	if err != nil {
		log.Printf("failed to get items: %v", err)
	}

	log.Printf("GetItems: %v", itemsResponse)

	// Get multiple specified items
	log.Printf("Get multiple specified items")

	itemsResponse, err = c.GetItems(ctx, &pb.ItemsRequest{
		Names: []string{"Item 1", "Item 3", "Item 4"},
	})

	if err != nil {
		log.Printf("failed to get items: %v", err)
	}

	log.Printf("GetItems: %v", itemsResponse)

	// Delete multiple items
	itemsResponse, err = c.DeleteItems(ctx, &pb.ItemsRequest{
		Names: []string{"Item 1", "Item 4"},
	})

	if err != nil {
		log.Printf("failed to delete items: %v", err)
	}

	log.Printf("DeleteItems: %v", itemsResponse)

	itemsResponse, err = c.GetItems(ctx, &pb.ItemsRequest{
		Names: nil,
	})

	if err != nil {
		log.Printf("failed to get items: %v", err)
	}

	log.Printf("GetItems: %v", itemsResponse)

	// Delete all items
	itemsResponse, err = c.DeleteItems(ctx, &pb.ItemsRequest{
		Names: nil,
	})

	if err != nil {
		log.Printf("failed to delete items: %v", err)
	}

	log.Printf("DeleteItems: %v", itemsResponse)

	itemsResponse, err = c.GetItems(ctx, &pb.ItemsRequest{
		Names: nil,
	})

	if err != nil {
		log.Printf("failed to get items: %v", err)
	}

	log.Printf("GetItems: %v", itemsResponse)

	// Test GetItemsAsStream
	// Set items
	itemsResponse, err = c.SetItems(ctx, &pb.SetItemsRequest{
		Items: []*pb.Item{
			{
				Name: "Item 5",
				Description: "Item 5 description",
			},
			{
				Name: "Item 6",
				Description: "Item 6 description",
			},
		},
	})

	if err != nil {
		log.Printf("failed to set items: %v", err)
	}

	log.Printf("SetItems: %v", itemsResponse)

	log.Println()

	// GetItemsAsStream
	log.Printf("--- Test get all items as stream with empty request ---")

	stream, err := c.GetItemsAsStream(ctx, &pb.ItemsRequest{
		Names: nil,
	})

	if err != nil {
		log.Printf("failed to get items as stream: %v", err)
	}

	for {
		item, err := stream.Recv()
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
		}
		log.Printf("GetItemsAsStream: %v", item)
	}

	log.Println()

	log.Printf("--- Test all items as stream with item names ---")
	log.Printf("Sending item names: Item 4, Item 5")
	stream, err = c.GetItemsAsStream(ctx, &pb.ItemsRequest{
		Names: []string{"Item 4", "Item 5"},
	})

	if err != nil {
		log.Printf("failed to get items as stream: %v", err)
	}

	for {
		item, err := stream.Recv()
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}
		}
		log.Printf("GetItemsAsStream: %v", item)
	}

	log.Println()

	// GetItemsAsStreamInteractive
	log.Printf("--- Test get items as stream interactive ---")
	stream, err = c.GetItemsAsStreamInteractive(context.Background())

	if err != nil {
		log.Printf("failed to open stream to get items: %v", err)
	}

	// Start a goroutine to receive items
	go func() {
		for {
			item, err := stream.Recv()
			if err != nil {
				if errors.Is(err, io.EOF) {
					break
				}
				log.Printf("failed to receive item: %v", err)
				return
			}

			log.Printf("GetItemsAsStreamInteractive: %v", item)
		}
	}()

	var itemName string
	for i := 0; i < 10; i++ {
		itemName = fmt.Sprintf("Item %d", i)
		log.Println("Sending item name:", itemName)
		err = stream.SendMsg(&pb.ItemRequest{Name: itemName})
		if err != nil {
			log.Printf("failed to send item: %v", err)
		}
	}

	err = stream.CloseSend()
	if err != nil {
		log.Printf("failed to close send: %v", err)
	}

	// Alternative way to receive items
	// for {
	// 	item, err := stream.Recv()
	// 	if err != nil {
	// 		if errors.Is(err, io.EOF) {
	// 			break
	// 		}
	// 	}
	// 	log.Printf("GetItemsAsStreamInteractive: %v", item)
	// }

	// Wait for 2 seconds to receive all items
	time.Sleep(2 * time.Second)

	log.Println()
}