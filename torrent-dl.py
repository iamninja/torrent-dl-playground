import sys
import time
import subprocess
import libtorrent as lt

magnetLink = "magnet:?xt=urn:btih:GAF3WUIXN3RNFA3VNYKRWT4PV5O6MEWX&tr=http://nyaa.tracker.wf:7777/announce&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://tracker.leechersparadise.org:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://p4p.arenabg.com:1337/announce&tr=udp://mgtracker.org:6969/announce&tr=udp://tracker.tiny-vps.com:6969/announce&tr=udp://peerfect.org:6969/announce&tr=http://share.camoe.cn:8080/announce&tr=http://t.nyaatracker.com:80/announce&tr=https://open.kickasstracker.com:443/announce"
params = {
    'save_path': './',
    'storage_mode': lt.storage_mode_t.storage_mode_allocate
}
# opened = False
ses = lt.session()

handle = lt.add_magnet_uri(ses, magnetLink, params)
lt.torrent_handle.set_sequential_download(handle, True)

print("Downloading metadata...")
while (not handle.has_metadata()): time.sleep(1)

print("Got metadata, starting downloading...")
while (handle.status().state != lt.torrent_status.seeding):
    # if (not opened and handle.status().progress*100 >= 5):
    #     subprocess.run(["mpv", "./" + handle.name()])
    #     opened = True
    print("%d %% done" % (handle.status().progress*100), end="\r", flush=True)
    time.sleep(1)


