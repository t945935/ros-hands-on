# 來源與版本紀錄

本書指定設備以讀者提供的規格為基礎；R2 專屬操作內容以原廠 YahboomTechnology/ROSMASTER-R2 公開教材為查證起點。本文目前固定參照 Git commit `3d0919af47f4dae9c77ffeea3b594795cd4f482c`（2025-09-26）。本書的 ROS 2 通訊概念亦參照 ROS 2 官方 `humble` 文件固定版本 `0eabd5aaf089cc5999a3b081c7843a66841352a4`。閱讀其他分支或新版手冊時，請另記版本差異，不要把不同映像、雷達選配、控制板或底盤規格混為一談。

## 使用界線

- 本書的設備構成與供電規格亦包含使用者提供的產品資料；若與原廠文件不一致，以實際套裝手冊及供應商確認為準。
- 原廠 PDF 中的設定、命令與參數只適用於文件列明的 R2 配置。尤其導航文件舉例為 Silan A1 雷射雷達、AstraPro Plus 相機及 Docker／Orin 等軟體組合；讀者需核對自己的套裝與選配，不可直接複製命令。
- 一般 ROS 2 範例與 R2 硬體控制程式分開。未經本機版本核對及安全驗證的程式不得標示為可直接驅動 R2。
- 引用教材只作查證與讀者延伸閱讀；本書程式應以自行撰寫、逐版測試為原則，不整份重製原廠 PDF 或程式包。
- 官方教程描述的功能或命令不代表目前讀者的特定硬體組態已驗證；本書章節會區分「原廠文件所述」與「本機實測」。

## 已查閱的內容

- 官方 repository 根目錄說明：產品概述、阿克曼結構、主控與選配設備。
- 「Install Rosmaster driver library」：工廠映像已包含驅動程式庫的版本條件與安裝說明。
- 「Controlling robot motion」：通用車體運動 API 的說明；文件也註明不同車型可能不同，本書不將其數值直接套用至本機 R2。
- 「ROS2 topic communication」：Python Publisher／Subscriber 概念與教學範例。
- 「Depth camera usage」：Astra 型號啟動範例、影像／深度資料檢視流程；套用前仍須核對套件版本與相機型號。
- 「Navigation and obstacle avoidance」：文件列出的導航架構、特定參考配置及流程；它不是對所有雷達選配的相容性保證。
- ROS 2 Humble 官方 Topic、Service、Action 說明。

## Sources

[1] https://github.com/YahboomTechnology/ROSMASTER-R2/tree/3d0919af47f4dae9c77ffeea3b594795cd4f482c — YahboomTechnology ROSMASTER-R2 repository, pinned commit
[2] https://github.com/YahboomTechnology/ROSMASTER-R2/blob/3d0919af47f4dae9c77ffeea3b594795cd4f482c/04.ROS2-R2%20Car%20Tutorial/05.%20Basic%20course/3.%20Install%20Rosmaster%20driver%20library.pdf — R2 course: Install Rosmaster driver library
[3] https://github.com/YahboomTechnology/ROSMASTER-R2/blob/3d0919af47f4dae9c77ffeea3b594795cd4f482c/04.ROS2-R2%20Car%20Tutorial/05.%20Basic%20course/8.%20Controlling%20robot%20motion.pdf — R2 course: Controlling robot motion
[4] https://github.com/YahboomTechnology/ROSMASTER-R2/blob/3d0919af47f4dae9c77ffeea3b594795cd4f482c/04.ROS2-R2%20Car%20Tutorial/08.ROS2%20Basic%20Tutorial/7.ROS2%20topic%20communication.pdf — R2 course: Topic communication
[5] https://github.com/YahboomTechnology/ROSMASTER-R2/blob/3d0919af47f4dae9c77ffeea3b594795cd4f482c/04.ROS2-R2%20Car%20Tutorial/11.%20Depth%20camera%20course/1%E3%80%81Depth%20camera%20usage.pdf — R2 course: Depth camera usage
[6] https://github.com/YahboomTechnology/ROSMASTER-R2/blob/3d0919af47f4dae9c77ffeea3b594795cd4f482c/04.ROS2-R2%20Car%20Tutorial/10.%20Lidar%20course/7%E3%80%81Navigation%20and%20obstacle%20avoidance.pdf — R2 course: Navigation and obstacle avoidance
[7] https://raw.githubusercontent.com/ros2/ros2_documentation/0eabd5aaf089cc5999a3b081c7843a66841352a4/source/Concepts/Basic/About-Topics.rst — ROS 2 Humble topic concepts, pinned documentation commit
[8] https://raw.githubusercontent.com/ros2/ros2_documentation/0eabd5aaf089cc5999a3b081c7843a66841352a4/source/Concepts/Basic/Interfaces-Topics-Services-Actions.rst — ROS 2 Humble topics, services, actions, pinned documentation commit
[9] https://github.com/YahboomTechnology/ROSMASTER-R2 — R2 原廠 repository 根目錄，列出選配雷射雷達名稱「SLAM A1/YDLIDAR 4ROS」；使用者已確認其實際配置為 YDLIDAR 4ROS。實機標籤、硬體版本與 ROS 驅動仍須另行核對。
[10] https://www.yahboom.net/public/upload/upload-html/1700712853/1.Preparation.html — Yahboom YDLIDAR 4ROS ROS 2 準備文件；列出 `4ros_ydlidar_launch.py` 與 `ydlidar_4ros_view_launch.py` 作為示例啟動檔名，並示範觀察 `/scan`。需核對實機套件與版本；非本機 runtime 測試結果。
[11] https://www.yahboom.net/public/upload/upload-html/1665711547/Lidar%20basic-4ROS.html — Yahboom YDLIDAR 4ROS 雷達基礎文件；描述其為 360° 2D 脈衝 ToF 雷達，5–12 Hz 可調、20 kHz 測距頻率、IP65。規格僅為原廠文件宣稱，非本機量測。
[12] https://orbbec.github.io/OrbbecSDK_ROS2/en/source/camera_devices/1_overview/introduction.html — Orbbec ROS 2 wrapper 相機支援表；Astra Pro Plus 列在 v1.x `main` 支援清單，v2.x 標示不支援。實機 driver branch／版本與 topic 仍須核對。
