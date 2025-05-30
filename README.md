[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://kgen-wallet-persona.streamlit.app/)

# Onchain Wallet Persona Generator

A modern Streamlit dashboard for analyzing Ethereum wallet addresses and generating AI-powered persona profiles. This app combines onchain analytics, behavioral tagging, and advanced AI (HuggingFace Mistral-7B-Instruct-v0.2) to deliver rich, actionable wallet insights for DeFi, NFT, and crypto communities.

---

## Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Visual Walkthrough](#-visual-walkthrough)
- [Setup Instructions](#️-setup-instructions)
- [How to Use the App](#-how-to-use-the-app)
- [AI Persona Generation & Data Pipeline](#-ai-persona-generation--data-pipeline)
- [Example Output](#-example-output)
- [Main Files & Data](#-main-files--data)
- [Tech Stack](#-tech-stack)
- [Credits](#-credits)


---

## 🚦 Try It Live

👉 [Launch the Onchain Wallet Persona Generator on Streamlit Cloud](https://kgen-wallet-persona.streamlit.app/)

---

## 🚀 Project Overview

**Onchain Wallet Persona Generator** is a data science and AI tool for:
- **Analyzing any Ethereum wallet address**
- **Extracting features**: net worth, DeFi/NFT stats, activity, risk, and behavioral tags
- **Visualizing wallet data**: top tokens, portfolio allocation, and more
- **Generating AI-powered persona summaries** using HuggingFace's Mistral-7B model
- **Providing personalized recommendations** for each wallet

Built for hackathons, research, and crypto product teams.

---

## ✨ Key Features

- **Modern Streamlit UI**: Responsive, interactive dashboard
- **Wallet Input**: Analyze any Ethereum address
- **Feature Extraction**: Net worth, DeFi/NFT positions, activity, risk, and behavioral tags
- **Visualizations**:
  - Bar chart: Top tokens by USD value
  - Pie chart: Portfolio allocation (Tokens, DeFi, NFTs)
  - Radar chart: Health, risk, and activity scores
- **AI Persona Generation**: Uses HuggingFace Mistral-7B-Instruct-v0.2 (local or with your token)
- **Markdown Persona Summaries**: Human-readable, actionable profiles
- **Personalized Recommendations**: dApps, strategies, and more
- **Data Pipeline**: Loads from local CSVs in `data/` (or fetches live via Moralis API)
- **Deployable**: Ready for Streamlit Community Cloud

---

## 🖼 Visual Walkthrough

Below are screenshots of the app in action (see the `images/` folder for more):

### Dashboard Home
![Dashboard Home](images/Screenshot%202025-05-30%20223049.png)

### Wallet Analysis & Persona
![Wallet Analysis](images/Screenshot%202025-05-30%20223118.png)

### Visualizations: Top Tokens & Portfolio
![Top Tokens](images/Screenshot%202025-05-30%20223133.png)
![Portfolio Pie](images/Screenshot%202025-05-30%20223139.png)

### Persona Summary & Recommendations
![Persona Summary](images/Screenshot%202025-05-30%20223147.png)
![Recommendations](images/Screenshot%202025-05-30%20223156.png)

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/Thunder25Beast/onchain-wallet-kgen
   cd onchain-wallet-kgen
   ```
2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
   (For AI features: also install `transformers`, `huggingface_hub`, `torch`, `accelerate`)
3. **(Optional) Set up Moralis API key:**
   - Create a `.env` file with `MORALIS_API_KEY=your_key_here` for live wallet data.
4. **Run the app:**
   ```powershell
   streamlit run app.py
   ```

---

## 🕹 How to Use the App

1. **Enter an Ethereum wallet address** in the input box (e.g., `0x...`).
2. **Click "Generate Persona"**.
3. **View extracted features**: net worth, DeFi/NFT stats, risk, and more.
4. **Explore visualizations**: bar charts, pie charts, radar scores.
5. **Read the AI-generated persona summary** and personalized recommendations.
6. **Expand the raw JSON** for full data details.

---

## 🤖 AI Persona Generation & Data Pipeline

- **Data Loading**: By default, loads from local CSVs in `data/` (e.g., `wallet_networth_all_chains.csv`, `token_balances.csv`, etc.).
- **Moralis API**: If enabled and local data is missing, fetches live wallet data (requires API key).
- **Feature Extraction**: `dataLoading.py` computes wallet features, risk, and behavioral tags.
- **AI Persona**: `wallet_persona_ai.py` uses HuggingFace's Mistral-7B-Instruct-v0.2 to generate a markdown persona profile. You can use the included token or supply your own.
- **Visualization**: `app.py` renders all UI, charts, and persona summaries.

---

## 📋 Example Output

```
# Persona Profile: CryptoWolf_0x1234_ab56

## 1. Crypto Identity
This persona is identified as a **whale, DeFi power user**, with a net worth of approximately **$1,200,000.00**. They hold **35** tokens and are involved in **12** unique NFT collections.

## 2. Trading Style
CryptoWolf_0x1234_ab56 is an active trader with frequent transactions and portfolio adjustments, showing consistent engagement in the crypto markets.

## 3. Risk Profile
Their risk profile indicates a **moderate risk appetite, open to some experimental opportunities**, with a risk score of 45 out of 100.

## 4. Blockchain Preferences
Primarily active on the Ethereum blockchain, leveraging its ecosystem for opportunities.

## 5. Personalized Recommendations
Based on their profile, the following recommendations may suit their interests and investment style:
- Explore DeFi yield farming protocols
- Check out exclusive NFT drops on OpenSea
- Diversify portfolio with Layer 2 tokens
```

---

## 🛠 Main Files & Data
- `app.py` — Streamlit dashboard UI
- `dataLoading.py` — Data loading, feature extraction, and Moralis API integration
- `wallet_persona_ai.py` — AI persona generation (HuggingFace/Mistral)
- `data/` — Local CSVs: `wallet_networth_all_chains.csv`, `token_balances.csv`, `defi_positions.csv`, `nft_collections_cleaned.csv`, `wallet_stats.csv`, `wallets.csv`
- `images/` — Screenshots for reference

---

## 🛠 Tech Stack
- Python 3.10+
- Streamlit
- Pandas, Numpy, Plotly
- HuggingFace Transformers (Mistral-7B)
- Moralis API

---

## 👥 Credits
- **Project Lead & Developer:** Team DeFiScore

