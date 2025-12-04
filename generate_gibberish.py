#!/usr/bin/env python3
"""
Gibberish Speech Generator for Ren'Py
Generates Animal Crossing / Undertale style speaking sounds
with adjustable pitch per character.
"""

import numpy as np
from scipy.io import wavfile
import os
import random

SAMPLE_RATE = 44100

def generate_phoneme(frequency=200, duration=0.08, formants=None):
    """Generate a vowel-like phoneme sound."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)

    # Base tone
    wave = np.sin(2 * np.pi * frequency * t)

    # Add formants for more natural vowel sound
    if formants is None:
        formants = [
            (frequency * 2.5, 0.4),  # First formant
            (frequency * 4, 0.2),    # Second formant
            (frequency * 6, 0.1),    # Third formant
        ]

    for f_freq, f_amp in formants:
        wave += f_amp * np.sin(2 * np.pi * f_freq * t)

    # Apply envelope (attack/decay) for smoother sound
    envelope = np.ones_like(t)
    attack = int(0.01 * SAMPLE_RATE)
    decay = int(0.02 * SAMPLE_RATE)
    envelope[:attack] = np.linspace(0, 1, attack)
    envelope[-decay:] = np.linspace(1, 0, decay)
    wave *= envelope

    # Normalize
    wave = wave / np.max(np.abs(wave))
    return wave

def generate_consonant(duration=0.03):
    """Generate a short noise burst (consonant-like)."""
    samples = int(SAMPLE_RATE * duration)
    noise = np.random.uniform(-0.3, 0.3, samples)

    # Apply envelope
    envelope = np.ones(samples)
    attack = int(0.005 * SAMPLE_RATE)
    decay = int(0.01 * SAMPLE_RATE)
    if attack < samples:
        envelope[:attack] = np.linspace(0, 1, attack)
    if decay < samples:
        envelope[-decay:] = np.linspace(1, 0, decay)

    return noise * envelope

def pitch_shift(audio, semitones):
    """Shift pitch by resampling (simple method)."""
    factor = 2 ** (semitones / 12.0)
    indices = np.round(np.arange(0, len(audio), factor)).astype(int)
    indices = indices[indices < len(audio)]
    return audio[indices]

def generate_gibberish_syllable(base_freq=200, variation=0.15):
    """Generate a single gibberish syllable."""
    # Random frequency variation
    freq = base_freq * (1 + random.uniform(-variation, variation))

    # Random duration
    duration = random.uniform(0.05, 0.12)

    # Sometimes add a consonant before
    parts = []
    if random.random() < 0.4:
        parts.append(generate_consonant(random.uniform(0.02, 0.04)))

    # Add the vowel phoneme
    parts.append(generate_phoneme(freq, duration))

    # Sometimes add ending consonant
    if random.random() < 0.2:
        parts.append(generate_consonant(random.uniform(0.01, 0.03)))

    return np.concatenate(parts)


def generate_short_blip(base_freq=200, duration=0.08):
    """Generate a very short blip for looping (Animal Crossing style)."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)

    # Simple tone with slight harmonics
    wave = np.sin(2 * np.pi * base_freq * t)
    wave += 0.3 * np.sin(2 * np.pi * base_freq * 2 * t)
    wave += 0.15 * np.sin(2 * np.pi * base_freq * 3 * t)

    # Quick attack/decay envelope for punchy sound
    envelope = np.ones_like(t)
    attack = int(0.005 * SAMPLE_RATE)
    decay = int(0.03 * SAMPLE_RATE)
    envelope[:attack] = np.linspace(0, 1, attack)
    envelope[-decay:] = np.linspace(1, 0, decay)
    wave *= envelope

    # Add tiny gap at end for clean looping
    gap = np.zeros(int(0.04 * SAMPLE_RATE))
    wave = np.concatenate([wave, gap])

    # Normalize
    wave = wave / np.max(np.abs(wave))
    return wave

