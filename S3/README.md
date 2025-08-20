# Using Amazon S3

Amazon S3 (Simple Storage Service) is a scalable object storage service. You can use it to store and retrieve any amount of data at any time.

## Basic Operations with AWS CLI

Here are some basic commands to interact with S3 using the AWS Command Line Interface (CLI).

### List Buckets

To list all of your S3 buckets:

```bash
aws s3 ls
```

### Create a Bucket

To create a new bucket, you need to provide a unique bucket name.

```bash
aws s3 mb s3://your-unique-bucket-name
```

**Note:** Bucket names must be globally unique.

### Upload a File

To upload a file to a bucket:

```bash
aws s3 cp my-local-file.txt s3://your-unique-bucket-name/
```

### Download a File

To download a file from a bucket:

```bash
aws s3 cp s3://your-unique-bucket-name/my-remote-file.txt .
```

### Sync a Directory

To synchronize a local directory with a bucket:

```bash
aws s3 sync my-local-directory/ s3://your-unique-bucket-name/
```
