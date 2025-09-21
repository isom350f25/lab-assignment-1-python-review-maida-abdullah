def main():
 # 1 Create 2 lists, one to store item names and the other to store its price

 # Lists to store item names 
 item_names = []
 # Lists to storeprices 
 item_prices = []


 # 2 Stop the program when the user hits enter without an item name
 while running:
    item = input("Enter item name: ").strip()
    
    # If user hits Enter without typing a name, stop input
    if item == "":
        raise ValueError("Item cannot be empty, please enter name")
      
    else: 
    # 3 The price should be a float between 0 and 200
     while True:
        try:
            price = float(input(f"Enter price for '{item}' (0-200): "))
            
            # Check if price is within the valid range
            if 0 <= price <= 200:
                item_names.append(item)
                item_prices.append(price)
                break
  
           # 4 The user should be alerted if an error occured when entering the price wrong
            else:
                print("Price must be between 0 and 200. Try again.")
        
        
        except ValueError as e: 
            print e
    
    # Store the valid item name and price
    
# After input, check if any items were entered
if len(item_names) == 0:
    print("No items entered.")
else:
    # Count total items
    count = len(item_names)
    
    # Calculate average price
    avg_price = sum(item_prices) / count
    
    # Find highest and lowest prices
    max_price = max(item_prices)
    min_price = min(item_prices)
    
    # Get the index of highest and lowest price to find corresponding items
    max_index = item_prices.index(max_price)
    min_index = item_prices.index(min_price)

    # Display results

    # 5 Count number of items
    print(f"\nNumber of items: {count}")
  
    # 6 Calculate Average price (2 decimals)
    print(f"Average price: {avg_price:.2f}")

    # 7 Show highest price and lowest price items

    print(f"Highest price item: '{item_names[max_index]}' at {max_price}")
    print(f"Lowest price item: '{item_names[min_index]}' at {min_price}")

main()


