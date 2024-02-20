import http.client

conn = http.client.HTTPSConnection("ski-resorts-and-conditions.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "a659fcac33msh15fecc0322dca9ap1bd64djsnae21d6a0c44c",
    'X-RapidAPI-Host': "ski-resorts-and-conditions.p.rapidapi.com"
}

conn.request("GET", "/v1/resort/whistler-blackcomb", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))