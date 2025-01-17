# Urimancy

URI Stores for unbreakable references.

## Motivation
Naming things is famously "one of the hard problems" in computer science.
Even harder, it is to quickly come up with a whole hierarchical tree of file paths that cannot ever be changed later on the way,
unless dealing with a whole lot of broken references.  
At the same time, people traditionally try to use filesystem trees to semantically organize and browse files,
yet trees are not much suitable for that purpose (compared to databases). There are filesystem links, but they are tedious and suboptimal (again, compared to databases). 

The idea is then to stop trying to come up with more and more sophisticated hierarchies to organize files.   
One simple hierarchy shall suffice for all storing purposes,
while databases can take care of the retrieval part (searching, browsing or querying, or a combination of the three). 

## Core concept

- You associate a directory 'D' with an Urimancy Store 'S'. Urimancy will start monitoring 'D' for filesystem changes.
- You place a file or a folder 'F' into the directory 'D' monitored by Urimancy.
- The file/folder 'F' gets copied in the associated Urimancy Store 'S'.
- The file/folder 'F' in the directory 'D' gets replaced by a link 'L'.
- You are free to rename, copy, move or delete the link 'L', as well as the content of the file/folder 'F'.
- If you don't need 'L' anymore...
  - you can just delete it.
- If you don't need 'F' anymore...
  - Delete the target of 'L'. Then delete all links pointing to 'F'.
- As long 'F' exists, it will always be accessible via its static path in its Urimancy Store.

## Install

_If using nix flakes (recommended)..._

1. add `urimancy.url = "github:damscal/urimancy";` to your `flake.nix`'s inputs.
2. add `inputs.urimancy.packages.${pkgs.system}.default` either to your `environment.systemPackages` list (for system-wide installation) or your `home.packages`list (to install via home-manager)

_If not using flakes..._

```
git clone https://github.com/damscal/urimancy.git
cd urimancy
nix build
nix profile install .
```

## Usage:

Drop any file (or a directory, or even a symlink) into the configurable `WATCH_DIR` folder.

Two things will happen:
1. The file will be moved into a subdirectory of the `STATIC_DIR` folder, organized by date and time of processing;
1. In `WATCH_DIR`, you get a new absolute symlink pointing to the original file's new location

```
usage: urimancy [-h] [-w WATCH_DIR] [-s STATIC_DIR]

Urimancy: Watch a directory and organize dropped files with symlinks

options:
  -h, --help            show this help message and exit
  -w WATCH_DIR, --watch-dir WATCH_DIR
                        Directory to watch for new files (default: drophere)
  -s STATIC_DIR, --static-dir STATIC_DIR
                        Directory where files will be stored (default: static)
```

## Automation

Urimancy instances can be automated as systemd user services. Home-manager example:

```
  systemd.user.services = 
    {
      urimancy-local_drive = {
        Unit.Description = "Executing urimancy daemon in local drive";
        Install.WantedBy = ["default.target"];
        Service = {
          ExecStart = "${lib.getExe' pkgs.urimancy "urimancy"} -w /PATH/TO/LOCAL_DRIVE/WATCH_FOLDER -s /PATH/TO/LOCAL_DRIVE/STORE_FOLDER";
          Type = "oneshot";
          RemainAfterExit = true;
        };
      };
    };
```