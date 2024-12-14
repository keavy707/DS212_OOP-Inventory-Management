class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_id, name, quantity, price, min_threshold, max_threshold):
        # Check if the item already exists
        for item in self.items:
            if item["id"] == item_id:
                return f"Item '{name}' already existed."
        
        # If item doesn't exist, add a new one
        self.items.append({
            "id": item_id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "min_threshold": min_threshold,
            "max_threshold": max_threshold
        })
        return f"Item '{name}' added successfully!"

    def update_item(self, item_id, quantity, price):
        for item in self.items:
            if item["id"] == item_id:
                item["quantity"] = quantity
                item["price"] = price
                return f"Item with ID {item_id} updated."
        return f"Item with ID {item_id} not found."

    def delete_item(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                self.items.remove(item)
                return f"Item with ID {item_id} deleted."
        return f"Item with ID {item_id} not found."

    def retrieve_items(self, item_id=None, quantity_requested=None):
        if item_id:
            for item in self.items:
                if item["id"] == item_id:
                    if quantity_requested is not None:
                        if item["quantity"] >= quantity_requested:
                            item["quantity"] -= quantity_requested
                            return f"Item '{item['name']}' retrieved. Remaining quantity: {item['quantity']}."
                        else:
                            return f"Not enough quantity of item '{item['name']}' available."
                    else:
                        return f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}."
            return f"Item with ID {item_id} not found."
        else:
            if not self.items:
                return "Inventory is empty."
            return "\n".join(
                [f"ID: {item['id']}, Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, "
                 f"Min Threshold: {item['min_threshold']}, Max Threshold: {item['max_threshold']}" for item in self.items]
            )

    def check_thresholds(self):
        low_stock = []
        over_stock = []
        for item in self.items:
            if item["quantity"] < item["min_threshold"]:
                low_stock.append(item)
            if item["quantity"] > item["max_threshold"]:
                over_stock.append(item)
        return low_stock, over_stock

