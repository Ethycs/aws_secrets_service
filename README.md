[Windows]
Running `sam local start-api` with `-p <number>` instead of 3000 use another number
may work if you attempt to run the local api server and encounter a socket error

1. Create or use role that allows R/W with Secrets Manager and allows LambdaExecution
This allows use to bundle permissions
2. Create User Group that allows basic resources of the previous role
3. Attach a json policy that allows the users in the group to assume the created role see below:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
                "AWS": "arn:aws:iam::068155203304:user/secrets-manager-dev"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

4. Create a user and then create an access key (note that the IAM Identity Center was unavailable at the time)
5. Add a trust policy to the role

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::068155203304:user/secrets-manager-dev"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

6. We use `aws sts assume-role --role-arn arn:aws:iam::068155203304:role/Secrets_manager_lambda --role-session-name DebugSession`
and then
```PS
$env:AWS_ACCESS_KEY_ID="<your-access-key>"
$env:AWS_SECRET_ACCESS_KEY="<your-secret-access-key>"
$env:AWS_SESSION_TOKEN="<your-session-token>" # If you're using temporary security credentials

sam local start-api

```

Make sure you delete the session token and reauth your developer key with `Remove-Item Env:AWS_SESSION_TOKEN `, if your sts session keys expire you will have to remove them and reuth to get new ones


We now take the following steps

AWS Management Console (Add layer option)
Open the AWS Lambda console at https://console.aws.amazon.com/lambda/.

Choose your function. In the Layers area, choose Add a layer.

In the Choose a layer area, choose the AWS layers option.

For AWS layers, choose AWS-Parameters-and-Secrets-Lambda-Extension, choose a version, and then choose Add.

https://docs.aws.amazon.com/systems-manager/latest/userguide/ps-integration-lambda-extensions.html
See the end of this article for the AWS Parameters and Secrets Lambda Extension ARNs