# Script to replace line on a server
file_line { 'replace-phpp-with-php':
ensure  => multiple,
path    => '/var/www/html/wp-settings.php',
line    => 'phpp',
match   => '^phpp$',
content => 'php',
replace => all,
backup  => '.bak',
diff    => true,
notify  => Exec['restart-apache'],
}

exec { 'restart-apache':
command   => 'systemctl restart apache2',
path      => ['/usr/local/bin', '/usr/bin', '/bin'],
refreshed => true,
}
