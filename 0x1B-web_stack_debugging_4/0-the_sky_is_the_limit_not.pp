# This script increases the amount of traffic my Nginx server can handle

exec { 'fix--for-nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx-restart':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
