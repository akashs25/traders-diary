# Trader Diary - Gann 7x7 Dynamic Form Project Documentation

## Project Overview
This project implements a dynamic trader diary and order management system with a focus on Gann 7x7 square calculations for trading analysis. The system is built as a single-page HTML/JavaScript application, designed for manual and semi-automated trading workflows.

### Key Features
- **Script Input & Live Data**: Enter a script name (e.g., HDFC) and fetch mock live data (LTP, VWAP, RSI, MACD, ADX, Time).
- **Trade Entry/Exit/SL/Time Input**: UI for entering multiple entries, exits, stop losses, and times for each.
- **Gann 7x7 Square Table**: Generates a 7x7 Gann square using Square Root Theory, with spiral fill and correct value calculation.
- **Upward/Downward Toggle**: Switch between upward and downward Gann tables.
- **Visual Highlighting**: Robust highlighting for center, stop-loss, targets, and gray lines, with tooltips.
- **Order Management**: Capital, leverage, max quantity, order quantity, executed rate, and risk/reward calculations.
- **Trigger Conditions**: Visual display of stop loss and target triggers with quantities.
- **Manual Refresh Button**: Red button to reset the form/page.
- **Debugging/Logging**: Visible log area for step-by-step status and error messages.

## Technical Stack
- **HTML/CSS/JavaScript**: All logic and UI are implemented in a single HTML file.
- **No backend/server**: All data is mock/hardcoded for demonstration.

## Workflow
1. **Refresh the page** (optional, resets all fields).
2. **Enter script name** (e.g., HDFC) in the Script Name field.
3. **Click "Fetch Live Data"** to populate the data fields.
4. **Enter trade details** (entries, exits, stop losses, times, etc.).
5. **Click "Generate Gann 7x7 Square"** to create the Gann table.
6. **Toggle Upward/Downward** as needed.
7. **Review calculated levels, triggers, and risk/reward.**

## Gann Table Logic
- **Square Root Theory**: The center value is the anchor price. Each spiral step is calculated as $(\sqrt{\text{anchor}} \pm n \times 0.125)^2$.
- **Spiral Fill**: The table is filled in a clockwise spiral from the center.
- **Highlighting**: Center, SL, T1, T2, T3, and gray lines are visually marked.

## Troubleshooting & Debugging
- **Debug Log**: A log area at the top of the page shows each step of the data-fetching process and any errors.
- **Error Messages**: If JavaScript is disabled or a script error occurs, a visible error message appears.

## Known Issues & Limitations
- **No real live data**: All stock data is hardcoded for demonstration.
- **Local file restrictions**: Some browsers may restrict JavaScript or page reloads for local files.
- **Refresh button**: Only resets the form/page; does not fetch new data automatically.

## Conversation & Development History
- Multiple iterations to fix the Script Name field (editable, empty on refresh, disables browser autofill).
- Added manual refresh button and ensured it works in local file context.
- Debugged why data fields were not updating (added error and log messages).
- Ensured Gann table only generates on explicit user action.
- Added robust highlighting and tooltips for all key Gann levels.
- Provided troubleshooting steps and user guidance throughout.

## Conversation Summary
- User requested a dynamic Gann table for trading, with live data, order management, and multi-script support.
- Iterative improvements: spiral fill, toggle for upward/downward, robust highlighting, correct Square Root Theory logic.
- Focused on workflow: refresh → type script name → fetch data → generate Gann table.
- Debugged issues with input field state, value updating, and browser compatibility.
- Added visible error/logging for user troubleshooting.

## How to Use
1. Open the HTML file in a modern browser (preferably Chrome or Edge).
2. Follow the workflow steps above.
3. Use the debug log to diagnose any issues.

---

For a full record of all conversations and discussions, please refer to the chat history in your Copilot session. This document summarizes all major technical and workflow decisions, as well as the evolution of the project.
