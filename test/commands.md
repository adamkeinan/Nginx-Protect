# List All verified Endpoints
POST 
https://{{CONTROLLER_FQDN}}/api/v1/auth/verify

#  list of all Forwarder resources
GET
https://{{CONTROLLER_FQDN}}/api/v1/analytics/forwarders

# Get ongoing Alerts
GET
https://{{CONTROLLER_FQDN}}/api/v1/analytics/alerts/rules/{alertRuleName}/alerts

# Create a Policy
METHOD    PATH
POST      /security/policies

https://{{CONTROLLER_FQDN}}/api/v1/security/policies