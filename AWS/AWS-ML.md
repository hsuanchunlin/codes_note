# Amazon Web Services (AWS)
## Amazon SageMaker
**Tip**: Always terminate the resources you used in this lab. Terminating resources that are not actively being used **reduces costs and is a best practice**. Not terminating your resources will result in charges to your account.

### Procedure
- Delete your endpoint: In your Jupyter notebook, copy and paste the following code and choose Run.
```
xgb_predictor.delete_endpoint(delete_endpoint_config=True)
```
- **Delete your training artifacts and S3 bucket**: In your Jupyter notebook, copy and paste the following code and choose Run.

```python
bucket_to_delete = boto3.resource('s3').Bucket(bucket_name)
bucket_to_delete.objects.all().delete()
```
- Delete your SageMaker Notebook: Stop and delete your SageMaker Notebook.
1. Open the **SageMaker console**.
1. Under Notebooks, choose **Notebook instances**.
1. Choose the notebook instance that you created for this tutorial, then choose **Actions, Stop**. The notebook instance takes up to several minutes to stop. When Status changes to Stopped, move on to the next step.
1. Choose **Actions**, then **Delete**.
1. Choose **Delete**.

## Data management
### Create the S3 bucket to store your data

**Note**: Make sure to replace the bucket_name your-s3-bucket-name with a unique S3 bucket name. If you don't receive a success message after running the code, change the bucket name and try again.

```python
bucket_name = 'your-s3-bucket-name' # <--- CHANGE THIS VARIABLE TO A UNIQUE NAME FOR YOUR BUCKET
s3 = boto3.resource('s3')
try:
    if  my_region == 'us-east-1':
      s3.create_bucket(Bucket=bucket_name)
    else: 
      s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={ 'LocationConstraint': my_region })
    print('S3 bucket created successfully')
except Exception as e:
    print('S3 error: ',e)
```
### Download the data to your SageMaker instance and load the data into a dataframe.

```python
try:
  urllib.request.urlretrieve ("https://d1.awsstatic.com/tmt/build-train-deploy-machine-learning-model-sagemaker/bank_clean.27f01fbbdf43271788427f3682996ae29ceca05d.csv", "bank_clean.csv")
  print('Success: downloaded bank_clean.csv.')
except Exception as e:
  print('Data load error: ',e)

try:
  model_data = pd.read_csv('./bank_clean.csv',index_col=0)
  print('Success: Data loaded into dataframe.')
except Exception as e:
    print('Data load error: ',e)
```