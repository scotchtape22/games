-- MySQL dump 10.13  Distrib 8.0.20, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: lzwclt_db
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `acct_types`
--

DROP TABLE IF EXISTS `acct_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acct_types` (
  `acct_id` int NOT NULL AUTO_INCREMENT,
  `acct_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`acct_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acct_types`
--

LOCK TABLES `acct_types` WRITE;
/*!40000 ALTER TABLE `acct_types` DISABLE KEYS */;
INSERT INTO `acct_types` VALUES (1,'Super'),(2,'Elite'),(3,'Paid'),(4,'User'),(5,'Bot'),(6,'Censured');
/*!40000 ALTER TABLE `acct_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `addiction`
--

DROP TABLE IF EXISTS `addiction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addiction` (
  `addiction_id` int NOT NULL AUTO_INCREMENT,
  `addiction_name` varchar(31) DEFAULT NULL,
  PRIMARY KEY (`addiction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `addiction`
--

LOCK TABLES `addiction` WRITE;
/*!40000 ALTER TABLE `addiction` DISABLE KEYS */;
INSERT INTO `addiction` VALUES (1,'Cocaine'),(2,'Marijuana'),(3,'Adderall'),(4,'Alcohol'),(5,'Steroids'),(6,'Cash'),(7,'Victory');
/*!40000 ALTER TABLE `addiction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contracts`
--

DROP TABLE IF EXISTS `contracts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contracts` (
  `contract_id` int unsigned NOT NULL AUTO_INCREMENT,
  `player` int NOT NULL,
  `c_status` enum('Pending','Reviewed','Expired') NOT NULL,
  `c_class` enum('Franchise','Standard','2-Way','Minor League','Mentor','Minor Coach','Medic','Scout','Marketeer') DEFAULT NULL,
  `c_cost` int DEFAULT NULL,
  `c_term` int DEFAULT NULL,
  `c_nmc` char(1) DEFAULT NULL,
  `c_bonus_ind` int DEFAULT NULL,
  `c_bonus_team` int DEFAULT NULL,
  PRIMARY KEY (`contract_id`),
  KEY `fk_players_idx` (`player`),
  CONSTRAINT `fk_players` FOREIGN KEY (`player`) REFERENCES `player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contracts`
--

LOCK TABLES `contracts` WRITE;
/*!40000 ALTER TABLE `contracts` DISABLE KEYS */;
/*!40000 ALTER TABLE `contracts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enhancements`
--

DROP TABLE IF EXISTS `enhancements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enhancements` (
  `enhancement_id` int NOT NULL AUTO_INCREMENT,
  `enhancement_name` varchar(31) DEFAULT NULL,
  PRIMARY KEY (`enhancement_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enhancements`
--

LOCK TABLES `enhancements` WRITE;
/*!40000 ALTER TABLE `enhancements` DISABLE KEYS */;
INSERT INTO `enhancements` VALUES (1,'Cocaine'),(2,'Marijuana'),(3,'Adderall'),(4,'Alcohol'),(5,'Steroids'),(6,'Nicotene'),(7,'Psychedelics');
/*!40000 ALTER TABLE `enhancements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event` (
  `event_id` int NOT NULL AUTO_INCREMENT,
  `event_type` varchar(45) DEFAULT NULL,
  `event_date` datetime NOT NULL,
  `event_league` int NOT NULL,
  `event_team` int DEFAULT NULL,
  `event_team2` int DEFAULT NULL,
  `event_ll` blob,
  PRIMARY KEY (`event_id`),
  KEY `fk_teams_idx` (`event_team`,`event_team2`),
  KEY `fk_league_idx` (`event_league`),
  KEY `fk_team_2_idx` (`event_team2`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genders`
--

DROP TABLE IF EXISTS `genders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genders` (
  `gen_id` int NOT NULL AUTO_INCREMENT,
  `gen_name` varchar(31) DEFAULT NULL,
  PRIMARY KEY (`gen_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genders`
--

LOCK TABLES `genders` WRITE;
/*!40000 ALTER TABLE `genders` DISABLE KEYS */;
INSERT INTO `genders` VALUES (1,'Male'),(2,'Female'),(3,'Neither'),(4,'Both'),(6,'Robot');
/*!40000 ALTER TABLE `genders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `humans`
--

DROP TABLE IF EXISTS `humans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `humans` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `u_pass` varchar(255) DEFAULT NULL,
  `u_class` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  KEY `fk_type_idx` (`u_class`),
  CONSTRAINT `fk_type` FOREIGN KEY (`u_class`) REFERENCES `acct_types` (`acct_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `humans`
--

LOCK TABLES `humans` WRITE;
/*!40000 ALTER TABLE `humans` DISABLE KEYS */;
/*!40000 ALTER TABLE `humans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `injury`
--

DROP TABLE IF EXISTS `injury`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `injury` (
  `inj_id` int NOT NULL AUTO_INCREMENT,
  `inj_name` varchar(31) DEFAULT NULL,
  PRIMARY KEY (`inj_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `injury`
--

LOCK TABLES `injury` WRITE;
/*!40000 ALTER TABLE `injury` DISABLE KEYS */;
/*!40000 ALTER TABLE `injury` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `league`
--

DROP TABLE IF EXISTS `league`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `league` (
  `league_id` int NOT NULL AUTO_INCREMENT,
  `league_name` varchar(255) DEFAULT NULL,
  `league_size` int DEFAULT NULL,
  `league_comish` int DEFAULT NULL,
  `comish_team` char(1) DEFAULT NULL,
  `season_length` int DEFAULT NULL,
  `season_freq` int DEFAULT NULL,
  `sal_cap` int DEFAULT NULL,
  `fog_of_war` char(1) DEFAULT NULL,
  `league_history` blob,
  PRIMARY KEY (`league_id`),
  KEY `fk_comish_idx` (`league_comish`),
  CONSTRAINT `fk_comish` FOREIGN KEY (`league_comish`) REFERENCES `humans` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `league`
--

LOCK TABLES `league` WRITE;
/*!40000 ALTER TABLE `league` DISABLE KEYS */;
/*!40000 ALTER TABLE `league` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `p_relationships`
--

DROP TABLE IF EXISTS `p_relationships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `p_relationships` (
  `player_1` int NOT NULL,
  `player_2` int NOT NULL,
  `relation_type` enum('Friend','Close Friend','Frenemy','Rival') NOT NULL,
  UNIQUE KEY `player_1_UNIQUE` (`player_1`),
  UNIQUE KEY `player_2_UNIQUE` (`player_2`),
  KEY `fk_players_idx` (`player_1`,`player_2`),
  CONSTRAINT `fk_players_1` FOREIGN KEY (`player_1`) REFERENCES `player` (`player_id`),
  CONSTRAINT `fk_players_2` FOREIGN KEY (`player_2`) REFERENCES `player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `p_relationships`
--

LOCK TABLES `p_relationships` WRITE;
/*!40000 ALTER TABLE `p_relationships` DISABLE KEYS */;
/*!40000 ALTER TABLE `p_relationships` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personality`
--

DROP TABLE IF EXISTS `personality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personality` (
  `personality_id` int NOT NULL AUTO_INCREMENT,
  `personality_name` varchar(31) DEFAULT NULL,
  PRIMARY KEY (`personality_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personality`
--

LOCK TABLES `personality` WRITE;
/*!40000 ALTER TABLE `personality` DISABLE KEYS */;
INSERT INTO `personality` VALUES (1,'Cautious'),(2,'Stoic'),(3,'Spirited'),(4,'Cocky'),(5,'Inquisitive'),(6,'Addictive'),(7,'Milquetoast'),(8,'Determined');
/*!40000 ALTER TABLE `personality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player`
--

DROP TABLE IF EXISTS `player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player` (
  `player_id` int NOT NULL AUTO_INCREMENT,
  `league` int DEFAULT NULL,
  `team` int DEFAULT NULL,
  `f_name` varchar(255) DEFAULT NULL,
  `l_name` varchar(255) DEFAULT NULL,
  `gen` char(1) DEFAULT NULL,
  `hometown` varchar(255) DEFAULT NULL,
  `home_region` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `personality` enum('Cautious','Stoic','Spirited','Cocky','Inquisitive','Addictive','Milquetoast','Determined') DEFAULT NULL,
  `addiction` int DEFAULT NULL,
  `gs_acc` int DEFAULT NULL,
  `gs_eva` int DEFAULT NULL,
  `gs_ini` int DEFAULT NULL,
  `ls_kno` int DEFAULT NULL,
  `ls_sta` int DEFAULT NULL,
  `ls_pot` int DEFAULT NULL,
  `ls_van` int DEFAULT NULL,
  `con_type` enum('Franchise','Standard','2-Way','Minor League','ML Coach','Mentor','Medic','Scout','Marketeer') DEFAULT NULL,
  `con_value` int DEFAULT NULL,
  `con_notes` varchar(255) DEFAULT NULL,
  `p_tac_1` enum('Skirmish','Charge','Snipe','Free Fire','Ambush','Guard') DEFAULT NULL,
  `p_tac_2` enum('Skirmish','Charge','Snipe','Free Fire','Ambush','Guard') DEFAULT NULL,
  `p_tac_3` enum('Skirmish','Charge','Snipe','Free Fire','Ambush','Guard') DEFAULT NULL,
  `p_r_status` enum('Starter','Substitute','Scratch','Minors') DEFAULT NULL,
  `p_subs_for` int DEFAULT NULL,
  `p_enhance` varchar(31) DEFAULT NULL,
  `inj_type` int DEFAULT NULL,
  `inj_dur` int DEFAULT NULL,
  `p_face` blob,
  PRIMARY KEY (`player_id`),
  KEY `league_idx` (`league`),
  KEY `team_idx` (`team`),
  KEY `region_idx` (`home_region`),
  KEY `sub_tree_idx` (`p_subs_for`),
  KEY `fk_con_type_idx` (`con_type`),
  KEY `fk_inj_idx` (`inj_type`),
  CONSTRAINT `fk_inj` FOREIGN KEY (`inj_type`) REFERENCES `injury` (`inj_id`),
  CONSTRAINT `fk_league` FOREIGN KEY (`league`) REFERENCES `league` (`league_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_team` FOREIGN KEY (`team`) REFERENCES `team` (`team_id`),
  CONSTRAINT `sub_tree` FOREIGN KEY (`p_subs_for`) REFERENCES `player` (`player_id`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player`
--

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `region`
--

DROP TABLE IF EXISTS `region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `region` (
  `region_id` int NOT NULL AUTO_INCREMENT,
  `region_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`region_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `region`
--

LOCK TABLES `region` WRITE;
/*!40000 ALTER TABLE `region` DISABLE KEYS */;
INSERT INTO `region` VALUES (1,'Japan'),(2,'Korea'),(3,'New England'),(4,'Eastern Canada'),(5,'Caribbean'),(6,'United Kingdom'),(7,'Midwest'),(8,'Dixie'),(9,'Texas'),(10,'California'),(11,'Rockies'),(12,'Mid-Atlantic'),(13,'Mediterranean'),(14,'China'),(15,'British Columbia'),(16,'The Future'),(17,'The Moon'),(18,'Mars'),(19,'The Belt'),(20,'Beyond'),(21,'Venus'),(22,'Mercury'),(23,'Middle East'),(24,'USSR'),(25,'Indo China'),(26,'Austrailia'),(27,'Latin America'),(28,'Brazil'),(29,'Cascadia'),(30,'Quebec');
/*!40000 ALTER TABLE `region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `team_id` int NOT NULL AUTO_INCREMENT,
  `league` int NOT NULL,
  `manager` int NOT NULL,
  `team_local` varchar(255) DEFAULT NULL,
  `team_mascot` varchar(255) DEFAULT NULL,
  `team_region` int DEFAULT NULL,
  `team_color_1` varchar(8) DEFAULT NULL,
  `team_color_2` varchar(8) DEFAULT NULL,
  `team_color_3` varchar(8) DEFAULT NULL,
  `team_treasure` int DEFAULT NULL,
  `fan_pro` int DEFAULT NULL,
  `fan_exp` int DEFAULT NULL,
  `fan_cur` int DEFAULT NULL,
  `sea_wins` int DEFAULT NULL,
  `sea_loss` int DEFAULT NULL,
  `sea_fc` int DEFAULT NULL,
  `sea_fs` int DEFAULT NULL,
  `sea_pf` int DEFAULT NULL,
  `sea_pa` int DEFAULT NULL,
  `tac_1_pref` int DEFAULT NULL,
  `tac_2_pref` int DEFAULT NULL,
  `tac_3_pref` int DEFAULT NULL,
  PRIMARY KEY (`team_id`),
  KEY `fk_league_idx` (`league`),
  KEY `fk_manager_idx` (`manager`),
  KEY `fk_region_idx` (`team_region`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-10 11:53:44
