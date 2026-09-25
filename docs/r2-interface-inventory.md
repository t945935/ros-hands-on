# R2 介面盤點表

實機控制程式開始前，先從原廠手冊／套件與安全條件下的觀察填妥。未確認項目保持空白，不要猜值。

| 欄位 | 實際值 | 來源／版本 | 已驗證？ |
|---|---|---|---|
| Jetson 記憶體、系統映像版本 | | | |
| R2 控制板／韌體版本 | | | |
| 原廠啟動命令／Launch | | | |
| PS2 輸入 Topic／訊息型別 | | | |
| 底盤命令 Topic／訊息型別 | | | |
| 線速度單位及允許範圍 | | | |
| 轉向命令單位及允許範圍 | | | |
| 馬達回饋 Topic／型別／單位 | | | |
| Astra Pro Plus ROS 2 驅動套件／版本／分支（Orbbec 官方列出 v1.x `main` 支援 Astra Pro Plus；v2.x 不支援，實機需以映像內容核對） | | | |
| Astra Pro Plus 啟動檔、彩色／深度／IR Topic 與型別（不可從其他 Astra 型號或 ROS 1 教學直接推定） | | | |
| YDLIDAR 4ROS ROS 2 套件版本／來源 | | | |
| YDLIDAR 4ROS 啟動方式（原廠 ROS 2 教學示例：`ros2 launch ydlidar_ros2_driver 4ros_ydlidar_launch.py`；須確認實機安裝之套件包含此 launch file） | | | |
| 雷射掃描 Topic／型別（原廠教學示例觀察 `/scan`；實機需以 `ros2 topic list`／`ros2 topic info` 核實） | | | |
| IMU Topic／座標框架 | | | |
| TF frame 名稱與連線 | | | |
| 正常停止方式 | | | |
| 硬體斷電／急停位置 | | | |

## 驗證紀錄
- 日期：
- 操作者：
- 測試區與安全措施：
- ROS_DOMAIN_ID（若設定）：
- 使用的命令（遮除敏感資料）：
- 預期結果與實際結果：
- 已確認停止並恢復初始狀態：是／否
