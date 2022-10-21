CREATE TABLE IF NOT EXISTS `driver_location` 
(
    `id` INT,
    `order_id` INT,
    `driver_id` INT,
    `driver_action` TEXT,
    `latitude` FLOAT,
    `longitude` FLOAT,
    `created_at` FLOAT,
    `updated_at` FLOAT,
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;