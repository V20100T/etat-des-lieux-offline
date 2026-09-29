"""Génère la voix off (synthèse vocale Windows, hors-ligne) : voix/<id>.wav + voix/durees.json"""
import json
import subprocess
import wave
from pathlib import Path

from scenes import SCENES

ICI = Path(__file__).parent
VOIX = ICI / "voix"
VOIX.mkdir(exist_ok=True)

PS = r"""
Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$v = $s.GetInstalledVoices() | Where-Object { $_.VoiceInfo.Culture.Name -eq 'fr-FR' } | Select-Object -First 1
$s.SelectVoice($v.VoiceInfo.Name)
$s.Rate = 1
$fmt = New-Object System.Speech.AudioFormat.SpeechAudioFormatInfo(44100, [System.Speech.AudioFormat.AudioBitsPerSample]::Sixteen, [System.Speech.AudioFormat.AudioChannel]::Mono)
$s.SetOutputToWaveFile($args[0], $fmt)
$s.Speak([IO.File]::ReadAllText($args[1], [Text.Encoding]::UTF8))
$s.Dispose()
"""

durees = {}
script = VOIX / "_tts.ps1"
script.write_text(PS, encoding="utf-8-sig")
for sc in SCENES:
    wav = VOIX / f"{sc['id']}.wav"
    manuel = VOIX / f"{sc['id']}.perso.wav"
    if manuel.exists():  # voix enregistrée à la main : prioritaire
        wav = manuel
    else:
        txt = VOIX / f"{sc['id']}.txt"
        txt.write_text(sc["voix"], encoding="utf-8")
        subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script), str(wav), str(txt)], check=True)
    with wave.open(str(wav)) as w:
        durees[sc["id"]] = {"fichier": wav.name, "duree": w.getnframes() / w.getframerate()}
    print(f"{sc['id']}: {durees[sc['id']]['duree']:.1f} s")

(VOIX / "durees.json").write_text(json.dumps(durees, indent=2), encoding="utf-8")
print("Total voix :", round(sum(d["duree"] for d in durees.values()), 1), "s")
