
## STEPS TO EXECUTE JENKINS JOB

# STEPS 1:

	1. docker run -d \
	  --name investor \
	  --privileged \
	  --user root \
	  -p 8080:8080 \
	  -p 50000:50000 \
	  -v jenkins_home:/var/jenkins_home \
	  -v /var/run/docker.sock:/var/run/docker.sock \
	  jenkins/jenkins:lts

	2. docker exec -it investor bash

	3. 
	- apt-get update
	- apt-get install -y docker.io

	4. run
	- docker version
	- docker ps

	5. exit ==> shell

	6. Jenkins → Manage Jenkins → Script Console
	- println "docker version".execute().text
	- println "docker ps".execute().text

# STEP 2: Install plugins
	- Pipeline
	- Docker Pipeline
	- Docker
	- Allure Jenkins Plugin
	  
	Configure Allure: Go to Manage Jenkins → Global Tool Configuration(Tool):

		- Scroll to Allure Commandline
		- Click Add Allure Commandline
		- Name: allure
		- Check Install automatically
		- Save

# STEP 3: set up jenkins job

	1. New item
	2. Enter item name: playwright-pytest-pipeline
	3. Choose pipeline
	4. Ok
	5. Go to pipeline script
	6. Select pipeline script from SCM 
	7. SCM -Git
	8. Repository URL: https://github.com/qascenarios/automationexercise-ii.git
	9. Branch Specifier: main
	10. Apply & Save
	11. Build now