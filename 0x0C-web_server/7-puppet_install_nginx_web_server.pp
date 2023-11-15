# Puppet script to install and configure Nginx

# Ensure the Nginx package is present
package {'nginx':
  ensure => 'present',
}

# Execute command to install Nginx
exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

# Create a Hello World index page
exec {'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

# Add a configuration for redirection in the Nginx default site
exec {'configure_redirect':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.google.com\/\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
}

# Restart Nginx to apply changes
exec {'restart_nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}

