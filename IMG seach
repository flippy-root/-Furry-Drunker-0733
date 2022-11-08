import string, random, os, sys, _thread, httplib2, time
thread_count = int(input('Input thread count: '))

bad_pick = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556, 6167]#constat

path = os.getcwd()
try:
	os.mkdir(f'{path}/picture')
except:
	os.chdir(f'{path}/picture') 




def scraper(thread):#scraper main

	while True:
	    url = 'http://i.imgur.com/'#full url to imgur.com
	    length = random.choice((5, 6))#code lenght
	    if length == 5:
	        url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
	    else:#code numbers
	        url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
	        url += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
	        url += '.jpg'

	        filename = url.rsplit('/', 1)[-1]#create file name without url path

	        h = httplib2.Http('.cache' + thread)
	        response, content = h.request(url)
	        out = open(filename, 'wb')
	        out.write(content)
	        out.close()

	        file_size = os.path.getsize(filename)
	        if file_size in bad_pick:#delete blocked pic
	            print("[-] " + url)
	            os.remove(filename)
	        else:
	            print("[+] " + url)
#discords server:https://discord.gg/5zRq8kux96
for thread in range(1, thread_count + 1):#start thread
    thread = str(thread)
    try:
        _thread.start_new_thread(scraper, (thread,))
    except:
        print(f'Can not start: {thread} thread')
print('Launch: ' + thread + ' threads.')

while True:
    time.sleep(1)
