# flask-lamba-starwars-quotes


### A little playground for flask and lambda, using the best thing ever Starwars quotes!

## Dependencies
1. Amazon AWS account
* https://aws.amazon.com
2. AWS access key pair
* https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
3. python 3.6, yes not ideal but zappa does not support 3.7 yet 
* https://www.python.org/downloads/release/python-368/
* https://github.com/Miserlou/Zappa/pull/1762
4. awscli configured env
* https://aws.amazon.com/cli
* Install and configure 
```console 
$ pip3 install awscli
$ awscli configure
``` 
5. virtualenv
```console
$ pip3 install virtualenv
```
6.clone the repo 
```console 
$ git clone https://github.com/jassinpain/flask-lambda-starwars-quotes.git
```
7. cd into cloned repo 
```console
$ cd flask-lambda-starwars-quotes
```
8.create a python 3.6 virtual env
```console
$ virtualenv . -p python3.6
```
9. Activate the virtual env, the prompt will change to show the virtual env name
```console
[jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ . ./bin/activate
(flask-lambda-starwars-quotes)
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$
```
10. Install the python modules needed
```console
pip install -r requirements.txt
```
11. Test locally, set the FLASK_APP env varible
```console
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ cd flask-lambda/
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ export FLASK_APP=flask-lambda.py
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ flask run
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
 12. Run curl against th url above in a new terminal window a few times to make sure it working as expected, looks like we could use a better seed as it defaults to server time
 ```console
 [jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"Never tell me the odds"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"Never tell me the odds"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"It's not my fault"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"It's not my fault"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"It's not my fault"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Leia","text":"Help me, Obi-Wan Kenobi"}
[jmiller@thecrypt ~]$ curl http://127.0.0.1:5000
{"author":"Han Solo","text":"Never tell me the odds"}
[jmiller@thecrypt ~]$
```
13. CTRL-C to exit out of the running flask process
14. From your activated virtual env console initialize zappa, I removed some of the output but basicly I just accepted all the defaults. I might be more useful to set your bucket name to something that is meaningful for your. For example: zappa-jmiller-flask-lambda
```console
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda (master)]$ cd ..
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ zappa init

...

Welcome to Zappa!

Zappa is a system for running server-less Python web applications on AWS Lambda and AWS API Gateway.
This `init` command will help you create and configure your new Zappa deployment.
Let's get started!

Your Zappa configuration can support multiple production stages, like 'dev', 'staging', and 'production'.
What do you want to call this environment (default 'dev'):

AWS Lambda and API Gateway are only available in certain regions. Let's check to make sure you have a profile set up in one that will work.
Okay, using profile default!

Your Zappa deployments will need to be uploaded to a private S3 bucket.
If you don't have a bucket yet, we'll create one for you too.
What do you want to call your bucket? (default 'zappa-tdytn3rhu'):

It looks like this is a Flask application.
What's the modular path to your app's function?
This will likely be something like 'your_module.app'.
We discovered: flask-lambda.flask-lambda.app
Where is your app's function? (default 'flask-lambda.flask-lambda.app'):

You can optionally deploy to all available regions in order to provide fast global service.
If you are using Zappa for the first time, you probably don't want to do this!
Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]: y

Okay, here's your zappa_settings.json:

...

Does this look okay? (default 'y') [y/n]: y

Done! You can also deploy all by executing:

	$ zappa deploy --all

After that, you can update your application code with:

	$ zappa update --all

To learn more, check out our project page on GitHub here: https://github.com/Miserlou/Zappa
and stop by our Slack channel here: https://slack.zappa.io

Enjoy!,
 ~ Team Zappa!
(flask-lambda-s
```
15. Deploy your lambda function to AWS (FYI this may incure cost as in $$$$$, simple testing should be fine but clean up once your done. 
* https://aws.amazon.com/lambda/pricing/
```console
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ zappa deploy dev
Calling deploy for stage dev..
Warning! Your project and virtualenv have the same name! You may want to re-create your venv with a new name, or explicitly define a 'project_name', as this may cause errors.
Downloading and installing dependencies..
 - markupsafe==1.1.0: Using locally cached manylinux wheel
 - sqlite==python36: Using precompiled lambda package
Packaging project as zip.
Uploading flask-lambda-st-dev-1550644486.zip (28.0MiB)..
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 29.4M/29.4M [00:13<00:00, 1.80MB/s]
Scheduling..
Scheduled flask-lambda-st-dev-zappa-keep-warm-handler.keep_warm_callback with expression rate(4 minutes)!
Uploading flask-lambda-st-dev-template-1550644517.json (1.6KiB)..
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1.64K/1.64K [00:00<00:00, 9.28KB/s]
Waiting for stack flask-lambda-st-dev to create (this can take a bit)..
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:13<00:00,  4.54s/res]
Deploying API Gateway..
Deployment complete!: https://youh18dyh6.execute-api.us-west-2.amazonaws.com/dev
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$
```
16. Lets test our new aws lambda app using the url provided in step 15
```console
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ curl https://youh18dyh6.execute-api.us-west-2.amazonaws.com/dev
{"author":"Han Solo","text":"It's not my fault"}
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ curl https://youh18dyh6.execute-api.us-west-2.amazonaws.com/dev
{"author":"Leia","text":"Help me, Obi-Wan Kenobi"}
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ curl https://youh18dyh6.execute-api.us-west-2.amazonaws.com/dev
{"author":"Leia","text":"Help me, Obi-Wan Kenobi"}
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ curl https://youh18dyh6.execute-api.us-west-2.amazonaws.com/dev
{"author":"Darth Vader","text":"I find your lack of faith disturbing."}
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$
```
17. Good deal it worked, now clean up so you dont wake up to a $1000.00 aws bill
```console
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$ zappa undeploy dev
Calling undeploy for stage dev..
Are you sure you want to undeploy? [y/n] y
Deleting API Gateway..
Waiting for stack flask-lambda-st-dev to be deleted..
Unscheduling..
Unscheduled flask-lambda-st-dev-zappa-keep-warm-handler.keep_warm_callback.
Deleting Lambda function..
Done!
(flask-lambda-starwars-quotes) [jmiller@thecrypt flask-lambda-starwars-quotes (master)]$
```
18. my awscli default region is us-west-2 so I can view the console and make verify the lambda function is cleaned up
https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/home

