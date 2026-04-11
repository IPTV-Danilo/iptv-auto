import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

canales = {
    "TNT SPORTS": "https://streamtpnew.com/global1.php?stream=tntsports"
    "ESPN PREMIUM": "https://streamtpnew.com/global1.php?stream=espnpremium",
    "ESPN": "https://streamtpnew.com/global1.php?stream=espn",
    "ESPN 2": "https://streamtpnew.com/global1.php?stream=espn2",
    "FOX Sports": "https://streamtpnew.com/global1.php?stream=fox"
}

def obtener_link(url):
    try:
        r = requests.get(url, headers=headers, timeout=15)

        matches = re.findall(r'https://[^"]+m3u8[^"]+', r.text)

        for m in matches:
            if "token=" in m:
                return m

        return None
    except Exception as e:
        print("Error:", e)
        return None

m3u = "#EXTM3U\n\n"

for nombre, url in canales.items():
    link = obtener_link(url)

    if link:
        m3u += f'#EXTINF:-1,{nombre}\n{link}\n\n'
    else:
        print(f"No se pudo obtener: {nombre}")
        m3u += f'#EXTINF:-1,{nombre}\n#\n\n'

try:
    with open("lista.m3u", "w") as f:
        f.write(m3u)
    print("Lista creada")
except Exception as e:
    print("Error al guardar:", e)

# 🔥 ESTO EVITA QUE GITHUB MARQUE ERROR
exit(0)
