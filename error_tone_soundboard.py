"""
Error Tone Soundboard
---------------------
A small desktop UI for auditioning the error tones in Tones_Round1.aup3.

Audacity .aup3 files are project databases, not ordinary audio files. This
soundboard therefore plays WAV exports of the individual Audacity tracks.

Export each track from Audacity as a WAV, then either:
  1. Put the WAVs in a folder named "error_tones" beside this script and use
     the suggested filenames below, or
  2. Click "Load WAV" on each row to assign the exported track manually.

Suggested filenames:
  01_aed_pad_placement.wav
  02_pulse_check_placement.wav
  03_cpr_depth_800.wav
  04_cpr_depth_300.wav
  05_cpr_rate_metronome.wav
  06_cpr_hand_placement.wav

Install playback dependency:
    python -m pip install pygame

Run:
    python error_tone_soundboard.py
"""

# from pathlib import Path
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import threading

print("hello")

# try:
#     import pygame
# except ImportError:
#     pygame = None


# BASE_DIRECTORY = Path(__file__).resolve().parent
# AUDIO_DIRECTORY = BASE_DIRECTORY / "error_tones"

# # Labels are based on the track/clip names visible in the supplied Audacity
# # project. The two CPR Depth variants are separate buttons.
# SOUNDS = [
#     ("AED Pad Placement — 500 Hz square, 0.3 s",
#      "01_aed_pad_placement.wav"),
#     ("Pulse Check Placement — 700 Hz square, 0.3 s",
#      "02_pulse_check_placement.wav"),
#     ("CPR Depth — 800 Hz square, 0.15 s",
#      "03_cpr_depth_800.wav"),
#     ("CPR Depth — 300 Hz square, 0.13 s",
#      "04_cpr_depth_300.wav"),
#     ("CPR Rate — 120 BPM metronome",
#      "05_cpr_rate_metronome.wav"),
#     ("CPR Hand Placement — 800 Hz square, 0.3 s",
#      "06_cpr_hand_placement.wav"),
# ]


# class ErrorToneSoundboard:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Error Tone Soundboard")
#         self.root.geometry("760x510")
#         self.root.minsize(650, 420)
#         self.root.configure(bg="#f3f4f6")

#         self.audio_paths = {}
#         self.current_sound = None
#         self.is_playing = False

#         if pygame is not None:
#             try:
#                 pygame.mixer.init()
#             except pygame.error as error:
#                 messagebox.showerror(
#                     "Audio initialization failed",
#                     f"Could not initialize audio playback:\n{error}"
#                 )

#         self._build_ui()
#         self._load_default_files()

#         self.root.protocol("WM_DELETE_WINDOW", self._close)

#     def _build_ui(self):
#         header = tk.Frame(self.root, bg="#f3f4f6")
#         header.pack(fill="x", padx=24, pady=(22, 8))

#         tk.Label(
#             header,
#             text="Error Tone Soundboard",
#             font=("Segoe UI", 21, "bold"),
#             fg="#111827",
#             bg="#f3f4f6",
#         ).pack(anchor="w")

#         tk.Label(
#             header,
#             text="Load each exported WAV, then press its error button to audition it.",
#             font=("Segoe UI", 10),
#             fg="#4b5563",
#             bg="#f3f4f6",
#         ).pack(anchor="w", pady=(5, 0))

#         self.status_var = tk.StringVar(
#             value="No audio loaded yet." if pygame else
#             "Install pygame to enable audio: python -m pip install pygame"
#         )
#         tk.Label(
#             self.root,
#             textvariable=self.status_var,
#             font=("Segoe UI", 9),
#             fg="#374151",
#             bg="#e5e7eb",
#             anchor="w",
#             padx=12,
#             pady=8,
#         ).pack(fill="x", padx=24, pady=(8, 14))

#         rows = tk.Frame(self.root, bg="#f3f4f6")
#         rows.pack(fill="both", expand=True, padx=24)

#         self.row_status = {}
#         for index, (label, filename) in enumerate(SOUNDS):
#             row = tk.Frame(
#                 rows, bg="white", highlightbackground="#d1d5db",
#                 highlightthickness=1
#             )
#             row.pack(fill="x", pady=5)

#             button = tk.Button(
#                 row,
#                 text=label,
#                 font=("Segoe UI", 10, "bold"),
#                 anchor="w",
#                 justify="left",
#                 bg="#ffffff",
#                 fg="#111827",
#                 activebackground="#e5e7eb",
#                 relief="flat",
#                 padx=14,
#                 pady=12,
#                 command=lambda sound_index=index: self.play_sound(sound_index),
#             )
#             button.pack(side="left", fill="x", expand=True)

