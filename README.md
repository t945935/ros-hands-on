# ROS 2 做中學：ROSMASTER R2 讀者服務資源

此 GitHub 儲存庫僅提供書籍搭配的讀者服務資料與程式範例，不存放章節全文、合併書稿或出版用稿件。書籍正文請閱讀另行取得的正式版本。

主線設備為 ROSMASTER R2 阿克曼 ROS 機器人、Jetson Orin Nano SUPER、Ubuntu 22.04、ROS 2 Humble 與 Python。不同套裝／映像版本與選配可能造成差異，請以你手上的原廠文件和實機為準。

## 讀者資源
1. 先閱讀 `docs/hardware-profile.md` 與 `docs/safety-checklist.md`。
2. 依你的 R2 套件版本填寫 `docs/r2-interface-inventory.md`。Topic、型別、單位與啟動命令以原廠資料及實機為準，本專案不猜測。
3. `examples/ros2_basics/` 是通用 ROS 2 Python 入門範例，不會直接驅動 R2。
4. `examples/r2/` 說明實機程式的驗證界線；尚未核實的控制介面不提供可執行指令。
5. `docs/source-register.md` 記錄原廠與 ROS 2 官方資料的版本及適用限制。

## 資料夾
- `docs/`：設備規格、安全流程、介面盤點、來源版本與實作紀錄
- `examples/ros2_basics/`：不依賴 R2 的 ROS 2 Python 範例
- `examples/r2/`：R2 專用程式資料；須依確切套件版本實測後才會加入

## 重要安全聲明
本資料不是原廠操作手冊。短路／過流保護不等於急停。上電與測試請遵守原廠手冊；先架空驅動輪或使用安全支架、限速、清空測試區，並由操作者確保可立即切斷供電。不要在未核對介面與命令範圍時執行任何底盤控制程式。

## 版本政策
主線以 ROS 2 Humble + Ubuntu 22.04 為參考環境。不同 Jetson 映像、R2 控制板、雷射雷達選配可能造成差異，請記錄版本與來源；發現差異請開 Issue，附上不含密碼／個資的環境資訊與重現步驟。

## 範例狀態
ROS 2 Humble 範例尚未在 Humble runtime 執行；本專案也未包含經 R2 真機驗證的底盤 Topic／導航設定。請勿將通用範例當成 R2 驅動程式。
