# Useful-Python-Scripts
A collection of scripts that were useful for me

## librenms_rename_devices.py (Currently MySQL/MariaDB only)
This script takes global environment variables for a MySQL/MariaDB database, imports a CSV file named `librenms_fix`, takes two fields (`old_hostname`, `new_hostname`) from the CSV, and sends a MySQL/MariaDB `UPDATE` command to the database to update the device hostname.  This was used to update a massive amount of network devices from IP's to FQDN's without having to do this one-by-one.

While writing this README, I found out that `renamehost.php` already exists inside the `./librenms/` app folder, making this script a much worse substitute.  Don't use this.
