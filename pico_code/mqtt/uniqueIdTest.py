import machine
mqtt_client_id = machine.unique_id().hex()
print (mqtt_client_id + " uuid")
print(type(mqtt_client_id))