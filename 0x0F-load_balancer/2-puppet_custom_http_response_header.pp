# This manifest automate the task of creating a custom HTTP header response

exec {'update apt-get':
    command => 'sudo apt-get update',
    path    => ['/bin', '/usr/bin']
}

package {'nginx':
    ensure  => installed,
    require => Exec['update apt-get']
}

file {'/var/www/html/index.html':
    ensure  => present,
    content => 'Hello World!'
}

file {'/var/www/html/404.html':
    ensure  => present,
    content => "Ceci n'est pas une page"
}

exec {'search and replace text':
    command => 'sudo sed -i "s|server_name _;|server_name _;\n\tadd_header X-Served-By \$hostname;|g" /etc/nginx/sites-enabled/default',
    path    => ['/usr/bin', '/bin']
}

service { 'nginx':
    ensure => running,
    enable => true
}
