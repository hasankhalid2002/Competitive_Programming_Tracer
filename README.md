# 📊 CP Analytics & Tracker Tool

A modular CLI tool built in Python to fetch, analyze, and visualize Codeforces user performance and problem-solving metrics using the Codeforces API.

## ✨ Features
- **User Profile Metrics**: Fetch rating, max rating, and global rank.
- **Submission Analysis**: Calculate total submissions, verdict breakdown (OK, WA, TLE), and overall acceptance rate.
- **Skill Mapping**: Visualize top solved problem topics (Tags) and difficulty rating distributions.
- **Robust Architecture**: Built with explicit error handling for missing handles and API timeouts.
- **Clean CLI Interface**: Beautiful, color-coded terminal tables using `rich`.

## 🛠️ Architecture
The project follows clean Object-Oriented Principles:
- `models/`: Data representations (`UserProfile`, `Submission`, `Problem`).
- `core/fetcher.py`: Interacts with Codeforces API and handles exceptions.
- `core/analyzer.py`: Computes statistical metrics and data aggregations.
- `ui/presenter.py`: CLI presentation layer powered by `rich`.

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Competitive_Programming_Tracer.git](https://github.com/YOUR_USERNAME/Competitive_Programming_Tracer.git)
   cd Competitive_Programming_Tracer