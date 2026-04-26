# 🧘‍♂️ Health Manager AI: 你的專屬智能健康管家

> **讓 AI 成為你的健康教練，而不僅僅是一個紀錄工具。**

Health Manager AI 是一個基於 **CrewAI** 與 **Google Gemini 1.5** 驅動的自動化健康管理系統。它不再只是冰冷的數字填寫，而是透過多個 AI 代理人（Agents）的協作，主動關心你的飲食、運動與睡眠，並在每日早晚提供精準的指導與回饋。

---

## 🎯 核心目標
本專案旨在解決現代人「有紀錄、沒執行」的痛點。透過 AI 的主動介入，我們將健康管理拆解為三個層次：
1.  **每日微調**：早晨給予目標，夜晚確認回饋。
2.  **中期回顧**：每週自動分析趨勢，找出健康的隱形殺手。
3.  **長期策略**：每月深度檢視進步幅度，調整下個月的體能目標。

---

## 🤖 系統架構：四位一體的 AI 專家團隊
本系統採用多代理人協作模式，每位 AI 都各司其職：

*   **🏃 專業健康教練 (Health Coach)**
    *   *職責*：分析歷史數據，根據你的體能與心情制定今日運動與飲食目標。
    *   *特色*：會根據你昨晚的睡眠品質調整今天的運動強度。

*   **📝 細心健康管理員 (Data Guardian)**
    *   *職責*：負責每日早晚的對話與紀錄，將繁雜的對話轉化為結構化的數據。
    *   *特色*：具備同理心，會在你疲憊時給予適當的鼓勵。

*   **📊 數據洞察專家 (Insight Analyst) - [開發中]**
    *   *職責*：每週與每月定期執行，掃描所有日誌，生成視覺化的健康簡報與趨勢分析。

*   **🚩 目標戰略家 (Target Strategist) - [計畫中]**
    *   *職責*：負責「長期目標建立」與「目標達成率追蹤（Target Tracing）」。例如：設定三個月內達成 5KM 跑步目標。

---

## ✨ 重點功能
- [x] **每日早晨規劃**：根據歷史狀態建議今日運動量與飲水量。
- [x] **每日夜晚紀錄**：透過對話捕捉當日的飲食、運動與睡眠狀態。
- [x] **自然語言互動**：直接輸入「今天吃了火鍋，有點負擔」，AI 會自動轉化為熱量提醒。
- [ ] **週/月健康簡報**：自動生成 Markdown 格式的健康報告，回顧體重、運動時數趨勢。
- [ ] **目標追蹤機制**：設定 KPI（如：體脂肪率、深蹲重量），AI 會計算當前進度與預期達成日。

---

## 🛠️ 技術棧
- **Framework**: [CrewAI](https://github.com/joaomoura/crewAI)
- **LLM Brain**: [Google Gemini 1.5 Flash/Pro](https://ai.google.dev/)
- **Storage**: Local Structured JSON (未來計畫支援 SQL/Notion API)
- **Language**: Python

---

## 🚀 快速開始
1. **設定環境變數**
   ```powershell
   $env:GOOGLE_API_KEY = "你的_GEMINI_API_KEY"
   ```
2. **安裝套件**
   ```bash
   pip install crewai langchain-google-genai
   ```
3. **啟動 AI 助手**
   ```bash
   python health_app.py
   ```

---

## 📅 未來藍圖 (Roadmap)
*   **Target Tracing**: 建立 `targets.json`，讓 AI 追蹤你的進步曲線。
*   **多維度感測**: 串接 Apple Health 或 Google Fit 數據。
*   **情緒分析**: 追蹤壓力和情緒對健康的影響。
*   **自動化簡報**: 每週日晚上 9 點自動推播週報到 LINE 或 Discord。

---
*Generated with ❤️ by Gemini CLI & CrewAI.*
