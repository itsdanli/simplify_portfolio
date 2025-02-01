# Optimal Portfolio Construction Using Simplify ETFs

## **Project Overview**
This project aims to build an **optimal investment portfolio** exclusively using Simplify ETFs. The portfolio will be designed to balance risk, return, and diversification by leveraging the **unique structural advantages** of Simplify’s ETF offerings. The process will involve:

- **Researching & Analyzing** each Simplify ETF, including investment strategies, risk exposures, and sector allocations.
- **Optimizing Portfolio Construction** based on asset allocation principles, risk mitigation techniques, and return maximization.
- **Developing Allocation Models** that incorporate **equities, fixed income, alternative assets, and volatility strategies**.
- **Evaluating Performance & Adjustments** based on market conditions and investment objectives.

---

## **Simplify ETF Summary**

| **ETF Ticker** | **ETF Name**                                      | **Investment Focus**                   | **Expense Ratio** |
|--------------|------------------------------------------------|--------------------------------|---------------|
| WUSA        | Wolfe US Equity 150/50 ETF                    | Leveraged Large-Cap Equity     | 0.75%         |
| HARD        | Commodities Strategy No K-1 ETF               | Broad Commodities Exposure     | 0.50%         |
| SPYC        | US Equity Plus Convexity ETF                  | S&P 500 with Convexity Overlay | 0.53%         |
| SURI        | Propel Opportunities ETF                      | Thematic Growth & Innovation  | 0.95%         |
| SPQ         | US Equity Plus QIS ETF                        | Systematic Equity Strategies   | 0.51%         |
| CTA         | Managed Futures Strategy ETF                  | Trend Following & Futures      | 0.75%         |
| QIS         | Multi-QIS Alternative ETF                     | Quantitative Strategies       | 0.69%         |
| NXTV        | Next Intangible Value Index ETF               | Intangible Asset-Focused Stocks | 0.59%         |
| CRDT        | Opportunistic Income ETF                      | Fixed Income & Credit Risk     | 0.50%         |
| NXTI        | Next Intangible Core Index ETF                | Core Intangible Growth        | 0.49%         |
| PINK        | Health Care ETF                               | U.S. Health Care Sector       | 0.50%         |
| MTBA        | MBS ETF                                       | Mortgage-Backed Securities    | 0.39%         |
| IOPP        | Tara India Opportunities ETF                  | India-Focused Equities        | 0.95%         |
| SPBC        | US Equity Plus Bitcoin Strategy ETF           | S&P 500 + Bitcoin Exposure    | 0.64%         |
| AGGH        | Aggregate Bond ETF                            | Broad Fixed Income Exposure   | 0.29%         |
| TUA         | Short-Term Treasury Futures Strategy ETF      | Short-Term U.S. Treasuries    | 0.25%         |
| TYA         | Intermediate-Term Treasury Futures ETF        | Mid-Term U.S. Treasuries      | 0.25%         |
| NMB         | National Muni Bond ETF                        | Tax-Exempt Municipal Bonds    | 0.25%         |
| MAXI        | Bitcoin Strategy Plus Income ETF              | Bitcoin + Income Strategies   | 0.95%         |
| CDX         | High Yield Plus Credit Hedge ETF              | High-Yield Bonds with Hedges  | 0.50%         |
| EQLS        | Market Neutral Equity Long/Short ETF          | Equity Long/Short Strategies  | 0.69%         |
| CAS         | China Shares Plus Income ETF                  | Chinese Equities with Income  | 0.59%         |
| HIGH        | Enhanced Income ETF                           | High-Yield Income Strategies  | 0.50%         |
| FIG         | Macro Strategy ETF                            | Global Macro & Hedging        | 0.75%         |
| SCY         | US Small Cap Plus Income ETF                  | Small Cap Stocks + Income     | 0.50%         |
| HEQT        | Hedged Equity ETF                             | S&P 500 with Downside Protection | 0.53%         |
| YGLD        | Gold Strategy Plus Income ETF                 | Gold Exposure + Income        | 0.50%         |
| TESL        | Volt TSLA Revolution ETF                      | Tesla-Focused Disruptive Growth | 1.20%        |
| BUCK        | Treasury Option Income ETF                    | Treasury Bonds + Options Income | 0.50%        |
| SPUC        | US Equity Plus Upside Convexity ETF           | S&P 500 with Upside Convexity | 0.53%         |
| PFIX        | Interest Rate Hedge ETF                       | Interest Rate Risk Hedging    | 0.50%         |
| SPD         | US Equity Plus Downside Convexity ETF         | S&P 500 with Downside Convexity | 0.53%        |
| SVOL        | Volatility Premium ETF                        | Short Volatility Exposure     | 0.50%         |
| RFIX        | Downside Interest Rate Hedge ETF              | Rate-Hedging Strategies       | 0.50%         |
| GAEM        | Gamma Emerging Market Bond ETF                | Emerging Market Bonds         | 0.76%         |

---
## **Traditional Portfolio Constructions**
Before constructing a portfolio using **Simplify ETFs**, we will analyze and compare traditional portfolio models. These models serve as benchmarks and starting points for portfolio design:

1. **60/40 Portfolio (Stocks/Bonds)**
   - **Overview**: A classic balanced portfolio with 60% equities and 40% fixed income.
   - **Pros**: Moderate risk, historically stable returns, reduces volatility.
   - **Cons**: Limited adaptability, potential underperformance in low-yield environments.

2. **Risk Parity Portfolio**
   - **Overview**: Allocates capital based on risk contribution rather than percentage weighting.
   - **Pros**: Diversifies across asset classes, lowers volatility.
   - **Cons**: Complex implementation, heavy reliance on leverage.

3. **All-Weather Portfolio (Ray Dalio)**
   - **Overview**: Designed to perform well across different economic cycles.
   - **Allocation**:
     - 30% Stocks
     - 40% Long-Term Bonds
     - 15% Intermediate Bonds
     - 7.5% Gold
     - 7.5% Commodities
   - **Pros**: Stability across market conditions, low drawdowns.
   - **Cons**: Lower upside potential, heavy bond allocation.

4. **Permanent Portfolio**
   - **Overview**: A simple, equal-weighted allocation across major asset classes.
   - **Allocation**:
     - 25% Stocks
     - 25% Bonds
     - 25% Gold
     - 25% Cash
   - **Pros**: Designed for resilience, steady returns.
   - **Cons**: Can underperform during economic booms.

5. **Endowment Model (Yale Model)**
   - **Overview**: Inspired by institutional investing with a focus on alternatives.
   - **Allocation**:
     - 30% Equities
     - 20% Bonds
     - 20% Private Equity
     - 20% Real Assets
     - 10% Hedge Funds
   - **Pros**: Long-term growth potential, diversified.
   - **Cons**: Illiquid investments, high complexity.

6. **Barbell Strategy**
   - **Overview**: Invests heavily in both high-risk and ultra-low-risk assets.
   - **Pros**: Mitigates downside risk while preserving upside.
   - **Cons**: Can be volatile, requires active management.
___

## **Next Steps**
- **Portfolio Optimization**: Identify risk-return tradeoffs and weightings for an optimal allocation.
- **Backtesting & Analysis**: Evaluate historical performance and stress-test different allocation models.
- **Final Portfolio Construction**: Develop an efficient and diversified portfolio solely using Simplify ETFs.

---

