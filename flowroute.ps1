# PowerShell script to send SMS via Flowroute API
# https://developer.flowroute.com/api/messages/v2.1/send-an-sms/

$username  = ''
$password = ''

$pair = "$($username):$($password)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))
$basicAuthValue = "Basic $encodedCreds"

$Headers = @{
    Authorization = $basicAuthValue
	'Content-Type' = 'application/json'
}

$url = "https://api.flowroute.com/v2/messages"
$url = $url + "?&start_date=2019-11-20"

$body = @{
	"to" = "+1"
	"from" = "+1"
	"body" = $args[0]
}


$request = Invoke-WebRequest -Uri $url -Headers $Headers -Method POST -Body $body
$request = $request | convertfrom-json
$request = $request.data.attributes