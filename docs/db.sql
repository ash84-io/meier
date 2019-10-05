CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_date` datetime DEFAULT NULL,
  `mo_date` datetime DEFAULT NULL,
  `post_name` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 NOT NULL,
  `content` text CHARACTER SET utf8 NOT NULL,
  `html` text CHARACTER SET utf8,
  `visibility` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `is_page` tinyint(1) DEFAULT '0',
  `featured_image` text CHARACTER SET utf8,
  PRIMARY KEY (`id`),
  UNIQUE KEY `post_name` (`post_name`),
  KEY `ix_post_in_date` (`in_date`),
  KEY `ix_post_mo_date` (`mo_date`),
  KEY `ix_post_title` (`title`),
  KEY `ix_post_status` (`status`),
  KEY `ix_post_visibility` (`visibility`),
  KEY `ix_post_is_page` (`is_page`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `post_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_date` datetime DEFAULT NULL,
  `mo_date` datetime DEFAULT NULL,
  `tag_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_post_tag_in_date` (`in_date`),
  KEY `ix_post_tag_mo_date` (`mo_date`),
  KEY `ix_post_tag_post_id` (`post_id`),
  KEY `ix_post_tag_tag_id` (`tag_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_date` datetime DEFAULT NULL,
  `mo_date` datetime DEFAULT NULL,
  `blog_title` varchar(255) NOT NULL,
  `blog_desc` varchar(255) NOT NULL,
  `post_per_page` int(11) DEFAULT NULL,
  `theme` varchar(255) NOT NULL,
  `domain` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_settings_in_date` (`in_date`),
  KEY `ix_settings_mo_date` (`mo_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_date` datetime DEFAULT NULL,
  `mo_date` datetime DEFAULT NULL,
  `tag` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_tag_mo_date` (`mo_date`),
  KEY `ix_tag_tag` (`tag`),
  KEY `ix_tag_in_date` (`in_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `test` (
  `idtest` int(11) NOT NULL,
  `testcol` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtest`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `in_date` datetime DEFAULT NULL,
  `mo_date` datetime DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  `profile_image` varchar(255) DEFAULT NULL,
  `user_desc` varchar(255) DEFAULT NULL,
  `twitter_profile` varchar(255) DEFAULT NULL,
  `facebook_profile` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_user_email` (`email`),
  KEY `ix_user_mo_date` (`mo_date`),
  KEY `ix_user_in_date` (`in_date`),
  KEY `ix_user_password` (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
