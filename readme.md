## AWS S3 file Uploader

This Python script uploads a local image file to an Amazon S3 bucket.

**Requirements:**

* Python 3.x
* boto3 library (install with `pip install boto3`)
* AWS account with S3 access

**Instructions:**

1. **Create an S3 Bucket:**
    * Log in to the AWS Management Console.
    * Go to the S3 service.
    * Click on "Create bucket".
    * Enter a bucket name (e.g., `eagleimagebucket`). Choose a unique name.
    * Select a region (e.g., `us-east-2`).
    * Click "Create".
2. **Create an IAM Policy:**
    * Go to the IAM service.
    * Click on "Policies".
    * Click on "Create policy".
    * Select "JSON" as the policy editor.
    * Paste the following policy document into the editor (replace `eagleimagebucket` with your bucket name):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowUploadToEagleImageBucket",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::eagleimagebucket/*",
        "arn:aws:s3:::eagleimagebucket"
      ]
    }
  ]
}
```

    * Click "Review" and then "Create policy".
3. **Create an IAM User:**
    * Go to the IAM service.
    * Click on "Users".
    * Click on "Add user".
    * Enter a user name (e.g., `eagleimagebucketuser`).
    * Select "Programmatic access".
    * Click on "Next: Permissions".
    * On the "Attach existing policies directly" section, search for and select the policy you created in step 2.
    * Click on "Next: Review".
    * Review the details and click "Create user".
    * Download the `.csv` file containing the access key and secret access key. This is the only time these keys will be displayed. Keep them secure!

4. **Configure Environment Variables:**
    * **Do not store access keys directly in your code!** 
    * Instead, set environment variables for the access key and secret access key. The script will read these variables.
    * Instructions for setting environment variables differ depending on your operating system. Refer to the official AWS documentation for your specific OS. Here are some general guidelines:
        * **Windows:** Open Command Prompt as administrator and run `setx AWS_ACCESS_KEY_ID your_access_key` and `setx AWS_SECRET_ACCESS_KEY your_secret_access_key`.
        * **Mac/Linux:** Open your terminal and run `export AWS_ACCESS_KEY_ID=your_access_key` and `export AWS_SECRET_ACCESS_KEY=your_secret_access_key`.
        * Replace `your_access_key` and `your_secret_access_key` with the actual values from your downloaded credentials file.

5. **Update Script (Optional):**
    * The script uses environment variables by default. You can optionally modify the code to specify the bucket name and region directly, but this is not recommended for security reasons.
    * If you choose to modify the code, update the `AWS_S3_BUCKET_NAME` and `AWS_REGION` variables at the beginning of the script with your desired values.

6. **Run the Script:**
    * Make sure you have a local image file named `eaglesoaring.jpg` in the same directory as the script.
    * Open a terminal or command prompt and navigate to the directory containing the script.
    * Run the script with `python upload_file_to_s3.py`.

The script will attempt to upload the image to your S3 bucket. If successful, a message will be logged indicating the upload response.

**Additional Notes:**

* This script uses basic error handling. More comprehensive error handling can be implemented for production use. 
* Consider using a configuration file to store your AWS credentials instead of environment variables for better maintainability. 
* This script grants the IAM user full access (put and get) to the S3 bucket. You may want to refine the policy document to restrict access based on your specific needs.


**Security:**

* **Never store your access key and secret access key directly in your code.** Use environment variables or IAM roles for a more secure