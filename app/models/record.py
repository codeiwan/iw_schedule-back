import sounddevice as sd
import numpy as np
import wave
import threading

class AudioRecorder:
    def __init__(self):
        self.channels = 1
        self.fs = 44100
        self.frames = []
        self.recording = False
        self.thread = None

    def start_recording(self):
        if self.recording:
            return
        self.frames = []
        self.recording = True
        self.thread = threading.Thread(target=self._record) # 백그라운드 실행
        self.thread.start()

    def _record(self):
        def callback(indata, frames, time, status):
            if self.recording:
                self.frames.append(indata.copy())

        with sd.InputStream(samplerate=self.fs, channels=self.channels, dtype='int16', callback=callback):
            while self.recording:
                sd.sleep(100)  # 짧은 sleep 반복 (녹음 유지)

    def stop_recording(self, filename="output_audio.wav"):
        if not self.recording:
            return
        self.recording = False
        self.thread.join()

        # numpy 배열로 병합 후 저장
        audio_data = np.concatenate(self.frames, axis=0)
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)  # int16 = 2 bytes
            wf.setframerate(self.fs)
            wf.writeframes(audio_data.tobytes())

    def cancel_recording(self):
        if not self.recording:
            return
        self.recording = False
        self.thread.join()
        self.frames = []
