# author : recehom
# github : https://github.com/recehom
# desc   : gk usah di recode ya zeyeng..

# import module
import requests, random, string, sys

# my function
def nama():
	l = string.ascii_lowercase
	return ''.join(random.choice(l) for i in range(5))

def daftar(r):
	t = random.randint(000000000000,999999999999)
	p = random.randint(0000,9999)
	n = nama()
	i = random.randint(0000000000000,9999999999999)
	a = 'Mars'
	d = f'telp={t}&pin={p}&nama={n}&referal={r}&imei={i}&alamat={a}'
	h = {
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi 4A Build/PQ3A.190505.002)',
		'Host': 'freerupiah.online',
		'Connection': 'Keep-Alive'
	}
	post = requests.post('http://freerupiah.online/api/register.php', headers=h, data=d)
	if 'BERHASIL' in post.text:
		return print(f'[!] Berhasil mengirim refferal ke {r}')
	else:
		return print(f'[!] Gagal mengirim refferal ke {r}')

if __name__=='__main__':    
    try:
        print('     -=[ bot rupiah app ]=-')
        print(' [ https://github.com/recehom ]\n')
        r = input('[?] Kode reff : ')
        l = input('[?] Limit     : ')
        if r != '' and l != '':
        	print('[!] Memulai Program...')
        	for i in range(int(l)):
        		daftar(r)

    except KeyboardInterrupt:
        print('[!] Program dihentikan...')
        sys.exit()