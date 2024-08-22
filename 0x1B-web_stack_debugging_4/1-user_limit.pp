# This script enables the user holberton to login and open files without any errors

# Increase hard file limit for user holberton
exec { 'update-hard-file-limit-for-holberton-users':
    command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'update-soft-file-limit-for-holberton-user':
    command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
    path    => '/usr/local/bin/:/bin/'
}
