CREATE DATABASE wpdb DEFAULT character SET utf8 collate utf8_unicode_ci;

GRANT ALL PRIVILEGES ON wpdb.* to 'wpuser'@'localhost' IDENTIFIED BY '123456';
flush privileges;