#             load_button = tk.Button(
#                 row,
#                 text="Load WAV",
#                 font=("Segoe UI", 9),
#                 bg="#e5e7eb",
#                 fg="#111827",
#                 relief="flat",
#                 padx=12,
#                 pady=9,
#                 command=lambda sound_index=index: self.load_file(sound_index),
#             )
#             load_button.pack(side="right", padx=10, pady=8)

#             status = tk.Label(
#                 row,
#                 text="Not loaded",
#                 font=("Segoe UI", 8),
#                 fg="#9ca3af",
#                 bg="white",
#                 width=12,
#                 anchor="e",
#             )
#             status.pack(side="right", padx=(4, 8))
#             self.row_status[index] = status

#         footer = tk.Frame(self.root, bg="#f3f4f6")
#         footer.pack(fill="x", padx=24, pady=(12, 20))

#         tk.Button(
#             footer,
#             text="STOP",
#             command=self.stop_sound,
#             font=("Segoe UI", 10, "bold"),
#             bg="#b91c1c",
#             fg="white",
#             activebackground="#991b1b",
#             activeforeground="white",
#             relief="flat",
#             padx=22,
#             pady=10,
#         ).pack(side="left")

#         tk.Button(
#             footer,
#             text="Open WAV folder",
#             command=self.open_audio_folder,
#             font=("Segoe UI", 9),
#             bg="#e5e7eb",
#             fg="#111827",
#             relief="flat",
#             padx=14,
#             pady=10,
#         ).pack(side="right")

#     def _load_default_files(self):
#         for index, (_, filename) in enumerate(SOUNDS):
#             candidate = AUDIO_DIRECTORY / filename
#             if candidate.is_file():
#                 self.audio_paths[index] = candidate
#                 self.row_status[index].configure(
#                     text="Ready", fg="#15803d"
#                 )
#         self._update_status()

#     def load_file(self, sound_index):
#         path = filedialog.askopenfilename(
#             title="Choose WAV for this error tone",
#             filetypes=[("WAV audio", "*.wav"), ("All files", "*.*")]
#         )
#         if not path:
#             return

#         self.audio_paths[sound_index] = Path(path)
#         self.row_status[sound_index].configure(text="Ready", fg="#15803d")
#         self._update_status()

#     def play_sound(self, sound_index):
#         if pygame is None:
#             messagebox.showerror(
#                 "Missing dependency",
#                 "Install pygame first:\n\npython -m pip install pygame"
#             )
#             return

#         path = self.audio_paths.get(sound_index)
#         if path is None or not path.is_file():
#             messagebox.showinfo(
#                 "WAV not loaded",
#                 "Load the WAV export for this error using the 'Load WAV' "
#                 "button on this row."
#             )
#             return

#         try:
#             pygame.mixer.music.stop()
#             pygame.mixer.music.load(str(path))
#             pygame.mixer.music.play()
#             self.current_sound = sound_index
#             self.is_playing = True
#             self.status_var.set(f"Playing: {SOUNDS[sound_index][0]}")
#         except pygame.error as error:
#             messagebox.showerror(
#                 "Playback error", f"Could not play this WAV:\n{error}"
#             )

#     def stop_sound(self):
#         if pygame is not None:
#             pygame.mixer.music.stop()
#         self.current_sound = None
#         self.is_playing = False
#         self.status_var.set("Playback stopped.")

#     def _update_status(self):
#         loaded_count = len(self.audio_paths)
#         self.status_var.set(
#             f"{loaded_count} of {len(SOUNDS)} sounds loaded."
#         )

#     def open_audio_folder(self):
#         AUDIO_DIRECTORY.mkdir(exist_ok=True)
#         try:
#             import os
#             os.startfile(str(AUDIO_DIRECTORY))
#         except AttributeError:
#             messagebox.showinfo(
#                 "WAV folder",
#                 f"Place your exported WAV files here:\n{AUDIO_DIRECTORY}"
#             )

#     def _close(self):
#         if pygame is not None:
#             pygame.mixer.music.stop()
#             pygame.mixer.quit()
#         self.root.destroy()


# def main():
#     root = tk.Tk()
#     ErrorToneSoundboard(root)
#     root.mainloop()


# if __name__ == "__main__":
#     main()
