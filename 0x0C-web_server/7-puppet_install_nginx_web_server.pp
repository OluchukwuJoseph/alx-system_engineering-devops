# This manifest configures our nginx web server

exec {'update apt-get':
    command => 'sudo apt-get update',
    path    => ['/bin', '/usr/bin']
}

package {'nginx':
    provider        => 'apt-get',
    install_options => ['-y']
}

file {'/var/www/html/index.html':
    ensure  => file,
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
    content => 'Hello World!'
}

file {'/var/www/html/404.html':
    ensure  => file,
    mode    => '0744',
    owner   => 'root',
    group   => 'root',
    content => "Ceci n'est pas une page"
}

# install file_line puppet module

exec {'file_line':
    command => 'puppet module install puppetlabs-stdlib',
    unless  => 'puppet module list | grep puppetlabs-stdlib',
    path    => ['/bin', 'usr/bin', '/opt/puppetlabs/bin']
}

file_line {'ensure server name':
    path              => '/etc/nginx/sites-enabled/default',
    line              => 'server_name _;'
    match             => 'server_name _;'
    match_for_absence => true,
}

file_line {'ensure root':
    path              => '/etc/nginx/sites-enabled/default',
    line              => 'root /var/www/html;',
    match             => 'root*',
    match_for_absence => true,
}

file_line {'ensure index':
    path => '/etc/nginx/sites-enabled/default',
    line => 'index index.html';,
    match             => 'index*',
    match_for_absence => true,
}

file_line { 'add_location_block':
    path => '/etc/nginx/sites-enabled/default',
    line => 'location / {',
}

file_line { 'add_try_files_line':
    path  => '/etc/nginx/sites-enabled/default',
    line  => '    try_files $uri $uri/ =404;',
    match => '    try_files \$uri \$uri/ =404;',
}

file_line { 'add_closing_bracket':
    path => '/etc/nginx/sites-enabled/default',
    line => '}',
}

file_line { 'add_location_redirect_block_opening':
    path => '/etc/nginx/sites-enabled/default',
    line => 'location /redirect {',
}

file_line { 'add_return_line':
    path  => '/etc/nginx/sites-enabled/default',
    line  => '    return 301 http://google.com;',
    match => '^    return 301 http://google.com;',
}

file_line { 'add_location_redirect_block_closing':
    path => '/etc/nginx/sites-enabled/default',
    line => '}',
}

file_line { 'add_error_page_404':
    path  => '/etc/nginx/sites-enabled/default',
    line  => 'error_page 404 /404.html;',
    match => '^error_page 404',
}

file_line { 'add_location_404_block_opening':
    path => '/etc/nginx/sites-enabled/default',
    line => 'location /404 {',
}

file_line { 'add_root_line':
    path  => '/etc/nginx/sites-enabled/default',
    line  => '    root /var/www/html;',
    match => '^    root /var/www/html;',
}

file_line { 'add_internal_line':
    path  => '/etc/nginx/sites-enabled/default',
    line  => '    internal;',
    match => '^    internal;',
}

file_line { 'add_location_404_block_closing':
    path => '/etc/nginx/sites-enabled/default',
    line => '}',
}
