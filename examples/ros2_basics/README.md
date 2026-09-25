# 通用 ROS 2 Python Publisher／Subscriber 範例

此 package 僅在 ROS 2 Humble 環境執行，使用 `std_msgs/String` 在 `chatter` Topic 傳文字；不控制 R2 馬達、舵機或任何硬體。

## 建置
在已安裝並 source ROS 2 Humble 的 Ubuntu 22.04 環境：

```bash
mkdir -p ~/ros2_ws/src
# 將本資料夾 ros2_basics 複製到 ~/ros2_ws/src/ros2_basics
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select ros2_basics
source install/setup.bash
```

## 執行
終端機一：

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run ros2_basics listener
```

終端機二：

```bash
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 run ros2_basics talker
```

預期 listener 每秒收到 `Hello ROS 2: 0`、`Hello ROS 2: 1` 等文字。按 Ctrl+C 停止各節點。

## 檢查
另開終端機執行 `ros2 topic list`、`ros2 topic echo /chatter`、`ros2 node list`，觀察節點與訊息。結束後確認節點均已停止。

本執行環境未安裝 ROS 2 Humble，因此此範例尚未在此處實際執行；請依書中版本在 Ubuntu 22.04 + Humble 驗證。
