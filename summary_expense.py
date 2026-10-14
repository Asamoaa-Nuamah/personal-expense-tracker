from database import get_category_summary


def show_summary():
    """Print a table of spending per category (amount, date of latest expense,
    share of total spending), followed by the total. No input is needed."""
    rows = get_category_summary()  # (category, total, latest_date), biggest total first

    if not rows:
        print("\nNo expenses found. Add an expense to see a summary.")
        return

    grand_total = sum(total for _, total, _ in rows)

    # Turn every value into text first, so column widths can be measured
    table = []
    for name, total, latest_date in rows:
        # Guard against dividing by zero if every amount is 0
        percent = (total / grand_total * 100) if grand_total else 0
        table.append((name, f"{total:,.2f}", latest_date, f"{percent:.1f}%"))

    headers = ("Category", "Amount (GHC)", "Date", "Percentage")

    # Each column is as wide as its longest value (or its header)
    widths = [
        max(len(header), *(len(row[i]) for row in table))
        for i, header in enumerate(headers)
    ]

    def format_row(cells):
        category, amount, latest_date, percent = cells
        return (
            f"{category:<{widths[0]}} | {amount:>{widths[1]}} | "
            f"{latest_date:<{widths[2]}} | {percent:>{widths[3]}}"
        )

    divider = "-+-".join("-" * width for width in widths)

    print("\n--- Spending summary ---")
    print(format_row(headers))
    print(divider)
    for row in table:
        print(format_row(row))
    print(divider)
    print(f"Total expense: GHC {grand_total:,.2f}")