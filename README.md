docker run -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /mnt/jenkins:/var/jenkins_home jenkins/jenkins:lts-jdk11
