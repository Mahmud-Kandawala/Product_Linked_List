class Node:
    def __init__(self, nm, pr, st):
        self.name = nm
        self.price = pr
        self.stock = st
        self.ref = None

class Linked_List:
    def __init__(self):
        self.end = None
        self.start = None
        self.count = 0

    def allProds(self):
        itemCount = self.end
        while itemCount:
            diffName = itemCount.name
            diffPrice = itemCount.price
            diffStock = itemCount.stock
            itemCount = itemCount.ref
            print("Name:", diffName, "", 
                  "Price:", diffPrice, "",
                  "Stock:", diffStock)

    def givenPrice(self,certain_price):
        itemCount = self.end
        while itemCount:
            if(itemCount.price > certain_price):
                diffName = itemCount.name
                diffPrice = itemCount.price
                diffStock = itemCount.stock
                itemCount = itemCount.ref
                print("Name:",diffName, "",
                      "Price:",diffPrice, "",
                      "Stock:",diffStock)
            else:
                itemCount=itemCount.ref

    def lowProducts(self):
        itemCount = self.end
        while itemCount:
            if (itemCount.price < 20):
                diffName = itemCount.name
                diffPrice = itemCount.price
                diffStock = itemCount.stock
                itemCount = itemCount.ref
                print("Name:",diffName, "",
                      "Price:",diffPrice, "",
                      "Stock:",diffStock)
            else:
                itemCount = itemCount.ref

    def endItem(self, nm, pr, st):
        node = Node(nm, pr, st)
        if self.start:
            self.start.ref = node
            self.start = node
        else:
            self.end = node
            self.start = node
        self.count += 1

item = Linked_List()
pick = 0

while pick != 5:
    print("\n1. Add product to the list (anywhere)")
    print("2. Print all products in the LinkedList")
    print("3. Print all products above certain price")
    print("4. Print all low-stock products (Less than 20 pounds)")
    print("5. Exit")
    pick = int(input("\nEnter Your Pick? ==> "))
    
    if(pick == 1):
        name=input("Enter Your Name: ")
        price=float(input("Enter Your Price: "))
        stock=float(input("Enter Your Stock: "))
        item.endItem(name,price,stock)
   
    elif(pick == 2):
        item.allProds()

    elif(pick == 3):
        certain_price = float(input("Enter a price to print all items above that amount: "))
        item.givenPrice(certain_price)

    elif(pick == 4):
        item.lowProducts()