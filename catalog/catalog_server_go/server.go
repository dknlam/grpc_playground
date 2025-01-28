package main

import (
	"context"
	"errors"
	"io"
	"log"
	"net"

	pb "github.com/dknlam/grpc_playground/catalog/catalog_proto"
	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedCatalogManagerServer
}

// Declare the map at the package level
var items = make(map[string]*pb.Item)

// TODO:
// 1. Implement APIs for multiple items
// 2. Implement APIs for Streaming items
// 3. Use Redis for storing items
// 4. Use MongoDB for storing items

// APIs for single item
func (s *server) GetItem(ctx context.Context, in *pb.ItemRequest) (*pb.ItemResponse, error) {
	// Check if ItemRequest is valid
	if in.Name == "" {
		// Return an error
		return nil, errors.New("invalid ItemRequest")
	}

	// Find the item from the map
	item, found := items[in.Name]
	if found {
		return &pb.ItemResponse{Item: item}, nil
	} else {
		// Return an error
		return nil, errors.New("item not found")
	}
}

func (s *server) SetItem(ctx context.Context, in *pb.SetItemRequest) (*pb.ItemResponse, error) {
	// Check if ItemRequest is valid
	if in.Item == nil || in.Item.Name == "" {
		// Return an error
		return nil, errors.New("invalid ItemRequest")
	}

	// Save or replace Item in a map
	items[in.Item.Name] = in.Item

	// Return the saved item
	return &pb.ItemResponse{Item: in.Item}, nil
}

func (s *server) DeleteItem(ctx context.Context, in *pb.ItemRequest) (*pb.ItemResponse, error) {
	// Check if ItemRequest is valid
	if in.Name == "" {
		return nil, errors.New("invalid ItemRequest")
	}

	// Check if the item exists
	item, found := items[in.Name]
	if found {
		// Delete the item from the map
		delete(items, in.Name)
	}

	// Return the deleted item
	return &pb.ItemResponse{Item: item}, nil
}

// APIs for multiple items
func (s *server) GetItems(ctx context.Context, in *pb.ItemsRequest) (*pb.ItemsResponse, error) {
	foundItems := make([]*pb.Item, 0)
	if len(in.Names) == 0 {
		// Return all items
		for _, item := range items {
			foundItems = append(foundItems, item)
		}
	} else {
		// Find the items from the map
		for _, name := range in.Names {
			item, found := items[name]
			if found {
				// Add the item to the list
				foundItems = append(foundItems, item)
			}
		}
    }

	return &pb.ItemsResponse{Items: foundItems}, nil
}

func (s *server) SetItems(ctx context.Context, in *pb.SetItemsRequest) (*pb.ItemsResponse, error) {
	// Check if SetItemsRequest is valid
	if len(in.Items) == 0 {
		// Return an error
		return nil, errors.New("invalid SetItemsRequest")
	}

	// Save or replace Items in a map
	processedItems := make([]*pb.Item, 0)
	for _, item := range in.Items {
		if item == nil || item.Name == "" {
			// Return an error
			return nil, errors.New("invalid Item")
		}
		items[item.Name] = item
		processedItems = append(processedItems, item)
	}

	return &pb.ItemsResponse{Items: processedItems}, nil
}

func (s *server) DeleteItems(ctx context.Context, in *pb.ItemsRequest) (*pb.ItemsResponse, error) {
	deletedItems := make([]*pb.Item, 0)
	if len(in.Names) == 0 {
		// delete all items
		for _, item := range items {
			delete(items, item.Name)
			deletedItems = append(deletedItems, item)
		}
	} else {
		// Check if the item exists
		for _, name := range in.Names {
			item, found := items[name]
			if found {
				// Delete the item from the map
				delete(items, name)
				deletedItems = append(deletedItems, item)
			}
		}
    }

	return &pb.ItemsResponse{Items: deletedItems}, nil
}

func (s *server) GetItemsAsStream(in *pb.ItemsRequest, srv grpc.ServerStreamingServer[pb.ItemResponse]) error {
	if len(in.Names) == 0 {
		// Return all items
		for _, item := range items {
			srv.Send(&pb.ItemResponse{Item: item})
		}
	} else {
		// Find the items from the map
		for _, name := range in.Names {
			item, found := items[name]
			if found {
				srv.Send(&pb.ItemResponse{Item: item})
			}
		}
	}

	return nil
}

func (s *server) GetItemsAsStreamInteractive(srv grpc.BidiStreamingServer[pb.ItemRequest, pb.ItemResponse]) error {
	for {
		in, err := srv.Recv()
		if err != nil {
			if errors.Is(err, io.EOF) {
				return nil
			}
			return err
		}
		item, found := items[in.Name]
		if found {
			srv.Send(&pb.ItemResponse{Item: item})
		}
	}
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterCatalogManagerServer(grpcServer, &server{})

	log.Println("Golang Catalog Server listening on :50051")

	if err := grpcServer.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}