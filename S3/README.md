# Using Amazon S3

Amazon S3 (Simple Storage Service) is a scalable object storage service. You can use it to store and retrieve any amount of data at any time.

## Using the AWS Console

### Creating a Bucket
1. Sign in to the AWS Management Console
2. Navigate to S3 from the Services menu
3. Click "Create bucket"
4. Enter a unique bucket name
5. Choose the AWS Region
6. Configure options (versioning, tags, encryption)
7. Set permissions (public access settings, bucket policies)
8. Click "Create bucket"

### Uploading Files
1. Open your bucket from the S3 console
2. Click "Upload" or drag & drop files
3. Select files from your computer
4. Set properties (storage class, encryption)
5. Set permissions
6. Review and click "Upload"

### Managing Files
1. **Download Files:**
   - Select the file(s)
   - Click "Download" or use "Actions" menu

2. **Delete Files:**
   - Select the file(s)
   - Click "Delete" or use "Actions" menu

3. **Share Files:**
   - Select the file
   - Click "Share" or generate a presigned URL
   - Set expiration time and permissions

### Managing Bucket Properties
- Enable/disable versioning
- Configure lifecycle rules
- Set up static website hosting
- Manage bucket policies
- Configure CORS

## Basic Operations with AWS CLI

For automation and scripting, you can also use the AWS CLI:

### List Buckets
```bash
aws s3 ls
```

### Create a Bucket
```bash
aws s3 mb s3://your-unique-bucket-name
```

### Upload/Download Files
```bash
# Upload
aws s3 cp my-local-file.txt s3://your-unique-bucket-name/

# Download
aws s3 cp s3://your-unique-bucket-name/my-remote-file.txt .
```

### Sync Directory
```bash
aws s3 sync my-local-directory/ s3://your-unique-bucket-name/
```

## Best Practices
1. Use appropriate bucket naming conventions
2. Enable versioning for important data
3. Set up lifecycle policies for cost optimization
4. Use appropriate security settings
5. Monitor bucket access and usage
