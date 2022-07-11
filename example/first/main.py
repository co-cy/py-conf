from config import FirstConfig

url = FirstConfig.url
# OR FirstConfig().get("url")
print(url)

dict_val = FirstConfig()
print(dict_val)
