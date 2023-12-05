from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.s3_to_local_operator import S3ToLocaFileSystemOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'seismic_data_dag',
    default_args=default_args,
    description='DAG for downloading seismic data from S3',
    schedule_interval=timedelta(days=1),
)

# S3 bucket and prefix where seismic data is stored
s3_bucket = 'my-test-bucket'
s3_prefix = 'your-s3-prefix'

# Local directory to store downloaded files
local_dir = '/path/to/local/directory'

# Download 12 files
for i in range(1, 13):
    task_id = f'download_file_{i}'
    s3_key = f'{s3_prefix}/seismic_data_{i}.csv'

    # Download file from S3 to local filesystem
    download_task = S3ToLocaFileSystemOperator(
        task_id=task_id,
        aws_conn_id='aws_default',
        bucket_name=s3_bucket,
        object_name=s3_key,
        local_file=local_dir,
        replace=True,
        dag=dag,
    )

    # You can perform any additional processing here if needed

    # Bash operator to print a message indicating successful download
    success_message = f"echo 'Seismic data file {i} downloaded successfully'"
    success_task = BashOperator(
        task_id=f'success_message_{i}',
        bash_command=success_message,
        dag=dag,
    )

    # Set up dependencies between tasks
    download_task >> success_task

# You can define additional tasks and dependencies as needed