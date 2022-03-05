DROP DATABASE IF EXISTS `BarnesAndIgnoble`;
CREATE DATABASE IF NOT EXISTS `BarnesAndIgnoble`; 
USE `BarnesAndIgnoble`;

SET NAMES UTF8MB4;
SET character_set_client = UTF8MB4;

-- --------------------------------------
--  Publishers Table
-- --------------------------------------

CREATE TABLE `Publishers` (
	`PublisherID` 		int NOT NULL AUTO_INCREMENT,
	`Name` 		        varchar (50) NOT NULL ,
	`City` 		        varchar (25) NOT NULL ,
  	PRIMARY KEY (`PublisherID`),	
	INDEX `PublisherID` (`PublisherID`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  BOOKS TABLE
-- --------------------------------------

CREATE TABLE `Books` (
	`ISBN` 		        varchar (13) NOT NULL,
	`Title` 		    varchar (75) NOT NULL,
	`Genre` 			varchar (20) NOT NULL,	
	`PubDate` 		    year NULL,
	`Price` 			FLOAT(6, 2) NULL,
	`PublisherID` 	    int NOT NULL,
  	PRIMARY KEY (`ISBN`),	
	FOREIGN KEY (`PublisherID`) REFERENCES `Publishers` (`PublisherID`),
	INDEX `ISBN` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Authors Table
-- --------------------------------------

CREATE TABLE `Authors` (
	`AuthorID` 		    int NOT NULL AUTO_INCREMENT,
	`Name` 		        varchar (50) NOT NULL ,
  	PRIMARY KEY (`AuthorID`),	
	INDEX `AuthorID` (`AuthorID`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Editors Table
-- --------------------------------------

CREATE TABLE `Editors` (
	`EditorID` 			int NOT NULL AUTO_INCREMENT,
	`PublisherID` 	    int NOT NULL ,
	`Name` 		    	varchar (50) NOT NULL,
  	PRIMARY KEY (`EditorID`),
	FOREIGN KEY (`PublisherID`) REFERENCES `Publishers` (`PublisherID`),
	INDEX `EditorID` (`EditorID`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Customers Table
-- --------------------------------------

CREATE TABLE `Customers` (
	`CustomerID` 		int NOT NULL AUTO_INCREMENT,
	`Name` 		    	varchar (50) NOT NULL,
  	PRIMARY KEY (`CustomerID`),	
	INDEX `CustomerID` (`CustomerID`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Orders Table
-- --------------------------------------

CREATE TABLE `Orders` (
	`OrderID` 			int NOT NULL AUTO_INCREMENT,
	`Date` 		    	year NULL,
	`Total` 	    	FLOAT(6, 2) NULL,
	`CustomerID` 	   	int NOT NULL,
  	PRIMARY KEY (`OrderID`),
	FOREIGN KEY (`CustomerID`) REFERENCES `Customers` (`CustomerID`),
	INDEX `OrderID` (`OrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Shipments Table
-- --------------------------------------

CREATE TABLE `Shipments` (
	`OrderID` 			int NOT NULL AUTO_INCREMENT,
	`ISBN` 		    	varchar (13) NOT NULL,
	INDEX `OrderID` (`OrderID` ASC),
  	PRIMARY KEY (`OrderID`,`ISBN`),	
	FOREIGN KEY (`OrderID`) REFERENCES `Orders` (`OrderID`),
	FOREIGN KEY (`ISBN`) REFERENCES `Books` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Book Editors Table
-- --------------------------------------

CREATE TABLE `BookEditors` (
	`EditorID` 			int NOT NULL,
	`ISBN` 		    	varchar (13) NOT NULL,
  	PRIMARY KEY (`EditorID`,`ISBN`),	
	FOREIGN KEY (`EditorID`) REFERENCES `Editors` (`EditorID`),
	FOREIGN KEY (`ISBN`) REFERENCES `Books` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------
--  Book Authors Table
-- --------------------------------------

CREATE TABLE `BookAuthors` (
	`AuthorID` 			int NOT NULL,
	`ISBN` 		    	varchar (13) NOT NULL,
	`Royalty` 	    	FLOAT(10, 2),
  	PRIMARY KEY (`AuthorID`,`ISBN`),	
	FOREIGN KEY (`AuthorID`) REFERENCES `Authors` (`AuthorID`),
	FOREIGN KEY (`ISBN`) REFERENCES `Books` (`ISBN`)
) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;