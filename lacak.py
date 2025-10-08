import requests
import folium
import os

def header():
    os.system("cls" if os.name == "nt" else "clear")
    print("="*70)   
    print("  ______    _                _     ______            _       _ _ ")
    print(" |  ____|  (_)              | |   |  ____|          | |     (_) | ")  
    print(" | |__ _ __ _  ___ _ __   __| |___| |__  __  ___ __ | | ___  _| |_ ") 
    print(" |  __| '__| |/ _ \\ '_ \\ / _` / __|  __| \\ \\/ / '_ \\| |/ _ \\| | __| ")
    print(" | |  | |  | |  __/ | | | (_| \\__ \\ |____ >  <| |_) | | (_) | | |_ ") 
    print(" |_|  |_|  |_|\\___|_| |_|\\__,_|___/______/_/\\_\\ .__/|_|\\___/|_|\\__| ")
    print("                                              | |  ")                
    print("                                              |_|  ")               
    print("               📡 FRIENDS EXPLOIT - Lacak Lokasi") 
    print("="*70)
    print()

def lacak_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] == "success":
            lat = data['lat']
            lon = data['lon']
            location_info = {
                "IP": data['query'],
                "Negara": data['country'],
                "Wilayah": data['regionName'],
                "Kota": data['city'],
                "Koordinat": f"{lat}, {lon}",
                "ISP": data['isp']
            }

            print("\n[✅] Informasi Lokasi:")
            for key, value in location_info.items():
                print(f"{key:10}: {value}")

            # Buat dan simpan peta
            lokasi_map = folium.Map(location=[lat, lon], zoom_start=12)
            folium.Marker(
                location=[lat, lon],
                popup=f"{data['city']}, {data['country']} ({ip})",
                tooltip="Lokasi Berdasarkan IP"
            ).add_to(lokasi_map)

            file_html = f"lokasi_{ip.replace('.', '_')}.html"
            lokasi_map.save(file_html)
            print(f"\n[💾] Peta disimpan sebagai: {file_html}")
            print("[ℹ️] Silakan buka file HTML tersebut secara manual di browser.")

        else:
            print("[❌] Gagal melacak IP. Status:", data["message"])

    except requests.exceptions.RequestException as e:
        print("[❌] Error koneksi:", e)

if __name__ == "__main__":
    header()
    target_ip = input("Masukkan IP Address: ")
    lacak_ip(target_ip)
