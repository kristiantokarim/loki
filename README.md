Simple HTTP mock service with cerberus validators
Allowed validator can be found at http://docs.python-cerberus.org/en/stable/validation-rules.html

POST to /inject
```
{
  "url": "/<END POINT>",
  "request": <CAN BE SCHEMA>,
  "response": <EXPECTED RESPONSE>
}
```
example :
POST to /inject
```
{
  "url": "/myendpoint",
  "request": {
    "req attribute": {
      "type": "integer"
    }
  },
  "response": {
    "resp attribute": "my expected response"
  }
}
```

next time you post to /myendpoint with 
```
{
  "req attribute" : 1
}
```
it will return
```
{
  "resp attribute": "my expected response"
}
```
