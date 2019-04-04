CREATE TABLE `books` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `book_id` int(11) NOT NULL,
  `title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `authors` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `image` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `image_2x` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `create_on` datetime NOT NULL,
  `publisher` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '',
  `release_date` date NOT NULL,
  `price` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pages` int(11) NOT NULL,
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `create_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1859 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;