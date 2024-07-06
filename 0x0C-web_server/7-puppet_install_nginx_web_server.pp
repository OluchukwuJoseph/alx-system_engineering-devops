#  Install Nginx web server (w/ Puppet)

# Update
exec { 'apt_update':
    command => 'apt-get update',
    path    => ['/usr/bin', '/sbin', '/bin']
}

# Install nginx
package { 'nginx':
    ensure   => 'installed',
    provider => 'apt-get',
}

# Write in index.html
file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!\n'
}

# Write in error-page.html
file { '/var/www/html/404.html':
    ensure  => file,
    content => "Ceci n'est pas une page\n"
}

# redirection & error page
$redirection = "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html;
        server_name _;
	    location / {
                try_files \$uri \$uri/ =404;
        }

        error_page 404 /404.html;
        location /404.html {
                root /var/www/html;
                internal;
        }

        location /redirect_me {
                return 301 https://google.com;
        }

}
"

# Handle redirection and error page
file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content => $redirection
}

# restart nginx
exec { 'service_restart':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}

# start nginx
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
