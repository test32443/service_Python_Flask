# service_Python_Flask
Sample RESTful service application using Python and Flask library

# Prerequisites installation and configuration
run prep.sh

# API
POST to /track/api/v1.0/domains/<url>   - Update counter for specific URL
GET from /track/api/v1.0/domains/top3   - return JSON document with top 3 domains
DEKETE ti /track/api/v1.0/domains/clear - Clean up counter values

# Sample invocations:
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.aa.com/ddd/ccc

curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ab.com/
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ab.com/1

curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ac.com/
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ac.com/a
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ac.com/b/b/b
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/http://www.ac.com/c/c/c

curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/https://www.ad.com/
curl -X POST http://127.0.0.1:5000/track/api/v1.0/domains/https://www.ad.com/


curl http://127.0.0.1:5000/track/api/v1.0/domains/top3

curl -X DELETE http://127.0.0.1:5000/track/api/v1.0/domains/clear
curl http://127.0.0.1:5000/track/api/v1.0/domains/top3
