# ROS 2 做中學：ROSMASTER R2 讀者實作資源

本儲存庫提供書中練習程式、設備盤點表、操作紀錄表與勘誤。主線設備為 ROSMASTER R2 阿克曼 ROS 機器人，Jetson Orin Nano SUPER、Ubuntu 22.04、ROS 2 Humble、Python。

## 開始使用
1. 先閱讀 `docs/hardware-profile.md` 與 `docs/safety-checklist.md`。
2. 依你的 R2 套件版本填寫 `docs/r2-interface-inventory.md`。Topic、型別、單位與啟動命令以原廠資料及實機為準，本專案不猜測。
3. `examples/ros2_basics/` 是通用 ROS 2 Python 入門範例，不會直接驅動 R2。
4. 只有在確認原廠底盤介面、停止方式和限速範圍後，才可編寫並測試實車控制程式。

## 資料夾
- `docs/`：設備規格、安全流程、介面盤點與實作紀錄
- `examples/ros2_basics/`：不依賴 R2 的 ROS 2 Python 範例
- `examples/r2/`：R2 實機專用範例（待依確切套件版本實測後加入）

## 重要安全聲明
本資料不是原廠操作手冊。短路／過流保護不等於急停。上電與測試請遵守原廠手冊；先架空驅動輪或使用安全支架、限速、清空測試區，並由操作者確保可立即切斷供電。不要在未核對介面與命令範圍時執行任何底盤控制程式。

## 版本政策
主線以 ROS 2 Humble + Ubuntu 22.04 為準。不同 Jetson 映像、R2 控制板、雷射雷達選配可能造成差異，請記錄版本與來源；發現差異請開 Issue，附上不含密碼／個資的環境資訊與重現步驟。

## 目前狀態
入門範例為教學素材，需在 ROS 2 Humble 環境中執行驗證；目前未包含經 R2 真機驗證的底盤 Topic／導航設定。請勿將通用範例當成 R2 驅動程式。
