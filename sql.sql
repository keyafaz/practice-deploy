CREATE DATABASE  IF NOT EXISTS `belt_exam_python` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `belt_exam_python`;
-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: belt_exam_python
-- ------------------------------------------------------
-- Server version	5.7.9

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pokes`
--

DROP TABLE IF EXISTS `pokes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pokes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poker_id` int(11) DEFAULT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_pokes_users_idx` (`users_id`),
  CONSTRAINT `fk_pokes_users` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pokes`
--

LOCK TABLES `pokes` WRITE;
/*!40000 ALTER TABLE `pokes` DISABLE KEYS */;
/*!40000 ALTER TABLE `pokes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  `birthday` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Keya','keya','test@email.com','$2b$12$jXzGp1Bjw6xKyuKgmHcHWuQdr.dmSESOTElhyKo8mrfp8.0BSKLGy','2016-06-24 14:39:45'),(2,'shay','sh','shay@shay.com','$2b$12$aDHssF4WvQ.5NHh33JOtA.pfuxgYI9BXtQnwJf9zMfEWaXwKn9kiG','2016-06-24 14:47:41'),(3,'hi','hi','hihi@gmail.com','$2b$12$yFdU85UzLv.13v2egVTO9un.hjoNFcBFBgpxjQWaOeff8C8vD/pbO','2016-06-24 14:49:32'),(4,'asdsd','asd','love@love.com','$2b$12$j39URtklue1HT8uTNREEYu8FgR93FHRSPyjpkEd7jU1.Ld.mcm.wW','2016-06-24 14:57:42'),(5,'asdsd','asd','lovss@love.com','$2b$12$nfpUAdakB8e/vNhIk5Bub.AI2jcie.QQbQNh5fKO460f7iGJdBogu','2016-06-24 14:58:17'),(6,'asdsd','asd','lovscs@love.com','$2b$12$gmgKLZF5tJhLYfAUwwlfiuG0MSS53olcx.tqrAfLFdOQ0CJcg0Nr2','2016-06-24 14:58:37'),(7,'asdsd','asd','lovsscs@love.com','$2b$12$coYe5OhXhkisdMxc8uB/oelNAmLA9Wy.gK2U//1104Oe0HB9mO6bi','2016-06-24 14:59:58'),(8,'sdf','fd','dff@gg.com','$2b$12$4eoRVGG3cDzwPQHCizACyuUwYVLKZz8kOleaodN8mgvnaxYhj1Kda','2016-06-24 15:02:03'),(9,'zczxcv','zvzx','testdf@email.com','$2b$12$QxE1Ac/9Ny.DSLwXbu52Hev4MUszuUpnEntzkOWTNx6.kUFGJlhl6','2016-06-24 15:03:31'),(10,'sadfsafgd','asdgagd','agag@sdfg.com','$2b$12$tneR0TI3xO2xVAQWm9m.B.dmSNN3Cvf2lfHMv2EiYShFgK6b1CWD2','2016-06-24 15:09:48'),(11,'pizza','hut','pizza@pizza.com','$2b$12$TKv6duoJYeTUZ..LfOvMAOq9SMW.l4SS5hGIZ5AIMOZU0uBwXrEBG','2016-06-24 15:11:29'),(12,'pizza','hut','pizza1@pizza.com','$2b$12$l51jc04MH1xOfiMOmZoutOZ9qP6ed/UpS2iqKhXJt2AN2PcON7MDO','2016-06-24 15:12:11'),(13,'pizza1','hut','pizza11@pizza.com','$2b$12$OknC1btD3tFHZZ9QvTzW6uz2wEaEzz0MLSp6PTNnmXNcRlmdldRIW','2016-06-24 15:14:04'),(14,'ff','ff','fff@fff.com','$2b$12$2hj6ckLyHJtOmGQ7TW1AoOyP7BldAOMv20AxuOK9eIK5oeAWNy34.','2016-06-24 15:14:58'),(15,'asdgf','asdf','asd@gmail.com','$2b$12$3rli1URGY2LsrnfZiDjfOe9PmVqF7vjhTJ1TjO2nnWz50zoKGwZY6','2016-06-24 15:16:48'),(16,'asdgf','asdf','assd@gmail.com','$2b$12$8kkRwZFhn.8GS8sQxUMV6OEBDLaln3e1jnemDZgwV5kwDYDxo1k72','2016-06-24 15:17:40'),(17,'asdgf','asdf','assad@gmail.com','$2b$12$Zlh.eKarOpCPawYuRMibl.T1fI4berdmWpUskxXTtcsHn2kouceKO','2016-06-24 15:18:36'),(18,'asdgf','asdf','asdsad@gmail.com','$2b$12$OozzxEu4QJgmpEw12HsUW.GNXVkbqPvGWI8EKzMTyi5FcKmC0zGsq','2016-06-24 15:19:10'),(19,'asdgf','asdf','asdsasd@gmail.com','$2b$12$bbQFuqjYKQE7aR9bkPiSG.GoQ9Ii2tw4z7zWIo8iDkp4JmeSVMi7.','2016-06-24 15:20:41'),(20,'asdgf','asdf','asdsassd@gmail.com','$2b$12$D1WvvAdpRhfmGqV9G8cl/eBiBvci/UiT6QIV5DksOZ6js0T8x.c5O','2016-06-24 15:21:09'),(21,'asdgf','asdf','asdssassd@gmail.com','$2b$12$U6qvt3U3YAxAUz.ZTxkCQO8I.Bmty0nIjxMF7CxFLjuRR3xZwwvSS','2016-06-24 15:22:07'),(22,'asdgf','asdf','asdssxassd@gmail.com','$2b$12$331U6JSZMcPDvRXhJ2ICw.o4omhLiyEwNJ/J54qdiR7OpjHGnvD1a','2016-06-24 15:23:09'),(23,'asd','asd','asd@fa.com','$2b$12$MLDSdZ9D4MTasgThLP4LjOK69u7xE.zFmGBtitfTmpzJb88FVllyK','2016-06-24 15:23:43'),(24,'asd','asd','asd@fss.com','$2b$12$rZ2JvzbgpyHfR4wWD6VaD.Tzeso2Y.DhzsIa3Pkriuax0EEx24EEG','2016-06-24 15:24:44'),(25,'sdfg','sdfg','tqqst@email.com','$2b$12$rUpb/F6p7e3Plm/nJ7p2ou/SsAyWbLYHINyk1W.cTGkd9nKHN3Pe2','2016-06-24 15:27:57'),(26,'dd','dd','dd@dd.com','$2b$12$uUUHJ9.rAqQmo8ifchG2IuIBZ1TdifsZKLaFo1Sn2PryPD7LxcahG','2016-06-24 15:29:33'),(27,'dd','dd','dsd@dd.com','$2b$12$ctwSwVhHOfErQc0wMKYvZeEvI5MLPWVxH6nH/FLU4UpaSf1R2CT6a','2016-06-24 15:30:07'),(28,'aaa','aaa','qqq@aaa.com','$2b$12$haquJzfPQkMOFl5q7QTjz.6DFEwVRHXIcqFj2/RMs9Yxk20TpE2n2','2016-06-24 15:31:32'),(29,'aaa','aaa','qqsq@aaa.com','$2b$12$nXa4fTVG4BY50IiFoG7gJ.GJX3zFJLIuI7XuRjoPic12RJ0qnCI9.','2016-06-24 15:33:49'),(30,'create','status','status@status.com','$2b$12$FyKOzJ9j4UOSM3jeioo9LuKVK.EotGc7wcKUTMVLBcq9zUnGcIxma','2016-06-24 15:34:23');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-24 16:51:59
