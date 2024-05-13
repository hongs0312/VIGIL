character_information_create = \
"CREATE TABLE `character_information` (`id` INT(10) UNSIGNED NOT NULL,\
	`name` CHAR(128) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`primary` INT(10) UNSIGNED NOT NULL DEFAULT '0',\
	`secondary` INT(10) UNSIGNED NOT NULL DEFAULT '0',\
	`special` INT(10) UNSIGNED NOT NULL DEFAULT '0',\
	`passive` INT(10) UNSIGNED NOT NULL DEFAULT '0',\
	`strike` INT(10) UNSIGNED NOT NULL DEFAULT '0',\
	PRIMARY KEY (`id`) USING BTREE\
)\
COLLATE='utf8mb4_general_ci'\
ENGINE=InnoDB\
;"

skill_information_create = \
"CREATE TABLE `skill_information` (\
	`id` INT(10) UNSIGNED NOT NULL,\
	`name` CHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`cooldown` CHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`damage` CHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`description` VARCHAR(1000) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`image` CHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	`feature` CHAR(200) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',\
	PRIMARY KEY (`id`) USING BTREE\
)\
COLLATE='utf8mb4_general_ci'\
ENGINE=InnoDB\
;"