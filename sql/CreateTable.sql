DROP TABLE IF EXISTS `computer`;
CREATE TABLE `computer` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `computer_id` int(11),# 范围 1 - 72
    `time` datetime,
    `state` boolean, # 0关机，1开机
    `cpu` decimal(10,2),   # 范围 0 - 100
    `memory` decimal(10,2),# 范围 0 - 100
    `disk` decimal(10,2),  # 范围 0 - 100
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

# 然后这里，有两种温度，一种房间温度，一种电脑温度。
# 如果 computer_id 为 0 room_id 不为 0 代表是房间温度
# 如果 computer_id 不为 0 room_id 为 0 代表是电脑温度
DROP TABLE IF EXISTS `temperature`;
CREATE TABLE `temperature` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`time` datetime,
`temperature` decimal(10,2),
`computer_id` int(11),
`room_id` int(11), # 范围 1 - 4 下面一样
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `humidity`;
CREATE TABLE `humidity` (
   `id` int(11) NOT NULL AUTO_INCREMENT,
   `time` datetime,
   `humidity` decimal(10,4),
   `room_id` int(11),
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `people`;
CREATE TABLE `people` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `time` datetime,
    `number_of_people` int(5),# 房间人数
    `room_id` int(11),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


