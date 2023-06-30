import re
import subprocess

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE
creationflags = subprocess.CREATE_NO_WINDOW
invisibledict = {
    "startupinfo": startupinfo,
    "creationflags": creationflags,
    "start_new_session": True,
}


def get_all_devices(ffmpegexe: str) -> dict:
    r"""
        Retrieves information about all available video and audio devices using FFmpeg.

        Args:
            ffmpegexe (str): The path to the FFmpeg executable.

        Returns:
            dict: A dictionary containing information about all available devices.
                  The dictionary has two keys: "video" and "audio".
                  The value of each key is another dictionary with all device infos

        Example:
            from pprint import pprint as pp
            from ffmpegdevices import get_all_devices
            ffmpegexe = r"C:\ffmpeg\ffmpeg.exe"
            devices = get_all_devices(ffmpegexe)
            pp(devices)

    {'audio': {0: {'alternative_name': '@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\\wave_{70C2267E-6685-4496-B3E7-23FAA519FC58}',
                   'name': 'Krisp Microphone (Krisp Audio)',
                   'options': {0: {'bits': 16, 'ch': 2, 'rate': 44100},
                               1: {'bits': 16, 'ch': 1, 'rate': 44100},
                               2: {'bits': 16, 'ch': 2, 'rate': 32000},
                               3: {'bits': 16, 'ch': 1, 'rate': 32000},
                               4: {'bits': 16, 'ch': 2, 'rate': 22050},
                               5: {'bits': 16, 'ch': 1, 'rate': 22050},
                               6: {'bits': 16, 'ch': 2, 'rate': 11025},
                               7: {'bits': 16, 'ch': 1, 'rate': 11025},
                               8: {'bits': 16, 'ch': 2, 'rate': 8000},
                               9: {'bits': 16, 'ch': 1, 'rate': 8000},
                               10: {'bits': 8, 'ch': 2, 'rate': 44100},
                               11: {'bits': 8, 'ch': 1, 'rate': 44100},
                               12: {'bits': 8, 'ch': 2, 'rate': 22050},
                               13: {'bits': 8, 'ch': 1, 'rate': 22050},
                               14: {'bits': 8, 'ch': 2, 'rate': 11025},
                               15: {'bits': 8, 'ch': 1, 'rate': 11025},
                               16: {'bits': 8, 'ch': 2, 'rate': 8000},
                               17: {'bits': 8, 'ch': 1, 'rate': 8000},
                               18: {'bits': 16, 'ch': 2, 'rate': 48000},
                               19: {'bits': 16, 'ch': 1, 'rate': 48000},
                               20: {'bits': 16, 'ch': 2, 'rate': 96000},
                               21: {'bits': 16, 'ch': 1, 'rate': 96000}}},
               1: {'alternative_name': '@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\\wave_{FC0D8211-5530-4CC1-8B8D-14AC7C65BED9}',
                   'name': 'Microphone (2- USB Advanced Audio Device)',
                   'options': {0: {'bits': 16, 'ch': 2, 'rate': 44100},
                               1: {'bits': 16, 'ch': 1, 'rate': 44100},
                               2: {'bits': 16, 'ch': 2, 'rate': 32000},
                               3: {'bits': 16, 'ch': 1, 'rate': 32000},
                               4: {'bits': 16, 'ch': 2, 'rate': 22050},
                               5: {'bits': 16, 'ch': 1, 'rate': 22050},
                               6: {'bits': 16, 'ch': 2, 'rate': 11025},
                               7: {'bits': 16, 'ch': 1, 'rate': 11025},
                               8: {'bits': 16, 'ch': 2, 'rate': 8000},
                               9: {'bits': 16, 'ch': 1, 'rate': 8000},
                               10: {'bits': 8, 'ch': 2, 'rate': 44100},
                               11: {'bits': 8, 'ch': 1, 'rate': 44100},
                               12: {'bits': 8, 'ch': 2, 'rate': 22050},
                               13: {'bits': 8, 'ch': 1, 'rate': 22050},
                               14: {'bits': 8, 'ch': 2, 'rate': 11025},
                               15: {'bits': 8, 'ch': 1, 'rate': 11025},
                               16: {'bits': 8, 'ch': 2, 'rate': 8000},
                               17: {'bits': 8, 'ch': 1, 'rate': 8000},
                               18: {'bits': 16, 'ch': 2, 'rate': 48000},
                               19: {'bits': 16, 'ch': 1, 'rate': 48000},
                               20: {'bits': 16, 'ch': 2, 'rate': 96000},
                               21: {'bits': 16, 'ch': 1, 'rate': 96000}}}},
     'video': {0: {'alternative_name': '@device_pnp_\\\\?\\usb#vid_046d&pid_0892&mi_00#8&222f6f15&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global',
                   'name': 'HD Pro Webcam C920',
                   'options': {0: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '640x480',
                                   'min_s': '640x480',
                                   'pixel_format': 'yuyv422'},
                               1: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '160x90',
                                   'min_s': '160x90',
                                   'pixel_format': 'yuyv422'},
                               2: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '160x120',
                                   'min_s': '160x120',
                                   'pixel_format': 'yuyv422'},
                               3: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '176x144',
                                   'min_s': '176x144',
                                   'pixel_format': 'yuyv422'},
                               4: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '320x180',
                                   'min_s': '320x180',
                                   'pixel_format': 'yuyv422'},
                               5: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '320x240',
                                   'min_s': '320x240',
                                   'pixel_format': 'yuyv422'},
                               6: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '352x288',
                                   'min_s': '352x288',
                                   'pixel_format': 'yuyv422'},
                               7: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '432x240',
                                   'min_s': '432x240',
                                   'pixel_format': 'yuyv422'},
                               8: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '640x360',
                                   'min_s': '640x360',
                                   'pixel_format': 'yuyv422'},
                               9: {'fps': 30,
                                   'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                   'max_s': '800x448',
                                   'min_s': '800x448',
                                   'pixel_format': 'yuyv422'},
                               10: {'fps': 24,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '800x600',
                                    'min_s': '800x600',
                                    'pixel_format': 'yuyv422'},
                               11: {'fps': 24,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '864x480',
                                    'min_s': '864x480',
                                    'pixel_format': 'yuyv422'},
                               12: {'fps': 15,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '960x720',
                                    'min_s': '960x720',
                                    'pixel_format': 'yuyv422'},
                               13: {'fps': 15,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '1024x576',
                                    'min_s': '1024x576',
                                    'pixel_format': 'yuyv422'},
                               14: {'fps': 10,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '1280x720',
                                    'min_s': '1280x720',
                                    'pixel_format': 'yuyv422'},
                               15: {'fps': 7.5,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '1600x896',
                                    'min_s': '1600x896',
                                    'pixel_format': 'yuyv422'},
                               16: {'fps': 5,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '1920x1080',
                                    'min_s': '1920x1080',
                                    'pixel_format': 'yuyv422'},
                               17: {'fps': 2,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '2304x1296',
                                    'min_s': '2304x1296',
                                    'pixel_format': 'yuyv422'},
                               18: {'fps': 2,
                                    'info': '(tv, bt470bg/bt709/unknown, topleft)',
                                    'max_s': '2304x1536',
                                    'min_s': '2304x1536',
                                    'pixel_format': 'yuyv422'},
                               19: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '640x480',
                                    'min_s': '640x480',
                                    'vcodec': 'mjpeg'},
                               20: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '160x90',
                                    'min_s': '160x90',
                                    'vcodec': 'mjpeg'},
                               21: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '160x120',
                                    'min_s': '160x120',
                                    'vcodec': 'mjpeg'},
                               22: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '176x144',
                                    'min_s': '176x144',
                                    'vcodec': 'mjpeg'},
                               23: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '320x180',
                                    'min_s': '320x180',
                                    'vcodec': 'mjpeg'},
                               24: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '320x240',
                                    'min_s': '320x240',
                                    'vcodec': 'mjpeg'},
                               25: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '352x288',
                                    'min_s': '352x288',
                                    'vcodec': 'mjpeg'},
                               26: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '432x240',
                                    'min_s': '432x240',
                                    'vcodec': 'mjpeg'},
                               27: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '640x360',
                                    'min_s': '640x360',
                                    'vcodec': 'mjpeg'},
                               28: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '800x448',
                                    'min_s': '800x448',
                                    'vcodec': 'mjpeg'},
                               29: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '800x600',
                                    'min_s': '800x600',
                                    'vcodec': 'mjpeg'},
                               30: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '864x480',
                                    'min_s': '864x480',
                                    'vcodec': 'mjpeg'},
                               31: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '960x720',
                                    'min_s': '960x720',
                                    'vcodec': 'mjpeg'},
                               32: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '1024x576',
                                    'min_s': '1024x576',
                                    'vcodec': 'mjpeg'},
                               33: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '1280x720',
                                    'min_s': '1280x720',
                                    'vcodec': 'mjpeg'},
                               34: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '1600x896',
                                    'min_s': '1600x896',
                                    'vcodec': 'mjpeg'},
                               35: {'fps': 30,
                                    'info': '(pc, bt470bg/bt709/unknown, center)',
                                    'max_s': '1920x1080',
                                    'min_s': '1920x1080',
                                    'vcodec': 'mjpeg'}}},
               1: {'alternative_name': '@device_sw_{860BB310-5D01-11D0-BD3B-00A0C911CE86}\\{4A2FEA90-B0A0-438E-8BC3-D84157660D0A}',
                   'name': 'Logi Capture',
                   'options': {}},
               2: {'alternative_name': '@device_sw_{860BB310-5D01-11D0-BD3B-00A0C911CE86}\\{A3FCE0F5-3493-419F-958A-ABA1250EC20B}',
                   'name': 'OBS Virtual Camera',
                   'options': {}}}}

    """
    p = subprocess.run(
        [ffmpegexe, "-list_devices", "true", "-f", "dshow", "-i", "dummy"],
        capture_output=True,
        **invisibledict,
    )
    alldevices = {}

    for d in [
        (q[1][1:-1].decode("utf-8"), q[0].decode("utf-8"), q[-1].decode("utf-8"))
        for q in [
            re.findall(
                rb'("([^"]+)"[^"]+(\([^\)]+\))[^"]+"([^"]+)")',
                x.replace(b"\n", b" ").replace(b"\r", b" "),
            )[0][1:]
            for x in re.findall(
                rb'(\[[^\]]+\][^\n\r]+\([^\)]+\)[\r\n]+.*?Alternative name\s+"[^\r\n]+)',
                p.stderr,
                flags=re.DOTALL,
            )
        ]
    ]:
        if d[0] not in alldevices:
            alldevices[d[0]] = {}
        alldevices[d[0]][d[1]] = d[2]

    def get_audio_options(alt_dev):
        p1 = subprocess.run(
            [
                ffmpegexe,
                "-list_options",
                "true",
                "-f",
                "dshow",
                "-i",
                f"audio={alt_dev}",
            ],
            capture_output=True,**invisibledict
        )
        return {
            list(j.keys())[0]: list(j.items())[0][-1]
            for j in [
                {ini: {"ch": q[0], "bits": q[1], "rate": q[2]}}
                for ini, q in enumerate(
                    [
                        [int(z.split("=")[-1].strip()) for z in y if len(y) == 3]
                        for y in [
                            x.split(b"] ")[-1]
                            .strip()
                            .decode("utf-8")
                            .split(", ", maxsplit=2)
                            for x in p1.stderr.strip().splitlines()
                            if x[0] == 91 and b"=" in x
                        ]
                    ]
                )
            ]
        }

    def get_video_options(alt_dev):
        p2 = subprocess.run(
            [
                ffmpegexe,
                "-list_options",
                "true",
                "-f",
                "dshow",
                "-i",
                f"video={alt_dev}",
            ],
            capture_output=True,**invisibledict
        )
        return {
            ini: u
            for ini, u in enumerate(
                [
                    {
                        q[0]: (
                            int(float(q[1]))
                            if float(q[1]).is_integer()
                            else float(q[1])
                        )
                        if q[0] == "fps"
                        else q[1]
                        for q in dict(
                            z.split("=") if "=" in z else ("info", z) for z in y
                        ).items()
                    }
                    for y in [
                        re.split(
                            r"\s+",
                            x.decode("utf-8")
                            .replace("max s", "max_s")
                            .replace("min s", "min_s"),
                            maxsplit=5,
                        )
                        for x in [
                            x.split(b"] ")[-1].strip()
                            for x in p2.stderr.strip().splitlines()
                            if x[0] == 91 and b"=" in x and b"(" in x
                        ]
                    ]
                ]
            )
        }

    alld = {}
    for key, items in alldevices.items():
        if not key in alld:
            alld[key] = {}
        ini = 0
        for key2, item2 in items.items():
            try:
                if key == "audio":
                    opt = get_audio_options(alt_dev=item2)
                else:
                    opt = get_video_options(alt_dev=item2)
            except Exception as e:
                opt = {"ERROR": str(e)}

            alld[key][ini] = {"name": key2, "alternative_name": item2, "options": opt}
            ini += 1

    return alld
