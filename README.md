# CryptoGuide-Data-Pipeline-and-Market-Predictions


## Overview
This Python application fetches the latest cryptocurrency data from the **CoinGecko** API, identifies the **top 10 cryptocurrencies to sell** and **bottom 10 to buy**, and sends an email with the report **daily at 8 AM**.

## Features
- Fetches real-time cryptocurrency market data.
- Identifies **top 10 cryptocurrencies** with the highest price increase in 24 hours.
- Identifies **bottom 10 cryptocurrencies** with the highest price decrease in 24 hours.
- Sends an automated email with the analysis and a CSV report.
- Schedules the task to run **every day at 8 AM**.

## Technologies Used
- **Python** (for scripting and automation)
- **Requests** (for API calls)
- **Pandas** (for data processing and analysis)
- **smtplib & email** (for sending emails)
- **Schedule** (for task scheduling)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/amanjaiswal09/crypto-alert.git
   ```
2. Navigate to the project folder:
   ```bash
   cd crypto-alert
   ```
3. Install required dependencies:
   ```bash
   pip install pandas requests schedule
   ```

## Usage
Run the script manually:
```bash
python crypto_alert.py
```

Or let the script **automatically run daily at 8 AM** by keeping it running in the background.

## Configuration
- Update the **SMTP settings** (server, email, password) in the `send_mail` function.
- Modify the **receiver email address** in `receiver_mail`.
- Adjust the **task scheduling time** in `schedule.every().day.at('08:00')` if needed.

## How It Works
1. **Fetches Crypto Data**: Calls CoinGecko API and retrieves data for **250+ cryptocurrencies**.
2. **Data Processing**:
   - Filters and cleans the data.
   - Identifies the **top 10 gainers** and **top 10 losers**.
   - Saves the data in a **CSV file**.
3. **Email Notification**:
   - Composes an email with the summary.
   - Attaches the **CSV report**.
   - Sends the email to the configured recipient.
4. **Automated Scheduling**:
   - The task is scheduled to run **every day at 8 AM**.

## Future Enhancements
- Add **Telegram or Slack notifications**.
- Implement **a web dashboard** for visualization.
- Integrate **Machine Learning** for predictive analysis.

## Contact
For any queries, feel free to reach out:
- **GitHub**: [Your GitHub](https://github.com/amanjaiswal09)
- **Email**: jaiswalaman1699@gmail.com