def generate_speech(text, base_freq=200, pitch_semitones=0, speed=1.0):
    """
    Generate gibberish speech for a text string.

    Args:
        text: The text to "speak" (length determines duration)
        base_freq: Base frequency in Hz (higher = higher voice)
        pitch_semitones: Additional pitch shift in semitones
        speed: Speed multiplier (higher = faster)
    """
    syllables = []

    # Generate syllables based on text length (roughly 1 syllable per 2-3 chars)
    num_syllables = max(1, len(text) // 3)

    for i in range(num_syllables):
        syllable = generate_gibberish_syllable(base_freq)

        # Apply pitch shift if needed
        if pitch_semitones != 0:
            syllable = pitch_shift(syllable, pitch_semitones)

        syllables.append(syllable)

        # Add small gap between syllables
        gap = int(SAMPLE_RATE * random.uniform(0.02, 0.06) / speed)
        syllables.append(np.zeros(gap))

    audio = np.concatenate(syllables)

    # Speed adjustment via resampling
    if speed != 1.0:
        indices = np.round(np.arange(0, len(audio), speed)).astype(int)
        indices = indices[indices < len(audio)]
        audio = audio[indices]

    return audio

def save_audio(audio, filename, sample_rate=SAMPLE_RATE):
    """Save audio as WAV file."""
    # Convert to 16-bit integer
    audio_int = np.int16(audio * 32767 * 0.8)  # 0.8 to avoid clipping
    wavfile.write(filename, sample_rate, audio_int)
    print(f"Saved: {filename}")

def convert_to_ogg(wav_path):
    """Convert WAV to OGG using ffmpeg if available."""
    ogg_path = wav_path.replace('.wav', '.ogg')
    result = os.system(f'ffmpeg -y -i "{wav_path}" -c:a libvorbis -q:a 4 "{ogg_path}" 2>/dev/null')
    if result == 0:
        os.remove(wav_path)
        print(f"Converted to: {ogg_path}")
        return ogg_path
    return wav_path


# Character voice presets (base_freq, pitch_semitones, speed)
CHARACTER_VOICES = {
    'gary': (180, 0, 1.0),           # Normal male voice
    'aria': (300, 5, 1.2),           # High-pitched, fast AI
    'leonardo': (150, -3, 0.9),      # Deep, slow, wise
    'lorenzo': (160, -2, 0.95),      # Authoritative
    'giulia': (280, 3, 1.1),         # Female, warm
    'savonarola': (130, -5, 0.8),    # Deep, menacing, slow
    'pope': (140, -4, 0.85),         # Deep, commanding
    'bianca': (320, 4, 1.15),        # High female voice
}


def generate_character_blip(character, output_dir):
    """Generate a short loopable blip for a character."""
    if character not in CHARACTER_VOICES:
        print(f"Unknown character: {character}, using default")
        base_freq, pitch, speed = 200, 0, 1.0
    else:
        base_freq, pitch, speed = CHARACTER_VOICES[character]

    # Generate a short loopable blip
    audio = generate_short_blip(base_freq, duration=0.08)

    # Apply pitch shift if needed
    if pitch != 0:
        audio = pitch_shift(audio, pitch)

    filename = os.path.join(output_dir, f"voice_{character}.wav")
    save_audio(audio, filename)
    convert_to_ogg(filename)


def generate_all_character_blips(output_dir):
    """Generate blips for all defined characters."""
    os.makedirs(output_dir, exist_ok=True)

    for character in CHARACTER_VOICES:
        generate_character_blip(character, output_dir)

    print(f"\nGenerated {len(CHARACTER_VOICES)} character voice blips!")


if __name__ == "__main__":
    output_dir = "/home/deck/Documents/sputinikus/game/audio/voice"

    print("Gibberish Speech Generator")
    print("=" * 40)
    print("\nCharacter voices:")
    for char, (freq, pitch, speed) in CHARACTER_VOICES.items():
        print(f"  {char}: freq={freq}Hz, pitch={pitch:+d} semitones, speed={speed}x")

    print(f"\nGenerating blips to: {output_dir}")
    generate_all_character_blips(output_dir)

    # Also generate a test phrase
    print("\nGenerating test phrase...")
    test_audio = generate_speech(
        "Hello, I am speaking gibberish!",
        base_freq=200,
        pitch_semitones=0
    )
    test_path = os.path.join(output_dir, "test_speech.wav")
    save_audio(test_audio, test_path)
    convert_to_ogg(test_path)

    print("\nDone! Voice blips ready for Ren'Py.")
