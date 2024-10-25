import asyncio
from torrentp import TorrentDownloader

torrent_file = "breaking_bad.torrent"
download_folder = "./downloads"

new_torrent = TorrentDownloader(torrent_file, download_folder)

asyncio.run(new_torrent.start_download())