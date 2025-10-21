#!/usr/bin/env python3
"""
Generate Celebratory Sounds for Calculator
=========================================

This script generates simple but pleasant sounds for the calculator.
Creates success and error sounds using Python's wave module.
"""

import wave
import struct
import math
import os

def generate_success_sound():
    """Generate a happy, celebratory success sound"""
    print("🎵 Generating success sound...")
    
    # Sound parameters
    sample_rate = 44100
    duration = 0.8
    num_samples = int(sample_rate * duration)
    
    # Create a happy ascending chime
    frequencies = [523, 659, 784, 1047]  # C, E, G, C (major chord)
    samples = []
    
    for i in range(num_samples):
        sample = 0
        for j, freq in enumerate(frequencies):
            # Create sine wave for each frequency
            wave_value = math.sin(2 * math.pi * freq * i / sample_rate)
            
            # Apply envelope (fade in and out)
            envelope = 1.0
            if i < sample_rate * 0.1:  # Fade in
                envelope = i / (sample_rate * 0.1)
            elif i > sample_rate * 0.6:  # Fade out
                envelope = (num_samples - i) / (num_samples - sample_rate * 0.6)
            
            # Add some harmonics for richness
            wave_value += 0.3 * math.sin(2 * math.pi * freq * 2 * i / sample_rate)
            
            sample += wave_value * envelope * 0.2
        
        # Convert to 16-bit PCM
        sample = max(-1, min(1, sample))
        samples.append(int(sample * 32767))
    
    # Write WAV file
    with wave.open('success.wav', 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Convert samples to bytes
        frames = struct.pack('<' + 'h' * len(samples), *samples)
        wav_file.writeframes(frames)
    
    print("✅ Success sound created: success.wav")

def generate_error_sound():
    """Generate a gentle error sound"""
    print("🎵 Generating error sound...")
    
    # Sound parameters
    sample_rate = 44100
    duration = 0.5
    num_samples = int(sample_rate * duration)
    
    # Create a gentle descending tone
    frequencies = [400, 300, 200]  # Descending frequencies
    samples = []
    
    for i in range(num_samples):
        sample = 0
        
        # Create a gentle descending tone
        freq = 400 - (200 * i / num_samples)  # Descend from 400 to 200 Hz
        wave_value = math.sin(2 * math.pi * freq * i / sample_rate)
        
        # Apply envelope (fade out)
        envelope = math.exp(-i / (sample_rate * duration * 1.5))
        
        sample = wave_value * envelope * 0.3
        
        # Convert to 16-bit PCM
        sample = max(-1, min(1, sample))
        samples.append(int(sample * 32767))
    
    # Write WAV file
    with wave.open('error.wav', 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Convert samples to bytes
        frames = struct.pack('<' + 'h' * len(samples), *samples)
        wav_file.writeframes(frames)
    
    print("✅ Error sound created: error.wav")

def generate_diwali_sound():
    """Generate a festive Diwali-style sound"""
    print("🎵 Generating Diwali celebration sound...")
    
    # Sound parameters
    sample_rate = 44100
    duration = 1.2
    num_samples = int(sample_rate * duration)
    
    samples = []
    
    for i in range(num_samples):
        sample = 0
        
        # Create multiple bursts like firecrackers
        time = i / sample_rate
        
        # First burst
        if 0.1 < time < 0.4:
            freq = 800 + 200 * math.sin(time * 20)
            wave_value = math.sin(2 * math.pi * freq * i / sample_rate)
            envelope = math.exp(-(time - 0.1) * 3)
            sample += wave_value * envelope * 0.4
        
        # Second burst
        if 0.3 < time < 0.7:
            freq = 600 + 300 * math.sin(time * 15)
            wave_value = math.sin(2 * math.pi * freq * i / sample_rate)
            envelope = math.exp(-(time - 0.3) * 2)
            sample += wave_value * envelope * 0.3
        
        # Third burst
        if 0.6 < time < 1.0:
            freq = 1000 + 400 * math.sin(time * 25)
            wave_value = math.sin(2 * math.pi * freq * i / sample_rate)
            envelope = math.exp(-(time - 0.6) * 2.5)
            sample += wave_value * envelope * 0.5
        
        # Add some noise for crackling effect
        if 0.2 < time < 1.0:
            import random
            noise = (random.random() - 0.5) * 0.1
            sample += noise
        
        # Convert to 16-bit PCM
        sample = max(-1, min(1, sample))
        samples.append(int(sample * 32767))
    
    # Write WAV file
    with wave.open('diwali.wav', 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Convert samples to bytes
        frames = struct.pack('<' + 'h' * len(samples), *samples)
        wav_file.writeframes(frames)
    
    print("✅ Diwali sound created: diwali.wav")

def main():
    """Generate all sounds"""
    print("🎵 Professional Calculator - Sound Generator")
    print("=" * 50)
    
    try:
        # Generate basic sounds
        generate_success_sound()
        generate_error_sound()
        
        # Generate festive sound
        generate_diwali_sound()
        
        print("\n🎉 All sounds generated successfully!")
        print("\n📁 Files created:")
        print("   - success.wav (Happy chime for successful calculations)")
        print("   - error.wav (Gentle tone for errors)")
        print("   - diwali.wav (Festive celebration sound)")
        
        print("\n📖 To use Diwali sound:")
        print("   1. Rename 'diwali.wav' to 'success.wav'")
        print("   2. Or modify script.js to use 'diwali.wav'")
        
        print("\n🚀 Your calculator now has celebratory sounds!")
        
    except Exception as e:
        print(f"❌ Error generating sounds: {e}")

if __name__ == "__main__":
    main()
