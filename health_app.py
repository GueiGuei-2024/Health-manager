import os
import json
from datetime import datetime
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool

# 1. 設定 API Key 與模型
# 原理：使用 CrewAI 提供的 LLM 類別。這可以解決 Pydantic 驗證錯誤，
# 並提供更穩定的連線機制。
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

# 建立 LLM 物件
# 機制：使用 provider/model_name 格式，並顯式傳入 API Key。
my_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=api_key
)

# 2. 定義自定義工具
@tool("health_log_reader")
def read_health_log():
    """讀取健康日誌檔案內容。"""
    try:
        with open("health_log.json", "r", encoding="utf-8") as f:
            content = json.load(f)
            return content if content else "目前日誌是空的。"
    except Exception:
        return "目前沒有歷史日誌。"

@tool("health_log_writer")
def save_daily_status(status_update: str):
    """將今日的達成狀態儲存到健康日誌中。"""
    log_file = "health_log.json"
    data = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
    
    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": status_update
    }
    data.append(new_entry)
    
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return f"成功存檔：{status_update}"

@tool("get_user_input")
def get_user_input(question: str):
    """當需要詢問用戶問題時使用。"""
    print(f"\n[AI 提問]: {question}")
    user_response = input("你的回答: ")
    return user_response

# 3. 定義 Agent
coach = Agent(
    role='專業健康教練',
    goal='根據歷史紀錄，制定今日健康任務。',
    backstory='你是一位專業教練，會根據用戶過去的表現（讀取日誌）給予適當的壓力。',
    tools=[read_health_log],
    llm=my_llm, 
    verbose=True,
    allow_delegation=False
)

tracker = Agent(
    role='健康管理員',
    goal='詢問用戶達成狀況並存檔。',
    backstory='你負責監督用戶是否完成任務，並將過程詳細記錄。',
    tools=[get_user_input, save_daily_status],
    llm=my_llm,
    verbose=True,
    allow_delegation=False
)

# 4. 定義任務
plan_task = Task(
    description='1. 讀取歷史日誌。 2. 為今天制定一個具體的運動任務（如：跑步30分鐘）。 3. 清楚地告訴用戶任務內容。',
    expected_output='今日具體運動任務描述。',
    agent=coach
)

track_task = Task(
    description='1. 參考 coach 剛才給出的今日任務。 2. 詢問用戶是否完成。 3. 將用戶的回答原封不動地或摘要後存入日誌。',
    expected_output='確認紀錄存檔成功的訊息。',
    agent=tracker,
    context=[plan_task]
)

# 5. 組建 Crew
health_crew = Crew(
    agents=[coach, tracker],
    tasks=[plan_task, track_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    if not api_key:
        print("錯誤：找不到 API Key，請先設定 GOOGLE_API_KEY 環境變數。")
    else:
        print("### 健康管理系統啟動 ###")
        health_crew.kickoff()
