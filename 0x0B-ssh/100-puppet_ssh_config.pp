# This manifest makes changes to our SSH Client config file

file {'/etc/ssh/sshd_config':
    ensure  => file,
    content => 'IdentityFile ~/.ssh/school\nPasswordAuthentication no\n',
    mode    => '0600'
}
