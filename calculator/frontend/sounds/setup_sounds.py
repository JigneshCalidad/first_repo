#!/usr/bin/env python3
"""
Sound Setup Script for Professional Calculator
============================================

This script helps you download and set up celebratory sounds for the calculator.
It creates placeholder sounds and provides instructions for getting real sounds.

Usage:
    python setup_sounds.py
"""

import os
import sys
import urllib.request
import wave
import struct
import math

def create_placeholder_sounds():
    """Create placeholder sound files for testing"""
    
    # Create success sound (happy chime)
    success_freq = 800  # Higher frequency for success
    duration = 0.6
    sample_rate = 44100
    
    print("🎵 Creating placeholder sounds...")
    
    # Success sound - ascending chime
    create_chime_sound("success.wav", [523, 659, 784, 1047], duration, sample_rate)
    
    # Error sound - descending tone
    create_chime_sound("error.wav", [400, 300, 200], duration * 0.8, sample_rate)
    
    print("✅ Placeholder sounds created!")
    print("📁 Files created:")
    print("   - success.wav (Happy chime)")
    print("   - error.wav (Error tone)")

def create_chime_sound(filename, frequencies, duration, sample_rate):
    """Create a chime sound with multiple frequencies"""
    
    samples = []
    num_samples = int(sample_rate * duration)
    
    for i in range(num_samples):
        sample = 0
        for freq in frequencies:
            # Create a sine wave for each frequency
            wave = math.sin(2 * math.pi * freq * i / sample_rate)
            # Apply envelope (fade out)
            envelope = math.exp(-i / (sample_rate * duration * 2))
            sample += wave * envelope * 0.3
        
        # Convert to 16-bit PCM
        sample = max(-1, min(1, sample))
        samples.append(int(sample * 32767))
    
    # Write WAV file
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)
        
        # Convert samples to bytes
        frames = struct.pack('<' + 'h' * len(samples), *samples)
        wav_file.writeframes(frames)

def download_real_sounds():
    """Instructions for downloading real sounds"""
    
    print("\n🎵 For Real Celebratory Sounds:")
    print("=" * 50)
    print("1. Freesound.org (Free sounds):")
    print("   - Go to: https://freesound.org")
    print("   - Search: 'success chime' or 'happy sound'")
    print("   - Download MP3/WAV files")
    print("   - Rename to: success.mp3, error.mp3")
    
    print("\n2. Zapsplat (Professional sounds):")
    print("   - Go to: https://zapsplat.com")
    print("   - Search: 'success notification' or 'error alert'")
    print("   - Download and convert to MP3/WAV")
    
    print("\n3. Create your own sounds:")
    print("   - Use GarageBand (Mac) or Audacity (Free)")
    print("   - Record or create chime sounds")
    print("   - Export as MP3 or WAV")
    
    print("\n4. Diwali-style celebratory sounds:")
    print("   - Search: 'diwali firecracker' or 'celebration sound'")
    print("   - Look for: 'festival sound effects'")
    print("   - Download and rename to success.mp3")

def setup_sound_files():
    """Set up the sound files in the correct directory"""
    
    sounds_dir = "sounds"
    
    # Create sounds directory if it doesn't exist
    if not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)
        print(f"📁 Created directory: {sounds_dir}")
    
    # Change to sounds directory
    os.chdir(sounds_dir)
    
    # Create placeholder sounds
    create_placeholder_sounds()
    
    # Create instructions file
    with open("SOUND_SETUP_INSTRUCTIONS.md", "w") as f:
        f.write("""# Sound Setup Instructions

## Current Files
- success.wav - Placeholder success sound
- error.wav - Placeholder error sound

## To Add Real Sounds

### Option 1: Download from Freesound.org
1. Go to https://freesound.org
2. Search for "success chime" or "happy notification"
3. Download MP3 or WAV files
4. Rename to: success.mp3, error.mp3
5. Place in this directory

### Option 2: Diwali Celebration Sounds
1. Search for "diwali firecracker sound" or "celebration sound"
2. Download festive sounds
3. Rename to: success.mp3, error.mp3
4. Place in this directory

### Option 3: Create Your Own
1. Use GarageBand (Mac) or Audacity (Free)
2. Create chime sounds
3. Export as MP3 or WAV
4. Place in this directory

## Supported Formats
- MP3 (recommended)
- WAV
- OGG

## File Names
- success.mp3 or success.wav - Plays on successful calculations
- error.mp3 or error.wav - Plays on errors

The calculator will automatically use these sounds when available.
""")
    
    print(f"\n📝 Instructions saved to: {sounds_dir}/SOUND_SETUP_INSTRUCTIONS.md")
    
    # Go back to parent directory
    os.chdir("..")

def main():
    """Main function"""
    print("🎵 Professional Calculator - Sound Setup")
    print("=" * 50)
    
    try:
        setup_sound_files()
        
        print("\n🎉 Sound setup complete!")
        print("\n📖 Next steps:")
        print("1. Run the calculator: python server.py")
        print("2. Test the sounds by performing calculations")
        print("3. Replace placeholder sounds with real ones")
        print("4. Enjoy your celebratory calculator!")
        
    except Exception as e:
        print(f"❌ Error setting up sounds: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
