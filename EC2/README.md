# Cloud Computing Setup Instructions

This guide provides instructions for setting up a web server on an AWS EC2 instance.

## Connecting to Your EC2 Instance

1.  **Set Permissions for Your Key File:**
    Before you can use your `.pem` key file to connect to your EC2 instance, you need to set the correct permissions for it. This is a security measure to ensure that only you can read the file.

    ```bash
    chmod 400 "CloudComputing101.pem"
    ```

2.  **Connect via SSH:**
    Use the following command to connect to your EC2 instance using SSH (Secure Shell). You'll need to replace `<.pem file path>` with the actual path to your key file and `<public DNS>` with the public DNS of your instance.

    ```bash
    ssh -i "<.pem file path>" ubuntu@<public DNS>
    ```

    Here is an example with a sample key file and public DNS:
    ```bash
    ssh -i "CloudComputing101.pem" ubuntu@ec2-35-153-184-244.compute-1.amazonaws.com
    ```

## Setting Up the Web Server

Once you are connected to your instance, you can set up the Apache web server.

1.  **Update and Upgrade Packages:**
    It's good practice to update the package lists and upgrade the installed packages to their latest versions.

    ```bash
    sudo apt-get update && sudo apt-get upgrade -y
    ```

2.  **Install Apache:**
    Install the Apache HTTP Server.

    ```bash
    sudo apt install apache2
    ```

3.  **Navigate to the Web Root:**
    The default directory for website files on an Apache server is `/var/www/html`. You can navigate to it with the following command.

    ```bash
    cd /var/www/html
    ```