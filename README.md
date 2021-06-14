# Nginx-Protect
Nginx-DDoS controller Protect mechanism

## NGINX Controller REST API Prerequisites
Perquisites for Setting up NGINX Controller and NGINX App Protect 
### NGINX Controller REST API version=v3.16+	
### NGINX App Protect version=>v2.1.1

### Linux 
Debian 9
Ubuntu 18.04 LTS, Ubuntu 20.04 LTS

### Docker Requirements.
Docker Community Edition (CE) => 18.09.
Containerd.io => 1.2.10

### Appending Trial License

### First, you need to sign up for a trial license for NGINX Controller.
https://docs.nginx.com/nginx-controller/admin-guides/install/try-nginx-controller-app-sec/

### Download the NGINX Controller installer package from the MyF5 Customer Portal
https://my.f5.com/manage/s/downloads

## Extract & Install  package files
Run the installation script:

$ cd controller-installer
$ ./install.sh

## Important: Add the NGINX App Protect Instance to NGINX Controller
Add your new Instance by selecting "Add an existing instance"

NGINX Controller 3.6 and earlier require Python 2.6 or 2.7. You’ll be prompted to install Python 

## Start Up Nginx
$ /opt/nginx-controller/helper.sh controller start

### Back up the Controller Agent agent.conf
cp /etc/controller-agent/agent.conf <temporary location>
### Login and capture the session cookie:

$ curl -c cookie.txt -X POST --url 'https://198.51.100.10/api/v1/platform/login' --header 'Content-Type: application/json' --data '{"credentials": {"type": "BASIC","username": "arthur@arthurdent.net","password": "Towel$123"}}'
# Nginx-Splunk
The new Splunk Docker image contains logic that allows your default.yml and license files to be centrally served via url.

#### Assuming you have pulled splunk:latest successfully, you can navigate to the nginx-data-www folder and use the following command to generate a sample default.yml

$ docker run splunk/splunk:latest create-defaults > ./default.yml

#### Once you have generated your default.yaml and inserted your license XML into the mySplunkLicense.lic file, it should look something like this:

$ cd nginx-data-www/
ls -la
#### hen, from the nginx directory create your configmaps:
$ kubectl -n splunk create configmap nginx-data-www --from-file=nginx-data-www

#### Then create one for the sample nginx conf file:
$ kubectl -n splunk create configmap nginx-config --from-file=nginx-static.conf

#### The deploy the nginx controllers:
$ kubectl -n splunk apply -f controllers

### Kubernetes 
Use kubectl -n splunk logs -f <podname> to watch for the Ansible plays to finish

show pods in the splunk name space with wide output - kubectl -n splunk get pods -o wide
# Quickstart
Start a single containerized instance of Splunk Enterprise with the command below, replacing <password> with a password string that conforms to the Splunk Enterprise password requirements.

$ docker run -p 8000:8000 -e "SPLUNK_PASSWORD=<password>" \
             -e "SPLUNK_START_ARGS=--accept-license" \
             -it --name so1 splunk/splunk:latest
## To enter the container and run Splunk CLI commands, run:
### Defaults to the user "ansible"
$ docker exec -it so1 /bin/bash
### Run shell as the user "splunk"
$ docker exec -u splunk -it so1 bash             

### Execute the following to bring up your deployment:
$ docker run --name so1 --hostname so1 -p 8000:8000 \
              -e "SPLUNK_PASSWORD=<password>" \
              -e "SPLUNK_START_ARGS=--accept-license" \
              -it splunk/splunk:latest

### Create standalone and universal forwarder
Execute the following to bring up your deployment:

$ SPLUNK_PASSWORD=<password> docker-compose up -d 

And Then:

$ openssl req -x509 -newkey rsa:4096 -passout pass:abcd1234 -keyout /home/key.pem -out /home/cert.pem  -days 365 -subj /CN=localhost

Once you have your certificates available, you can execute the following to bring up your deployment with SSL enabled on the Splunk Web UI:

$ docker run --name so1 --hostname so1 -p 8000:8000 \
              -e "SPLUNK_HTTP_ENABLESSL=true" \
              -e "SPLUNK_HTTP_ENABLESSL_CERT=/home/cert.pem" \
              -e "SPLUNK_HTTP_ENABLESSL_PRIVKEY=/home/key.pem" \
              -e "SPLUNK_HTTP_ENABLESSL_PRIVKEY_PASSWORD=abcd1234" \
              -e "SPLUNK_PASSWORD=<password>" \
              -e "SPLUNK_START_ARGS=--accept-license" \
              -v /home:/home \
              -it splunk/splunk:latest