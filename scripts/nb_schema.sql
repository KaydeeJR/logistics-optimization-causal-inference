CREATE TABLE IF NOT EXISTS `completed_orders` 
(
    `Trip_ID` INT,
    `Trip_Origin` TEXT,
    `Trip_Destination` TEXT,
    `Trip_Start_Time` TIMESTAMP,
    `Trip_End_Time` TIMESTAMP,
    PRIMARY KEY (`Trip_ID`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;