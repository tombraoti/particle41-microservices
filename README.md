# mynginx
# Clone the github

# Run Docker build command
# Give your own reponame which you have in Docker Hub
docker build -t tombraoti/particle41:1.0.0 .

# Push the Docker Image to DockerHub
docker push tombraoti/particle41:1.0.0
   

# Run kubernetes Deployment
Run Kubectl create -f microservice.yaml
