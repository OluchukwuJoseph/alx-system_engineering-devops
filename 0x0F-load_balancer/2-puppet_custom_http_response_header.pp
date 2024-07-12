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

$server_name = 'server_name _;'
$add_header = 'add_header X-Served-By \$hostname;'
$redirect_location = 'location /redirect_me {\n\t\treturn 301 /;\n\t}'
$error_page = 'error_page 404 /404.html;'
$error_location = 'location /404.html {\n\t\troot /var/www/html;\n\t\tinternal;\n\t}'

# Combine variables into a single string
$new_text = "${server_name}\n\t${add_header}\n\t${redirect_location}\n\t${error_page}\n\t${error_location}"

exec {'search and replace text':
    command => 'sudo sed -i "s|server_name _;|${new_text}|g" /etc/nginx/sites-enabled/default',
    path    => ['/usr/bin', '/bin']
}

service { 'nginx':
    ensure => running,
    enable => true
}
