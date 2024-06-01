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
-- Table structure for table `listofevents`
--

DROP TABLE IF EXISTS `listofevents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `listofevents` (
  `eventmanager_contact` varchar(15) DEFAULT NULL,
  `event_name` varchar(50) DEFAULT NULL,
  `event_date` varchar(25) DEFAULT NULL,
  `venue` varchar(100) DEFAULT NULL,
  `timing` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listofevents`
--

LOCK TABLES `listofevents` WRITE;
/*!40000 ALTER TABLE `listofevents` DISABLE KEYS */;
INSERT INTO `listofevents` VALUES ('9920902061','Malhar','August-22-2023 ','St. Xavier’s College mumbai India ','10:00am onwards'),('9922222233','Umang','April-08-2023 ','NM college mumbai India','11:00am onwards'),('8273274868','Adorea','july-01-2023 ','Wilson college(BMS),mumbai,India','8:00am onwards'),('8369118712','Aiyana','September-13-2023 ','P.D.Hindija college,mumbai,India','9:00am onwards'),('8976128088','DJ uri','October-22-2023 ','Bonobo,mumbai India','9:00pm onwards'),('9693710942','Juliet Fox','June-02-2023 ',' Bandra mumbai India','7:00pm onwards'),('77715090304','Blackstreet Boys','May-12-2023 ','Jio Garden,mumbai, India','8:00pm onwards'),('9920923231','Malhar','August-22-2023 ','St. Xavier’s College mumbai India ','10:00am onwards'),('9923232323','Umang','April-08-2023 ','NM college mumbai India','11:00am onwards'),('8273276769','Adorea','july-01-2023 ','Wilson college(BMS),mumbai,India','8:00am onwards'),('8369000712','Aiyana','october-13-2023 ','P.D.Hindija college,mumbai,India','9:00am onwards'),('0099128088','DJ uri','june-22-2023 ','Bonobo,mumbai India','9:00pm onwards'),('96773710942','Juliet Fox','July-02-2023 ',' Bandra mumbai India','7:00pm onwards'),('88715090304','Blackstreet Boys','May-12-2023 ','Jio Garden,mumbai, India','8:00pm onwards');
/*!40000 ALTER TABLE `listofevents` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-02 21:04:50
