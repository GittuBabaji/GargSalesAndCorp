#!/bin/bash
echo "ubuntu" | sudo -S mysql -e "
CREATE DATABASE IF NOT EXISTS garg_variety_store;
CREATE USER IF NOT EXISTS 'garguser'@'localhost' IDENTIFIED BY 'gargpass';
GRANT ALL PRIVILEGES ON garg_variety_store.* TO 'garguser'@'localhost';
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;
" 2>&1
echo "=== MySQL setup done ==="
