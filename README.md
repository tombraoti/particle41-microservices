# mynginx
# Clone the github 

# Run Docker build command 
# Give your own reponame which you have in Docker Hub
docker build -t <yourreponame>/project:1.0.0 .
  
# Push the Docker Image to DockerHub
docker push <yourreponame>/project:1.0.0 .
  
# Replace <yourreponame> with you repo name in microservice.yaml file 
  
# Run kubernetes Deployment
Run Kubectl create -f microservice.yaml

  

  
