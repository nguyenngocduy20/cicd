python3 unit_test.py
VAR_CHECK=`python3 getResultUnittest.py`
if [ "$VAR_CHECK" = "true" ]
then
docker build -t gn1k/push-thesis-jenkins:v${BUILD_NUMBER} .
cd /home/jenkins
mkdir -p ./.docker
cd .docker
echo "{\n\t\"auths\": {\n\t\t\"https://index.docker.io/v1/\": {\n\t\t\t\"auth\": \"Z24xazpodWJkb2NrZXJfU2FsdF85QA==\"\n\t\t}\n\t}\n}" > config.json
docker tag gn1k/push-thesis-jenkins:v${BUILD_NUMBER} gn1k/push-thesis-jenkins:latest
docker push gn1k/push-thesis-jenkins:v${BUILD_NUMBER}
docker push gn1k/push-thesis-jenkins:latest
docker rmi gn1k/push-thesis-jenkins:latest
fi
