# AWS EC2 Setup Guide

This guide provides step-by-step instructions for setting up a web server on an AWS EC2 instance.

## Prerequisites
- AWS Account with EC2 access
- `.pem` key file for your EC2 instance
- SSH client (built into Linux/macOS, PuTTY for Windows)

## Setting Up Key File Permissions

### For Linux/macOS Users
```bash
chmod 400 "CloudComputing101.pem"
```

### For Windows Users
Run these commands in PowerShell:
```powershell
# Remove inherited permissions
icacls "CloudComputing101.pem" /inheritance:r

# Grant full control to your user account only
# Replace "YourUsername" with your Windows username
icacls "CloudComputing101.pem" /grant:r "YourUsername:F"

# Verify permissions
icacls "CloudComputing101.pem"
```

Note: Replace "YourUsername" with your actual Windows username (the one you see when you run `echo $env:USERNAME`)

## Configuring AWS Security Group

Before connecting to your instance, ensure your security group is properly configured:

1. **Open AWS Console and Navigate to EC2**
2. **Select Security Groups from the left sidebar**
3. **Select the security group associated with your instance**
4. **Add Inbound Rules:**
   - SSH (Port 22) - For remote access
   - HTTP (Port 80) - For web server access
   - HTTPS (Port 443) - If you plan to use SSL/TLS

## Connecting to Your EC2 Instance

1. **Get Your Instance's Public DNS**
   - Open AWS Console
   - Navigate to EC2 Dashboard
   - Select your instance
   - Copy the Public DNS (IPv4) address

2. **Connect via SSH**
   ```bash
   ssh -i "CloudComputing101.pem" ubuntu@<public-dns>
   ```
   Example:
   ```bash
   ssh -i "CloudComputing101.pem" ubuntu@ec2-35-153-184-244.compute-1.amazonaws.com
   ```

## Setting Up the Web Server

### 1. Update System Packages
```bash
sudo apt-get update && sudo apt-get upgrade -y
```

### 2. Install Apache Web Server
```bash
sudo apt install apache2
```

### 3. Verify Apache Installation
```bash
# Check Apache status
sudo systemctl status apache2

# Enable Apache to start on boot
sudo systemctl enable apache2
```

### 4. Configure Firewall (Optional)
```bash
# Allow Apache through firewall
sudo ufw allow 'Apache'

# Enable firewall
sudo ufw enable
```

### 5. Web Root Directory
The default web root is `/var/www/html/`. You can place your website files here:
```bash
cd /var/www/html
```

### 6. Verify Web Server Access
After setting up Apache:
1. Get your instance's public IP or DNS from AWS Console
2. Open a web browser and navigate to:
   ```
   http://<your-instance-public-dns>
   ```
   or
   ```
   http://<your-instance-public-ip>
   ```
3. You should see the default Apache welcome page

### 7. Deploy Your Website
To deploy your website:
```bash
# Clear default Apache page (optional)
sudo rm /var/www/html/index.html

# Copy your website files
sudo cp -r /path/to/your/website/* /var/www/html/

# Set proper permissions
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/
```

## Common Tasks

### View Apache Error Logs
```bash
sudo tail -f /var/log/apache2/error.log
```

### Restart Apache
```bash
sudo systemctl restart apache2
```

### Test Configuration
```bash
sudo apache2ctl configtest
```

## Troubleshooting

### Permission Denied Errors
If you see "Permission denied" when using the key file:
1. Check file permissions
2. Ensure key file is readable only by you
3. Run the permission commands from the setup section

### Connection Timed Out
1. Check Security Group settings in AWS Console
2. Ensure port 22 (SSH) is open in inbound rules
3. Verify instance is running

### Apache Not Starting
1. Check error logs
2. Verify ports aren't in use
3. Check configuration syntax

## Security Best Practices
1. Keep your `.pem` file secure and never share it
2. Use Security Groups to limit access
3. Regularly update system packages
4. Use strong passwords
5. Monitor instance logs

## Fixing PEM File Access Issues in Windows

When working with EC2 instances in Windows, you might encounter permission-related issues with your `.pem` file. Here's a detailed guide to fix these issues using PowerShell commands:

### 1. Remove Inherited Permissions
```powershell
icacls "CloudComputing101.pem" /inheritance:r
```
This command:
- Removes all inherited permissions from parent directories
- Keeps only explicitly set permissions
- Helps in setting up a clean permission state

### 2. Set Correct User Permissions
```powershell
icacls "CloudComputing101.pem" /grant:r "Aftab S:F"
```
This command:
- Grants Full control (F) to your user account only
- Uses `/grant:r` to replace all existing permissions
- Replace "Aftab S" with your actual Windows username
- The `:F` flag specifies full control permission

### 3. Verify Permissions
```powershell
icacls "CloudComputing101.pem"
```
This command:
- Displays current file permissions
- Use this to verify that only your user account has access
- Ensure no other users or groups have permissions

### Common Permission Issues
1. **Error: "Unprotected private key file"**
   - This occurs when the .pem file has too broad permissions
   - Follow the steps above to restrict access

2. **Error: "Bad permissions"**
   - Usually means multiple users have access to the key
   - Use the commands above to limit access to just your user

3. **Error: "Permission denied" during SSH**
   - Verify file ownership is correct
   - Double-check all permissions using the verify command
   - Ensure you're using the correct username in the grant command

## Additional Resources
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [Apache Documentation](https://httpd.apache.org/docs/)
- [Linux Security Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html)
- [Windows Security Permissions Guide](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/icacls)
