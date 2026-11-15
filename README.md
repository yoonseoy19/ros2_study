# ROS2 Humble Study

Python(rclpy)으로 직접 작성한 ROS2 노드로 Turtlesim 거북이를 제어한 스터디 기록입니다.

- `my_subscriber.py`: `/turtle1/pose`를 구독해 거북이 좌표(x, y, theta)를 출력
- `my_publisher.py`: 0.5초마다 `/turtle1/cmd_vel`로 속도 명령을 보내 원 그리기

## 실행

    colcon build --symlink-install
    source install/local_setup.bash
    ros2 run turtlesim turtlesim_node
    ros2 run my_first_package my_publisher
    ros2 run my_first_package my_subscriber
