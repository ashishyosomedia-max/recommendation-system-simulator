# Subtitle process

Input from user: a Hinglish `.srt` (usually Devanagari, auto-generated) + the `.wav` audio.
Output: one final `.srt` in Latin script, saved in this folder.

1. Keep numbering and timestamps exactly as in the original SRT.
2. Transcribe the audio (`transcribe.py`, English and Hindi modes) and fix every
   speech-recognition mistake in the original against what is actually said.
3. Script: Hindi words in Roman letters (Woh, Yeh, Toh, nahi hai, badhaate hain,
   chahiye, zameen...), English words in normal English spelling.
4. Capitalize the first letter of every name and place, and of every sentence.
5. Spell-check every word; no double spaces or trailing spaces.
6. Commit + push, then send the final SRT.

Model note: Hugging Face is blocked here; Whisper small (CTranslate2) is available
from npm as `@skillninja/shortmovie-telop-model-p0`..`p3` (concatenate
`model.bin.part0-3`, check `model.sha256`). `pip install faster-whisper`.
