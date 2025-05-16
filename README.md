# 🏠 Flatmate Bill Splitter

A Python-based CLI application that helps roommates split shared bills fairly. Inspired by apps like **Splitwise**, this tool calculates each flatmate’s share based on the number of days stayed, generates PDF and Excel reports, and tracks settlements in a ledger.

---

## 🚀 Features

- ✅ Add and manage expense categories via admin menu
- ✅ Dynamic support for multiple flatmates
- ✅ Fair split based on days stayed
- ✅ Multi-category expense input (Rent, Electricity, etc.)
- ✅ Generate PDF report for each billing period
- ✅ Export bill history to Excel
- ✅ Debt settlement suggestion with simplification logic
- ✅ Record settlement payments in a persistent ledger
- ✅ View all past transactions in a tabulated format
- ✅ Insightful statistics: total, average, fairness index, top contributor
- ✅ CLI-driven interactive experience with validations

---

## 📂 Project Structure

```
flatmate_bill/
├── main.py                 # Main entry point with menu
├── admin.py                # Admin interface to manage categories
├── bill.py                 # Bill object with category expenses
├── flatmate.py             # Flatmate model and payment logic
├── reports.py              # PDF report generator
├── settlement.py           # Debt simplification logic
├── ledger.py               # Records settlements and payments
├── storage.py              # Saves billing records to CSV
├── utils.py                # Input validation functions
├── categories.txt          # List of predefined expense categories
├── bill_history.csv        # All past bill records
├── ledger.csv              # Transaction log of settlements
├── files/                  # PDF reports and images (optional)
```

---

## 🔁 Flow of Execution

1. 🏁 User launches `main.py`
2. 🧾 User selects `Generate Bill`
3. ✅ User selects expense categories and enters amounts
4. 👥 User enters flatmates and number of days they stayed
5. 📄 App shows:
   - each flatmate's share by category
   - total bill
   - fairness metrics
   - debt settlement suggestions
6. 📤 PDF report is generated
7. 📒 User can view historical reports and transactions

---

## 💡 Sample Input

```
Billing Period: March 2025

Available Categories:
1. Rent
2. Electricity
3. Internet

Select Category: 1
Amount: 3000
Select Category: 2
Amount: 600
...

Flatmate 1: Alice, 30 days
Flatmate 2: Bob, 15 days
Flatmate 3: Charlie, 15 days
```

---

## ✅ Sample Output

```
Bill Breakdown for March 2025:
- Alice pays Rs. 1800.00 for Rent
- Bob pays Rs. 900.00 for Rent
- Charlie pays Rs. 900.00 for Rent
...

📈 Report Summary:
🧮 Total: Rs. 5400.00
📊 Average: Rs. 1800.00
💸 Highest Contributor: Alice
⚖️ Fairness Index: 60000.00

🤝 Debt Settlement:
- Bob owes ₹900.00 to Alice
- Charlie owes ₹900.00 to Alice
```

📄 PDF opens with summary  
📤 Excel generated if chosen  
🧾 Settlements saved to `ledger.csv`

---

## 📦 How to Run

### 1. Clone the project
```bash
git clone https://github.com/yourname/flatmate-bill-splitter.git
cd flatmate-bill-splitter
```

### 2. Install dependencies
```bash
pip install fpdf tabulate openpyxl
```

### 3. Run the app
```bash
python main.py
```

---

## 🔧 Admin Commands

1. Add/Remove/List categories
2. Stored in `categories.txt`
3. Used when generating bills

---

## 📈 Sample Ledger Output

| Payer   | Receiver | Amount | Note     |
|---------|----------|--------|----------|
| Bob     | Alice    | 900.00 | Rent     |
| Charlie | Alice    | 900.00 | Internet |

---

## 💡 Future Enhancements

- Web interface using Flask
- Login system for flatmates
- Monthly reminders via email
- Visual dashboards with charts
- Mobile-friendly version using React Native or Flutter

---

## 📜 License

MIT License

---

## 🙌 Acknowledgments

Inspired by Splitwise, Tricount, and budget sharing apps. Built to help roommates split expenses transparently.---

## 📊 How Calculation Works

### 1. Bill Collection
- Admin enters the **billing period** and selects **expense categories** with amounts.
- A `Bill` object is created storing all category expenses.

### 2. Flatmate Selection
- Admin selects users (flatmates) and enters their **stay duration** in days.

### 3. Proportional Expense Split
- Total days = sum of all flatmates' days
- For each flatmate:
  ```
  weight = days_in_house / total_days
  share = category_amount × weight
  ```

#### Example:
```
Electricity = Rs. 1500, Groceries = Rs. 1200
Alice: 30 days, Bob: 20 days → total = 50 days

Alice: 60% share → Rs. 900 (Elec) + Rs. 720 (Gro) = Rs. 1620
Bob:   40% share → Rs. 600 (Elec) + Rs. 480 (Gro) = Rs. 1080
```

### 4. Settlement
- Fair share = Total amount ÷ Number of people
- Compare each flatmate's paid amount with fair share
- Debtors and creditors are matched using a greedy algorithm
```
Bob owes ₹270.00 to Alice
```