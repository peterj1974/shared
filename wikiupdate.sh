# Bash script to take input from option types and update wiki for instance.

TOKEN="<%=morpheus.apiAccessToken%>"
ID="<%=instance.id%>"
MORPHEUS="10.30.20.59"
LOCATION="<%=customOptions.location%>"
CONTACT="<%=customOptions.contactname%>"
EMEA="<%=customOptions.emeadept%>"
ASIAPAC="<%=customOptions.asiapacdept%>"
AMERICAS="<%=customOptions.americasdept%>"

if [[ ! -z $EMEA ]]
then 
	DEPT="<%=customOptions.emeadept%>"
elif [[ ! -z $ASIAPAC ]]
then 
    DEPT="<%=customOptions.asiapacdept%>"
elif [[ ! -z $AMERICAS ]]
then 
    DEPT="<%=customOptions.americasdept%>"
fi

curl -k -XPUT "https://$MORPHEUS/api/instances/$ID/wiki" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
  \"page\":{
    \"content\": \"**Instance Details**\r\n\r\nLocation: $LOCATION\r\nContact: $CONTACT\r\nDepartment: $DEPT\"
  }
}"
