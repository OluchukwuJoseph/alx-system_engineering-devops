# This script installs flask

package {'/usr/bin/pip3':
    ensure => present
}

exec {'flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
    path    => ['/usr/bin', '/bin'],
    require => Package['usr/bin/pip3']
}
