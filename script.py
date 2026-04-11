import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0"
}

# 🔴 CANALES (podés agregar más después)
canales = {
    "TNT SPORTS": "https://streamtpnew.com/global1.php?stream=tntsports"
    "ESPN PREMIUM": "https://streamtpnew.com/global1.php?stream=espnpremium",
    "ESPN": "https://streamtpnew.com/global1.php?stream=espn",
    "ESPN 2": "https://streamtpnew.com/global1.php?stream=espn2",
    "FOX Sports": "https://streamtpnew.com/global1.php?stream=fox"
    

def obtener_link(url):
    try:
        r = requests.get(url, headers=headers, timeout=10)
        match = re.search(r'https://.*?m3u8.*?token=.*?"', r.text)
        if match:
            return match.group(0).replace('"', '')
    except:
        return None

m3u = "#EXTM3U\n\n"

for nombre, url in canales.items():
    link = obtener_link(url)
    if link:
        m3u += f'#EXTINF:-1,{nombre}\n{link}\n\n'
    else:
        print(f"No se pudo obtener: {nombre}")

with open("lista.m3u", "w") as f:
    f.write(m3u)

print("Lista actualizada")
