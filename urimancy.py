#!/usr/bin/env python3

import os
import sys
import time
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from urllib.parse import quote

class UrimancyHandler(FileSystemEventHandler):
    def __init__(self, watch_dir: Path, static_dir: Path):
        self.watch_dir = Path(watch_dir)
        self.static_dir = Path(static_dir)

    def encode_filename(self, filename: str) -> str:
        """URL encode the filename for storage."""
        # Split into name and extension
        if '.' in filename:
            base, ext = filename.rsplit('.', 1)
            return f"{quote(base)}.{quote(ext)}"
        return quote(filename)

    def transform_symlink_name(self, filename: str) -> str:
        """Transform filename for symlink by replacing spaces with underscores."""
        return filename.replace(' ', '_')

    def get_structured_path(self, original_name: str) -> tuple[Path, str]:
        now = datetime.now()
        
        # Create the directory structure
        year_dir = now.strftime("%Y")
        month_dir = now.strftime("%m")
        day_dir = now.strftime("%d")
        
        # Create the new filename with timestamp and URL encoding
        timestamp = now.strftime("%H-%M-%S-%f")
        encoded_name = self.encode_filename(original_name)
        new_filename = f"{timestamp}_{encoded_name}"
        
        # Construct the full path
        full_dir = self.static_dir / year_dir / month_dir / day_dir
        
        return full_dir, new_filename

    def on_created(self, event):
        src_path = Path(event.src_path)
            
        # Ignore symlinks entirely
        if os.path.islink(src_path):
            return
            
        original_name = src_path.name

        # Wait a brief moment to ensure the file/directory is fully written
        time.sleep(0.5)

        try:
            # Get the structured directory path and new filename
            dest_dir, new_filename = self.get_structured_path(original_name)
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / new_filename

            # Handle files and directories
            if os.path.isdir(src_path):
                print(f"Processing directory: {original_name}")
                shutil.copytree(src_path, dest_path)
                shutil.rmtree(src_path)
            else:
                print(f"Processing file: {original_name}")
                shutil.move(str(src_path), str(dest_path))

            # Create symlink in the watch directory with transformed name
            symlink_name = self.transform_symlink_name(original_name)
            symlink_path = self.watch_dir / symlink_name
            if symlink_path.exists() or os.path.islink(symlink_path):
                os.remove(symlink_path)
            os.symlink(dest_path.absolute(), symlink_path)
            print(f"Created symlink: {symlink_path} -> {dest_path}")

        except Exception as e:
            print(f"Error processing {original_name}: {str(e)}")
            print(f"Full error: {str(e.__class__.__name__)}: {str(e)}")

def parse_args():
    parser = argparse.ArgumentParser(
        description='Urimancy: Watch a directory and organize files and directories',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-w', '--watch-dir',
        type=str,
        default='drophere',
        help='Directory to watch for new items'
    )
    parser.add_argument(
        '-s', '--static-dir',
        type=str,
        default='static',
        help='Directory where items will be stored'
    )
    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_args()

    # Convert to absolute paths
    watch_dir = Path(args.watch_dir).absolute()
    static_dir = Path(args.static_dir).absolute()

    # Create directories if they don't exist
    watch_dir.mkdir(exist_ok=True)
    static_dir.mkdir(exist_ok=True)

    print(f"Watching directory: {watch_dir}")
    print(f"Static directory: {static_dir}")
    print("Ready to process files and directories (symlinks will be ignored)...")

    # Initialize the event handler and observer
    event_handler = UrimancyHandler(watch_dir, static_dir)
    observer = Observer()
    observer.schedule(event_handler, str(watch_dir), recursive=False)
    
    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping Urimancy...")
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()