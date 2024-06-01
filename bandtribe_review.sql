-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: bandtribe
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review` (
  `review` varchar(200) DEFAULT NULL,
  `reviewno` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review`
--

LOCK TABLES `review` WRITE;
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
INSERT INTO `review` VALUES ('\"This app has been a game-changer for my team. We can now collaborate and communicate seamlessly, no matter where we are. Highly recommended!\"',NULL),('I\'ve been using this app for a few weeks now, and I\'m already seeing improvements in the way my team works together. The chat and file-sharing features are incredibly helpful.',NULL),('This app has made collaborating with my colleagues so much easier. I love being able to see everyone\'s progress and make real-time edits to our shared documents',NULL),('If you\'re looking for an app that makes collaborating with others effortless, this is it. It\'s user-friendly and has all the features you need to get work done quickly',NULL),('I\'ve tried a lot of collaboration apps, but this one is by far the best. The interface is clean and intuitive, and the video conferencing feature is top-notch.',NULL),('I\'m so impressed with this app\'s ability to keep everyone on the same page. It\'s made project management a breeze for our team.',NULL),('This app has made working remotely a lot less lonely. The virtual workspace and real-time collaboration features make it easy to stay connected with my colleagues.',NULL),('This app has made working remotely a lot less lonely. The virtual workspace and real-time collaboration features make it easy to stay connected with my colleagues.',NULL),('This app has everything you need to collaborate with others, all in one place. I love the ability to share files, chat with team members, and schedule meetings.',NULL),('If you\'re looking for an app that will help you work better with others, look no further. This app is a must-have for anyone who needs to collaborate on projects',NULL),('I\'ve been using this app to collaborate with colleagues across the country, and it\'s been amazing. The video conferencing feature is especially helpful for our remote team.',NULL),('Totally a new place for me here and I love this application coz different ppls here to learn different things',NULL);
/*!40000 ALTER TABLE `review` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-02 21:30:54
