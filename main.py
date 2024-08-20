import matplotlib.pyplot as plt

class Drug:
    def __init__(self, name, manufacturer, batch_number):
        self.name = name
        self.manufacturer = manufacturer
        self.batch_number = batch_number
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def __str__(self):
        return f"Drug: {self.name}, Manufacturer: {self.manufacturer}, Batch: {self.batch_number}, Transactions: {len(self.transactions)}"


class Transaction:
    def __init__(self, action, location, timestamp):
        self.action = action
        self.location = location
        self.timestamp = timestamp

    def __str__(self):
        return f"Action: {self.action}, Location: {self.location}, Timestamp: {self.timestamp}"


class SupplyChain:
    def __init__(self):
        self.drugs = {}

    def add_drug(self, drug):
        self.drugs[drug.batch_number] = drug
        print(f"Added: {drug}")

    def record_transaction(self, batch_number, action, location, timestamp):
        if batch_number in self.drugs:
            transaction = Transaction(action, location, timestamp)
            self.drugs[batch_number].add_transaction(transaction)
            print(f"Recorded transaction for {batch_number}: {transaction}")
        else:
            print("Error: Drug not found in the supply chain.")

    def display_drug_info(self, batch_number):
        if batch_number in self.drugs:
            print(self.drugs[batch_number])
            for transaction in self.drugs[batch_number].transactions:
                print(transaction)
        else:
            print("Error: Drug not found.")

    def efficiency_report(self):
        drug_names = []
        transaction_counts = []

        for drug in self.drugs.values():
            drug_names.append(drug.name)
            transaction_counts.append(len(drug.transactions))

        plt.figure(figsize=(10, 6))
        plt.bar(drug_names, transaction_counts, color='blue')
        plt.xlabel('Drugs')
        plt.ylabel('Number of Transactions')
        plt.title('Efficiency Report: Number of Transactions per Drug')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def main():
    supply_chain = SupplyChain()

    while True:
        print("\nOptions:")
        print("1. Add Drug")
        print("2. Record Transaction")
        print("3. Display Drug Info")
        print("4. Show Efficiency Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter drug name: ")
            manufacturer = input("Enter manufacturer: ")
            batch_number = input("Enter batch number: ")
            drug = Drug(name, manufacturer, batch_number)
            supply_chain.add_drug(drug)

        elif choice == '2':
            batch_number = input("Enter batch number: ")
            action = input("Enter action (e.g., Manufactured, Shipped, Delivered): ")
            location = input("Enter location: ")
            timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM): ")
            supply_chain.record_transaction(batch_number, action, location, timestamp)

        elif choice == '3':
            batch_number = input("Enter batch number: ")
            supply_chain.display_drug_info(batch_number)

        elif choice == '4':
            supply_chain.efficiency_report()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
