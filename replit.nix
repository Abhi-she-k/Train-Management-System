{ pkgs }: {
  deps = [
    pkgs.run
    pkgs.python39Packages.pip
    pkgs.sudo
    pkgs.sudo
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server  
  ];
}