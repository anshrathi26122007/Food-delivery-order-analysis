
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_FOLDER = Path(__file__).parent
DATA_FILE = PROJECT_FOLDER / "data" / "orders.csv"
if not DATA_FILE.exists():
    
    DATA_FILE = PROJECT_FOLDER / "orders.csv"


def show_help():
   
    print("""
Available commands:
  help                 Show this command list
  all                  Show all 400 order rows
  revenue              Show total order value
  average order value  Show average order value
  delivery             Show delivery-time statistics
  ratings              Show average customer rating
  city summary         Summarize by city
  area summary         Summarize by delivery area
  cuisine summary      Summarize by cuisine
  restaurant summary   Summarize by restaurant
  payment summary      Summarize by payment method
  status summary       Count delivered, delayed, and cancelled orders
  discounts            Show total discounts and discount usage
  distance             Show delivery-distance statistics
  top order            Show the highest-value order
  city <name>          Show orders in a city (example: city Delhi)
  cuisine <name>       Show orders for a cuisine (example: cuisine Biryani)
  exit                 Quit the program
""")


def handle_command(command, orders):
    command = command.strip().lower()

    if command in {"exit", "quit", "q"}:
        return False
    if command in {"help", "?"}:
        show_help()
    elif command == "all":
        print(orders.to_string(index=False))
    elif command == "revenue":
        print(f"Total order value: {orders['order_value'].sum():,.2f}")
    elif command == "average order value":
        print(f"Average order value: {orders['order_value'].mean():,.2f}")
    elif command == "delivery":
        times = orders["delivery_minutes"].to_numpy()
        fast_count = np.count_nonzero(times < 30)
        print(f"Average delivery time: {np.mean(times):.1f} minutes")
        print(f"Median delivery time: {np.median(times):.1f} minutes")
        print(f"Under 30 minutes: {fast_count} orders ({fast_count / len(orders):.1%})")
    elif command == "ratings":
        print(f"Average customer rating: {orders['customer_rating'].mean():.2f} / 5")
    elif command == "city summary":
        grouped_summary(orders, "city")
    elif command == "area summary":
        grouped_summary(orders, "area")
    elif command == "cuisine summary":
        grouped_summary(orders, "cuisine")
    elif command == "restaurant summary":
        grouped_summary(orders, "restaurant")
    elif command == "payment summary":
        grouped_summary(orders, "payment_method")
    elif command == "status summary":
        print(orders["order_status"].value_counts().to_string())
    elif command == "discounts":
        discounted = np.count_nonzero(orders["discount"].to_numpy() > 0)
        print(f"Total discounts given: {orders['discount'].sum():,.2f}")
        print(f"Orders with a discount: {discounted} / {len(orders)} ({discounted / len(orders):.1%})")
    elif command == "distance":
        distances = orders["distance_km"].to_numpy()
        print(f"Average delivery distance: {np.mean(distances):.1f} km")
        print(f"Longest delivery distance: {np.max(distances):.1f} km")
    elif command == "top order":
        order = orders.loc[orders["order_value"].idxmax()]
        print(f"Order #{int(order['order_id'])} in {order['city']}: {order['order_value']:.2f}")
    elif command.startswith("city "):
        value = command[5:].strip()
        matches = orders[orders["city"].str.lower() == value]
        print(matches.to_string(index=False) if not matches.empty else f"No orders found for city: {value}")
    elif command.startswith("cuisine "):
        value = command[8:].strip()
        matches = orders[orders["cuisine"].str.lower() == value]
        print(matches.to_string(index=False) if not matches.empty else f"No orders found for cuisine: {value}")
    else:
        print("I don't recognize that command. Type 'help' to see the options.")

    return True


def grouped_summary(orders, group_column):
    """Print orders, sales value, discount, and rating by a category."""
    summary = orders.groupby(group_column).agg(
        orders=("order_id", "count"),
        total_order_value=("order_value", "sum"),
        average_order_value=("order_value", "mean"),
        average_discount=("discount", "mean"),
        average_rating=("customer_rating", "mean"),
    ).sort_values("total_order_value", ascending=False)
    print(summary.round(2).to_string())


def main():
    # This reads the expanded CSV containing 400 orders and 17 columns.
    orders = pd.read_csv(DATA_FILE, parse_dates=["order_date"])
    print("FOOD DELIVERY DATA ANALYSIS")
    print(f"Loaded {len(orders)} orders with {len(orders.columns)} columns.")
    print("Type 'help' to choose what data to print.")

    while True:
        try:
            command = input("\nWhat data do you want to print? ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not handle_command(command, orders):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

