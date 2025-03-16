package main

import (
	"bufio"
	"context"
	"fmt"
	"os"
	"strings"
	"time"

	pb "github.com/dknlam/grpc_playground/catalog/catalog_proto"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	conn, err := grpc.NewClient("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		fmt.Printf("did not connect: %v\n", err)
		return
	}
	defer conn.Close()
	client := pb.NewCatalogManagerClient(conn)

	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("Options:")
		fmt.Println("1. Add item")
		fmt.Println("2. Delete item")
		fmt.Println("3. Add multiple items")
		fmt.Println("4. Delete multiple items")
		fmt.Println("5. Get item description")
		fmt.Println("6. Get multiple items descriptions")
		fmt.Println("7. Get items as a stream")
		fmt.Println("8. Get items descriptions interactively")
		fmt.Println("9. List all items")
		fmt.Println("10. Quit")
		fmt.Print("Enter your choice: ")
		choice, _ := reader.ReadString('\n')
		choice = strings.TrimSpace(choice)

		switch choice {
		case "1":
			fmt.Print("Enter item name: ")
			name, _ := reader.ReadString('\n')
			name = strings.TrimSpace(name)
			fmt.Print("Enter item description: ")
			description, _ := reader.ReadString('\n')
			description = strings.TrimSpace(description)
			item := &pb.Item{Name: name, Description: description}
			request := &pb.SetItemRequest{Item: item}
			response, err := client.SetItem(context.Background(), request)
			if err != nil {
				fmt.Printf("Error adding item: %v\n", err)
			} else {
				fmt.Printf("Item added: %v\n", response.Item)
			}

		case "2":
			fmt.Print("Enter item name to delete: ")
			name, _ := reader.ReadString('\n')
			name = strings.TrimSpace(name)
			request := &pb.ItemRequest{Name: name}
			_, err := client.DeleteItem(context.Background(), request)
			if err != nil {
				fmt.Printf("Error deleting item: %v\n", err)
			} else {
				fmt.Printf("Item deleted: %s\n", name)
			}

		case "3":
			var items []*pb.Item
			for {
				fmt.Print("Enter item name (or 'done' to finish): ")
				name, _ := reader.ReadString('\n')
				name = strings.TrimSpace(name)
				if name == "done" {
					break
				}
				fmt.Print("Enter item description: ")
				description, _ := reader.ReadString('\n')
				description = strings.TrimSpace(description)
				items = append(items, &pb.Item{Name: name, Description: description})
			}
			request := &pb.SetItemsRequest{Items: items}
			_, err := client.SetItems(context.Background(), request)
			if err != nil {
				fmt.Printf("Error adding items: %v\n", err)
			} else {
				fmt.Println("Items added successfully.")
			}

		case "4":
			fmt.Print("Enter item names to delete (comma separated): ")
			names, _ := reader.ReadString('\n')
			names = strings.TrimSpace(names)
			request := &pb.ItemsRequest{Names: strings.Split(names, ",")}
			_, err := client.DeleteItems(context.Background(), request)
			if err != nil {
				fmt.Printf("Error deleting items: %v\n", err)
			} else {
				fmt.Println("Items deleted successfully.")
			}

		case "5":
			fmt.Print("Enter item name: ")
			name, _ := reader.ReadString('\n')
			name = strings.TrimSpace(name)
			request := &pb.ItemRequest{Name: name}
			response, err := client.GetItem(context.Background(), request)
			if err != nil {
				fmt.Printf("Error getting item description: %v\n", err)
			} else {
				fmt.Printf("Item description: %s\n", response.Item.Description)
			}

		case "6":
			fmt.Print("Enter item names (comma separated): ")
			names, _ := reader.ReadString('\n')
			names = strings.TrimSpace(names)
			request := &pb.ItemsRequest{Names: strings.Split(names, ",")}
			response, err := client.GetItems(context.Background(), request)
			if err != nil {
				fmt.Printf("Error getting items descriptions: %v\n", err)
			} else {
				for _, item := range response.Items {
					fmt.Printf("Item: %s, Description: %s\n", item.Name, item.Description)
				}
			}

		case "7":
			fmt.Print("Enter item names (comma separated): ")
			names, _ := reader.ReadString('\n')
			names = strings.TrimSpace(names)
			request := &pb.ItemsRequest{Names: strings.Split(names, ",")}
			stream, err := client.GetItemsAsStream(context.Background(), request)
			if err != nil {
				fmt.Printf("Error getting items as a stream: %v\n", err)
			} else {
				for {
					response, err := stream.Recv()
					if err != nil {
						break
					}
					fmt.Printf("Item: %s, Description: %s\n", response.Item.Name, response.Item.Description)
				}
			}

		case "8":
			ctx, cancel := context.WithTimeout(context.Background(), time.Minute*10)
			defer cancel()
			stream, err := client.GetItemsAsStreamInteractive(ctx)
			if err != nil {
				fmt.Printf("Error getting items descriptions interactively: %v\n", err)
				continue
			}

			go func() {
				for {
					response, err := stream.Recv()
					if err != nil {
						fmt.Printf("Error receiving item: %v\n", err)
						break
					}
					fmt.Printf("Item: %s, Description: %s\n", response.Item.Name, response.Item.Description)
				}
			}()

			for {
				fmt.Print("Enter item name (or 'done' to finish): ")
				name, _ := reader.ReadString('\n')
				name = strings.TrimSpace(name)
				if name == "done" {
					break
				}
				if err := stream.Send(&pb.ItemRequest{Name: name}); err != nil {
					fmt.Printf("Error sending item request: %v\n", err)
					break
				}
			}
			stream.CloseSend()

		case "9":
			request := &pb.ItemsRequest{Names: []string{}}
			response, err := client.GetItems(context.Background(), request)
			if err != nil {
				fmt.Printf("Error listing items: %v\n", err)
			} else {
				for _, item := range response.Items {
					fmt.Printf("Item: %s, Description: %s\n", item.Name, item.Description)
				}
			}

		case "10":
			fmt.Println("Quitting...")
			return

		default:
			fmt.Println("Invalid choice. Please try again.")
		}
	}
}
