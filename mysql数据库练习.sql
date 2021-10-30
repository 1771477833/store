/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.24 : Database - 学生数据库
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`学生数据库` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `学生数据库`;

/*Table structure for table `学生表` */

DROP TABLE IF EXISTS `学生表`;

CREATE TABLE `学生表` (
  `sno` char(4) NOT NULL,
  `sn` char(8) DEFAULT NULL,
  `sex` char(8) DEFAULT NULL,
  `age` int(2) DEFAULT NULL,
  `dept` int(11) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `学生表` */

insert  into `学生表`(`sno`,`sn`,`sex`,`age`,`dept`) values 
('s1','徐啸','女',17,2),
('s2','新国华','男',18,6),
('s3','徐伟','女',20,1),
('s4','邓一明','男',23,6),
('s5','张季扬','男',19,6),
('s6','张辉','女',22,3),
('s7','王克华','男',18,6),
('s8','王刃','男',19,3);

/*Table structure for table `学生选课表` */

DROP TABLE IF EXISTS `学生选课表`;

CREATE TABLE `学生选课表` (
  `sno` char(4) NOT NULL DEFAULT '',
  `cno` char(4) NOT NULL DEFAULT '',
  `grade` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sno`,`cno`,`grade`),
  KEY `FK_课程表_学生选课表` (`cno`),
  CONSTRAINT `FK_学生表_学生选课表` FOREIGN KEY (`sno`) REFERENCES `学生表` (`sno`),
  CONSTRAINT `FK_课程表_学生选课表` FOREIGN KEY (`cno`) REFERENCES `课程表` (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `学生选课表` */

insert  into `学生选课表`(`sno`,`cno`,`grade`) values 
('s1','c1',80),
('s2','c1',66),
('s1','c2',85),
('s2','c2',90),
('s3','c2',55),
('s7','c2',88),
('s1','c3',56),
('s2','c3',91),
('s3','c3',12),
('s8','c3',99),
('s1','c5',90),
('s2','c5',92),
('s4','c5',6),
('s5','c5',15),
('s6','c5',42),
('s1','c6',75),
('s2','c6',94),
('s4','c6',22),
('s5','c6',36),
('s6','c6',55),
('s1','c7',47),
('s6','c7',69);

/*Table structure for table `课程表` */

DROP TABLE IF EXISTS `课程表`;

CREATE TABLE `课程表` (
  `cno` char(4) NOT NULL,
  `cn` char(19) DEFAULT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `课程表` */

insert  into `课程表`(`cno`,`cn`) values 
('c1','数学'),
('c2','英语'),
('c3','Fortran77'),
('c4','Pascal'),
('c5','政治'),
('c6','物理'),
('c7','逻辑');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
