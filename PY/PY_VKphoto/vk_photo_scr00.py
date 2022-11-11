import requests, json, time, os

VK_USER_ID = 26170628
VK_TOKEN = "vk1.a.elzISGmpxuWHm-vd9YhJclAIRM9C2JdWdoUv-f-GpUWYoHi9kB6TRpoZU8lUh8qXYJTJ2A618yjzfVHK5ai-obctuqykLj1O53bTkzySWC8OmpU_O2yQGaRrnUamcFemimzpyn6_hbrYd3o7nJjtJ7_3JT1LkOGOo9Rf5YIuD0bc6jZE7NcMXjtGupO8-DYQ"

def get_foto_data(offset=0, count=50):
	api = requests.get("https://api.vk.com/method/photos.getAll", params={
		'owner_id': VK_USER_ID,
		'access_token': VK_TOKEN,
		'offset': offset,
		'count': count,
		'photo_sizes': 0,
        'no_service_albums' : 0,
       #'need_hidden' : 1,
		'v': 5.131
	})
	return json.loads(api.text)

def get_foto():
	data = get_foto_data()
	count_foto = data["response"]["count"]
	i = 0
	count = 50
	fotos = []
	while i <= count_foto:
		if i != 0:
			data = get_foto_data(offset=i, count=count)

		for files in data["response"]["items"]:
			file_url = files["sizes"][-1]["url"]
			filename = file_url.split("/")[-1]
			fotos.append(filename)
			time.sleep(0.02)
			api = requests.get(file_url)
			print(f'| {len(fotos)} | N :: {filename.split("/")[-1].split("?")[0]} | URL :: {file_url} |')
           
			with open("PY/PY_VKphoto/images/%s" % filename.split("/")[-1].split("?")[0], "wb") as file:
				file.write(api.content)
    
		#print(i)
        #print(i, filename.split("/")[-1].split("?")[0])
		i += count
	#print(len(fotos))

def main():
    print('')
    print('cwd :: ', os.getcwd())
    get_foto()

if __name__ == "__main__":
	main()