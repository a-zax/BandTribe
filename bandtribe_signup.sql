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
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signup` (
  `name` varchar(45) DEFAULT NULL,
  `phoneno` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `artist` varchar(45) DEFAULT NULL,
  `instrument` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup`
--

LOCK TABLES `signup` WRITE;
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
INSERT INTO `signup` VALUES ('dfd','fdfd','fdd','fdd','dfdfd','dfdf'),('df','dfd','df','dfdf','dfd','dfd'),('sd','sds','ds','dsds','dsds','ds'),('zx','zxz','zx','zxzx','zxz','zxz'),('xx','xx','xx','xxx','xx','xxx'),('zfx','f','fxfx','xfxx','fxf','xf'),('xsd','sds','ds','sdsds','dsd','sds'),('xcx','cx','cxc','xcx','cxcx','cxc'),('sdsd','ssd','sdsd','sdsd','sdsd','sds'),('sd','sd','sd','sdsd','sds','dsd'),('aryan','03929','aryan1@gmail.com','dancer','flute','aryan1234'),('Ashish','459856594','ashishcoll@gmail.in','singer','flute','123'),('rohit','5655916','yadav@123','comedian','piano','1234'),('sd','sdsdsd','sdsds','dsdsd','guitar','sdsdsd'),('aman','9163122229','aman.v.singh@slrtce.in','dancer','flute','1234'),('Ashish singh','1111','ashish.v.singh@yahoo.com','dancer','Guitar','1234'),('aryan singh','8273274866','Aryan.ashish@yahoo.com','comedian ','guitar','1234'),('rahul yadav','888363899','rahul.yadav@yahoo.com','megician','asasa','1234'),('ADITIYA','GHHHHJJ','1111','HGVTY','HJB','1212'),('pinkey yadav','8288817175','pinkey.v.yadav@yahoo.com','dancer','Guitar','1234'),('Aryan  ashish shukla','8377838880','shukla.@gmail.com','comedian','Guitar','1111'),('abhiji  vagle','8772366237','abhijit1977@gmail.com','singer','Guitar ','15444'),('Ritik singh','6874141831','ritiksingh@outlook.com','singer','Guitar','12222'),('Anita yadav','8783387327','anita@yahoo.com','singer','piano','1234'),('amisha','7821313873','amisha@gmail.com','singer','Flute','1234'),('preeti','2123138788','preeti.r.@gmail.com','comedian','no','12329'),('poonam singh','8193189800','poonma@yahoo.com','comedian and singer','piano','13212'),('kabir thakur','8499387388','kabir@outlook.com','Dancer','Guitar','1221'),('Bassi punjabi','3213827130','Bassi@outlook.com','comedian','piano','241131'),('mitali singh','3723823700','mitali.v.singh@slrtce.in','singer','flute','12333'),('mohommad abdul ','7323236260','abdul@yahoo.com','comedian','guitar','2323123'),('aaaa','2183712112','x','sDSA','ASDAD','11');
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;
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
