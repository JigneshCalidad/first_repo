#!/usr/bin/env python3
"""
Quick Sound Setup for Calculator
===============================

This script generates celebratory sounds for the calculator.
Run this to add sounds to your calculator!

Usage:
    python run_sound_setup.py
"""

import os
import sys
import subprocess

def main():
    print("🎵 Setting up celebratory sounds for your calculator...")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists("generate_sounds.py"):
        print("❌ Error: Please run this script from the sounds directory")
        print("   cd calculator/frontend/sounds")
        print("   python run_sound_setup.py")
        sys.exit(1)
    
    try:
        # Run the sound generation script
        print("🎵 Generating celebratory sounds...")
        subprocess.run([sys.executable, "generate_sounds.py"], check=True)
        
        print("\n🎉 Sound setup complete!")
        print("\n📁 Your calculator now has:")
        print("   ✅ Success sound (happy chime)")
        print("   ✅ Error sound (gentle tone)")
        print("   ✅ Diwali celebration sound (festive!)")
        
        print("\n🚀 To test your sounds:")
        print("   1. Start the calculator: cd .. && python server.py")
        print("   2. Open browser: http://localhost:3000")
        print("   3. Perform calculations and enjoy the sounds!")
        
        print("\n🎵 To use Diwali sound:")
        print("   - Rename 'diwali.wav' to 'success.wav' for festive celebrations!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error generating sounds: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
