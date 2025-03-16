{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    python = pkgs.python312;
  in {

    packages.${system}.default = pkgs.python312Packages.buildPythonPackage {
      pname = "watermark";
      version = "1.0";

      src = ./.;
      nativeBuildInputs = [ pkgs.hatch ];
      propagatedBuildINputs = [
        pkgs.python312Packages.pillow
      ];

      doCheck = false;
    };

    devShells.${system}.default = pkgs.mkShell {
      packages = [
        python
        pkgs.hatch
        pkgs.ruff
      ];
    };
  };
}
