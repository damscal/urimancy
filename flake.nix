# flake.nix
{
  description = "Urimancy - File organization utility";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonEnv = pkgs.python3.withPackages (ps:
          with ps; [
            watchdog
          ]);
      in {
        packages.default = pkgs.stdenv.mkDerivation {
          name = "urimancy";
          version = "0.0.1";
          src = ./.;

          buildInputs = [
            pythonEnv
          ];

          installPhase = ''
            mkdir -p $out/bin
            cp urimancy.py $out/bin/urimancy
            chmod +x $out/bin/urimancy
            # Ensure the Python script uses the correct interpreter
            substituteInPlace $out/bin/urimancy \
              --replace "#!/usr/bin/env python3" "#!${pythonEnv}/bin/python3"
          '';
        };

        apps.default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/urimancy";
        };
      }
    );
}
